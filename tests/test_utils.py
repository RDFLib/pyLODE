from pylode.profiles import OntPub
from pylode.utils import *
from pylode.rdf_elements import CLASS_PROPS

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, XSD
import pytest


# scope="session" so that this is reused without regeneration in this testing session
@pytest.fixture(scope="session")
def fix_ont():
    od = OntPub(Path(__file__).parent / "prof.ttl")
    return od.ont


@pytest.fixture(scope="session")
def fix_load_background_onts():
    return load_background_onts()


@pytest.fixture(scope="session")
def fix_get_ns(fix_ont):
    return get_ns(fix_ont)


def test_get_ns(fix_ont):
    prefix, namespace = get_ns(fix_ont)
    assert (
        namespace == "http://www.w3.org/ns/dx/prof"
    ), "get_ns did not retrieve PROF's namespace"


def test_make_title_from_iri():
    data = [
        ("http://linked.data.gov.au/def/gnaf#StreetAddress", "Street Address"),
        ("http://linked.data.gov.au/def/gnaf#postalAddress", "postal address"),
        ("http://example.com/Something", "Something"),
        ("http://example.com/Something#Else", "Else"),
        ("http://example.com/Something/Else/Another", "Another"),
        ("http://", None),
        ("what??", None),
        ("", None),
    ]
    for datum in data:
        assert make_title_from_iri(datum[0]) == datum[1]


def test_generate_fid():
    fids = {
        "http://example.com/thing/One": "One",
        "http://example.com/thing/Three": "three",
        "http://example.com/thing/five": "five",
        "http://example.com/thing/sevenseven": "sevenseven",
    }
    expected = [
        ("http://example.com/other/One", "One", "One1"),
        ("http://example.com/thing/Two", "Two", "Two"),
        ("http://example.com/thing/Four", None, "Four"),
        ("http://example.com/thing/FiveFive", "Five 5", "Five5"),
        ("http://example.com/thing/FiveFive", None, "Five5"),  # from existing fid above
        ("http://example.com/thing/Eight_Eight", None, "Eight_Eight"),
        ("http://example.com/thing/Nine%20Nine", None, "Nine%20Nine"),
    ]
    for ex in expected:
        assert generate_fid(ex[1], ex[0], fids) == ex[2]


def test_rdf_obj_html(fix_ont, fix_load_background_onts, fix_get_ns):
    data = [
        ([Literal(1)], "<p>1</p>"),
        ([Literal(True)], "<p>true</p>"),
        ([Literal("Hello World")], "<p>Hello World</p>"),
        ([Literal(41), Literal(42)], "<ul><li><p>41</p></li><li><p>42</p></li></ul>"),
        (
            [URIRef("http://example.com/thing/One")],
            '<a href="#One">http://example.com/thing/One</a>',
        ),
        (
            [URIRef("http://example.com/thing/FiveFive")],
            '<a href="#Five5">http://example.com/thing/FiveFive</a>',
        ),
        (
            [URIRef("http://other.com/thing/Six")],
            '<a href="#Six">http://other.com/thing/Six</a>',
        ),
        ([URIRef("not-a-uri")], '<a href="not-a-uri">not-a-uri</a>'),
    ]

    fids = {
        "http://example.com/thing/FiveFive": "Five5",
    }
    for datum in data:
        o = rdf_obj_html(
            fix_ont,
            fix_load_background_onts,
            ("", "http://example.com/thing/"),
            datum[0],
            fids,
        )
        actual = de_space_html(o.render(pretty=False))
        assert actual == datum[1], f"Object HTML '{actual}' != '{datum[1]}'"


def test_rdf_obj_html_bn(fix_load_background_onts):
    g = OntPub(Path(__file__).parent.parent / "examples/ontpub/skos-thes.ttl").ont
    bn = None
    for x in g.objects(
        URIRef("http://purl.org/iso25964/skos-thes#status"), RDFS.domain
    ):
        bn = x

    o = rdf_obj_html(
        g,
        fix_load_background_onts,
        None,
        [bn],
        {},
    )
    # we have to check for each part separately as order in RDF is random
    expected1 = """<span>
  <a href="http://www.w3.org/2008/05/skos-xl#Label">skosxl:Label</a>
  <sup class="sup-c" title="OWL/RDFS Class">c</sup>
</span>"""
    expected2 = """<span class="cardinality">or</span>"""
    expected3 = """<span>
  <a href="http://www.w3.org/2004/02/skos/core#Concept">Concept</a>
  <sup class="sup-c" title="OWL/RDFS Class">c</sup>
</span>"""
    actual = o.render()

    assert expected1 in actual, "exp1 failed"
    assert expected2 in actual, "exp2 failed"
    assert expected3 in actual, "exp3 failed"


def test_prop_obj_pair_html(fix_ont, fix_load_background_onts, fix_get_ns):
    """
    ont: Graph,
    back_onts: Graph,
    ns: Namespace,

    table_or_dl: str,
    prop_iri: URIRef,
    property_title: Literal,

    property_description: Literal,
    ont_title: Literal,
    fids,

    obj: List[Union[URIRef, BNode, Literal]],
    obj_type: Optional[str] = None,
    """
    prop_desc = "Information about rights held in and over the resource."
    ont_title = "DCMI Metadata Terms"
    obj = Literal("2019-10-25", datatype=XSD.date)
    pp = prop_obj_pair_html(
        fix_ont,
        fix_load_background_onts,
        fix_get_ns,
        "dl",
        DCTERMS.created,
        "Rights",
        prop_desc,
        ont_title,
        {},
        [obj],
    )
    expected = '<div><dt><a class="hover_property" href="http://purl.org/dc/terms/created" title="Information about rights held in and over the resource. Defined in DCMI Metadata Terms">Rights</a></dt><dd><p>2019-10-25</p></dd></div>'
    actual = de_space_html(pp.render(pretty=False))

    assert actual == expected, f"Object HTML '{actual}' != '{expected}'"
