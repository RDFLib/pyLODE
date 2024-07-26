import shutil
from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import Dict
from typing import Union

import dominate
from dominate.tags import (
    h2,
    h1,
    h4,
    style,
    link,
    meta,
    script,
    dl,
    strong,
    a,
    sup,
    tr,
    td,
    ul,
    li,
    code,
    table,
    h3,
    div,
    dt,
    dd,
)
from dominate.util import raw
from rdflib import Literal, Graph
from rdflib.namespace import (
    DC,
    DCTERMS,
    FOAF,
    ORG,
    OWL,
    PROF,
    PROV,
    RDF,
    RDFS,
    SDO,
    SKOS,
)

from pylode.utils import PylodeError

try:
    from .utils import (
        load_ontology,
        load_background_onts,
        load_background_onts_titles,
        back_onts_label_props,
        get_ns,
        prop_obj_pair_html,
        section_html,
        sort_ontology,
        make_pylode_logo,
    )

    from .rdf_elements import ONTDOC, AGENT_PROPS, ONT_PROPS, CLASS_PROPS, PROP_PROPS

    from .version import __version__
except ImportError:
    from pylode.utils import (
        load_ontology,
        load_background_onts,
        load_background_onts_titles,
        back_onts_label_props,
        get_ns,
        prop_obj_pair_html,
        section_html,
        sort_ontology,
        make_pylode_logo,
    )

    from pylode.rdf_elements import (
        ONTDOC,
        AGENT_PROPS,
        ONT_PROPS,
        CLASS_PROPS,
        PROP_PROPS,
    )

    from pylode.version import __version__

RDF_FOLDER = Path(__file__).parent / "rdf"


class OntPub:
    """Ontology Document class used to create HTML documentation
    from OWL Ontologies.

    Use:
        # initialise
        od = OntDoc(ontology="some-ontology-file.ttl")

        # produce HTML
        html = od.make_html()

        # or save HTML to a file
        od.make_html(destination="some-resulting-html-file.html")
    """

    def __init__(self, ontology: Union[Graph, Path, str], sort_subjects: bool = False):
        self.ont = load_ontology(ontology)
        if sort_subjects:
            self.ont = sort_ontology(self.ont)
        self._ontdoc_inference(self.ont)
        self.back_onts = load_background_onts()
        self.back_onts_titles = load_background_onts_titles(self.back_onts)
        self.props_labeled = back_onts_label_props(self.back_onts)

        self.toc: Dict[str, str] = {}
        self.fids: Dict[str, str] = {}
        self.ns = get_ns(self.ont)

        # make HTML doc with title
        t = None
        for s in chain(
            self.ont.subjects(RDF.type, OWL.Ontology),
            self.ont.subjects(RDF.type, PROF.Profile),
            self.ont.subjects(RDF.type, SKOS.ConceptScheme),
        ):
            for o2 in self.ont.objects(s, DCTERMS.title):
                t = str(o2)
        if t is None:
            raise PylodeError(
                "You MUST supply a title property "
                "(dcterms:title, rdfs:label or sdo:name) for your ontology"
            )
        self.doc = dominate.document(title=t)

        with self.doc:
            self.content = div(id="content")

    def make_html(self, destination: Path = None, include_css: bool = True):
        """Makes the complete OntDoc HTML document.

        Either writes to a file or returns a string"""
        self._make_head(
            self._make_schema_org(), include_css=include_css, destination=destination
        )
        self._make_body()

        if destination is not None:
            open(destination, "w", encoding="utf8").write(self.doc.render())
        else:
            return self.doc.render()

    def _ontdoc_inference(self, g):
        """Expands the ontology's graph to make OntDoc querying easier.

        Uses axioms made up for OntDoc, but they are simple and obvious
        and don't collide with well-known ontologies"""
        # class types
        for s_ in g.subjects(RDF.type, OWL.Class):
            g.add((s_, RDF.type, RDFS.Class))

        # # property types
        # for s_ in chain(
        #     g.subjects(RDF.type, OWL.ObjectProperty),
        #     g.subjects(RDF.type, OWL.FunctionalProperty),
        #     g.subjects(RDF.type, OWL.DatatypeProperty),
        #     g.subjects(RDF.type, OWL.AnnotationProperty),
        # ):
        #     g.add((s_, RDF.type, RDF.Property))

        # name
        for s_, o in chain(
            g.subject_objects(DC.title),
            g.subject_objects(RDFS.label),
            g.subject_objects(SKOS.prefLabel),
            g.subject_objects(SDO.name),
        ):
            g.add((s_, DCTERMS.title, o))

        # description
        for s_, o in chain(
            g.subject_objects(DC.description),
            g.subject_objects(RDFS.comment),
            g.subject_objects(SKOS.definition),
            g.subject_objects(SDO.description),
        ):
            g.add((s_, DCTERMS.description, o))

        # source
        for s_, o in g.subject_objects(DC.source):
            g.add((s_, DCTERMS.source, o))

        # license
        for s_, o in g.subject_objects(SDO.license):
            g.add((s_, DCTERMS.license, o))

        #
        #   Blank Node Types
        #
        for s_ in g.subjects(OWL.onProperty, None):
            g.add((s_, RDF.type, OWL.Restriction))

        for s_ in chain(
            g.subjects(OWL.unionOf, None), g.subjects(OWL.intersectionOf, None)
        ):
            g.add((s_, RDF.type, OWL.Class))

        # we do these next few so we only need to loop through
        # Class & Property properties once: single subject
        for s_, o in g.subject_objects(RDFS.subClassOf):
            g.add((o, ONTDOC.superClassOf, s_))

        for s_, o in g.subject_objects(RDFS.subPropertyOf):
            g.add((o, ONTDOC.superPropertyOf, s_))

        for s_, o in g.subject_objects(RDFS.domain):
            g.add((o, ONTDOC.inDomainOf, s_))

        for s_, o in g.subject_objects(SDO.domainIncludes):
            g.add((o, ONTDOC.inDomainIncludesOf, s_))

        for s_, o in g.subject_objects(RDFS.range):
            g.add((o, ONTDOC.inRangeOf, s_))

        for s_, o in g.subject_objects(SDO.rangeIncludes):
            g.add((o, ONTDOC.inRangeIncludesOf, s_))

        for s_, o in g.subject_objects(RDF.type):
            g.add((o, ONTDOC.hasMember, s_))

        #
        #   Agents
        #
        # creator
        for s_, o in chain(
            g.subject_objects(DC.creator),
            g.subject_objects(SDO.creator),
            g.subject_objects(SDO.author),
        ):
            g.remove((s_, DC.creator, o))
            g.remove((s_, SDO.creator, o))
            g.remove((s_, SDO.author, o))
            g.add((s_, DCTERMS.creator, o))

        # contributor
        for s_, o in chain(
            g.subject_objects(DC.contributor),
            g.subject_objects(SDO.contributor),
        ):
            g.remove((s_, DC.contributor, o))
            g.remove((s_, SDO.contributor, o))
            g.add((s_, DCTERMS.contributor, o))

        # publisher
        for s_, o in chain(
            g.subject_objects(DC.publisher), g.subject_objects(SDO.publisher)
        ):
            g.remove((s_, DC.publisher, o))
            g.remove((s_, SDO.publisher, o))
            g.add((s_, DCTERMS.publisher, o))

        # indicate Agent instances from properties
        for o in chain(
            g.objects(None, DCTERMS.publisher),
            g.objects(None, DCTERMS.creator),
            g.objects(None, DCTERMS.contributor),
        ):
            g.add((o, RDF.type, PROV.Agent))

        # Agent annotations
        for s_, o in g.subject_objects(FOAF.name):
            g.add((s_, SDO.name, o))

        for s_, o in g.subject_objects(FOAF.mbox):
            g.add((s_, SDO.email, o))

        for s_, o in g.subject_objects(ORG.memberOf):
            g.add((s_, SDO.affiliation, o))

    def _make_head(
        self, schema_org: Graph, include_css: bool = True, destination: Path = None
    ):
        """Healper function for make_html(). Makes <head>???</head> content"""
        with self.doc.head:
            # use standard pyLODE stylesheet
            if include_css:
                style(
                    raw(
                        "\n"
                        + open(Path(__file__).parent.parent / "pylode.css").read()
                        + "\n\t"
                    )
                )
            else:
                link(href="pylode.css", rel="stylesheet", type="text/css")
                shutil.copy(
                    Path(__file__).parent.parent / "pylode.css",
                    destination.parent / "pylode.css",
                )
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
            script(
                raw("\n" + schema_org.serialize(format="json-ld") + "\n\t"),
                type="application/ld+json",
                id="schema.org",
            )

    def _make_body(self):
        """Healper function for make_html(). Makes <body>???</body> content.

        Just calls other helper functions in order"""
        make_pylode_logo(
            self.doc, __version__, "OntPub", "https://w3id.org/profile/ontpub"
        )
        self._make_metadata()
        self._make_main_sections()
        self._make_namespaces()
        self._make_legend()
        self._make_toc()

    def _make_metadata(self):
        # get all ONT_PROPS props and their (multiple) values
        this_onts_props = defaultdict(list)
        for s_ in chain(
            self.ont.subjects(predicate=RDF.type, object=OWL.Ontology),
            self.ont.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
            self.ont.subjects(predicate=RDF.type, object=PROF.Profile),
        ):
            iri = s_
            for p_, o in self.ont.predicate_objects(s_):
                if p_ in ONT_PROPS:
                    this_onts_props[p_].append(o)

        # make HTML for all props in order of ONT_PROPS
        sec = div(h1(this_onts_props[DCTERMS.title]), id="metadata", _class="section")
        sec.appendChild(h2("Metadata"))
        d = dl(div(dt(strong("IRI")), dd(code(str(iri)))))
        for prop in ONT_PROPS:
            if prop in this_onts_props.keys():
                d.appendChild(
                    prop_obj_pair_html(
                        self.ont,
                        self.back_onts,
                        self.ns,
                        "dl",
                        prop,
                        self.props_labeled[prop]["title"],
                        self.props_labeled[prop]["description"],
                        self.props_labeled[prop]["ont_title"],
                        self.fids,
                        this_onts_props[prop],
                    )
                )
        sec.appendChild(d)
        self.content.appendChild(sec)

    def _make_schema_org(self):
        sdo = Graph()
        for ont_iri in chain(
            self.ont.subjects(predicate=RDF.type, object=OWL.Ontology),
            self.ont.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
            self.ont.subjects(predicate=RDF.type, object=PROF.Profile),
        ):
            sdo.add((ont_iri, RDF.type, SDO.DefinedTermSet))
            for p_, o in self.ont.predicate_objects(ont_iri):
                if p_ == DCTERMS.title:
                    sdo.add((ont_iri, SDO.name, o))
                elif p_ == DCTERMS.description:
                    sdo.add((ont_iri, SDO.description, o))
                elif p_ == DCTERMS.publisher:
                    sdo.add((ont_iri, SDO.publisher, o))
                    if not isinstance(o, Literal):
                        for p2, o2 in self.ont.predicate_objects(o):
                            if p2 in AGENT_PROPS:
                                sdo.add((o, p2, o2))
                elif p_ == DCTERMS.creator:
                    sdo.add((ont_iri, SDO.creator, o))
                    if not isinstance(o, Literal):
                        for p2, o2 in self.ont.predicate_objects(o):
                            if p2 in AGENT_PROPS:
                                sdo.add((o, p2, o2))
                elif p_ == DCTERMS.contributor:
                    sdo.add((ont_iri, SDO.contributor, o))
                    if not isinstance(o, Literal):
                        for p2, o2 in self.ont.predicate_objects(o):
                            if p2 in AGENT_PROPS:
                                sdo.add((o, p2, o2))
                elif p_ == DCTERMS.created:
                    sdo.add((ont_iri, SDO.dateCreated, o))
                elif p_ == DCTERMS.modified:
                    sdo.add((ont_iri, SDO.dateModified, o))
                elif p_ == DCTERMS.issued:
                    sdo.add((ont_iri, SDO.dateIssued, o))
                elif p_ == DCTERMS.license:
                    sdo.add((ont_iri, SDO.license, o))
                elif p_ == DCTERMS.rights:
                    sdo.add((ont_iri, SDO.copyrightNotice, o))

        return sdo

    def _make_main_sections(self):
        with self.content:
            if (None, RDF.type, OWL.Class) in self.ont:
                d = section_html(
                    "Classes",
                    self.ont,
                    self.back_onts,
                    self.ns,
                    OWL.Class,
                    CLASS_PROPS,
                    self.toc,
                    "classes",
                    self.fids,
                    self.props_labeled,
                )
                d.render()

            if (None, RDF.type, RDF.Property) in self.ont:
                d = section_html(
                    "Properties",
                    self.ont,
                    self.back_onts,
                    self.ns,
                    RDF.Property,
                    PROP_PROPS,
                    self.toc,
                    "properties",
                    self.fids,
                    self.props_labeled,
                )
                d.render()

            if (None, RDF.type, OWL.ObjectProperty) in self.ont:
                d = section_html(
                    "Object Properties",
                    self.ont,
                    self.back_onts,
                    self.ns,
                    OWL.ObjectProperty,
                    PROP_PROPS,
                    self.toc,
                    "objectproperties",
                    self.fids,
                    self.props_labeled,
                )
                d.render()

            if (None, RDF.type, OWL.DatatypeProperty) in self.ont:
                d = section_html(
                    "Datatype Properties",
                    self.ont,
                    self.back_onts,
                    self.ns,
                    OWL.DatatypeProperty,
                    PROP_PROPS,
                    self.toc,
                    "datatypeproperties",
                    self.fids,
                    self.props_labeled,
                )
                d.render()

            if (None, RDF.type, OWL.AnnotationProperty) in self.ont:
                d = section_html(
                    "Annotation Properties",
                    self.ont,
                    self.back_onts,
                    self.ns,
                    OWL.AnnotationProperty,
                    PROP_PROPS,
                    self.toc,
                    "annotationproperties",
                    self.fids,
                    self.props_labeled,
                )
                d.render()

            if (None, RDF.type, OWL.FunctionalProperty) in self.ont:
                d = section_html(
                    "Functional Properties",
                    self.ont,
                    self.back_onts,
                    self.ns,
                    OWL.FunctionalProperty,
                    PROP_PROPS,
                    self.toc,
                    "functionalproperties",
                    self.fids,
                    self.props_labeled,
                )
                d.render()

    def _make_legend(self):
        with self.content:
            with div(id="legend"):
                h2("Legend")
                with table(_class="entity"):

                    if self.toc.get("classes") is not None:
                        with tr():
                            td(sup("c", _class="sup-c", title="OWL/RDFS Class"))
                            td("Classes")
                    if self.toc.get("properties") is not None:
                        with tr():
                            td(sup("p", _class="sup-p", title="RDF Property"))
                            td("Properties")
                    if self.toc.get("objectproperties") is not None:
                        with tr():
                            td(sup("op", _class="sup-op", title="OWL Object Property"))
                            td("Object Properties")
                    if self.toc.get("datatypeproperties") is not None:
                        with tr():
                            td(
                                sup(
                                    "dp",
                                    _class="sup-dp",
                                    title="OWL Datatype Property",
                                )
                            )
                            td("Datatype Properties")
                    if self.toc.get("annotationproperties") is not None:
                        with tr():
                            td(
                                sup(
                                    "ap",
                                    _class="sup-ap",
                                    title="OWL Annotation Property",
                                )
                            )
                            td("Annotation Properties")
                    if self.toc.get("functionalproperties") is not None:
                        with tr():
                            td(
                                sup(
                                    "fp",
                                    _class="sup-fp",
                                    title="OWL Functional Property",
                                )
                            )
                            td("Functional Properties")
                    if self.toc.get("named_individuals") is not None:
                        with tr():
                            td(sup("ni", _class="sup-ni", title="OWL Named Individual"))
                            td("Named Individuals")

    def _make_namespaces(self):
        # only get namespaces used in ont
        nses = {}
        for n in chain(self.ont.subjects(), self.ont.predicates(), self.ont.objects()):
            # a list of prefixes we don't like
            excluded_namespaces = (
                # "https://linked.data.gov.au/def/"
            )
            if not str(n).startswith(excluded_namespaces):
                for prefix, ns in self.ont.namespaces():
                    if str(n).startswith(ns):
                        nses[prefix] = ns

        # # deduplicate namespaces
        # temp = []
        # res = dict()
        # for k, v in nses.items():
        #     if v not in temp:
        #         temp.append(v)
        #         res[k] = v
        # nses = res

        with self.content:
            with div(id="namespaces"):
                h2("Namespaces")
                with dl():
                    if self.toc.get("namespaces") is None:
                        self.toc["namespaces"] = []
                    for prefix, ns in sorted(nses.items()):
                        p_ = prefix if prefix != "" else ":"
                        dt(p_, id=p_)
                        dd(code(ns))
                        self.toc["namespaces"].append(("#" + prefix, prefix))

    def _make_toc(self):
        with self.doc:
            with div(id="toc"):
                h3("Table of Contents")
                with ul(_class="first"):
                    li(h4(a("Metadata", href="#metadata")))

                    if (
                        self.toc.get("classes") is not None
                        and len(self.toc["classes"]) > 0
                    ):
                        with li():
                            h4(a("Classes", href="#classes"))
                            with ul(_class="second"):
                                for c in self.toc["classes"]:
                                    li(a(c[1], href=c[0]))

                    if (
                        self.toc.get("properties") is not None
                        and len(self.toc["properties"]) > 0
                    ):
                        with li():
                            h4(a("Properties", href="#properties"))
                            with ul(_class="second"):
                                for c in self.toc["properties"]:
                                    li(a(c[1], href=c[0]))

                    if (
                        self.toc.get("objectproperties") is not None
                        and len(self.toc["objectproperties"]) > 0
                    ):
                        with li():
                            h4(a("Object Properties", href="#objectproperties"))
                            with ul(_class="second"):
                                for c in self.toc["objectproperties"]:
                                    li(a(c[1], href=c[0]))

                    if (
                        self.toc.get("datatypeproperties") is not None
                        and len(self.toc["datatypeproperties"]) > 0
                    ):
                        with li():
                            h4(a("Datatype Properties", href="#datatypeproperties"))
                            with ul(_class="second"):
                                for c in self.toc["datatypeproperties"]:
                                    li(a(c[1], href=c[0]))

                    if (
                        self.toc.get("annotationproperties") is not None
                        and len(self.toc["annotationproperties"]) > 0
                    ):
                        with li():
                            h4(a("Annotation Properties", href="#annotationproperties"))
                            with ul(_class="second"):
                                for c in self.toc["annotationproperties"]:
                                    li(a(c[1], href=c[0]))

                    if (
                        self.toc.get("functionalproperties") is not None
                        and len(self.toc["functionalproperties"]) > 0
                    ):
                        with li():
                            h4(a("Functional Properties", href="#functionalproperties"))
                            with ul(_class="second"):
                                for c in self.toc["functionalproperties"]:
                                    li(a(c[1], href=c[0]))

                    with li():
                        h4(a("Namespaces", href="#namespaces"))
                        with ul(_class="second"):
                            for n in self.toc["namespaces"]:
                                li(a(n[1], href="#" + n[1]))

                    li(h4(a("Legend", href="#legend")), ul(_class="second"))
