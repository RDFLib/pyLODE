from pathlib import Path

import pytest

from pylode import __version__
from pylode.profiles import ValPub

current_dir = Path(__file__).parent


@pytest.fixture(scope="session")
def fix_html():
    v = ValPub(current_dir / "data" / "valpub" / "basic.ttl")
    return v.make_html()


def test_basic(fix_html):
    expected_html = open(current_dir / "data" / "valpub" / "basic.html").read()
    expected_html = expected_html.replace("3.5.1", __version__)

    assert fix_html == expected_html
