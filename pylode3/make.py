import dominate
from dominate.tags import *
from dominate.util import raw


def _make_document(title, schema_org_json, version):
    doc = dominate.document(title=title)
    _make_header(doc, schema_org_json)
    _make_body(doc, title, version)

    return doc


def _make_header(doc, schema_org_json):
    # use standard pyLODE stylesheet
    css = "\n" + open("pylode.css").read() + "\n\t"
    with doc.head:
        style(css)
        link(rel="icon", type="image/png", sizes="16x16", href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABhklEQVQ4jbWPzStEURjG3yQLirlGKUnKFO45Z+SjmXvnnmthQcpCoVhYmD/AwmJiI3OvZuZc2U3UlKU0/gAslMw9JgvhHxAr2fko7r0jHSsl+TgbTz2Lt5731/MASEiJW9ONml2QyX6rsGalmnT74v8BDf12hxJfpV8d1uwNKUBYszabdFv84L8B9X0rESVmmUup2fme0cVhJWaZHw4NWL1SewEAfDe6H3Dy6Ll456WEJsRZS630MwCAOI20ei5OBpxse5zcBZw8eS4uPpfIuDiCainIg9umBCU0GZzgLZ9Hn31OgoATL+CkLDGB5H1OKj4nFd/FBxUXJ0UZNb4edw/6nLyJXaj5FeCVyPLNIVmYK8TG1IwWb16L1gEACAFV90ftoT8bdOX0EeyY99gxBXZMgRz6qGb1KantAACI0UvE6F5XJqEjpsdURouI0Vt5gGOUkUNnPu7ObGIIMfNaGqDmjDRi9FZldF1lRgYzeqUyeoiY4ag5Iy3RgOYRM8+/M2bG8efsO4hGrpmJseyMAAAAAElFTkSuQmCC")
        link(rel="icon", type="image/png", sizes="32x32", href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAC40lEQVRYhe2UT0hUQRzHp6Iss1B3VZKIDbbdfW9mnoi4f3zzjkJQeOgS0SEIb1EWBGGlLLu460zQPQM1unUIIjA6rfpm6ZAhHjoIRVQUFUlEbG+euTsdXG1d3VL3bVD4g+9h+L35fT/8fvN7ADgY9aHY5fpIvK82HO9ysu66wxWOzbkjcekKx0a2ALYA/n2AGi3a6ArFezcidziecQygNhhrcUficjP6PwBqtGijKxy/thnVBePHywYoDsFhl53GV8SEcsTx4usCMLUewTVpc23BNvEzm6Neyf1+KcG2vwqwUjgrOJq2JmHftwmkVBRGTvncFodnbI7vChO/FRznCmHsNM7aHM9Yk7Df5iqsLMw9sMNOK2g+jS4IEz0UJv4iuJZb2RltWnB4UZqH6ioGAgAAGe5vtiZhtzDx7OoRadLmeM7m6IRjhnLMW2Vx1bA5GhAmnhIcz6/xNj4Ujsky8UspwfayjDPjsF2Y6L7N8Vzx/BfP+KPg6LbgSqd8DnfJW2CnbaLhfH5ephpqygJYvQU4Z3P82TLRsDDhUTnmrSq+Y3N0Mg+Xldy/zwEAnLMWZ3pHpNExmfLs/t0dOdVcbT0JeKxUwFP2VljjqiE47Jp53LTXNxhsUZjerTByXWX6VZWRs/4bIQ2ACv+UAomgDzLCISNZxAxZKMhIDjLy1JfsaK+I+eGBUBNk5E2x8RogX/PdcDZUqieWTSh5D6nOVKqfhoycUmlHFFIyu5RXqf7AcQDISCpv/tqbMBqK883RtmpISRoxQyJKPgGn3wNk5NEigDFa6hslqV/Kj+FdBQD0bshIDlKSLlVcoWQo36UhR80BAMB73lulMn0EMpJTqD6qJiOt3mho/8GbkT2BZNgDB/V+RI0fkOrT3kRIVQbaDizJm2hdNbINBxwk5xAj3yEjuV9rZ1iIkgxixkLBA83mz8uCjLwoGwAx0vOnFSy5mtR4VTaAQvVORMnwZgSpzkrV/QmdE2tKe46+MQAAAABJRU5ErkJggg==")
        meta(http_equiv="Content-Type", content="text/html; charset=utf-8")
        script(raw("\n" + schema_org_json + "\n\t"), type="application/ld+json")


def _make_body(doc, title, version):
    _make_pylode_logo(doc, version)
    with doc:
        h1(title)


def _make_pylode_logo(doc, version):
    with doc:
        with div(id="pylode"):
            with p("made by "):
                with a(href="https://github.com/rdflib/pyLODE"):
                    span("p", id="p")
                    span("y", id="y")
                    span("LODE")
                a(version, href="https://github.com/rdflib/pyLODE/release/" + version, id="version")
    """
    <div id="pylode">
        made by <a href="http://github.com/rdflib/pyLODE">
        <span style="color:#329545;">p</span>
        <span style="color:#f9cb33;">y</span>LODE</a>
        <span style="font-size:smaller;">2.13.0</span>
    </div>
    """


if __name__ == "__main__":
    sdo_json = """[
      {
        "@id": "https://example.com",
        "@type": [
          "https://schema.org/DefinedTermSet"
        ],
        "https://schema.org/description": [
          {
            "@value": "<p>This ontology contains several simple classes and properties about animals that are defined only to show off pyLODE's ability to represent different forms of example rendering.</p>"
          }
        ],
        "https://schema.org/license": [
          {
            "@id": "https://creativecommons.org/licenses/by/4.0/"
          }
        ],
        "https://schema.org/name": [
          {
            "@value": "Examples Ontology"
          }
        ],
        "https://schema.org/rights": [
          {
            "@value": "&copy; SURROUND Australia Pty Ltd"
          }
        ]
      }
    ]"""
    version = "3.0.0"

    d = _make_document("Some Ont", sdo_json, version)
    open("some.html", "w").write(d.render())
