import re
from pathlib import Path

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SDO, SH

from pylode.profiles import OntPub, ValPub, VocPub


EX = Namespace("https://example.com/")
SVG = Literal(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10">'
    '<circle cx="5" cy="5" r="4" /></svg>'
)


def test_svg_image_literals_render_as_images():
    source = Path(__file__).parent.parent / "examples" / "vocpub" / "image-test.ttl"

    html = VocPub(source).make_html()
    apron = re.search(
        r'<div class="entity">\s*<h3[^>]*>Apron</h3>(.*?)</table>',
        html,
        re.DOTALL,
    ).group(1)
    plane = re.search(
        r'<div class="entity">\s*<h3[^>]*>Plane</h3>(.*?)</table>',
        html,
        re.DOTALL,
    ).group(1)

    for concept in (apron, plane):
        assert re.search(r'<a href="https://schema.org/image"[^>]*>Image</a>', concept)
        assert '<svg xmlns="http://www.w3.org/2000/svg"' in concept
        assert "&lt;svg" not in concept


def test_ontpub_renders_svg_image_literals():
    graph = Graph()
    graph.add((EX.ontology, RDF.type, OWL.Ontology))
    graph.add((EX.ontology, DCTERMS.title, Literal("Image ontology")))
    graph.add((EX.Thing, RDF.type, OWL.Class))
    graph.add((EX.Thing, RDFS.label, Literal("Thing")))
    graph.add((EX.Thing, SDO.image, SVG))
    graph.add((EX.relatedTo, RDF.type, OWL.ObjectProperty))
    graph.add((EX.relatedTo, RDFS.label, Literal("related to")))
    graph.add((EX.relatedTo, SDO.image, SVG))

    html = OntPub(graph).make_html()

    assert html.count(str(SVG)) == 2
    assert "&lt;svg" not in html


def test_valpub_renders_svg_image_literals():
    graph = Graph()
    graph.add(
        (
            EX.graph,
            RDF.type,
            URIRef("http://www.w3.org/ns/shacl#ShapesGraph"),
        )
    )
    graph.add((EX.graph, DCTERMS.title, Literal("Image shapes graph")))
    graph.add((EX.shape, RDF.type, SH.NodeShape))
    graph.add((EX.shape, DCTERMS.title, Literal("Image shape")))
    graph.add((EX.shape, SDO.image, SVG))

    html = ValPub(graph).make_html()

    assert str(SVG) in html
    assert "&lt;svg" not in html
