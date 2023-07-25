import shutil
from pathlib import Path
from typing import Type

import dominate
from dominate.tags import (
    style,
    link,
    meta,
    script,
    body,
    div,
    h1,
    table,
    colgroup,
    col,
    tbody,
    tr,
    td,
    p,
    strong,
    a,
    img,
    hr,
    ul,
    li,
    pre,
    code,
    thead,
    th,
    em,
)
from dominate.util import raw
from rdflib import (
    Graph,
    OWL,
    SDO,
    DCTERMS,
)
from pylode.profiles.supermodel.fragment import make_html_fragment

from pylode.utils import (
    PylodeError,
    load_ontology,
)
from pylode.profiles.supermodel.query import Query
from pylode.profiles.supermodel.model import ComponentModel, Class
from pylode.profiles.supermodel.component import metadata_row, h2, h3, h4, h5, h6

RDF_FOLDER = Path(__file__).parent / "rdf"


class Supermodel:
    def __init__(
        self, ontology: Graph | Path | str, QueryClass: Type[Query] = Query
    ) -> None:
        self.ont = load_ontology(ontology)
        self.query = QueryClass(self.ont)

        self.toc: dict[str, str] = {}
        self.fids: dict[str, str] = {}
        self.ns = self.query.get_ns()
        self.iri = self.query.get_supermodel_iri()
        self.figure_count = 0

        # make HTML doc with title
        title = self.query.get_title(self.iri)
        if title is None:
            raise PylodeError(
                "You MUST supply a title property "
                "(dcterms:title, rdf:label or sdo:name) for your ontology"
            )
        self.doc = dominate.document(title=title)

    def make_html(self, destination: Path = None, include_css: bool = True):
        self._make_head(
            self.query.get_schema_org_metadata_graph(),
            include_css=include_css,
            destination=destination,
        )
        self._make_body()

        if destination is not None:
            open(destination, "w").write(self.doc.render())
        else:
            return self.doc.render()

    def _make_body(self):
        self.body: body = self.doc.add(body(_class="book toc2 toc-left"))

        self._make_header(self.query.onts_props[DCTERMS.title])
        self._make_content()

    def _make_header(self, title: str):
        self.header: div = self.body.add(div(id="header"))
        self.header.add(h1(title))

    def _make_content(self):
        self.content = self.body.add(div(id="content"))
        self._make_preamble()
        self._make_images()
        self._make_component_models()

    def _make_component_model_class(self, cls: Class):
        with div(_class="sect3"):
            h4(f"Class: {cls.name}", True)

            with p():
                a(cls.iri, href=cls.iri)

            if cls.description:
                with div(_class="paragraph"):
                    p(cls.description)

            if cls.notes:
                for note in cls.notes:
                    with div(_class="admonitionblock note"):
                        with table():
                            with tbody():
                                with tr():
                                    with td(_class="icon"):
                                        div("Note", _class="title")
                                    td(note, _class="content")

            if cls.superclasses:
                h5("Subclass of")
                with div(_class="sect5"):
                    for superclass in cls.superclasses:
                        with div(_class="ulist"):
                            with ul():
                                with li():
                                    with p():
                                        a(superclass.name, href="#")

            if cls.images:
                h5("Images")
                with div(_class="sect5"):
                    for image in cls.images:
                        h6(image.name)
                        with div(_class="sect6"):
                            with div(_class="imageblock text-center"):
                                with div(_class="content"):
                                    img(src=image.url, alt=image.description)
                                div(
                                    f"Figure {self.figure_count + 1}. {image.description}",
                                    _class="title",
                                )
                                self.figure_count += 1

            if cls.examples:
                h5("Examples")
                with div(_class="sect5"):
                    for example in cls.examples:
                        with div(_class="listingblock"):
                            with div(_class="content"):
                                with pre(_class="highlight"):
                                    code(example)

            if cls.properties:
                h5("Properties")
                with div(_class="sect5"):
                    with table(
                        _class="tableblock frame-all grid-all stripes-odd fit-content stretch"
                    ):
                        with thead():
                            with tr():
                                th(
                                    "Property",
                                    _class="tableblock halign-left valign-top",
                                )
                                th(
                                    "Description",
                                    _class="tableblock halign-left valign-top",
                                )
                                th(
                                    "Cardinality",
                                    _class="tableblock halign-left valign-top",
                                )
                                th(
                                    "Value type",
                                    _class="tableblock halign-left valign-top",
                                )
                                th(
                                    "Value class type",
                                    _class="tableblock halign-left valign-top",
                                )
                        with tbody():
                            for property in cls.properties:
                                with tr():
                                    with td(_class="tableblock halign-left valign-top"):
                                        p(property.name)
                                        with em():
                                            p(f"From {property.belongs_to_class}")
                                    with td(_class="tableblock halign-left valign-top"):
                                        p(property.description)
                                    with td(_class="tableblock halign-left valign-top"):
                                        if (
                                            property.cardinality_min is None
                                            and property.cardinality_max is None
                                        ):
                                            p("[0..*]")
                                        elif (
                                            property.cardinality_min is None
                                            and isinstance(
                                                property.cardinality_max, int
                                            )
                                        ):
                                            p(f"[0..{property.cardinality_max}]")
                                        elif (
                                            isinstance(property.cardinality_min, int)
                                            and property.cardinality_max is None
                                        ):
                                            p(f"[{property.cardinality_min}..*]")
                                        elif (
                                            property.cardinality_min
                                            == property.cardinality_max
                                        ):
                                            p(f"[{property.cardinality_max}]")
                                        else:
                                            p(
                                                f"[{property.cardinality_min}..{property.cardinality_max}]"
                                            )
                                    with td(_class="tableblock halign-left valign-top"):
                                        p(property.value_type)
                                    with td(_class="tableblock halign-left valign-top"):
                                        p(property.value_class_type)

    def _make_component_model(self, component_model: ComponentModel):
        with div(_class="sect2"):
            h3(f"Module: {component_model.name}", True)
            with div(_class="sect3"):
                with div(_class="paragraph"):
                    with p():
                        a(component_model.iri, href=component_model.iri)

                if component_model.description:
                    with div(_class="paragraph"):
                        p(component_model.description)

                if component_model.images:
                    h4("Images")
                    with div(_class="sect4"):
                        for image in component_model.images:
                            h5(image.name, True)
                            with div(_class="sect5"):
                                with div(_class="imageblock text-center"):
                                    with div(_class="content"):
                                        img(src=image.url, alt=image.description)
                                    div(
                                        f"Figure {self.figure_count + 1}. {image.description}",
                                        _class="title",
                                    )
                                    self.figure_count += 1

                for cls in component_model.classes:
                    self._make_component_model_class(cls)

            hr()

    def _make_component_models(self):
        with self.content:
            with div(_class="sect1"):
                h2("Component Models", True)

                for component_model in self.query.component_models:
                    self._make_component_model(component_model)

    def _make_images(self):
        with self.content:
            with div(_class="sect1"):
                for image in self.query.images:
                    h2(image.name, True)
                    with div(_class="sectionbody"):
                        with div(_class="sect2"):
                            with div(_class="imageblock text-center"):
                                with div(_class="content"):
                                    img(src=image.url, alt=image.description)
                                div(
                                    f"Figure {self.figure_count + 1}. {image.description}",
                                    _class="title",
                                )
                                self.figure_count += 1

    def _make_preamble(self):
        with self.content:
            with div(id="preamble"):
                with div(_class="sectionbody"):
                    with table(
                        _class="tableblock frame-none grid-none stripes-odd stretch"
                    ):
                        with colgroup():
                            col(style="width: 100%")

                        with tbody():
                            with tr(style="background-color:white;"):
                                with td(_class="tableblock halign-right valign-top"):
                                    with p(_class="tableblock"):
                                        strong(
                                            "Intergovernmental Committee on Surveying and Mapping",
                                            _class="big",
                                        )

                            # Submission Date
                            if (
                                DCTERMS.created in self.query.onts_props
                                and len(self.query.onts_props[DCTERMS.created]) > 0
                            ):
                                metadata_row(
                                    "Submission Date",
                                    str(self.query.onts_props[DCTERMS.created][0]),
                                )

                            # Approval Date
                            if (
                                DCTERMS.dateAccepted in self.query.onts_props
                                and len(self.query.onts_props[DCTERMS.dateAccepted]) > 0
                            ):
                                metadata_row(
                                    "Approval Date",
                                    str(self.query.onts_props[DCTERMS.dateAccepted][0]),
                                )

                            # Publication Date
                            if (
                                DCTERMS.issued in self.query.onts_props
                                and len(self.query.onts_props[DCTERMS.issued]) > 0
                            ):
                                metadata_row(
                                    "Publication Date",
                                    str(self.query.onts_props[DCTERMS.issued][0]),
                                )

                            # External identifier of this document
                            metadata_row(
                                "External identifier of this document",
                                str(self.iri),
                                True,
                            )

                            # Internal reference number of this document
                            if (
                                SDO.identifier in self.query.onts_props
                                and len(self.query.onts_props[SDO.identifier]) > 0
                            ):
                                metadata_row(
                                    "Internal reference number of this document",
                                    str(self.query.onts_props[SDO.identifier][0]),
                                )

                            # Version
                            if (
                                OWL.versionInfo in self.query.onts_props
                                and len(self.query.onts_props[OWL.versionInfo]) > 0
                            ):
                                metadata_row(
                                    "Version",
                                    str(self.query.onts_props[OWL.versionInfo][0]),
                                )

                            # Category
                            if (
                                SDO.category in self.query.onts_props
                                and len(self.query.onts_props[SDO.category]) > 0
                            ):
                                categories = [
                                    str(category)
                                    for category in self.query.onts_props[SDO.category]
                                ]
                                metadata_row("Category", categories)

                            # Editors
                            if (
                                DCTERMS.creator in self.query.onts_props
                                and len(self.query.onts_props[DCTERMS.creator]) > 0
                            ):
                                editors = [
                                    str(editor)
                                    for editor in self.query.onts_props[DCTERMS.creator]
                                ]
                                metadata_row(
                                    "Editors",
                                    editors,
                                )

                            # Contributors
                            if (
                                DCTERMS.contributor in self.query.onts_props
                                and len(self.query.onts_props[DCTERMS.contributor]) > 0
                            ):
                                contributors = [
                                    str(contributor)
                                    for contributor in self.query.onts_props[
                                        DCTERMS.contributor
                                    ]
                                ]
                                metadata_row(
                                    "Contributors",
                                    contributors,
                                )

    def _make_head(
        self, schema_org: Graph, include_css: bool = True, destination: Path = None
    ):
        """Healper function for make_html(). Makes <head>???</head> content"""
        with self.doc.head:
            # use standard pyLODE stylesheet
            if include_css:
                style(
                    raw(
                        "\n"
                        + open(
                            Path(__file__).parent.parent.parent / "static/asciidoc.css"
                        ).read()
                        + "\n\t"
                    )
                )
            else:
                link(href="pylode.css", rel="stylesheet", type="text/css")
                shutil.copy(
                    Path(__file__).parent.parent / "pylode.css",
                    destination.parent / "pylode.css",
                )
            link(
                rel="icon",
                type="image/png",
                sizes="16x16",
                href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABhklEQVQ4jbWPzStEURjG3yQLirlGKUnKFO45Z+SjmXvnnmthQcpCoVhYmD/AwmJiI3OvZuZc2U3UlKU0/gAslMw9JgvhHxAr2fko7r0jHSsl+TgbTz2Lt5731/MASEiJW9ONml2QyX6rsGalmnT74v8BDf12hxJfpV8d1uwNKUBYszabdFv84L8B9X0rESVmmUup2fme0cVhJWaZHw4NWL1SewEAfDe6H3Dy6Ll456WEJsRZS630MwCAOI20ei5OBpxse5zcBZw8eS4uPpfIuDiCainIg9umBCU0GZzgLZ9Hn31OgoATL+CkLDGB5H1OKj4nFd/FBxUXJ0UZNb4edw/6nLyJXaj5FeCVyPLNIVmYK8TG1IwWb16L1gEACAFV90ftoT8bdOX0EeyY99gxBXZMgRz6qGb1KantAACI0UvE6F5XJqEjpsdURouI0Vt5gGOUkUNnPu7ObGIIMfNaGqDmjDRi9FZldF1lRgYzeqUyeoiY4ag5Iy3RgOYRM8+/M2bG8efsO4hGrpmJseyMAAAAAElFTkSuQmCC",
            )
            link(
                rel="icon",
                type="image/png",
                sizes="32x32",
                href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAC40lEQVRYhe2UT0hUQRzHp6Iss1B3VZKIDbbdfW9mnoi4f3zzjkJQeOgS0SEIb1EWBGGlLLu460zQPQM1unUIIjA6rfpm6ZAhHjoIRVQUFUlEbG+euTsdXG1d3VL3bVD4g+9h+L35fT/8fvN7ADgY9aHY5fpIvK82HO9ysu66wxWOzbkjcekKx0a2ALYA/n2AGi3a6ArFezcidziecQygNhhrcUficjP6PwBqtGijKxy/thnVBePHywYoDsFhl53GV8SEcsTx4usCMLUewTVpc23BNvEzm6Neyf1+KcG2vwqwUjgrOJq2JmHftwmkVBRGTvncFodnbI7vChO/FRznCmHsNM7aHM9Yk7Df5iqsLMw9sMNOK2g+jS4IEz0UJv4iuJZb2RltWnB4UZqH6ioGAgAAGe5vtiZhtzDx7OoRadLmeM7m6IRjhnLMW2Vx1bA5GhAmnhIcz6/xNj4Ujsky8UspwfayjDPjsF2Y6L7N8Vzx/BfP+KPg6LbgSqd8DnfJW2CnbaLhfH5ephpqygJYvQU4Z3P82TLRsDDhUTnmrSq+Y3N0Mg+Xldy/zwEAnLMWZ3pHpNExmfLs/t0dOdVcbT0JeKxUwFP2VljjqiE47Jp53LTXNxhsUZjerTByXWX6VZWRs/4bIQ2ACv+UAomgDzLCISNZxAxZKMhIDjLy1JfsaK+I+eGBUBNk5E2x8RogX/PdcDZUqieWTSh5D6nOVKqfhoycUmlHFFIyu5RXqf7AcQDISCpv/tqbMBqK883RtmpISRoxQyJKPgGn3wNk5NEigDFa6hslqV/Kj+FdBQD0bshIDlKSLlVcoWQo36UhR80BAMB73lulMn0EMpJTqD6qJiOt3mho/8GbkT2BZNgDB/V+RI0fkOrT3kRIVQbaDizJm2hdNbINBxwk5xAj3yEjuV9rZ1iIkgxixkLBA83mz8uCjLwoGwAx0vOnFSy5mtR4VTaAQvVORMnwZgSpzkrV/QmdE2tKe46+MQAAAABJRU5ErkJggg==",
            )
            meta(http_equiv="Content-Type", content="text/html; charset=utf-8")
            script(
                raw("\n" + schema_org.serialize(format="json-ld") + "\n\t"),
                type="application/ld+json",
                id="schema.org",
            )
