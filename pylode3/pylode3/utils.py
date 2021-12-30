from pathlib import Path
from rdflib import Graph, URIRef
from itertools import chain
import pickle
from properties import *
import re
import logging
from typing import Union

RDF_FOLDER = Path(__file__).parent / "rdf"


def check_all_props_are_known():
    bg = load_background_onts()
    for prop in PROPS:
        if (prop, RDF.type, None) not in bg:
            print(f"Unknown property: {prop}")
            print(f'Estimating title as "{make_title_from_iri(prop)}"')
            print()


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


def load_ontology(ontology: Union[Graph, Path, str]) -> Graph:
    if isinstance(ontology, Graph):
        return ontology
    elif isinstance(ontology, Path):
        return Graph().parse(ontology)
    elif isinstance(ontology, str):
        # see if it's a file path
        if Path(ontology).is_file():
            return Graph().parse(ontology)
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
            return Graph().parse(data=ontology, format=input_format)
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
    for s, o in chain(
        g.subject_objects(DC.title),
        g.subject_objects(RDFS.label),
        g.subject_objects(SKOS.prefLabel),
        g.subject_objects(SDO.name),
    ):
        g.add((s, DCTERMS.title, o))

    # make regular descriptions
    for s, o in chain(
        g.subject_objects(DC.description),
        g.subject_objects(RDFS.comment),
        g.subject_objects(SKOS.definition),
        g.subject_objects(SDO.description),
    ):
        g.add((s, DCTERMS.description, o))


def get_background_ontology_titles(g):
    onts_titles = {}
    for s in g.subjects(predicate=RDF.type, object=OWL.Ontology):
        for o in g.objects(subject=s, predicate=DCTERMS.title):
            onts_titles[str(s)] = str(o)

    return {k: v for k, v in sorted(onts_titles.items(), key=lambda item: item[1])}


def pickle_background_onts(g):
    with open(RDF_FOLDER / "refs.pickle", "wb") as f:
        pickle.dump(g, f)


def pickle_background_onts_titles(ont_titles):
    with open(RDF_FOLDER / "refs_titles.pickle", "wb") as f:
        pickle.dump(ont_titles, f)


if __name__ == "__main__":
    # g = _parse_background_onts()
    # _expand_background_onts_graph(g)
    # pickle_background_onts(g)
    # pickle_background_onts_titles(get_background_ontology_titles(g))

    check_all_props_are_known()
