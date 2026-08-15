import sys
from pathlib import Path

sys.path.append(str(Path().parent.parent.resolve() / "pylode"))
import pytest

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
