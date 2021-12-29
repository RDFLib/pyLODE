import dominate
from dominate.tags import *
from dominate.util import raw
from pylode3.pylode3.ontdoc import OntDoc


def test_basic_toc():
    d = dominate.document()

    od = OntDoc()
    od.toc
    od._make_toc(
        d,
        [
            ("Classes", [
                ("Fish", "#Fish"),
                ("Chicken", "#Chick"),
            ]),
            ("Properties", None),
            ("Namespaces", [
                ("dcterms", "http://purl.org/dc/terms/"),
                ("owl", "http://www.w3.org/2002/07/owl#"),
                ("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
                ("sdo", "https://schema.org/"),
                ("xsd", "http://www.w3.org/2001/XMLSchema#"),
            ]),
            ("Legend", None),
        ]
    )

    html = str(d)
    assert '<a href="#Classes">Classes</a>' in html
    assert '<a href="#Properties">Properties</a>' not in html
    assert '<a href="#Namespaces">Namespaces</a>' in html
