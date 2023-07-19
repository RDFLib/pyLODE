from dominate import tags

from pylode.profiles.supermodel.fragment import make_html_fragment


def heading(
    value: str,
    heading_type: str,
    generate_fragment_from_value: bool,
    identifier: str | None,
) -> tags.h1 | tags.h2 | tags.h3 | tags.h4 | tags.h5 | tags.h6:
    """Generate a Dominate HTML heading.

    :param value: Value of the heading.
    :param heading_type: The HTML heading type. One of ("h1", "h2", "h3", "h4", "h5", "h6").
    :param generate_fragment_from_value: Whether to generate the fragment ID based on the value.
    :param identifier: This is used for the identifier only if `generate_fragment_from_value` is False.
    """
    if generate_fragment_from_value:
        fragment_id = make_html_fragment(value)
    else:
        fragment_id = make_html_fragment(identifier)

    dominate_heading = getattr(tags, heading_type)

    with dominate_heading(id=fragment_id) as component:
        tags.a(
            _class="anchor",
            href=f"#{fragment_id}",
        )
        tags.div(value or "")

        return component


def h2(
    value: str,
    generate_fragment_from_value: bool = False,
    identifier: str = None,
) -> tags.h2:
    return heading(value, "h2", generate_fragment_from_value, identifier)


def h3(
    value: str,
    generate_fragment_from_value: bool = False,
    identifier: str = None,
) -> tags.h3:
    return heading(value, "h3", generate_fragment_from_value, identifier)


def h4(
    value: str,
    generate_fragment_from_value: bool = False,
    identifier: str = None,
) -> tags.h4:
    return heading(value, "h4", generate_fragment_from_value, identifier)


def h5(
    value: str,
    generate_fragment_from_value: bool = False,
    identifier: str = None,
) -> tags.h5:
    return heading(value, "h5", generate_fragment_from_value, identifier)


def h6(
    value: str,
    generate_fragment_from_value: bool = False,
    identifier: str = None,
) -> tags.h6:
    return heading(value, "h6", generate_fragment_from_value, identifier)
