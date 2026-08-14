from pathlib import Path

from pylode.profiles import OntPub
from pylode.utils import de_space_html

current_dir = Path(__file__).parent


def test_equivalentproperty():
    """owl:equivalentProperty renders on properties (issue #175)"""
    html = OntPub(current_dir / "data" / "equivalentproperty.ttl").make_html()

    assert (
        de_space_html(
            """
            <a class="hover_property" href="http://www.w3.org/2002/07/owl#equivalentProperty"
            title="The property that determines that two given properties are equivalent.
            Defined in The OWL 2 Schema vocabulary (OWL 2)">Equivalent Property</a>
            """
        )
        in de_space_html(html)
    ), "equivalentProperty header not rendered/labeled"

    # in-ontology target links to its anchor; external target links out
    assert '<a href="#surname">' in html, "internal equivalent property not anchor-linked"
    assert "schema.org/familyName" in html, "external equivalent property not rendered"
