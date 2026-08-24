from pathlib import Path

import pytest
from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SH, VANN, XSD

from pylode.profiles.supermodel.html import Supermodel
from pylode.utils import de_space_html

current_dir = Path(__file__).parent


@pytest.fixture(scope="session")
def fix_html():
    sm = Supermodel(current_dir / "data" / "supermodel.ttl")
    return sm.make_html()


def test_equivalent_class_section_rendered(fix_html):
    """owl:equivalentClass must be displayed in supermodel mode."""
    assert "Equivalent to" in de_space_html(fix_html)


def test_equivalent_class_internal_link(fix_html):
    """An equivalent class documented in the same ontology links though a
    link fragment whose target is that class's heading id."""
    html = de_space_html(fix_html)
    assert '<a href="#http://example.com/ont/Human">Human</a>' in html


def test_equivalent_class_external_link(fix_html):
    """An equivalent class outside the ontology renders as an external link."""
    assert 'href="http://xmlns.com/foaf/0.1/Agent"' in fix_html


def test_class_and_property_svg_image_literals_render_as_images(fix_html):
    assert fix_html.count('<svg xmlns="http://www.w3.org/2000/svg"') == 2
    assert "&lt;svg" not in fix_html


def test_ontology_iri_can_differ_from_preferred_namespace():
    ex = Namespace("https://example.com/ontology#")
    ontology = Namespace("https://example.com/").ontology
    graph = Graph()
    graph.add((ontology, RDF.type, OWL.Ontology))
    graph.add((ontology, DCTERMS.title, Literal("Hash namespace ontology")))
    graph.add((ontology, VANN.preferredNamespaceUri, Literal(str(ex))))
    graph.add((ex.Thing, RDF.type, OWL.Class))
    graph.add((ex.Thing, RDFS.label, Literal("Thing")))

    html = Supermodel(graph).make_html()

    assert "Hash namespace ontology" in html
    assert "Thing" in html


@pytest.fixture
def property_shape_graph():
    """A class with an implicit-target node shape carrying one property shape
    that uses only optional-absent constraints (no sh:uniqueLang etc.)."""
    ex = Namespace("https://example.com/ontology#")
    graph = Graph()
    graph.add((ex.ont, RDF.type, OWL.Ontology))
    graph.add((ex.ont, DCTERMS.title, Literal("Property shape ontology")))
    graph.add((ex.Thing, RDF.type, OWL.Class))
    graph.add((ex.Thing, RDF.type, SH.NodeShape))
    graph.add((ex.Thing, RDFS.label, Literal("Thing")))
    graph.add((ex.Thing, SH.property, ex.thingNameShape))
    graph.add((ex.thingNameShape, SH.path, ex.name))
    graph.add((ex.thingNameShape, SH.name, Literal("name")))
    graph.add((ex.thingNameShape, SH.minCount, Literal(1)))
    graph.add(
        (ex.thingNameShape, SH.datatype, URIRef(XSD.string))
    )
    return graph


def test_property_shape_without_unique_lang_renders(property_shape_graph):
    """A property shape that omits optional constraints such as sh:uniqueLang
    must render, not crash with AttributeError on None."""
    html = Supermodel(property_shape_graph).make_html()

    assert "name" in html
    assert "Cardinality" in html


def test_has_value_without_node_kind_renders(property_shape_graph):
    """sh:hasValue without sh:nodeKind is legal SHACL and must render the
    expected value, not crash rendering the absent value type."""
    ex = Namespace("https://example.com/ontology#")
    property_shape_graph.add(
        (ex.thingNameShape, SH.hasValue, Literal("fixed"))
    )

    html = Supermodel(property_shape_graph).make_html()

    assert "Expected value" in html
    assert "fixed" in html


def test_sh_in_values_render(property_shape_graph):
    """sh:in enumerations must render as 'Allowable values', independently of
    sh:languageIn."""
    ex = Namespace("https://example.com/ontology#")
    values = BNode()
    property_shape_graph.add((ex.thingNameShape, SH["in"], values))
    property_shape_graph.add((values, RDF.first, Literal("alpha")))
    property_shape_graph.add((values, RDF.rest, RDF.nil))

    html = Supermodel(property_shape_graph).make_html()

    assert "Allowable values" in html
    assert "alpha" in html
