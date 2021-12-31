from collections import defaultdict
from typing import Optional, List
import dominate
import markdown
import rdflib
from dominate.tags import *
from dominate.util import raw
from rdflib import BNode, Literal
from rdflib.paths import ZeroOrMore

from utils import *

RDF_FOLDER = Path(__file__).parent / "rdf"


class OntDoc:
    def __init__(self, ontology: Union[Graph, Path, str]):
        self.g = load_ontology(ontology)
        self._expand_graph_to_ontdoc_profile()

        self.background_onts = load_background_onts()
        self.background_onts_titles = load_background_onts_titles()
        self._get_property_labels()
        self.props_labeled = self._get_property_labels()

        self.toc = {}
        self.fids = {}
        self.default_namespace = self._get_default_namespace()

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

        # indicate Agent instances from properties
        for o in chain(
            self.g.objects(None, DCTERMS.publisher),
            self.g.objects(None, DCTERMS.creator),
            self.g.objects(None, DCTERMS.contributor)
        ):
            self.g.add((o, RDF.type, PROV.Agent))

        # Agent annotations
        for s, o in self.g.subject_objects(FOAF.name):
            self.g.add((s, SDO.name, o))

        for s, o in self.g.subject_objects(FOAF.mbox):
            self.g.add((s, SDO.email, o))

        for s, o in self.g.subject_objects(ORG.memberOf):
            self.g.add((s, SDO.affiliation, o))

    def _get_property_labels(self):
        pl = {}
        for prop in PROPS:
            pl[prop] = self._get_property_label(prop)
        return pl

    def _get_property_label(self, property_iri: URIRef) -> dict:
        title = None
        description = None
        ont_title = None
        for p, o in self.background_onts.predicate_objects(property_iri):
            if p == DCTERMS.title:
                title = o
            if p == DCTERMS.description:
                description = o
        for k, v in self.background_onts_titles.items():
            if property_iri.startswith(k):
                ont_title = v

        if title is None:
            title = make_title_from_iri(property_iri)

        return {
            "title": title,
            "description": description,
            "ont_title": ont_title,
        }

    def _make_fid(self, title: Literal, iri: URIRef):
        """Makes the fragment ID for a class, property, Named Individual (any entity) based on URI or name"""
        if isinstance(iri, URIRef):
            iri = str(iri)

        if isinstance(title, Literal):
            title = str(title)

        # does this URI already have a fid?
        existing_fid = self.fids.get(iri)
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
                self.fids[iri] = fid
                return fid

        # this fid is already present so generate a new one from the URI instead

        # split URI for last slash segment
        segments = iri.split("/")
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
            self.fids[iri] = fid
            return fid
        else:
            # since it's in use but we've exhausted generation options, just add 1 to existing fid name
            self.fids[iri] = fid + "1"
            return fid + "1"  # yeah yeah, there could be more than one but unlikely

    def _make_metadata(self):
        # get all ONT_PROPS props and their (multiple) values
        this_onts_props = defaultdict(list)
        for s in chain(
                self.g.subjects(predicate=RDF.type, object=OWL.Ontology),
                self.g.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
                self.g.subjects(predicate=RDF.type, object=PROF.Profile),
        ):
            for p, o in self.g.predicate_objects(s):
                if p in ONT_PROPS:
                    this_onts_props[p].append(o)

        # make HTML for all props in order of ONT_PROPS
        with self.content:
            with div(id="metadata", _class="section"):
                h1(this_onts_props[DCTERMS.title])
                with dl():
                    dt(strong("IRI"))
                    dd(code(str(s)))
                    for prop in ONT_PROPS:
                        if prop in this_onts_props.keys():
                            self._dl(
                                prop,
                                self.props_labeled[prop]["title"],
                                self.props_labeled[prop]["description"],
                                this_onts_props[prop],
                            )

    def _make_all_elements(self):
        with self.content:
            with div(id="classes", _class="section"):
                h2("Classes")
                self._make_elements(OWL.Class, CLASS_PROPS, "classes")

            with div(id="properties", _class="section"):
                h2("Properties")
                self._make_elements(RDF.Property, PROP_PROPS, "properties")

                with div(id="objectproperties", _class="section"):
                    h3("Object Properties")
                    self._make_elements(OWL.ObjectProperty, PROP_PROPS, "objectproperties")

                with div(id="datatypeproperties", _class="section"):
                    h3("Datatype Properties")
                    self._make_elements(OWL.DatatypeProperty, PROP_PROPS, "datatypeproperties")

                with div(id="annotationproperties", _class="section"):
                    h3("Annotation Properties")
                    self._make_elements(OWL.AnnotationProperty, PROP_PROPS, "annotationproperties")

                with div(id="functionalproperties", _class="section"):
                    h3("Functional Properties")
                    self._make_elements(OWL.FunctionalProperty, PROP_PROPS, "functionalproperties")

    def _make_elements(self, obj_class: URIRef, prop_list: list, toc_ul_id: str):
        # get all objects of this class
        for s in self.g.subjects(predicate=RDF.type, object=obj_class):
            if obj_class == RDF.Property:
                specialised_props = [
                    (s, RDF.type, OWL.ObjectProperty),
                    (s, RDF.type, OWL.DatatypeProperty),
                    (s, RDF.type, OWL.AnnotationProperty),
                    (s, RDF.type, OWL.FunctionalProperty),
                ]
                if any(x in self.g for x in specialised_props):
                    continue
            if isinstance(s, URIRef):  # ignore blank nodes for things like [ owl:unionOf ( ... ) ]
                this_props = defaultdict(list)
                # get all properties of this object
                for p, o in self.g.predicate_objects(subject=s):
                    # ... in the property list for this class
                    if p in prop_list:
                        if p == RDFS.subClassOf and (o, RDF.type, OWL.Restriction) in self.g:
                            this_props[ONTDOC.restriction].append(o)
                        else:
                            this_props[p].append(o)
                if len(this_props[DCTERMS.title]) == 0:
                    this_fid = self._make_fid(None, s)
                    this_title = make_title_from_iri(s)
                else:
                    this_fid = self._make_fid(this_props[DCTERMS.title][0], s)
                    this_title = this_props[DCTERMS.title]

                # add to ToC
                if self.toc.get(toc_ul_id) is None:
                    self.toc[toc_ul_id] = []
                self.toc[toc_ul_id].append(("#" + this_fid, this_title))

                # create properties table
                self._property_table(s, this_fid, this_title, obj_class, prop_list, this_props)

    def _property_table(self, iri, fid, title, ont_type, props_list, this_props):
        d = div(id=fid, _class="property entity")
        with d:
            h3(title, sup(ONT_TYPES[ont_type][0], _class="sup-" + ONT_TYPES[ont_type][0], title=ONT_TYPES[ont_type][1]))
            with table():
                with tr():
                    th("IRI")
                    td(code(str(iri)))
                # order the properties as per PROP_PROPS list order
                for prop in props_list:
                    if prop != DCTERMS.title:
                        if prop in this_props.keys():
                            self._table_row(
                                prop,
                                self.props_labeled[prop]["title"],
                                self.props_labeled[prop]["description"],
                                self.props_labeled[prop]["ont_title"],
                                this_props[prop]
                            )
        return d

    def _table_row(
        self,
        property_iri: URIRef,
        property_title: Literal,
        property_description: Literal,
        ont_title: Literal,
        obj: Union[list, URIRef, BNode, Literal],
        obj_type: Optional[str] = None
    ):
        t = tr()
        t.appendChild(
            th(
                a(
                    str(property_title).title(),
                    title=str(property_description).rstrip(".") + ". Defined in " + str(ont_title),
                    _class="hover_property",
                    href=str(property_iri),
                )
            )
        )
        t.appendChild(
            td(
                self._rdf_obj_multi(obj, obj_type=obj_type)
            )
        )
        return t

    def _dl(
        self,
        property_iri: URIRef,
        property_title: Literal,
        property_description: Literal,
        obj: Union[list, URIRef, BNode, Literal],
        obj_type: Optional[str] = None
    ):
        dt(
            a(
                str(property_title).title(),
                title=str(property_description),
                _class="hover_property",
                href=str(property_iri),
            )
        )
        dd(
            self._rdf_obj_multi(obj, obj_type=obj_type)
        )

    def _rdf_obj(self, obj: Union[URIRef, BNode, Literal], obj_type=None):
        if (obj, RDF.type, PROV.Agent) in self.g:
            return self._agent(obj)
        else:
            if isinstance(obj, URIRef):
                return self._hyperlink(obj, rdf_type=obj_type)
            elif isinstance(obj, BNode):
                # we can only handle BNs that are Agents (above) or Restrictions
                return self._restriction(obj)
            elif isinstance(obj, Literal):
                if str(obj).startswith("http"):
                    return self._hyperlink(obj)
            return raw(markdown.markdown(str(obj)))

    def _rdf_obj_multi(self, obj: List[Union[URIRef, BNode, Literal]], obj_type=None):
        if len(obj) == 1:
            return self._rdf_obj(obj[0], obj_type=obj_type)
        else:
            u = ul()
            for x in obj:
                u.appendChild(li(self._rdf_obj(x, obj_type=obj_type)))
            return u

    def _hyperlink(self, iri, rdf_type: Optional[URIRef] = None):
        try:
            qname = self.g.compute_qname(iri, True)
        except ValueError:
            qname = iri

        # find type
        if rdf_type is None:
            rdf_type = self._get_ont_type(iri)

        prefix = "" if qname[0] == "" else f'{qname[0]}:'
        if str(iri).startswith(self.default_namespace):
            iri = "#" + self._make_fid(None, iri)

        if rdf_type is not None:
            ret = span()
            ret.appendChild(a(f'{prefix}{qname[2]}', href=iri))
            ret.appendChild(sup(ONT_TYPES[rdf_type][0], _class="sup-" + ONT_TYPES[rdf_type][0], title=ONT_TYPES[rdf_type][1]))
            return ret
        else:
            if isinstance(qname, tuple):
                return a(f'{prefix}{qname[2]}', href=iri)
            return a(f'{qname}', href=iri)

    def _get_ont_type(self, iri):
        rdf_types = []
        for o in self.g.objects(iri, RDF.type):
            if o in ONT_TYPES.keys():
                rdf_types.append(o)

        if OWL.ObjectProperty in rdf_types:
            return OWL.ObjectProperty
        elif OWL.DatatypeProperty in rdf_types:
            return OWL.DatatypeProperty
        elif OWL.AnnotationProperty in rdf_types:
            return OWL.AnnotationProperty
        elif OWL.FunctionalProperty in rdf_types:
            return OWL.FunctionalProperty
        elif OWL.InverseFunctionalProperty in rdf_types:
            return OWL.InverseFunctionalProperty
        elif OWL.InverseFunctionalProperty in rdf_types:
            return OWL.InverseFunctionalProperty
        elif RDF.Property in rdf_types:
            return RDF.Property
        elif OWL.Class in rdf_types:
            return OWL.Class

        rdf_types = []
        for o in self.background_onts.objects(iri, RDF.type):
            if o in ONT_TYPES.keys():
                rdf_types.append(o)
        if OWL.ObjectProperty in rdf_types:
            return OWL.ObjectProperty
        elif OWL.DatatypeProperty in rdf_types:
            return OWL.DatatypeProperty
        elif OWL.AnnotationProperty in rdf_types:
            return OWL.AnnotationProperty
        elif OWL.FunctionalProperty in rdf_types:
            return OWL.FunctionalProperty
        elif OWL.InverseFunctionalProperty in rdf_types:
            return OWL.InverseFunctionalProperty
        elif OWL.InverseFunctionalProperty in rdf_types:
            return OWL.InverseFunctionalProperty
        elif RDF.Property in rdf_types:
            return RDF.Property
        elif OWL.Class in rdf_types:
            return OWL.Class

        return None

    def _agent(self, obj: Union[URIRef, BNode, Literal]):
        if isinstance(obj, Literal):
            return str(obj)
        honorific_prefix = None
        name = None
        identifier = None
        orcid = None
        orcid_logo = """
                <svg width="15px" height="15px" viewBox="0 0 72 72" version="1.1"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink">
                    <title>Orcid logo</title>
                    <g id="Symbols" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <g id="hero" transform="translate(-924.000000, -72.000000)" fill-rule="nonzero">
                            <g id="Group-4">
                                <g id="vector_iD_icon" transform="translate(924.000000, 72.000000)">
                                    <path d="M72,36 C72,55.884375 55.884375,72 36,72 C16.115625,72 0,55.884375 0,36 C0,16.115625 16.115625,0 36,0 C55.884375,0 72,16.115625 72,36 Z" id="Path" fill="#A6CE39"></path>
                                    <g id="Group" transform="translate(18.868966, 12.910345)" fill="#FFFFFF">
                                        <polygon id="Path" points="5.03734929 39.1250878 0.695429861 39.1250878 0.695429861 9.14431787 5.03734929 9.14431787 5.03734929 22.6930505 5.03734929 39.1250878"></polygon>
                                        <path d="M11.409257,9.14431787 L23.1380784,9.14431787 C34.303014,9.14431787 39.2088191,17.0664074 39.2088191,24.1486995 C39.2088191,31.846843 33.1470485,39.1530811 23.1944669,39.1530811 L11.409257,39.1530811 L11.409257,9.14431787 Z M15.7511765,35.2620194 L22.6587756,35.2620194 C32.49858,35.2620194 34.7541226,27.8438084 34.7541226,24.1486995 C34.7541226,18.1301509 30.8915059,13.0353795 22.4332213,13.0353795 L15.7511765,13.0353795 L15.7511765,35.2620194 Z" id="Shape"></path>
                                        <path d="M5.71401206,2.90182329 C5.71401206,4.441452 4.44526937,5.72914146 2.86638958,5.72914146 C1.28750978,5.72914146 0.0187670918,4.441452 0.0187670918,2.90182329 C0.0187670918,1.33420133 1.28750978,0.0745051096 2.86638958,0.0745051096 C4.44526937,0.0745051096 5.71401206,1.36219458 5.71401206,2.90182329 Z" id="Path"></path>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </svg>"""
        url = None
        email = None
        affiliation = None

        for px, o in self.g.predicate_objects(obj):
            if px in AGENT_PROPS:
                if px == SDO.name:
                    name = str(o)
                elif px == SDO.honorificPrefix:
                    honorific_prefix = str(o)
                elif px == SDO.identifier:
                    identifier = str(o)
                    if "orcid.org" in str(o):
                        orcid = True
                elif px == SDO.url:
                    url = str(o)
                elif px == SDO.email:
                    email = str(o)
                elif px == SDO.affiliation:
                    affiliation = o

        p = span()
        with p:
            if name is not None:
                if honorific_prefix is not None:
                    name = honorific_prefix + " " + name

                if url is not None:
                    a(name, href=url)
                else:
                    span(name)

                if orcid:
                    a(raw(orcid_logo), href=identifier)
                elif identifier is not None:
                    a(identifier, href=identifier)

                if email is not None:
                    email = email.replace("mailto:", "")
                    span("(", a(email, href="mailto:" + email), ")")

                if affiliation is not None:
                    self._affiliation(affiliation)
        return p

    def _affiliation(self, obj):
        name = None
        url = None

        for px, o in self.g.predicate_objects(obj):
            if px in AGENT_PROPS:
                if px == SDO.name:
                    name = str(o)
                elif px == SDO.url:
                    url = str(o)

        p = span()
        with p:
            if name is not None:
                if url is not None:
                    em(" of ", a(name, href=url))
                else:
                    em(" of ", name)
            else:
                if "http" in obj:
                    em(" of ", a(obj, href=obj))
        return p

    def _restriction(self, obj: BNode):
        prop = None
        card = None
        cls = None

        for px, o in self.g.predicate_objects(obj):
            if px != RDF.type:
                if px == OWL.onProperty:
                    prop = self._hyperlink(o)
                elif px in RESTRICTION_TYPES:
                    if px in [
                        OWL.minCardinality, OWL.minQualifiedCardinality,
                        OWL.maxCardinality, OWL.maxQualifiedCardinality,
                        OWL.cardinality, OWL.qualifiedCardinality
                    ]:
                        if px in [OWL.minCardinality, OWL.minQualifiedCardinality]:
                            card = "min"
                        elif px in [OWL.maxCardinality, OWL.maxQualifiedCardinality]:
                            card = "max"
                        elif px in [OWL.cardinality, OWL.qualifiedCardinality]:
                            card = "exactly"

                        card = span(span(card, _class="cardinality"), span(str(o)))
                    else:
                        if px == OWL.allValuesFrom:
                            card = "only"
                        elif px == OWL.someValuesFrom:
                            card = "some"
                        elif px == OWL.hasValue:
                            card = "value"

                        if type(o) == BNode:  # this is a Union or Intersection class - a list
                            # what is the nature of the list join?
                            t = None
                            for p2, o2 in self.g.predicate_objects(o):
                                if p2 == OWL.unionOf:
                                    t = ' <span class="cardinality">or</span> '
                                elif p2 == OWL.intersectionOf:
                                    t = ' <span class="cardinality">and</span> '

                            # must iterate through RDF list to get members using property path
                            col_members = set()
                            for s3, o3 in self.g.subject_objects(RDF.rest*ZeroOrMore / RDF.first):
                                if str(o3).startswith(self.default_namespace):
                                    iri = "#" + self._make_fid(None, o3)
                                else:
                                    iri = o3
                                col_members.add(f'<a href="{iri}">{self.g.qname(o3)}</a><sup class="sup-c" style="margin-left:1px;">c</sup>')
                            col = " (" + t.join([x for x in sorted(col_members)]) + ")"
                            card = span(span(card, _class="cardinality"), raw(col))
                        else:
                            card = span(span(card, _class="cardinality"), span(self._hyperlink(o, OWL.Class)))

        restriction = span(prop, card, br()) if card is not None else prop
        restriction = span(restriction, cls, br()) if cls is not None else restriction

        return span(restriction)

    def _make_document(self, title, schema_org_json, version):
        self.doc.title = title
        self._make_header(schema_org_json)
        self._make_body(version)

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

    def _make_body(self, version):
        self._make_pylode_logo(version)
        self._make_metadata()
        self._make_all_elements()
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
                            td(
                                sup(
                                    "op", _class="sup-op", title="OWL Object Property"
                                )
                            )
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

    def _get_default_namespace(self):
        # if this ontology declares a preferred URI, use that
        prefn_iri = None
        for s, o in self.g.subject_objects(
            predicate=VANN.preferredNamespaceUri
        ):
            prefn_iri = str(o)

        prefn_prefix = None
        for s, o in self.g.subject_objects(
            predicate=VANN.preferredNamespacePrefix
        ):
            prefn_prefix = str(o)
        if prefn_prefix is None:
            prefn_prefix = ""

        if prefn_iri is not None:
            return prefn_prefix, prefn_iri

        # if not, try the URI of the main object, compared to all prefixes
        else:
            default_iri = None

            for s in chain(
                self.g.subjects(predicate=RDF.type, object=OWL.Ontology),
                self.g.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
                self.g.subjects(predicate=RDF.type, object=PROF.Profile),
            ):
                default_iri = str(s)

            if default_iri is not None:
                prefix = self.g.compute_qname(default_iri, True)[0]
                if prefix is not None:
                    return prefix, default_iri
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
                    if self.toc.get("namespaces") is None:
                        self.toc["namespaces"] = []
                    for prefix, ns in sorted(nses.items()):
                        p = prefix if prefix != "" else ":"
                        dt(p, id=p)
                        dd(code(ns))
                        self.toc["namespaces"].append(("#" + prefix, prefix))

    def _make_toc(self):
        with self.doc:
            with div(id="toc"):
                h3("Table of Contents")
                with ul(_class="first"):
                    li(h4(a("Metadata", href="#metadata")))

                    if self.toc.get("classes") is not None and len(self.toc["classes"]) > 0:
                        with li():
                            h4(a("Classes", href="#classes"))
                            with ul(_class="second"):
                                for c in self.toc["classes"]:
                                    li(a(c[1], href=c[0]))

                    if self.toc.get("properties") is not None and len(self.toc["properties"]) > 0:
                        with li():
                            h4(a("Properties", href="#properties"))
                            with ul(_class="second"):
                                for c in self.toc["properties"]:
                                    li(a(c[1], href=c[0]))

                    if self.toc.get("objectproperties") is not None and len(self.toc["objectproperties"]) > 0:
                        with li():
                            h4(a("Object Properties", href="#objectproperties"))
                            with ul(_class="second"):
                                for c in self.toc["objectproperties"]:
                                    li(a(c[1], href=c[0]))

                    if self.toc.get("datatypeproperties") is not None and len(self.toc["datatypeproperties"]) > 0:
                        with li():
                            h4(a("Datatype Properties", href="#datatypeproperties"))
                            with ul(_class="second"):
                                for c in self.toc["datatypeproperties"]:
                                    li(a(c[1], href=c[0]))

                    if self.toc.get("annotationproperties") is not None and len(self.toc["annotationproperties"]) > 0:
                        with li():
                            h4(a("Annotation Properties", href="#annotationproperties"))
                            with ul(_class="second"):
                                for c in self.toc["annotationproperties"]:
                                    li(a(c[1], href=c[0]))

                    if self.toc.get("functionalproperties") is not None and len(self.toc["functionalproperties"]) > 0:
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


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

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

    # import cProfile
    #
    # pr = cProfile.Profile()
    # pr.enable()
    #
    # check_all_props_are_known()
    #
    # pr.disable()
    # pr.print_stats(sort='time')
