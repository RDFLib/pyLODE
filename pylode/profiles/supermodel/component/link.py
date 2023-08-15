from dominate.tags import a, i


def external_link(value: str, href: str) -> a:
    """An anchor tag with an external icon with the target attribute set to _blank."""
    with a(
        value, href=href, target="_blank", style="white-space: nowrap;"
    ) as component:
        i(
            _class="fa fa-external-link",
            style="margin-left: 4px;",
        )

    return component
