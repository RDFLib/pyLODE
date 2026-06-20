
from pathlib import Path

import pytest

from pylode.profiles import OntPub, Supermodel
from pylode.utils import de_space_html

current_dir = Path(__file__).parent

@pytest.fixture(scope="session")
def fix_html():
    od = OntPub(Path(__file__).parent / "data" / "issues.ttl")
    return od.make_html()


def test_issue_261(fix_html):
    # open("issues.html", "w").write(fix_html)
    assert de_space_html(
        """[&gt;=0, &lt;42]"""
    ) in de_space_html(fix_html), "Min/Max datatype cardinality restriction incorrect"

    assert de_space_html(
        """[&lt;=42]"""
    ) in de_space_html(fix_html), "Max datatype cardinality restriction incorrect"