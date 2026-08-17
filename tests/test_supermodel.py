from pathlib import Path

import pytest
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, VANN

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
