import sys
from pathlib import Path

sys.path.append(str(Path().parent.parent.resolve() / "pylode"))
import pytest

from pylode.profiles import ValPub
from pylode.utils import de_space_html

current_dir = Path(__file__).parent


@pytest.fixture(scope="session")
def fix_html():
    v = ValPub(current_dir / "data" / "valpub" / "basic.ttl")
    return v.make_html()


def test_basic(fix_html):
    expected_html = open(current_dir / "data" / "valpub" / "basic.html").read()

    assert fix_html == expected_html
