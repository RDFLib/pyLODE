from pathlib import Path

from pylode.profiles import OntPub, VocPub
from pylode.utils import de_space_html

current_dir = Path(__file__).parent


def test_seealso_ontpub():
    """rdfs:seeAlso renders on ontology metadata, classes and properties (issue #174)"""
    html = OntPub(current_dir / "data" / "seealso.ttl").make_html()

    for target in [
        "https://example.org/more-about-this-ontology",
        "https://example.org/more-about-myclass",
        "https://example.org/more-about-myprop",
    ]:
        assert f'<a href="{target}">' in html, f"seeAlso link to {target} not rendered"

    assert de_space_html(
        """
            <a class="hover_property" href="http://www.w3.org/2000/01/rdf-schema#seeAlso"
            title="Further information about the subject resource.
            Defined in The RDF Schema vocabulary (RDFS)">See Also</a>
            """
    ) in de_space_html(html), "seeAlso property header not labeled correctly"


def test_seealso_vocpub():
    """rdfs:seeAlso renders on SKOS Concepts in the VocPub profile (issue #174)"""
    html = VocPub(current_dir / "data" / "seealso-vocpub.ttl").make_html()
    assert '<a href="https://example.org/more-about-c1">' in html, (
        "concept seeAlso link not rendered"
    )
