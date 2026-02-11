from dominate.tags import a, button, code, div, i, li, p, span, td, tr, ul
from rdflib import Literal, URIRef

from pylode.profiles.supermodel.component import external_link, tooltip
from pylode.profiles.supermodel.fragment import make_html_fragment
from pylode.profiles.supermodel.model import (Class, CodedProperty, Property,
                                              Resource, SimpleCodedProperty)


def render_resource_or_literal(item: Resource | Literal, class_: Class, class_index):
    if isinstance(item, Literal):
        span(str(item))
    elif class_.iri in class_index:
        fragment = make_html_fragment(class_.iri)
        a(
            item.label,
            href=f"#{fragment}",
        )
    else:
        external_link(
            item.label,
            item.iri,
        )


def create_length_interval(property_: Property) -> str | None:
    parts = []
    if property_.min_length is not None:
        parts.append(f"≥ {property_.min_length}")
    if property_.max_length is not None:
        parts.append(f"≤ {property_.max_length}")

    return " and ".join(parts) if parts else None


def create_range_interval(property_: Property) -> str | None:
    parts = []
    if property_.min_inclusive is not None:
        parts.append(f"≥ {property_.min_inclusive}")
    elif property_.min_exclusive:
        parts.append(f"> {property_.min_exclusive}")

    if property_.max_inclusive is not None:
        parts.append(f"≤ {property_.max_inclusive}")
    elif property_.max_exclusive:
        parts.append(f"< {property_.max_exclusive}")

    return " and ".join(parts) if parts else None


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
                        "In profile ",
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
                style="margin-bottom: 0px;",
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
                    if property_.datatype is not None:
                        dt_class = property_.datatype
                        with p("Expected Datatype: "):
                            if dt_class.iri in class_index:
                                fragment = make_html_fragment(dt_class.iri)
                                a(dt_class.name, href=f"#{fragment}")
                            else:
                                external_link(dt_class.name, dt_class.iri)

                if property_.constraints:
                    p(property_.constraints)

            if cardinality:
                p(f"Cardinality: {cardinality}")

            # Other constraints
            if property_.has_value:
                with p("Value kind: "):
                    render_resource_or_literal(
                        Resource(property_.value_type.iri, property_.value_type.name),
                        property_.value_type,
                        class_index,
                    )
            if property_.has_value:
                with p("Expected value: "):
                    render_resource_or_literal(
                        property_.has_value, property_.belongs_to_class, class_index
                    )
            if property_.language_in:
                p("Allowable values:", style="margin-bottom: 0px;")
                with ul():
                    for item in property_.value_in:
                        with li():
                            render_resource_or_literal(
                                item, property_.belongs_to_class, class_index
                            )
            if property_.regex_pattern:
                with p("Expected to match pattern: "):
                    code(property_.regex_pattern)
            if property_.language_in:
                with p("Allowable languages:", style="margin-bottom: 0px;"), ul():
                    for lang in property_.language_in:
                        li(code(lang))
            if property_.unique_lang is not None:
                p("Only one value per language is expected.")
            length_string = create_length_interval(property_)
            if length_string:
                p(f"Length: {length_string}")
            value_range_string = create_range_interval(property_)
            if value_range_string is not None:
                p(f"Range: {value_range_string}")
            if property_.less_than_predicates:
                p(
                    "Values are expected to be less than the values for the following properties:",
                    style="margin-bottom: 0px;",
                )
                with ul():
                    for pred in property_.less_than_predicates:
                        with li():
                            render_resource_or_literal(
                                pred, property_.belongs_to_class, class_index
                            )
            if property_.less_than_or_equals_predicates:
                p(
                    "Values are expected to be less than or equal to the values for the following properties:",
                    style="margin-bottom: 0px;",
                )
                with ul():
                    for pred in property_.less_than_or_equals_predicates:
                        with li():
                            render_resource_or_literal(
                                pred, property_.belongs_to_class, class_index
                            )
            if property_.equals_predicates:
                p(
                    "Values are expected to be equal the values for the following properties:",
                    style="margin-bottom: 0px;",
                )
                with ul():
                    for pred in property_.equals_predicates:
                        with li():
                            render_resource_or_literal(
                                pred, property_.belongs_to_class, class_index
                            )
            if property_.disjoint_predicates:
                p("Disjoint with:", style="margin-bottom: 0px;")
                with ul():
                    for pred in property_.disjoint_predicates:
                        with li():
                            render_resource_or_literal(
                                pred, property_.belongs_to_class, class_index
                            )
            if property_.default_value is not None:
                with p("Default value:"):
                    render_resource_or_literal(
                        property_.default_value, property_.belongs_to_class, class_index
                    )

            # Coded property
            if isinstance(property_, CodedProperty):
                p(
                    "Values expected to be from the following vocabulary:",
                    style="margin-bottom: 0px;",
                )
                with ul():
                    for codelist in property_.codelist:
                        with li():
                            external_link(codelist.label, codelist.iri)
                p("with an expected class type of:", style="margin-bottom: 0px;")

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
