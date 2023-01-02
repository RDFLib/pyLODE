from pathlib import Path
from pylode.profiles import OntPub


def test_example_preformatting():
    input_rdf = Path(__file__).parent / "abisdm.ttl"

    html = OntPub(input_rdf).make_html()

    assert (
        """<pre># Dataset with a embargo period
PREFIX abisdm: &lt;https://linked.data.gov.au/def/abisdm/&gt;
PREFIX dcterms: &lt;http://purl.org/dc/terms/&gt;
PREFIX sdo: &lt;https://schema.org/&gt;
PREFIX tern: &lt;https://w3id.org/tern/ontologies/tern/&gt;
PREFIX xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt;

&lt;http://example.org/dataset/embargoed-test-01&gt;
    a tern:RDFDataset ;
    dcterms:title &quot;Margaret River Flora&quot; ;
    dcterms:description &quot;202201 CBR Flora and Vegetation report_draftv1.pdf by Stream Environment and Water Pty Ltd&quot; ;
    dcterms:creator &lt;http://example.org/Stream-Environment-and-Water-Pty-Ltd&gt; ;
    dcterms:created &quot;2022-02-24&quot;^^xsd:date ;
    abisdm:embargoPeriod &quot;P1Y6M&quot;^^xsd:duration ;
.

&lt;http://example.org/Stream-Environment-and-Water-Pty-Ltd&gt;
    a sdo:Organization ;
    sdo:name &quot;Stream Environment and Water Pty Ltd&quot; ;
.</pre>"""
        in html
    )
