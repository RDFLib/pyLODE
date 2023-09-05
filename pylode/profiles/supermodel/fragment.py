from pylode.profiles.supermodel.random import random_id


def make_html_fragment(value: str | None):
    if value is None or value == "":
        return random_id()
    return value.replace(" ", "-")
