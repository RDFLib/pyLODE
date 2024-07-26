import logging
import pickle
import re
from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import Optional, List, Tuple, Union, cast

import markdown
from dominate.tags import (
    h2,
    br,
    th,
    em,
    pre,
    p,
    a,
    span,
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
from rdflib import BNode, Literal, Graph, URIRef
from rdflib.namespace import DC, DCTERMS, PROF, PROV, OWL, RDF, RDFS, SDO, SKOS, VANN
from rdflib.paths import ZeroOrMore

try:
    from .rdf_elements import (
        AGENT_PROPS,
        ONTDOC,
        ONT_TYPES,
        OWL_SET_TYPES,
        PROPS,
        RESTRICTION_TYPES,
    )
except ImportError:
    from rdf_elements import (
        AGENT_PROPS,
        ONTDOC,
        ONT_TYPES,
        OWL_SET_TYPES,
        PROPS,
        RESTRICTION_TYPES,
    )

RDF_FOLDER = Path(__file__).parent / "rdf"


def check_all_props_are_known():
    """Check all properties listed in the combined property lists in
    properties.py to see if their titles and descriptions are present in the
    background ontologies in the folder rdf/. Run after performing labelling
    inferencing."""
    bg = load_background_onts()
    for prop in PROPS:
        if (prop, RDF.type, None) not in bg:
            print(f"Unknown property: {prop}")
            print(f'Estimating title as "{make_title_from_iri(prop)}"')
            print()


def get_ns(ont: Graph) -> Tuple[str, str]:
    """Gets the default Namespace for the given graph (ontology)"""
    # if this ontology declares a preferred URI, use that
    pref_iri = None
    for s_, o in ont.subject_objects(predicate=VANN.preferredNamespaceUri):
        pref_iri = str(o)

    pref_prefix = None
    for s_, o in ont.subject_objects(predicate=VANN.preferredNamespacePrefix):
        pref_prefix = str(o)
    if pref_prefix is None:
        pref_prefix = ""

    if pref_iri is not None:
        return pref_prefix, pref_iri

    # if not, try the URI of the main object, compared to all prefixes
    else:
        default_iri = None

        for s_ in chain(
            ont.subjects(predicate=RDF.type, object=OWL.Ontology),
            ont.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
            ont.subjects(predicate=RDF.type, object=PROF.Profile),
        ):
            default_iri = str(s_)

        if default_iri is not None:
            prefix = ont.compute_qname(default_iri, True)[0]
            if prefix is not None:
                return prefix, default_iri
        else:
            # can't find either a declared or default namespace
            # so we have an error
            raise Exception(
                "pyLODE can't detect a URI for an owl:Ontology, "
                "a skos:ConceptScheme or a prof:Profile"
            )


def make_title_from_iri(iri: URIRef):
    """Makes a human-readable title for an RDF resource from its IRI"""
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

    id_part = (
        segments[-1].split("#")[-1]
        if segments[-1].split("#")[-1] != ""
        else segments[-1].split("#")[-2]
    )

    # split CamelCase
    # title case if the first char is upercase (likely a Class)
    # else lower (property/Named Individual)
    words = re.split(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", id_part)
    if words[0][0].isupper():
        return " ".join(words).title()
    else:
        return " ".join(words).lower()


def generate_fid(title_: Union[Literal, None], iri: URIRef, fids: dict):
    """Makes an HTML fragment ID for an RDF resource,
    based on title (preferred) or IRI"""
    s_iri = str(iri) if iri is not None else None
    s_title_ = str(title_) if title_ is not None else None

    # does this URI already have a fid?
    existing_fid = fids.get(s_iri)
    if existing_fid is not None:
        return existing_fid

    # if we get here, there is no fid, so make one
    def _remove_non_ascii_chars(s_):
        return "".join(j for j in s_ if ord(j) < 128).replace("&", "")

    # try creating an ID from label
    # remove spaces, escape all non-ASCII chars
    if s_title_ is not None:
        fid = _remove_non_ascii_chars(s_title_.replace(" ", ""))

        # if this generated fid is not in use, add it to fids and return it
        if fid not in fids.values():
            fids[s_iri] = fid
            return fid

        # this fid is already present
        # so generate a new one from the URI instead

    # split URI for last slash segment
    segments = s_iri.split("/")

    # return None for empty string - URI ends in slash
    if len(segments[-1]) < 1:
        return None

    # return None for domains, i.e. ['http:', '', '{domain}'],
    # no path segments
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

    # if this generated fid is not in use, add it to fids and return it
    if fid not in fids.values():
        fids[s_iri] = fid
        return fid
    else:
        # since it's in use but we've exhausted generation options,
        # just add 1 to existing fid name
        fids[s_iri] = fid + "1"
        return fid + "1"
        # yeah yeah, there could be more than one but unlikely


def back_onts_label_props(back_onts: Graph):
    """Gets titles and descriptions for all properties
    in the background ontologies"""
    back_onts_titles = load_background_onts_titles(back_onts)

    def _get_prop_label(prop_iri: URIRef, back_onts: Graph) -> dict:
        title_ = None
        description = None
        ont_title = None
        for p_, o in back_onts.predicate_objects(prop_iri):
            if p_ == DCTERMS.title:
                title_ = o
            elif p_ == DCTERMS.description:
                description = o

        for k, v in back_onts_titles.items():
            if prop_iri.startswith(k):
                ont_title = v

        if title_ is None:
            title_ = make_title_from_iri(prop_iri)

        return {
            "title": title_,
            "description": description,
            "ont_title": ont_title,
        }

    pl = {}
    for prop in PROPS:
        pl[prop] = _get_prop_label(prop, back_onts)
    return pl


def _is_file(filepath: str) -> bool:
    try:
        if Path(filepath).is_file():
            return True
        return False
    except:
        return False


def load_ontology(ontology: Union[Graph, Path, str]) -> Graph:
    """Loads and ontology into an RDFLib Graph.

    Can handle string data, file path, URL or Graph input"""
    try:
        # try URL
        if isinstance(ontology, str) and ontology.startswith("http"):
            return Graph(bind_namespaces="core").parse(location=ontology)
        elif isinstance(ontology, str):
            if _is_file(ontology):
                return Graph(bind_namespaces="core").parse(ontology)
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
                return Graph(bind_namespaces="core").parse(data=ontology, format=input_format)
        elif isinstance(ontology, Graph):
            return cast(Graph, ontology)
        elif isinstance(ontology, Path):
            return Graph(bind_namespaces="core").parse(ontology)
        else:
            raise ValueError(
                "The ontology you supply to OntDoc must be either "
                "an RDFlib Graph, a Path (to an RDF file) or a string "
                "(of RDF data)"
            )
    except Exception as e:
        print(f"{type(e).__name__} Error {e}")
        exit()

def sort_ontology(ont_orig: Graph) -> Graph:
    """Creates a copy of the supplied ontology, sorted by subjects"""
    trpls = ont_orig.triples((None, None, None))
    trpls_srt = sorted(trpls)
    ont_sorted = Graph(bind_namespaces="core")
    for trpl in trpls_srt:
        ont_sorted.add(trpl)
    return ont_sorted

def load_background_onts():
    """Loads background ontology files into an RDFLib graph from either
    RDF source files or a pickled Graph.

    Performs title and description inference and stores a pickle if
    generating from RDF source files."""

    def _parse_background_onts():
        g_ = Graph(bind_namespaces="core")
        for f_ in RDF_FOLDER.glob("*.ttl"):
            g_.parse(f_)

        return g_

    def _expand_background_onts_graph(back_ont: Graph):
        # make regular titles
        for s_, o in chain(
            back_ont.subject_objects(DC.title),
            back_ont.subject_objects(RDFS.label),
            back_ont.subject_objects(SKOS.prefLabel),
            back_ont.subject_objects(SDO.name),
        ):
            back_ont.add((s_, DCTERMS.title, o))

        # make regular descriptions
        for s_, o in chain(
            back_ont.subject_objects(DC.description),
            back_ont.subject_objects(RDFS.comment),
            back_ont.subject_objects(SKOS.definition),
            back_ont.subject_objects(SDO.description),
        ):
            back_ont.add((s_, DCTERMS.description, o))

    def _pickle_background_onts(back_ont: Graph):
        try:
            with open(RDF_FOLDER / "refs.pickle", "wb") as f_:
                pickle.dump(back_ont, f_)
        except FileNotFoundError:
            logging.warning("Could not cache background ontologies graph")

    if Path(RDF_FOLDER / "refs.pickle").is_file():
        logging.info("Loading background ontologies from a pickle file")
        with open(RDF_FOLDER / "refs.pickle", "rb") as f:
            return pickle.load(f)
    else:
        logging.info("Loading background ontologies from RDF files")
        g = _parse_background_onts()
        _expand_background_onts_graph(g)
        _pickle_background_onts(g)
        return g


def load_background_onts_titles(ont: Graph):
    """Loads the titles of background ontologies
    into a dictionary of Ontology IRI / title"""

    def _get_background_ontology_titles(back_ont: Graph):
        onts_titles = {}
        for s_ in back_ont.subjects(predicate=RDF.type, object=OWL.Ontology):
            for o in back_ont.objects(subject=s_, predicate=DCTERMS.title):
                onts_titles[str(s_)] = str(o)

        return {k: v for k, v in sorted(onts_titles.items(), key=lambda item: item[1])}

    def _pickle_background_onts_titles(ont_titles: dict):
        try:
            with open(RDF_FOLDER / "refs_titles.pickle", "wb") as f_:
                pickle.dump(ont_titles, f_)
        except FileNotFoundError:
            logging.warning("Could not cache background ontologies' titles graph")

    if Path(RDF_FOLDER / "refs_titles.pickle").is_file():
        with open(RDF_FOLDER / "refs_titles.pickle", "rb") as f:
            return pickle.load(f)
    else:
        t = _get_background_ontology_titles(ont)
        _pickle_background_onts_titles(t)
        return t


def rdf_obj_html(
    ont: Graph,
    back_onts: Graph,
    ns: Tuple[str, str],
    obj: List[Union[URIRef, BNode, Literal, Tuple[Union[URIRef, BNode], str]]],
    fids,
    rdf_type=None,
    prop=None,
):
    """Makes a sensible HTML rendering of an RDF resource.

    Can handle IRIs, Blank Nodes of Agents or OWL Restrictions or Literals"""

    def _rdf_obj_single_html(
        ont_: Graph,
        back_onts_: Graph,
        ns_: Tuple[str, str],
        obj_: Union[URIRef, BNode, Literal, Tuple[Union[URIRef, BNode], str]],
        fids_,
        rdf_type_=None,
        prop=None,
    ):
        def _hyperlink_html(
            ont__: Graph,
            back_onts__: Graph,
            ns__: Tuple[str, str],
            iri__: URIRef,
            fids__,
            rdf_type__: Optional[URIRef] = None,
        ):
            if (iri__, RDF.type, PROV.Agent) in ont__:
                return _agent_html(ont__, iri__)

            def _get_ont_type(ont___, back_onts___, iri___):
                types_we_know = [
                    OWL.Class,
                    OWL.ObjectProperty,
                    OWL.DatatypeProperty,
                    OWL.AnnotationProperty,
                    OWL.FunctionalProperty,
                    RDF.Property,
                ]

                this_objects_types = []
                for o in ont___.objects(iri___, RDF.type):
                    if o in ONT_TYPES.keys():
                        this_objects_types.append(o)

                for x_ in types_we_know:
                    if x_ in this_objects_types:
                        return x_

                for o in back_onts___.objects(iri___, RDF.type):
                    if o in ONT_TYPES.keys():
                        this_objects_types.append(o)

                for x_ in types_we_know:
                    if x_ in this_objects_types:
                        return x_

            # find type
            if rdf_type__ is None:
                rdf_type__ = _get_ont_type(ont__, back_onts__, iri__)

            # if it's a thing in this ontology, use a fragment link
            frag_iri = None
            if ns__ is not None and str(iri__).startswith(ns__):
                fid = generate_fid(None, iri__, fids__)
                if fid is not None:
                    frag_iri = "#" + fid

            # use the objet's label for hyperlink text, if it has one
            # if not, try and use a prefixed hyperlink
            # if not, just the iri
            v = back_onts__.value(
                subject=iri__, predicate=DCTERMS.title
            )  # no need to check other labels: inference
            if v is None:
                v = ont__.value(subject=iri__, predicate=DCTERMS.title)
            if v is not None:
                anchor = a(f"{v}", href=frag_iri if frag_iri is not None else iri__)
            else:
                try:
                    qname = ont__.compute_qname(iri__, False)
                    if "ASGS" in qname[2]:
                        print(qname)
                except Exception:
                    qname = iri__
                prefix = "" if qname[0] == "" else f"{qname[0]}:"

                if isinstance(qname, tuple):
                    anchor = a(
                        f"{prefix}{qname[2]}",
                        href=frag_iri if frag_iri is not None else iri__,
                    )
                else:
                    anchor = a(
                        f"{qname}", href=frag_iri if frag_iri is not None else iri__
                    )

            if rdf_type__ is not None:
                ret = span()
                ret.appendChild(anchor)
                ret.appendChild(
                    sup(
                        ONT_TYPES[rdf_type__][0],
                        _class="sup-" + ONT_TYPES[rdf_type__][0],
                        title=ONT_TYPES[rdf_type__][1],
                    )
                )
                return ret
            else:
                return anchor

        def _literal_html(obj__):
            if str(obj__).startswith("http"):
                return _hyperlink_html(
                    ont_, back_onts_, ns_, cast(URIRef, obj__), fids_
                )
            else:
                if prop == SKOS.example:
                    return pre(str(obj__))
                else:
                    return raw(markdown.markdown(str(obj__)))

        def _agent_html(ont__, obj__: Union[URIRef, BNode, Literal]):
            def _affiliation_html(ont___, obj___):
                name_ = None
                url_ = None

                for p_, o_ in ont___.predicate_objects(obj___):
                    if p_ in AGENT_PROPS:
                        if p_ == SDO.name:
                            name_ = str(o_)
                        elif p_ == SDO.url:
                            url_ = str(o_)

                sp_ = span()
                if name_ is not None:
                    if url_ is not None:
                        sp_.appendChild(em(" of ", a(name_, href=url_)))
                    else:
                        sp_.appendChild(em(" of ", name_))
                else:
                    if "http" in obj___:
                        sp_.appendChild(em(" of ", a(obj___, href=obj___)))
                return sp_

            if isinstance(obj__, Literal):
                return span(str(obj__))
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

            if "orcid.org" in str(obj__):
                orcid = True

            for px, o in ont__.predicate_objects(obj__):
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
                    if "orcid.org" in obj__:
                        sp.appendChild(a(raw(orcid_logo), href=obj__))
                    else:
                        sp.appendChild(a(raw(orcid_logo), href=identifier))
                elif identifier is not None:
                    sp.appendChild(a(identifier, href=identifier))
                if email is not None:
                    email = email.replace("mailto:", "")
                    sp.appendChild(span("(", a(email, href="mailto:" + email), " )"))

                if affiliation is not None:
                    sp.appendChild(_affiliation_html(ont__, affiliation))
            else:
                if orcid:
                    return sp.appendChild(a(obj__, href=obj__))
                else:
                    return obj__
            return sp

        def _restriction_html(ont__, obj__, ns__):
            prop = None
            card = None
            cls = None

            for px, o in ont__.predicate_objects(obj__):
                if px != RDF.type:
                    if px == OWL.onProperty:
                        prop = _hyperlink_html(ont__, back_onts_, ns__, o, fids_)
                    elif px in RESTRICTION_TYPES + OWL_SET_TYPES:
                        if px in [
                            OWL.minCardinality,
                            OWL.minQualifiedCardinality,
                            OWL.maxCardinality,
                            OWL.maxQualifiedCardinality,
                            OWL.cardinality,
                            OWL.qualifiedCardinality,
                        ]:
                            if px in [OWL.minCardinality, OWL.minQualifiedCardinality]:
                                card = "min"
                            elif px in [
                                OWL.maxCardinality,
                                OWL.maxQualifiedCardinality,
                            ]:
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
                            elif px == OWL.unionOf:
                                card = "union"
                            elif px == OWL.intersectionOf:
                                card = "intersection"

                                card = span(
                                    span(card, _class="cardinality"),
                                    raw(_rdf_obj_single_html),
                                )
                            
                            card = span(
                                span(card, _class="cardinality"),
                                span(
                                    _hyperlink_html(
                                        ont__, back_onts_, ns__, o, fids_, OWL.Class
                                    )
                                ),
                            )

            restriction = span(prop, card, br()) if card is not None else prop
            restriction = (
                span(restriction, cls, br()) if cls is not None else restriction
            )

            return span(restriction) if restriction is not None else "None"

        def _setclass_html(ont__, obj__, back_onts__, ns__, fids__):
            """Makes lists of (union) 'ClassX or Class Y or ClassZ' or
            (intersection) 'ClassX and Class Y and ClassZ'"""
            if (obj__, OWL.unionOf, None) in ont__:
                joining_word = span("or", _class="cardinality")
            elif (obj__, OWL.intersectionOf, None) in ont__:
                joining_word = span("and", _class="cardinality")
            else:
                joining_word = span(",", _class="cardinality")

            class_set = set()
            for o in ont__.objects(obj__, OWL.unionOf | OWL.intersectionOf):
                for o2 in ont__.objects(o, RDF.rest * ZeroOrMore / RDF.first):
                    class_set.add(
                        _rdf_obj_single_html(
                            ont__, back_onts__, ns__, o2, fids__, OWL.Class
                        )
                    )

            return intersperse(class_set, joining_word)

        def _bn_html(ont__, back_onts__, ns__, fids__, obj__: BNode):
            # TODO: remove back_onts and fids if not needed by subfunctions
            # What kind of BN is it?
            # An Agent, a Restriction or a Set Class (union/intersection)
            # handled all typing added in OntDoc inferencing
            if (obj__, RDF.type, PROV.Agent) in ont__:
                return _agent_html(ont__, obj__)
            elif (obj__, RDF.type, OWL.Restriction) in ont__:
                return _restriction_html(ont__, obj__, ns__)
            else:  # (obj, RDF.type, OWL.Class) in ont:  # Set Class
                return _setclass_html(ont__, obj__, back_onts__, ns__, fids__)

        if isinstance(obj_, Tuple) or isinstance(obj_, URIRef):
            ret = _hyperlink_html(
                ont_, back_onts_, ns_, obj_, fids_, rdf_type__=rdf_type_
            )
        elif isinstance(obj_, BNode):
            ret = _bn_html(ont_, back_onts_, ns_, fids_, obj_)
        else:  # isinstance(obj, Literal):
            ret = _literal_html(obj_)

        return ret if ret is not None else span()

    if len(obj) == 1:
        return _rdf_obj_single_html(
            ont, back_onts, ns, obj[0], fids, rdf_type_=rdf_type, prop=prop
        )
    else:
        u_ = ul()
        for x in obj:
            u_.appendChild(
                li(
                    _rdf_obj_single_html(
                        ont, back_onts, ns, x, fids, rdf_type_=rdf_type, prop=prop
                    )
                )
            )
        return u_


def prop_obj_pair_html(
    ont: Graph,
    back_onts: Graph,
    ns: Tuple[str, str],
    table_or_dl: str,
    prop_iri: URIRef,
    property_title: Literal,
    property_description: Literal,
    ont_title: Literal,
    fids,
    obj: List[Union[URIRef, BNode, Literal, Tuple[Union[URIRef, BNode], str]]],
    obj_type: Optional[str] = None,
):
    """Makes an HTML Definition list dt & dd pair or a Table tr, th & td set,
    for a given RDF property & resource pair"""
    prop = a(
        str(property_title).title(),
        title=str(property_description).rstrip(".") + ". Defined in " + str(ont_title),
        _class="hover_property",
        href=str(prop_iri),
    )
    o = rdf_obj_html(ont, back_onts, ns, obj, fids, rdf_type=obj_type, prop=prop_iri)

    if table_or_dl == "table":
        t = tr(th(prop), td(o))
    else:  # dl
        t = div(dt(prop), dd(o))

    return t


def section_html(
    section_title: str,
    ont: Graph,
    back_onts: Graph,
    ns: Tuple[str, str],
    obj_class: URIRef,
    prop_list: list,
    toc,
    toc_ul_id: str,
    fids: dict,
    props_labeled,
):
    """Makes all the HTML (div, title & table) for all instances of a
    given RDF class, e.g. owl:Class or owl:ObjectProperty"""

    def _element_html(
        ont_: Graph,
        back_onts_: Graph,
        ns_: Tuple[str, str],
        iri: URIRef,
        fid: str,
        title_: str,
        ont_type: URIRef,
        props_list,
        this_props_,
        fids_: dict,
        props_labeled_,
    ):
        """Makes all the HTML (div, title & table) for one instance of a
        given RDF class, e.g. owl:Class or owl:ObjectProperty"""
        d = div(
            h3(
                title_,
                sup(
                    ONT_TYPES[ont_type][0],
                    _class="sup-" + ONT_TYPES[ont_type][0],
                    title=ONT_TYPES[ont_type][1],
                ),
            ),
            id=fid,
            _class="property entity",
        )
        t = table(tr(th("IRI"), td(code(str(iri)))))
        # order the properties as per PROP_PROPS list order
        for prop in props_list:
            if prop != DCTERMS.title:
                if prop in this_props_.keys():
                    t.appendChild(
                        prop_obj_pair_html(
                            ont_,
                            back_onts_,
                            ns_,
                            "table",
                            prop,
                            props_labeled_.get(prop).get("title")
                            if props_labeled_.get(prop) is not None
                            else None,
                            props_labeled_.get(prop).get("description")
                            if props_labeled_.get(prop) is not None
                            else None,
                            props_labeled_.get(prop).get("ont_title")
                            if props_labeled_.get(prop) is not None
                            else None,
                            fids_,
                            this_props_[prop],
                        )
                    )
        d.appendChild(t)
        return d

    elems = div(id=toc_ul_id, _class="section")
    elems.appendChild(h2(section_title))
    # get all objects of this class
    for s_ in ont.subjects(predicate=RDF.type, object=obj_class):
        if obj_class == RDF.Property:
            specialised_props = [
                (s_, RDF.type, OWL.ObjectProperty),
                (s_, RDF.type, OWL.DatatypeProperty),
                (s_, RDF.type, OWL.AnnotationProperty),
                (s_, RDF.type, OWL.FunctionalProperty),
            ]
            if any(x in ont for x in specialised_props):
                continue
        if isinstance(
            s_, URIRef
        ):  # ignore blank nodes for things like [ owl:unionOf ( ... ) ]
            this_props = defaultdict(list)
            # get all properties of this object
            for p_, o in ont.predicate_objects(subject=s_):
                # ... in the property list for this class
                if p_ in prop_list:
                    if p_ == RDFS.subClassOf and (o, RDF.type, OWL.Restriction) in ont:
                        this_props[ONTDOC.restriction].append(o)
                    else:
                        this_props[p_].append(o)
            if len(this_props[DCTERMS.title]) == 0:
                this_fid = generate_fid(None, s_, fids)
                this_title = make_title_from_iri(s_)
            else:
                this_fid = generate_fid(this_props[DCTERMS.title][0], s_, fids)
                this_title = this_props[DCTERMS.title]

            # add to ToC
            if toc.get(toc_ul_id) is None:
                toc[toc_ul_id] = []
            toc[toc_ul_id].append(("#" + this_fid, this_title))

            # create properties table
            elems.appendChild(
                _element_html(
                    ont,
                    back_onts,
                    ns,
                    s_,
                    this_fid,
                    this_title,
                    obj_class,
                    prop_list,
                    this_props,
                    fids,
                    props_labeled,
                )
            )

    return elems


def intersperse(lst, sep):
    result = [sep] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

def de_space_html(html):
    # s = "".join([l_.strip().replace("\n", " ") for l_ in html.split("\n")])
    # return re.sub(" +", " ", s)
    s = re.sub(r">\s+<", "><", html)
    return re.sub(r"\s+", " ", s)


def make_pylode_logo(doc, version, profile_name, profile_iri):
    with doc:
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
                span(" with the ")
                a(profile_name, href=profile_iri, id="profile")
                span("profile")


class PylodeError(Exception):
    pass
