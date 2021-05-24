from pylode.common import MakeDocco
from pylode.profiles.base import BaseProfile

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
        rdfs:range xsd:string ;
        <http://some-other-prop.com/other/thing> 23 ;
        <http://schemas.talis.com/2005/address/schema#> "24" ;
    .
    """

m = MakeDocco(data=o1)


def test_ontdoc_extract_namespaces():
    global m

    bp = BaseProfile(m.G, None)
    bp._extract_namespaces()

    # for k, v in bp.NAMESPACES.items():
    #     print(f"{k:4}\t{v}")

    assert "ad" in bp.NAMESPACES.keys()
    assert "owl" in bp.NAMESPACES.keys()
    assert len(bp.NAMESPACES.keys()) == 10


if __name__ == '__main__':
    test_ontdoc_extract_namespaces()
