import sys
from pathlib import Path

sys.path.append(str(Path().parent.parent.resolve() / "pylode"))
import pytest

from pylode.profiles import OntPub
from pylode.utils import get_ns, de_space_html

current_dir = Path(__file__).parent


# scope="session" so that this is reused without regeneration in this testing session
@pytest.fixture(scope="session")
def fix_ont():
    od = OntPub(Path(__file__).parent / "data" / "issues.ttl")
    return od.ont


@pytest.fixture(scope="session")
def fix_html():
    od = OntPub(Path(__file__).parent / "data" / "issues.ttl")
    return od.make_html()


def test_issue_13(fix_html):
    """
    Tests that multiple literals for the same predicate, e.g. schema:description, are concatenated nicely
    """
    expected_html = de_space_html("""
        <td>
            <ul class="pylodelitlist">
                <li><p>This object property associate a wfprov:Processrun to its wfdesc:Process description.</p></li>
                <li><p>Second annoying description for Issue #13 testing</p></li>
            </ul>
        </td>
    """)

    # open("issues.html", "w").write(fix_html)
    assert expected_html in de_space_html(fix_html)


def test_issue_20(fix_html):
    """
    Tests that the HTML fragments match the case of RDF elements, e.g. wfprov:describedByParameter
    """
    expected_html = """<div class="property entity" id="describedByParameter">"""
    # open("issues.html", "w").write(de_space_html(fix_html))
    assert expected_html in de_space_html(fix_html)


def test_issue_30_markdown(fix_html):
    """
    Before checking HTML rendering in test_issue_30_markdown, just ensure Markdown is rendered as HTML correctly by default first
    """
    expected_html_from_markdown = """<p>Is <strong>THIS</strong> Markdown <em>working</em> correctly? If so, <a href="https://google.com">this</a> is a hyperlink to Google.</p>"""
    assert expected_html_from_markdown in fix_html


def test_issue_30_html(fix_html):
    """
    Check that HTML literals indicated with rdf:HTML are passed through unchanged
    """
    expected_html = de_space_html(
        """<p>2026-06: added this HTML literal history note for testing</p>
           <p>2026-05: a fake history note for testing</p>
           <p>Foods Nick likes:</p>
           <ul>
               <li>smoked chicken</li>
               <li>gorgonzola cheese</li>
           </ul>
        """
    )
    # open("issues.html", "w").write(de_space_html(fix_html))
    assert expected_html in de_space_html(fix_html)


