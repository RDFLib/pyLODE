from dominate.tags import html_tag


class tooltip(html_tag):
    """A Shoelace tooltip custom element."""

    def __init__(self, content: str, *args, **kwargs):
        self.tagname = "sl-tooltip"
        super().__init__(*args, content=content, **kwargs)
