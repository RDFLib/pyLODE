from dominate.tags import tr, td, p, a, i, span, ul, li, button

from pylode.profiles.supermodel.component import external_link, tooltip
from pylode.profiles.supermodel.fragment import make_html_fragment


def property_table_row(
    row_style: str,
    property_,
    class_index,
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
            # TODO: have a property tracker
            # If property is documented, link to it with fragment id,
            # else, provide an external link to the IRI.
            fragment = make_html_fragment(property_.iri)
            with p():
                a(property_.name, href=f"#{fragment}")

            if is_first and has_secondary:
                with button(_class="property-row-button"):
                    i(_class="fa fa-arrow-circle-right")

        with td(_class="tableblock halign-left valign-top"):
            if property_.belongs_to_class is not None:
                with p(_class="tableblock"):
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
                    with tooltip(f"In profile {property_.profile.name}"):
                        i(_class="fa fa-info", aria_hidden="true")
        with td(_class="tableblock halign-left valign-top"):
            p(property_.description)
        with td(_class="tableblock halign-left valign-top"):
            if property_.cardinality_min is None and property_.cardinality_max is None:
                p("[0..*]", _class="tableblock")
            elif property_.cardinality_min is None and isinstance(
                property_.cardinality_max, int
            ):
                p(
                    f"[0..{property_.cardinality_max}]",
                    _class="tableblock",
                )
            elif (
                isinstance(property_.cardinality_min, int)
                and property_.cardinality_max is None
            ):
                p(
                    f"[{property_.cardinality_min}..*]",
                    _class="tableblock",
                )
            elif property_.cardinality_min == property_.cardinality_max:
                p(
                    f"[{property_.cardinality_max}]",
                    _class="tableblock",
                )
            else:
                p(
                    f"[{property_.cardinality_min}..{property_.cardinality_max}]",
                    _class="tableblock",
                )
        # with td(
        #     _class="tableblock halign-left valign-top"
        # ):
        #     if property_.value_type is not None:
        #         if (
        #             property_.value_type.iri
        #             in self.query.class_index
        #         ):
        #             fragment = make_html_fragment(
        #                 property_.value_type.iri
        #             )
        #             a(
        #                 property_.value_type.name,
        #                 href=f"#{fragment}",
        #             )
        #         else:
        #             external_link(
        #                 property_.value_type.name,
        #                 property_.value_type.iri,
        #             )

        with td(_class="tableblock halign-left valign-top"):

            with p(
                _class="tableblock",
            ):
                for value_class_type in property_.value_class_types:
                    if value_class_type.iri in class_index:
                        fragment = make_html_fragment(value_class_type.iri)
                        a(
                            value_class_type.name,
                            href=f"#{fragment}",
                        )
                    else:
                        external_link(
                            value_class_type.name,
                            value_class_type.iri,
                        )

                # Coded properties
                for coded_property in property_.coded_properties:
                    span("Values expected to be from the following vocabulary:")
                    with ul():
                        for codelist in coded_property.codelist:
                            with li():
                                external_link(codelist, codelist)
                    span("with an expected class type of:")
                    if coded_property.expected_value in class_index:
                        fragment = make_html_fragment(coded_property.expected_value)
                        a(
                            coded_property.expected_value,
                            href=f"#{fragment}",
                        )
                    else:
                        external_link(
                            coded_property.expected_value,
                            coded_property.expected_value,
                        )

    return component
