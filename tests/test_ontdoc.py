from pylode.common import MakeDocco
from pylode.profiles import OntDoc

o1 = """
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix prov: <http://www.w3.org/ns/prov#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    
    @prefix : <http://example-ontology.org/> .
    
    <http://example-ontology.org>
        a owl:Ontology ;
        dcterms:title "Basic Ontology" ;
        dcterms:created "2019-05-30"^^xsd:date .
    
    # normal, basic
    :testprop
        a owl:ObjectProperty ;
        rdfs:label "Test Property" ;
        rdfs:domain skos:Concept ;
        rdfs:range xsd:string .
    """

m = MakeDocco(data=o1)


def test_ontdoc_expand_graph():
    global m

    assert len(m.G) == 7, "Error loading ontology before expansion. Should have 7 triples, got {}".format(len(m.G))

    # should add a single rdfs:label for the single dcterms:title
    # and a rdf:Property for the owl:ObjectProperty
    od = OntDoc(m.G, None, None, None, None, None)
    od._expand_graph()

    assert len(od.G) == 9, "Error loading ontology after expansion. Should have 9 triples, got {}".format(len(od.G))


if __name__ == '__main__':
    test_ontdoc_expand_graph()
