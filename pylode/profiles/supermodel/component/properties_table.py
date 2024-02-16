from dominate.tags import tr, td, p, a, i, span, ul, li, button, div
from rdflib import URIRef

from pylode.profiles.supermodel.model import (
    Property,
    CodedProperty,
    SimpleCodedProperty,
)
from pylode.profiles.supermodel.component import external_link, tooltip
from pylode.profiles.supermodel.fragment import make_html_fragment


def property_table_row(
    row_style: str,
    property_: Property,
    class_index,
    is_first: bool = False,
    has_secondary: bool = False,
    debug: bool = False,
):
    with tr(
        style=row_style,
        _class="property-row-main" if is_first else "property-row-secondary",
    ) as component:
        with td(
            _class="tableblock halign-left valign-top",
        ):
            p(property_.name)

            if property_.belongs_to_class is not None:
                div("Sourced from class:")
                with p(_class="tableblock whitespace-nowrap"):
                    if property_.belongs_to_class.iri in class_index:
                        a(
                            property_.belongs_to_class.name,
                            href=f"#{property_.belongs_to_class.iri}",
                        )
                    else:
                        external_link(
                            property_.belongs_to_class.name,
                            property_.belongs_to_class.iri,
                        )
                    with tooltip(
                        f"In profile {property_.profile.name}",
                        _class="property-row-profile-source",
                    ):
                        i(_class="fa fa-info cursor-help", aria_hidden="true")

                    with p(
                        f"In profile ",
                        _class="property-row-profile-source italic text-sm hidden",
                    ):
                        # TODO: Show as an external link if the profile is not a pylode:Module within the document.
                        fragment = make_html_fragment(property_.profile.iri)
                        a(property_.profile.name, href=f"#{fragment}")

            if is_first and has_secondary:
                with button(_class="property-row-button"):
                    i(_class="fa fa-arrow-circle-right")

        with td(_class="tableblock halign-left valign-top"):
            p(property_.description)
            if debug:
                if property_.method:
                    with tooltip(
                        f"Method: {property_.method}",
                        _class="property-row-profile-source",
                    ):
                        span("M", _class="font-bold cursor-help", aria_hidden="true")

                    p(
                        f"Method: {property_.method}",
                        _class="property-row-profile-source italic text-sm hidden",
                    )

                if property_.property_source:
                    with tooltip(
                        f"Property Source: {property_.property_source}",
                        _class="property-row-profile-source",
                    ):
                        span("PS", _class="font-bold cursor-help", aria_hidden="true")

                    p(
                        f"Property Source: {property_.property_source}",
                        _class="property-row-profile-source italic text-sm hidden",
                    )

        cardinality = ""
        if property_.cardinality_min is None and property_.cardinality_max is None:
            # Show nothing if no cardinality specified.
            ...
        elif property_.cardinality_min is None and isinstance(
            property_.cardinality_max, int
        ):
            cardinality = f"[0..{property_.cardinality_max}]"
        elif (
            isinstance(property_.cardinality_min, int)
            and property_.cardinality_max is None
        ):
            cardinality = f"[{property_.cardinality_min}..*]"
        elif property_.cardinality_min == property_.cardinality_max:
            cardinality = f"[{property_.cardinality_max}]"
        else:
            cardinality = f"[{property_.cardinality_min}..{property_.cardinality_max}]"

        with td(_class="tableblock halign-left valign-top"):

            with p(
                _class="tableblock",
            ):
                if not isinstance(property_, CodedProperty):
                    # Don't render this if it's a coded property since most coded properties
                    # will already render this same info based on their rdfs:range values.
                    for value_class_type in property_.value_class_types:
                        if value_class_type.iri in class_index:
                            fragment = make_html_fragment(value_class_type.iri)
                            with p("Expected class type "):
                                a(
                                    value_class_type.name,
                                    href=f"#{fragment}",
                                )
                        else:
                            with p("Expected class type "):
                                external_link(
                                    value_class_type.name,
                                    value_class_type.iri,
                                )

                if property_.constraints:
                    p(property_.constraints)

                # Coded property
                if isinstance(property_, CodedProperty):
                    span("Values expected to be from the following vocabulary:")
                    with ul():
                        for codelist in property_.codelist:
                            with li():
                                external_link(codelist.label, codelist.iri)
                    span("with an expected class type of:")

                    with ul():
                        for class_type in property_.value_class_types:
                            with li():
                                if class_type.iri in class_index:
                                    fragment = make_html_fragment(class_type.iri)
                                    a(
                                        class_type.name,
                                        href=f"#{fragment}",
                                    )
                                else:
                                    external_link(
                                        class_type.name,
                                        class_type.iri,
                                    )

            if cardinality:
                p(f"Cardinality: {cardinality}", _class="text-sm")

    return component


def property_table_vocabulary_row(
    row_style: str,
    property_: SimpleCodedProperty,
    class_index: set[URIRef],
    is_first: bool = False,
    has_secondary: bool = False,
):
    with tr(
        style=row_style,
        _class="property-row-main" if is_first else "property-row-secondary",
    ) as component:
        with td(
            _class="tableblock halign-left valign-top",
        ):
            with p(property_.name):
                if property_.description:
                    with tooltip(
                        property_.description,
                        _class="property-row-profile-source",
                    ):
                        i(_class="fa fa-info cursor-help", aria_hidden="true")

                    p(
                        property_.description,
                        _class="property-row-profile-source italic text-sm hidden",
                    )

            if is_first and has_secondary:
                with button(_class="property-row-button"):
                    i(_class="fa fa-arrow-circle-right")

        with td(_class="tableblock halign-left valign-top"):
            if property_.classes:
                with ul():
                    for cls in property_.classes:
                        with li():
                            if cls.iri in class_index:
                                a(
                                    cls.name,
                                    href=f"#{cls.iri}",
                                )
                            else:
                                external_link(cls.name, cls.iri)

        with td(_class="tableblock halign-left valign-top"):
            if property_.codelist:
                with ul():
                    for codelist in property_.codelist:
                        with li():
                            external_link(codelist.label, codelist.iri)

    return component
