import logging
import pickle
import re
from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import Optional, List
from typing import Union

import markdown
from dominate.tags import a, span, br, sup, tr, th, td, ul, li, em, code, table, h3, div, dt, dd
from dominate.util import raw, text
from rdflib import BNode, Literal
from rdflib import Graph, URIRef, Dataset
from rdflib.paths import ZeroOrMore

from properties import *

RDF_FOLDER = Path(__file__).parent / "rdf"


def elements_html(g, background_g, ns, obj_class: URIRef, prop_list: list, toc, toc_ul_id: str, fids, props_labeled):
    # get all objects of this class
    for s_ in g.subjects(predicate=RDF.type, object=obj_class):
        if obj_class == RDF.Property:
            specialised_props = [
                (s_, RDF.type, OWL.ObjectProperty),
                (s_, RDF.type, OWL.DatatypeProperty),
                (s_, RDF.type, OWL.AnnotationProperty),
                (s_, RDF.type, OWL.FunctionalProperty),
            ]
            if any(x in g for x in specialised_props):
                continue
        if isinstance(s_, URIRef):  # ignore blank nodes for things like [ owl:unionOf ( ... ) ]
            this_props = defaultdict(list)
            # get all properties of this object
            for p_, o in g.predicate_objects(subject=s_):
                # ... in the property list for this class
                if p_ in prop_list:
                    if p_ == RDFS.subClassOf and (o, RDF.type, OWL.Restriction) in g:
                        this_props[ONTDOC.restriction].append(o)
                    else:
                        this_props[p_].append(o)
            if len(this_props[DCTERMS.title]) == 0:
                this_fid = _generate_fid(None, s_, fids)
                this_title = make_title_from_iri(s_)
            else:
                this_fid = _generate_fid(this_props[DCTERMS.title][0], s_, fids)
                this_title = this_props[DCTERMS.title]

            # add to ToC
            if toc.get(toc_ul_id) is None:
                toc[toc_ul_id] = []
            toc[toc_ul_id].append(("#" + this_fid, this_title))

            # create properties table
            _prop_table_html(g, background_g, ns, s_, this_fid, this_title, obj_class, prop_list, this_props, fids, props_labeled)


def check_all_props_are_known():
    bg = load_background_onts()
    for prop in PROPS:
        if (prop, RDF.type, None) not in bg:
            print(f"Unknown property: {prop}")
            print(f'Estimating title as "{make_title_from_iri(prop)}"')
            print()


def label_props(background_g):
    pl = {}
    for prop in PROPS:
        pl[prop] = get_prop_label(prop, background_g)
    return pl


def get_prop_label(property_iri: URIRef, background_g) -> dict:
    title_ = None
    description = None
    ont_title = None
    for p_, o in background_g.predicate_objects(property_iri):
        if p_ == DCTERMS.title:
            title_ = o
        if p_ == DCTERMS.description:
            description = o
    background_g_titles = load_background_onts_titles()
    for k, v in background_g_titles.items():
        if property_iri.startswith(k):
            ont_title = v

    if title_ is None:
        title_ = make_title_from_iri(property_iri)

    return {
        "title": title_,
        "description": description,
        "ont_title": ont_title,
    }


def get_ns(g):
    # if this ontology declares a preferred URI, use that
    prefn_iri = None
    for s_, o in g.subject_objects(
        predicate=VANN.preferredNamespaceUri
    ):
        prefn_iri = str(o)

    prefn_prefix = None
    for s_, o in g.subject_objects(
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

        for s_ in chain(
            g.subjects(predicate=RDF.type, object=OWL.Ontology),
            g.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
            g.subjects(predicate=RDF.type, object=PROF.Profile),
        ):
            default_iri = str(s_)

        if default_iri is not None:
            prefix = g.compute_qname(default_iri, True)[0]
            if prefix is not None:
                return prefix, default_iri
        else:
            # can't find either a declared or default namespace so we have an error
            raise Exception(
                "pyLODE can't detect a URI for an owl:Ontology, a skos:ConceptScheme or a prof:Profile"
            )


def make_title_from_iri(iri):
    if isinstance(iri, URIRef):
        iri = str(iri)
    # can't tolerate any URI faults so return None if anything is wrong

    # URIs with no path segments or ending in slash
    segments = iri.split("/")
    if len(segments[-1]) < 1:
        return None

    # URIs with only a domain - no path segments
    if len(segments) < 4:
        return None

    # URIs ending in hash
    if segments[-1].endswith("#"):
        return None

    id_part = segments[-1].split("#")[-1] if segments[-1].split("#")[-1] != "" else segments[-1].split("#")[-2]

    # split CamelCase
    return " ".join(re.split(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", id_part)).title()


def load_ontology(ontology: Union[Graph, Path, str]) -> Dataset:
    d = Dataset()
    if isinstance(ontology, Graph):
        g = Graph(identifier=URIRef("ont"))
        g += ontology
        return d.add_graph(g)
    elif isinstance(ontology, Path):
        return d.parse(ontology, publicID=URIRef("ont"))
    elif isinstance(ontology, str):
        # see if it's a file path
        if Path(ontology).is_file():
            return d.parse(ontology, publicID=URIRef("ont"))
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
            return d.parse(data=ontology, format=input_format, publicID=URIRef("ont"))
    else:
        raise ValueError(
            "The ontology you supply to OntDoc must be either an RDFlib Graph, a Path (to an RDF file) "
            "or a string (of RDF data)"
        )


def load_background_onts():
    if Path(RDF_FOLDER / "refs.pickle").is_file():
        logging.info("Loading background ontologies from a pickle file")
        with open(RDF_FOLDER / "refs.pickle", "rb") as f:
            return pickle.load(f)
    else:
        logging.info("Loading background ontologies from RDF files")
        g = _parse_background_onts()
        _expand_background_onts_graph(g)
        pickle_background_onts(g)
        return g


def load_background_onts_titles():
    if Path(RDF_FOLDER / "refs_titles.pickle").is_file():
        with open(RDF_FOLDER / "refs_titles.pickle", "rb") as f:
            return pickle.load(f)
    else:
        t = get_background_ontology_titles(load_background_onts())
        pickle_background_onts_titles(t)
        return t


def _parse_background_onts():
    g = Graph()
    for f in RDF_FOLDER.glob("*.ttl"):
        g.parse(f)

    return g


def _expand_background_onts_graph(g):
    # make regular titles
    for s_, o in chain(
        g.subject_objects(DC.title),
        g.subject_objects(RDFS.label),
        g.subject_objects(SKOS.prefLabel),
        g.subject_objects(SDO.name),
    ):
        g.add((s_, DCTERMS.title, o))

    # make regular descriptions
    for s_, o in chain(
        g.subject_objects(DC.description),
        g.subject_objects(RDFS.comment),
        g.subject_objects(SKOS.definition),
        g.subject_objects(SDO.description),
    ):
        g.add((s_, DCTERMS.description, o))


def _generate_fid(title_: Union[Literal, None], iri: URIRef, fids: dict):
    """Makes the fragment ID for a class, property, Named Individual (any entity) based on URI or name"""
    s_iri = str(iri)
    s_title_ = str(title_)

    # does this URI already have a fid?
    existing_fid = fids.get(iri)
    if existing_fid is not None:
        return existing_fid

    # if we get here, there is no fid, so make one
    def _remove_non_ascii_chars(s_):
        return "".join(j for j in s_ if ord(j) < 128).replace("&", "")

    # try creating an ID from label
    # lowercase, remove spaces, escape all non-ASCII chars
    if s_title_ is not None:
        fid = _remove_non_ascii_chars(s_title_.replace(" ", ""))

        # do not return fid if it's already in use
        if fid not in fids.values():
            fids[s_iri] = fid
            return fid

    # this fid is already present so generate a new one from the URI instead

    # split URI for last slash segment
    segments = s_iri.split("/")
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
    if fid not in fids.values():
        fids[s_iri] = fid
        return fid
    else:
        # since it's in use but we've exhausted generation options, just add 1 to existing fid name
        fids[s_iri] = fid + "1"
        return fid + "1"  # yeah yeah, there could be more than one but unlikely


def get_background_ontology_titles(g):
    onts_titles = {}
    for s_ in g.subjects(predicate=RDF.type, object=OWL.Ontology):
        for o in g.objects(subject=s_, predicate=DCTERMS.title):
            onts_titles[str(s_)] = str(o)

    return {k: v for k, v in sorted(onts_titles.items(), key=lambda item: item[1])}


def pickle_background_onts(g):
    with open(RDF_FOLDER / "refs.pickle", "wb") as f:
        pickle.dump(g, f)


def pickle_background_onts_titles(ont_titles):
    with open(RDF_FOLDER / "refs_titles.pickle", "wb") as f:
        pickle.dump(ont_titles, f)


def prop_obj_pair_html(
    g,
    background_g,
    ns,
    table_or_dl: str,
    property_iri: URIRef,
    property_title: Literal,
    property_description: Literal,
    ont_title: Literal,
    fids,
    obj: List[Union[URIRef, BNode, Literal]],
    obj_type: Optional[str] = None
):
    prop = a(
        str(property_title).title(),
        title=str(property_description).rstrip(".") + ". Defined in " + str(ont_title),
        _class="hover_property",
        href=str(property_iri),
    )
    o = _rdf_obj_multi_html(g, background_g, ns, obj, fids, obj_type=obj_type)

    if table_or_dl == "table":
        t = tr(th(prop), td(o))
    else:  # dl
        t = div(dt(prop), dd(o))

    return t


def _prop_table_html(g, background_g, ns, iri, fid, title_, ont_type, props_list, this_props, fids, props_labeled):
    d = div(
        h3(
            title_,
            sup(ONT_TYPES[ont_type][0], _class="sup-" + ONT_TYPES[ont_type][0], title=ONT_TYPES[ont_type][1])
        ),
        id=fid,
        _class="property entity"
    )
    t = table(tr(th("IRI"), td(code(str(iri)))))
    # order the properties as per PROP_PROPS list order
    for prop in props_list:
        if prop != DCTERMS.title:
            if prop in this_props.keys():
                t.appendChild(
                    prop_obj_pair_html(
                        g,
                        background_g,
                        ns,
                        "table",
                        prop,
                        props_labeled[prop]["title"],
                        props_labeled[prop]["description"],
                        props_labeled[prop]["ont_title"],
                        fids,
                        this_props[prop]
                    )
                )
    d.appendChild(t)
    return d


def _rdf_obj_html(g: Graph, background_g, ns, obj: Union[URIRef, BNode, Literal], fids, obj_type=None):
    if (obj, RDF.type, PROV.Agent) in g:
        return _agent_html(g, obj)
    else:
        if isinstance(obj, URIRef):
            return _hyperlink_html(g, background_g, ns, obj, fids, rdf_type=obj_type)
        elif isinstance(obj, BNode):
            # we can only handle BNs that are Agents (above) or Restrictions
            return _restriction_html(g, ns, background_g, fids, obj)
        else:  # isinstance(obj, Literal):
            if str(obj).startswith("http"):
                return _hyperlink_html(g, background_g, ns, obj, fids)
            else:
                return raw(markdown.markdown(str(obj)))


def _rdf_obj_multi_html(g, background_g, ns, obj: List[Union[URIRef, BNode, Literal]], fids, obj_type=None):
    if len(obj) == 1:
        return _rdf_obj_html(g, background_g, ns, obj[0], fids, obj_type=obj_type)
    else:
        u_ = ul()
        for x in obj:
            u_.appendChild(li(_rdf_obj_html(g, background_g, ns, x, fids, obj_type=obj_type)))
        return u_


def _hyperlink_html(g, background_g, ns, iri, fids, rdf_type: Optional[URIRef] = None):
    try:
        qname = g.compute_qname(iri, True)
    except ValueError:
        qname = iri

    # find type
    if rdf_type is None:
        rdf_type = _get_ont_type(g, background_g, iri)

    prefix = "" if qname[0] == "" else f'{qname[0]}:'
    if str(iri).startswith(ns):
        iri = "#" + _generate_fid(None, iri, fids)

    if rdf_type is not None:
        ret = span()
        ret.appendChild(a(f'{prefix}{qname[2]}', href=iri))
        ret.appendChild(
            sup(ONT_TYPES[rdf_type][0], _class="sup-" + ONT_TYPES[rdf_type][0], title=ONT_TYPES[rdf_type][1]))
        return ret
    else:
        if isinstance(qname, tuple):
            return a(f'{prefix}{qname[2]}', href=iri)
        return a(f'{qname}', href=iri)


def _get_ont_type(g, background_g, iri):
    types_we_know = [
        OWL.Class,
        OWL.ObjectProperty,
        OWL.DatatypeProperty,
        OWL.AnnotationProperty,
        OWL.FunctionalProperty,
        RDF.Property
    ]

    this_objects_types = []
    for o in g.objects(iri, RDF.type):
        if o in ONT_TYPES.keys():
            this_objects_types.append(o)

    for x in types_we_know:
        if x in this_objects_types:
            return x

    for o in background_g.objects(iri, RDF.type):
        if o in ONT_TYPES.keys():
            this_objects_types.append(o)

    for x in types_we_know:
        if x in this_objects_types:
            return x


def _agent_html(g, obj: Union[URIRef, BNode, Literal]):
    if isinstance(obj, Literal):
        return span(str(obj))
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

    for px, o in g.predicate_objects(obj):
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

    sp = span()

    if name is not None:
        if honorific_prefix is not None:
            name = honorific_prefix + " " + name

        if url is not None:
            sp.appendChild(a(name, href=url))
        else:
            sp.appendChild(span(name))

        if orcid:
            sp.appendChild(a(raw(orcid_logo), href=identifier))
        elif identifier is not None:
            sp.appendChild(a(identifier, href=identifier))

        if email is not None:
            email = email.replace("mailto:", "")
            sp.appendChild(span("(", a(email, href="mailto:" + email), ")"))

        if affiliation is not None:
            sp.appendChild(_affiliation_html(g, affiliation))
    return sp


def _affiliation_html(g, obj):
    name = None
    url = None

    for px, o in g.predicate_objects(obj):
        if px in AGENT_PROPS:
            if px == SDO.name:
                name = str(o)
            elif px == SDO.url:
                url = str(o)

    sp = span()
    if name is not None:
        if url is not None:
            sp.appendChild(em(" of ", a(name, href=url)))
        else:
            sp.appendChild(em(" of ", name))
    else:
        if "http" in obj:
            sp.appendChild(em(" of ", a(obj, href=obj)))
    return sp


def _restriction_html(g, ns, background_g, fids, obj: BNode):
    prop = None
    card = None
    cls = None

    for px, o in g.predicate_objects(obj):
        if px != RDF.type:
            if px == OWL.onProperty:
                prop = _hyperlink_html(g, background_g, ns, o, fids)
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
                        t = ' <span class="cardinality">and</span> '
                        for p2, o2 in g.predicate_objects(o):
                            if p2 == OWL.unionOf:
                                t = ' <span class="cardinality">or</span> '
                            # p2 == OWL.intersectionOf:

                        # must iterate through RDF list to get members using property path
                        col_members = set()
                        for s3, o3 in g.subject_objects(RDF.rest*ZeroOrMore / RDF.first):
                            if str(o3).startswith(ns):
                                iri = "#" + _generate_fid(None, o3, fids)
                            else:
                                iri = o3
                            col_members.add(
                                f'<a href="{iri}">{g.qname(o3)}</a><sup class="sup-c" style="margin-left:1px;">c</sup>')
                        col_ = " (" + t.join([x for x in sorted(col_members)]) + ")"
                        card = span(span(card, _class="cardinality"), raw(col_))
                    else:
                        card = span(
                            span(card, _class="cardinality"),
                            span(_hyperlink_html(g, background_g, ns, o, fids, OWL.Class))
                        )

    restriction = span(prop, card, br()) if card is not None else prop
    restriction = span(restriction, cls, br()) if cls is not None else restriction

    return span(restriction)
