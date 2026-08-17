import re

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SH, SKOS

from pylode.profiles import OntPub, ValPub, VocPub

EX = Namespace("https://example.com/")


def _entity(html, entity_id):
    return re.search(
        rf'<div class="[^"]*entity" id="{entity_id}">(.*?)</table>',
        html,
        re.DOTALL,
    ).group(1)


def _concept(html, concept_id):
    return re.search(
        rf'<div class="entity">\s*<h3 id="{concept_id}">.*?</h3>(.*?)</table>',
        html,
        re.DOTALL,
    ).group(1)


def _assert_known_then_unknown(html, known_value, unknown_value):
    assert unknown_value in html
    assert html.index(known_value) < html.index(unknown_value)


def test_ontpub_renders_unknown_ontology_class_and_property_properties():
    graph = Graph()
    graph.add((EX.ontology, RDF.type, OWL.Ontology))
    graph.add((EX.ontology, DCTERMS.title, Literal("Example ontology")))
    graph.add((EX.ontology, DCTERMS.description, Literal("Known ontology value")))
    graph.add((EX.ontology, EX.extra, Literal("Unknown ontology value")))
    graph.add((EX.Fruit, RDF.type, OWL.Class))
    graph.add((EX.Fruit, RDFS.label, Literal("Fruit")))
    graph.add((EX.Fruit, DCTERMS.description, Literal("Known class value")))
    graph.add((EX.Fruit, EX.extra, Literal("Unknown class value")))
    graph.add((EX.relatedTo, RDF.type, OWL.ObjectProperty))
    graph.add((EX.relatedTo, RDFS.label, Literal("related to")))
    graph.add((EX.relatedTo, DCTERMS.description, Literal("Known property value")))
    graph.add((EX.relatedTo, EX.extra, Literal("Unknown property value")))
    graph.add((EX.extra, RDFS.label, Literal("extra detail")))

    html = OntPub(graph).make_html()

    metadata = re.search(
        r'<div class="section" id="metadata">(.*?)</dl>', html, re.DOTALL
    ).group(1)
    _assert_known_then_unknown(
        metadata, "Known ontology value", "Unknown ontology value"
    )
    _assert_known_then_unknown(
        _entity(html, "Fruit"), "Known class value", "Unknown class value"
    )
    _assert_known_then_unknown(
        _entity(html, "relatedTo"), "Known property value", "Unknown property value"
    )


def test_vocpub_renders_unknown_scheme_and_concept_properties():
    graph = Graph()
    graph.add((EX.scheme, RDF.type, SKOS.ConceptScheme))
    graph.add((EX.scheme, SKOS.prefLabel, Literal("Example scheme")))
    graph.add((EX.scheme, SKOS.definition, Literal("Known scheme value")))
    graph.add((EX.scheme, EX.extra, Literal("Unknown scheme value")))
    graph.add((EX.apple, RDF.type, SKOS.Concept))
    graph.add((EX.apple, SKOS.prefLabel, Literal("Apple")))
    graph.add((EX.apple, SKOS.inScheme, EX.scheme))
    graph.add((EX.apple, SKOS.definition, Literal("Known concept value")))
    graph.add((EX.apple, EX.extra, Literal("Unknown concept value")))
    graph.add((EX.extra, RDFS.label, Literal("extra detail")))

    html = VocPub(graph).make_html()

    metadata = re.search(
        r'<div class="section" id="metadata">(.*?)</dl>', html, re.DOTALL
    ).group(1)
    _assert_known_then_unknown(metadata, "Known scheme value", "Unknown scheme value")
    concept_id = re.search(r'<h3 id="([^"]+)">Apple</h3>', html).group(1)
    _assert_known_then_unknown(
        _concept(html, concept_id), "Known concept value", "Unknown concept value"
    )


def test_valpub_renders_unknown_graph_and_shape_properties():
    graph = Graph()
    graph.add((EX.graph, RDF.type, URIRef("http://www.w3.org/ns/shacl#ShapesGraph")))
    graph.add((EX.graph, DCTERMS.title, Literal("Example shapes graph")))
    graph.add((EX.graph, DCTERMS.description, Literal("Known graph value")))
    graph.add((EX.graph, EX.extra, Literal("Unknown graph value")))
    graph.add((EX.node, RDF.type, SH.NodeShape))
    graph.add((EX.node, DCTERMS.title, Literal("Example node")))
    graph.add((EX.node, DCTERMS.description, Literal("Known node value")))
    graph.add((EX.node, EX.extra, Literal("Unknown node value")))
    graph.add((EX.property, RDF.type, SH.PropertyShape))
    graph.add((EX.property, DCTERMS.title, Literal("Example property")))
    graph.add((EX.property, DCTERMS.description, Literal("Known shape value")))
    graph.add((EX.property, SH.path, EX.value))
    graph.add((EX.property, EX.extra, Literal("Unknown shape value")))
    graph.add((EX.extra, RDFS.label, Literal("extra detail")))

    html = ValPub(graph).make_html()

    metadata = re.search(
        r'<div class="section" id="metadata">(.*?)</dl>', html, re.DOTALL
    ).group(1)
    _assert_known_then_unknown(metadata, "Known graph value", "Unknown graph value")
    _assert_known_then_unknown(
        _entity(html, "Examplenode"), "Known node value", "Unknown node value"
    )
    _assert_known_then_unknown(
        _entity(html, "Exampleproperty"), "Known shape value", "Unknown shape value"
    )
