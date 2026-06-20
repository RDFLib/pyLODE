import sys
from pathlib import Path

sys.path.append(str(Path().parent.parent.resolve() / "pylode"))
import pytest

from pylode.profiles import OntPub
from pylode.utils import de_space_html, get_ns

current_dir = Path(__file__).parent


@pytest.fixture(scope="session")
def fix_html():
    od = OntPub(Path(__file__).parent / "data" / "issues.ttl")
    return od.make_html()


def test_issue_5(fix_html):
    # tested in test_vocpub::test_classes_hierarchy & test_vocpub::test_object_properties_hierarchy
    pass


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


def test_issue_84(fix_html):
    # open("issues.html", "w").write(fix_html)
    assert de_space_html(
        """
              <td>
                <span>
                  <span>
                    <a href="http://example.com/ns/fruits/notSameColourAs">fruits:notSameColourAs</a>
                    <span>
                      <span class="cardinality">exactly</span>
                      <span>1</span>
                    </span>
                    <span>
                      <a href="http://example.com/ns/fruits/Apple">Apple</a>
                      <sup class="sup-c" title="OWL/RDFS Class">c</sup>
                    </span>
                    <span class="cardinality">or</span>
                    <span>
                      <a href="http://example.com/ns/fruits/Orange">Orange</a>
                      <sup class="sup-c" title="OWL/RDFS Class">c</sup>
                    </span><br>
                  </span>
                </span>
              </td>            
            """
    ) in de_space_html(fix_html), "Union class restrictions not catered for correctly"


def test_issue_141(fix_html):
    # open("issues.html", "w").write(fix_html)
    assert de_space_html(
        """
      <div class="section" id="datatypes">
        <h2>Custom Datatypes</h2>
        <div class="property entity" id="AusPIXDGGSLiteral">
          <h3>AusPIX DGGS Literal
            <sup class="sup-dt" title="RDFS Datatypes">dt</sup>
          </h3>
          <table>
            <tr>
              <th>IRI</th>
              <td>
                <code>http://purl.org/wf4ever/wfprov#auspixDggsLiteral</code>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://www.w3.org/2000/01/rdf-schema#isDefinedBy" title="The definition of the subject resource. Defined in The RDF Schema vocabulary (RDFS)">Is Defined By</a>
              </th>
              <td>
                <a href="#wfprov">Workflow 4Ever Provenance Ontology</a>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://purl.org/dc/terms/description" title="An account of the resource. Defined in DCMI Metadata Terms">Description</a>
              </th>
              <td><p>A textual serialization of an AusPix Discrete Global Grid System (DGGS) geometry object.</p></td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://www.w3.org/2004/02/skos/core#scopeNote" title="A note that helps to clarify the meaning and/or the use of a concept. Defined in SKOS Vocabulary">Scope Note</a>
              </th>
              <td><p>This datatype is to be used only for a specific DGGS implementation - AusPix. Other DGGS implementations should declare their own datatypes.</p></td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://www.w3.org/2004/02/skos/core#example" title="An example of the use of a concept. Defined in SKOS Vocabulary">Example</a>
              </th>
              <td>
                <pre> &quot;OrdinateList (R3234)&quot;^^geo:auspixDggsLiteral</pre>
              </td>
            </tr>
          </table>
        </div>
      </div>            
            """
    ) in de_space_html(fix_html), "Datatypes not catered for correctly"


def test_issue_230(fix_html):
    open("issues.html", "w").write(fix_html)
    assert de_space_html(
        """
        <div>
            <dt>
              <a class="hover_property" href="https://schema.org/codeRepository" title="Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex). Defined in None">Code Repository</a>
            </dt>
            <dd>
              <a href="https://github.com/RDFLib/pyLODE/">https://github.com/RDFLib/pyLODE/</a>
            </dd>
          </div>
        """
    ) in de_space_html(fix_html), "Code Repository information not included"


def test_issue_234(fix_html):
    # open("issues.html", "w").write(fix_html)
    assert de_space_html(
        """<div class="property entity" id="Orange">
          <h3>Orange
            <sup class="sup-c" title="OWL/RDFS Class">c</sup>
          </h3>
          <table>
            <tr>
              <th>IRI</th>
              <td>
                <code>http://example.com/ns/fruits/Orange</code>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://www.w3.org/2000/01/rdf-schema#isDefinedBy" title="The definition of the subject resource. Defined in The RDF Schema vocabulary (RDFS)">Is Defined By</a>
              </th>
              <td>
                <a href="#wfprov">Workflow 4Ever Provenance Ontology</a>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://purl.org/dc/terms/description" title="An account of the resource. Defined in DCMI Metadata Terms">Description</a>
              </th>
              <td><p>Dummy desc</p></td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://www.w3.org/2000/01/rdf-schema#subClassOf" title="The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)">Sub Class Of</a>
              </th>
              <td>
                <span>
                  <a href="http://example.com/ns/fruits/Citrus">Citrus</a>
                  <sup class="sup-c" title="OWL/RDFS Class">c</sup>
                </span>
              </td>
            </tr>
          </table>
        </div>"""
    ) in de_space_html(fix_html), "ROR information not included"


def test_issue_246(fix_html):
    # open("issues.html", "w").write(fix_html)
    assert de_space_html(
        """<title>https://ror.org/00yczwp93</title>"""
    ) in de_space_html(fix_html), "ROR information not included"


def test_issue_261(fix_html):
    # open("issues.html", "w").write(fix_html)
    assert de_space_html(
        """[&gt;=0, &lt;42]"""
    ) in de_space_html(fix_html), "Min/Max datatype cardinality restriction incorrect"

    assert de_space_html(
        """[&lt;=42]"""
    ) in de_space_html(fix_html), "Max datatype cardinality restriction incorrect"