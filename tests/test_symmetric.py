from pathlib import Path

from pylode.profiles import OntPub

current_dir = Path(__file__).parent


def test_symmetric_property():
    """Properties typed only owl:SymmetricProperty (or other OWL 2 property
    characteristics) are documented as object properties"""
    html = OntPub(current_dir / "data" / "symmetric.ttl").make_html()
    toc = html[html.find('id="toc"'):]

    # dual-typed and characteristic-only properties both render...
    assert 'id="adjacentTo"' in html
    assert 'id="touches"' in html, "SymmetricProperty-only property not in body"

    # ...and both appear in the ToC
    assert '"#adjacentTo"' in toc
    assert '"#touches"' in toc, "SymmetricProperty-only property not in ToC"
