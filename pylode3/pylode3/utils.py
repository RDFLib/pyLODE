from pathlib import Path
from rdflib import Graph
from itertools import chain
from rdflib.namespace import DC, DCTERMS, DOAP, OWL, PROF, PROV, RDF, RDFS, SDO, SKOS
import pickle

RDF_FOLDER = Path(__file__).parent / "rdf"


def load_background_onts():
    g = Graph()
    for f in RDF_FOLDER.glob("*.ttl"):
        g.parse(f)

    return g


def expand_background_graph(g):
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
    g = load_background_onts()
    expand_background_graph(g)
    pickle_background_onts(g)
    pickle_background_onts_titles(get_background_ontology_titles(g))
