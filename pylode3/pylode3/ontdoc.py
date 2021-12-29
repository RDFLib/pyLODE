from typing import Union
from rdflib import Graph, BNode, Literal, URIRef, Namespace
from pathlib import Path
from itertools import chain
from rdflib.namespace import DC, DCTERMS, DOAP, OWL, PROF, PROV, RDF, RDFS, SDO, SKOS
import dominate
from dominate.tags import *
from dominate.util import raw
import markdown
import pickle
from utils import *
from collections import defaultdict

ONTDOC = Namespace("https://w3id.org/profile/ontdoc/")
RDF_FOLDER = Path(__file__).parent / "rdf"

CLASS_PROPS = [
    RDFS.isDefinedBy,
    DCTERMS.title,
    DCTERMS.description,
    SKOS.scopeNote,
    SKOS.example,
    DCTERMS.source,
    DCTERMS.provenance,
    SKOS.note,

    RDFS.subClassOf,
    ONTDOC.superClassOf,
    OWL.equivalentClass,
    # OWL.restriction,
    ONTDOC.inDomainOf,
    ONTDOC.inDomainIncludesOf,
    ONTDOC.inRangeOf,
    ONTDOC.inRangeIncludesOf,
    ONTDOC.hasInstance
]


class OntDoc:
    def __init__(self, ontology: Union[Graph, Path, str]):
        if isinstance(ontology, Graph):
            self.g = ontology
        elif isinstance(ontology, Path):
            self.g = Graph().parse(ontology)
        elif isinstance(ontology, str):
            # see if it's a file path
            if Path(ontology).is_file():
                self.g = Graph().parse(ontology)
            else:  # it's data
                if ontology.startswith("[") or ontology.startswith("{"):
                    input_format = "json-ld"
                elif (
                    ontology.startswith("<?xml")
                    or ontology.startswith("<!--")
                    or ontology.startswith("<rdf:RDF")
                ):
                    input_format = "xml"
                else:
                    input_format = "turtle"  # this will also cover n-triples
                self.g = Graph().parse(data=ontology, format=input_format)
        else:
            raise ValueError(
                "The ontology you supply to OntDoc must be either an RDFlib Graph, a Path (to an RDF file) "
                "or a string (of RDF data)"
            )
        self._expand_graph_to_ontdoc_profile()
        self.background_onts = self._load_background_onts()
        self.background_onts_titles = self._load_background_onts_titles()
        self.class_props_labeled = {}
        for prop in CLASS_PROPS:
            self.class_props_labeled[prop] = self._get_property_labels(prop)
        self.toc = {
            "Classes": {},
            "Properties": {},
            "Named Individuals": {},
            "Namespaces": {},
            "Legend": True,
        }
        self.fids = {}
        self._get_default_namespace()
        self.doc = dominate.document()
        with self.doc:
            self.content = div(id="content")

    def _expand_graph_to_ontdoc_profile(self):
        # class types
        for s in self.g.subjects(RDF.type, OWL.Class):
            self.g.add((s, RDF.type, RDFS.Class))

        # property types
        for s in chain(
            self.g.subjects(RDF.type, OWL.ObjectProperty),
            self.g.subjects(RDF.type, OWL.FunctionalProperty),
            self.g.subjects(RDF.type, OWL.DatatypeProperty),
            self.g.subjects(RDF.type, OWL.AnnotationProperty),
        ):
            self.g.add((s, RDF.type, RDF.Property))

        # name
        for s, o in chain(
            self.g.subject_objects(DC.title),
            self.g.subject_objects(RDFS.label),
            self.g.subject_objects(SKOS.prefLabel),
            self.g.subject_objects(SDO.name),
        ):
            self.g.add((s, DCTERMS.title, o))

        # description
        for s, o in chain(
            self.g.subject_objects(DC.description),
            self.g.subject_objects(RDFS.comment),
            self.g.subject_objects(SKOS.definition),
            self.g.subject_objects(SDO.description),
        ):
            self.g.add((s, DCTERMS.description, o))

        # source
        for s, o in self.g.subject_objects(DC.source):
            self.g.add((s, DCTERMS.source, o))

        # owl:Restrictions from Blank Nodes
        for s in self.g.subjects(OWL.onProperty):
            self.g.add((s, RDF.type, OWL.Restriction))

        # we do these next few so we only need to loop through Class & Property properties once: single subject
        for s, o in self.g.subject_objects(RDFS.subClassOf):
            self.g.add((o, ONTDOC.superClassOf, s))

        for s, o in self.g.subject_objects(RDFS.subPropertyOf):
            self.g.add((o, ONTDOC.superPropertyOf, s))

        for s, o in self.g.subject_objects(RDFS.domain):
            self.g.add((o, ONTDOC.inDomainOf, s))

        for s, o in self.g.subject_objects(SDO.domainIncludes):
            self.g.add((o, ONTDOC.inDomainIncludesOf, s))

        for s, o in self.g.subject_objects(RDFS.range):
            self.g.add((o, ONTDOC.inRangeOf, s))

        for s, o in self.g.subject_objects(SDO.rangeIncludes):
            self.g.add((o, ONTDOC.inRangeIncludesOf, s))

        for s, o in self.g.subject_objects(RDF.type):
            self.g.add((o, ONTDOC.hasMember, s))

        # Agents
        # creator
        for s, o in chain(
            self.g.subject_objects(DC.creator),
            self.g.subject_objects(SDO.creator),
            self.g.subject_objects(
                SDO.author
            ),  # conflate SDO.author with DCTERMS.creator
        ):
            self.g.remove((s, DC.creator, o))
            self.g.remove((s, SDO.creator, o))
            self.g.remove((s, SDO.author, o))
            self.g.add((s, DCTERMS.creator, o))

        # contributor
        for s, o in chain(
            self.g.subject_objects(DC.contributor),
            self.g.subject_objects(SDO.contributor),
        ):
            self.g.remove((s, DC.contributor, o))
            self.g.remove((s, SDO.contributor, o))
            self.g.add((s, DCTERMS.contributor, o))

        # publisher
        for s, o in chain(
            self.g.subject_objects(DC.publisher), self.g.subject_objects(SDO.publisher)
        ):
            self.g.remove((s, DC.publisher, o))
            self.g.remove((s, SDO.publisher, o))
            self.g.add((s, DCTERMS.publisher, o))

    def _load_background_onts(self):
        if Path(RDF_FOLDER / "refs.pickle").is_file():
            with open(RDF_FOLDER / "refs.pickle", "rb") as f:
                return pickle.load(f)
        else:
            g = load_background_onts()
            expand_background_graph(g)
            pickle_background_onts(g)
            return g

    def _load_background_onts_titles(self):
        if Path(RDF_FOLDER / "refs_titles.pickle").is_file():
            with open(RDF_FOLDER / "refs_titles.pickle", "rb") as f:
                return pickle.load(f)
        else:
            g = get_background_ontology_titles(self.background_onts)
            pickle_background_onts_titles(g)
            return g

    def _make_document(self, title, schema_org_json, version):
        self.doc.title = title
        self._make_header(schema_org_json)
        self._make_body(title, version)

    def _make_header(self, schema_org_json):
        # use standard pyLODE stylesheet
        css = "\n" + open("pylode.css").read() + "\n\t"
        with self.doc.head:
            style(raw(css))
            link(
                rel="icon",
                type="image/png",
                sizes="16x16",
                href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABhklEQVQ4jbWPzStEURjG3yQLirlGKUnKFO45Z+SjmXvnnmthQcpCoVhYmD/AwmJiI3OvZuZc2U3UlKU0/gAslMw9JgvhHxAr2fko7r0jHSsl+TgbTz2Lt5731/MASEiJW9ONml2QyX6rsGalmnT74v8BDf12hxJfpV8d1uwNKUBYszabdFv84L8B9X0rESVmmUup2fme0cVhJWaZHw4NWL1SewEAfDe6H3Dy6Ll456WEJsRZS630MwCAOI20ei5OBpxse5zcBZw8eS4uPpfIuDiCainIg9umBCU0GZzgLZ9Hn31OgoATL+CkLDGB5H1OKj4nFd/FBxUXJ0UZNb4edw/6nLyJXaj5FeCVyPLNIVmYK8TG1IwWb16L1gEACAFV90ftoT8bdOX0EeyY99gxBXZMgRz6qGb1KantAACI0UvE6F5XJqEjpsdURouI0Vt5gGOUkUNnPu7ObGIIMfNaGqDmjDRi9FZldF1lRgYzeqUyeoiY4ag5Iy3RgOYRM8+/M2bG8efsO4hGrpmJseyMAAAAAElFTkSuQmCC",
            )
            link(
                rel="icon",
                type="image/png",
                sizes="32x32",
                href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAC40lEQVRYhe2UT0hUQRzHp6Iss1B3VZKIDbbdfW9mnoi4f3zzjkJQeOgS0SEIb1EWBGGlLLu460zQPQM1unUIIjA6rfpm6ZAhHjoIRVQUFUlEbG+euTsdXG1d3VL3bVD4g+9h+L35fT/8fvN7ADgY9aHY5fpIvK82HO9ysu66wxWOzbkjcekKx0a2ALYA/n2AGi3a6ArFezcidziecQygNhhrcUficjP6PwBqtGijKxy/thnVBePHywYoDsFhl53GV8SEcsTx4usCMLUewTVpc23BNvEzm6Neyf1+KcG2vwqwUjgrOJq2JmHftwmkVBRGTvncFodnbI7vChO/FRznCmHsNM7aHM9Yk7Df5iqsLMw9sMNOK2g+jS4IEz0UJv4iuJZb2RltWnB4UZqH6ioGAgAAGe5vtiZhtzDx7OoRadLmeM7m6IRjhnLMW2Vx1bA5GhAmnhIcz6/xNj4Ujsky8UspwfayjDPjsF2Y6L7N8Vzx/BfP+KPg6LbgSqd8DnfJW2CnbaLhfH5ephpqygJYvQU4Z3P82TLRsDDhUTnmrSq+Y3N0Mg+Xldy/zwEAnLMWZ3pHpNExmfLs/t0dOdVcbT0JeKxUwFP2VljjqiE47Jp53LTXNxhsUZjerTByXWX6VZWRs/4bIQ2ACv+UAomgDzLCISNZxAxZKMhIDjLy1JfsaK+I+eGBUBNk5E2x8RogX/PdcDZUqieWTSh5D6nOVKqfhoycUmlHFFIyu5RXqf7AcQDISCpv/tqbMBqK883RtmpISRoxQyJKPgGn3wNk5NEigDFa6hslqV/Kj+FdBQD0bshIDlKSLlVcoWQo36UhR80BAMB73lulMn0EMpJTqD6qJiOt3mho/8GbkT2BZNgDB/V+RI0fkOrT3kRIVQbaDizJm2hdNbINBxwk5xAj3yEjuV9rZ1iIkgxixkLBA83mz8uCjLwoGwAx0vOnFSy5mtR4VTaAQvVORMnwZgSpzkrV/QmdE2tKe46+MQAAAABJRU5ErkJggg==",
            )
            meta(http_equiv="Content-Type", content="text/html; charset=utf-8")
            script(raw("\n" + schema_org_json + "\n\t"), type="application/ld+json")

    def _make_body(self, title, version):
        self._make_pylode_logo(version)

        with self.content:
            h1(title)
            p("Some other text")

        self._make_classes()
        self._make_namespaces()
        self._make_legend()
        self._make_toc()

    def _make_pylode_logo(self, version):
        with self.doc:
            with div(id="pylode"):
                with p("made by "):
                    with a(href="https://github.com/rdflib/pyLODE"):
                        span("p", id="p")
                        span("y", id="y")
                        span("LODE")
                    a(
                        version,
                        href="https://github.com/rdflib/pyLODE/release/" + version,
                        id="version",
                    )

    def _make_classes(self):
        with self.content:
            with div(id="classes", _class="section"):
                h2("Classes")
                for s in self.g.subjects(predicate=RDF.type, object=RDFS.Class):
                    this_classes_props = defaultdict(list)
                    # ignore blank nodes for things like [ owl:unionOf ( ... ) ]
                    if not isinstance(s, BNode):
                        for p, o in self.g.predicate_objects(subject=s):
                            if p in CLASS_PROPS:
                                this_classes_props[p].append(o)
                        this_fid = self._make_fid(this_classes_props[DCTERMS.title][0], s)
                        this_title = this_classes_props[DCTERMS.title]
                        self.toc["Classes"]["#"+this_fid] = this_title

                        with div(id=this_fid, _class="class entity"):
                            h3(this_title)
                            with table():
                                for k, v in this_classes_props.items():
                                    self._make_property_table_row(
                                        k,
                                        str(self.class_props_labeled[k]["title"]).title(),
                                        self.class_props_labeled[k]["description"],
                                        self.class_props_labeled[k]["ont_title"],
                                        v,
                                        "c" if k in [
                                            RDFS.subClassOf,
                                            ONTDOC.superClassOf,
                                            OWL.equivalentClass]
                                        else None
                                    )
            # TODO: restrictions = []

    def _get_property_labels(self, property_uri: URIRef) -> dict:
        title = None
        description = None
        ont_title = None
        for p, o in self.background_onts.predicate_objects(property_uri):
            if p == DCTERMS.title:
                title = o
            if p == DCTERMS.description:
                description = o
        for k, v in self.background_onts_titles.items():
            if property_uri.startswith(k):
                ont_title = v

        if title is None:
            title = self._make_title_from_uri(property_uri)

        return {
            "title": title,
            "description": description,
            "ont_title": ont_title,
        }

    def _make_property_table_row(
        self,
        property_uri: URIRef,
        property_title: Literal,
        property_description: Literal,
        ont_title: Literal,
        obj: Union[list, URIRef, BNode, Literal],
        obj_type: str
    ):
        with tr():
            th(
                a(
                    str(property_title),
                    title=str(property_description),
                    _class="hover_property",
                    href=str(property_uri),
                )
            )
            td(
                self._render_list_of_rdflib_objects_in_html(obj, obj_type=obj_type)
            )

    def _render_rdflib_object_in_html(self, obj: Union[URIRef, BNode, Literal], obj_type=None):
        if isinstance(obj, URIRef):
            return p(self._make_hyperlink(obj, type=obj_type))
        elif isinstance(obj, BNode):
            return p(raw("[ ]"))
        elif isinstance(obj, Literal):
            if str(obj).startswith("http"):
                return p(self._make_hyperlink(obj))
            return raw(markdown.markdown(str(obj)))

    def _render_list_of_rdflib_objects_in_html(self, obj: Union[list, URIRef, BNode, Literal], obj_type=None):
        if isinstance(obj, list):
            l = []
            for x in obj:
                l.append(self._render_rdflib_object_in_html(x, obj_type=obj_type))
            return l
        else:
            return self._render_rdflib_object_in_html(obj, obj_type=obj_type)

    def _make_legend(self):
        with self.content:
            with div(id="legend"):
                h2("Legend")
                with table(_class="entity"):

                    if self.toc["Classes"] is not None:
                        with tr():
                            td(sup("c", _class="sup-c", title="Classes"))
                            td("Classes")
                    if self.toc["Properties"] is not None:
                        with tr():
                            td(sup("p", _class="sup-p", title="Properties"))
                            td("Properties")
                        if self.toc["Properties"].get("Object Properties") is not None:
                            with tr():
                                td(
                                    sup(
                                        "op", _class="sup-op", title="Object Properties"
                                    )
                                )
                                td("Object Properties")
                        if (
                            self.toc["Properties"].get("Datatype Properties")
                            is not None
                        ):
                            with tr():
                                td(
                                    sup(
                                        "dp",
                                        _class="sup-dp",
                                        title="Datatype Properties",
                                    )
                                )
                                td("Datatype Properties")
                        if (
                            self.toc["Properties"].get("Annotation Properties")
                            is not None
                        ):
                            with tr():
                                td(
                                    sup(
                                        "ap",
                                        _class="sup-ap",
                                        title="Annotation Properties",
                                    )
                                )
                                td("Annotation Properties")
                        if (
                            self.toc["Properties"].get("Functional Properties")
                            is not None
                        ):
                            with tr():
                                td(
                                    sup(
                                        "fp",
                                        _class="sup-fp",
                                        title="Functional Properties",
                                    )
                                )
                                td("Functional Properties")
                    if self.toc["Named Individuals"] is not None:
                        with tr():
                            td(sup("ni", _class="sup-ni", title="Named Individuals"))
                            td("Named Individuals")

    def _get_default_namespace(self):
        # if this ontology declares a preferred URI, use that
        preferred_namespace_uri = None
        for s, o in self.g.subject_objects(
            predicate=URIRef("http://purl.org/vocab/vann/preferredNamespaceUri")
        ):
            preferred_namespace_uri = str(o)

        preferred_namespace_prefix = None
        for s, o in self.g.subject_objects(
            predicate=URIRef("http://purl.org/vocab/vann/preferredNamespacePrefix")
        ):
            preferred_namespace_prefix = str(o)
        if preferred_namespace_prefix is None:
            preferred_namespace_prefix = ""

        if preferred_namespace_uri is not None:
            self.default_namespace = (
                preferred_namespace_prefix,
                preferred_namespace_uri,
            )

        # if not, try the URI of the main object, compared to all prefixes
        else:
            default_uri = None

            for s in chain(
                self.g.subjects(predicate=RDF.type, object=OWL.Ontology),
                self.g.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
                self.g.subjects(predicate=RDF.type, object=PROF.Profile),
            ):
                default_uri = str(s)

            if default_uri is not None:
                prefix = self.g.compute_qname(default_uri, True)[0]
                if prefix is not None:
                    self.default_namespace = (prefix, default_uri)
            else:
                # can't find either a declared or default namespace so we have an error
                raise Exception(
                    "pyLODE can't detect a URI for an owl:Ontology, a skos:ConceptScheme or a prof:Profile"
                )

    def _make_namespaces(self):
        # get only namespaces used in ont
        nses = {}
        for n in chain(self.g.subjects(), self.g.predicates(), self.g.objects()):
            for prefix, ns in self.g.namespaces():
                if str(n).startswith(ns):
                    nses[prefix] = ns

        with self.content:
            with div(id="namespaces"):
                h2("Namespaces")
                with dl():
                    for prefix, ns in sorted(nses.items()):
                        p = prefix if prefix != "" else ":"
                        dt(p, id=p)
                        dd(code(ns))
                        self.toc["Namespaces"][p] = ns

    def _make_toc(self):
        with self.doc:
            with div(id="toc"):
                h3("Table of Contents")
                with ul(_class="first"):
                    for label, section in self.toc.items():
                        if section is not None:
                            li(a(label, href="#" + label.replace(" ", "").lower()))

                            if label == "Classes":
                                with ul(_class="second"):
                                    for cls_uri, cls_label in self.toc[
                                        "Classes"
                                    ].items():
                                        li(a(cls_label, href=cls_uri))

                            if label == "Namespaces":
                                with ul(_class="second"):
                                    for prefix, ns in self.toc["Namespaces"].items():
                                        li(a(prefix, href="#" + prefix))

    def _make_title_from_uri(self, uri):
        if isinstance(uri, URIRef):
            uri = str(uri)
        # can't tolerate any URI faults so return None if anything is wrong

        # URIs with no path segments or ending in slash
        segments = uri.split("/")
        if len(segments[-1]) < 1:
            return None

        # URIs with only a domain - no path segments
        if len(segments) < 4:
            return None

        # URIs ending in hash
        if segments[-1].endswith("#"):
            return None

        return (
            segments[-1].split("#")[-1]
            if segments[-1].split("#")[-1] != ""
            else segments[-1].split("#")[-2]
        )

    def _make_hyperlink(self, uri, type=None):
        try:
            qname = self.g.compute_qname(uri, True)
        except ValueError:
            qname = uri

        types = {
            "c": "class",
            "p": "property",
            "op": "object property",
            "dp": "datatype property",
            "ap": "annotation property",
            "fp": "functional property",
            "ni": "named individual",
        }

        if type in types.keys():
            # sup = f'<sup class="sup-{type}" title="{types[type]}">{type}</sup>'
            return span(
                a(f'{qname[0]}:{qname[2]}', href=uri),
                sup(type, _class="sup-" + type, title=types[type])
            )
        else:
            if isinstance(qname, tuple):
                return a(f'{qname[0]}:{qname[2]}', href=uri)
            return a(f'{qname}', href=uri)

    def _make_fid(self, title, uri):
        """Makes the fragment ID for a class, property, Named Individual (any entity) based on URI or name"""
        if isinstance(uri, URIRef):
            uri = str(uri)

        if isinstance(title, Literal):
            title = str(title)

        # does this URI already have a fid?
        existing_fid = self.fids.get(uri)
        if existing_fid is not None:
            return existing_fid

        # if we get here, there is no fid, so make one
        def _remove_non_ascii_chars(s):
            return "".join(j for j in s if ord(j) < 128).replace("&", "")

        # try creating an ID from label
        # lowercase, remove spaces, escape all non-ASCII chars
        if title is not None:
            fid = _remove_non_ascii_chars(title.replace(" ", ""))

            # do not return fid if it's already in use
            if fid not in self.fids.values():
                self.fids[uri] = fid
                return fid

        # this fid is already present so generate a new one from the URI instead

        # split URI for last slash segment
        segments = uri.split("/")
        # return None for empty string - URI ends in slash
        if len(segments[-1]) < 1:
            return None

        # return None for domains, i.e. ['http:', '', '{domain}'] - no path segments
        if len(segments) < 4:
            return None

        # split out hash URIs
        # remove any training hashes
        if segments[-1].endswith("#"):
            return None

        fid = (
            segments[-1].split("#")[-1]
            if segments[-1].split("#")[-1] != ""
            else segments[-1].split("#")[-2]
        )
        # fid = fid.lower()

        # do not return fid if it's already in use
        if fid not in self.fids.values():
            self.fids[uri] = fid
            return fid
        else:
            # since it's in use but we've exhausted generation options, just add 1 to existing fid name
            self.fids[uri] = fid + "1"
            return fid + "1"  # yeah yeah, there could be more than one but unlikely


if __name__ == "__main__":
    sdo_json = """[
      {
        "@id": "https://example.com",
        "@type": [
          "https://schema.org/DefinedTermSet"
        ],
        "https://schema.org/description": [
          {
            "@value": "<p>This ontology contains several simple classes and properties about animals that are defined only to show off pyLODE's ability to represent different forms of example rendering.</p>"
          }
        ],
        "https://schema.org/license": [
          {
            "@id": "https://creativecommons.org/licenses/by/4.0/"
          }
        ],
        "https://schema.org/name": [
          {
            "@value": "Examples Ontology"
          }
        ],
        "https://schema.org/rights": [
          {
            "@value": "&copy; SURROUND Australia Pty Ltd"
          }
        ]
      }
    ]"""
    version = "3.0.0"

    od = OntDoc(ontology="agrif.ttl")
    od._make_document("Some Ont", sdo_json, version)
    open("some.html", "w").write(od.doc.render())
