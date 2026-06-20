import sys
from pathlib import Path

sys.path.append(str(Path().parent.parent.resolve() / "pylode"))
import pytest

from pylode.profiles import OntPub
from pylode.utils import de_space_html, get_ns

current_dir = Path(__file__).parent


@pytest.fixture(scope="session")
def fix_html():
    od = OntPub(Path(__file__).parent / "data" / "issues-vocpub.ttl")
    return od.make_html()


def test_issue_230(fix_html):
    open("issues.html", "w").write(fix_html)
    assert de_space_html(
        """
          <div>
            <dt>
              <a class="hover_property" href="https://schema.org/codeRepository" title="Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex). Defined in None">Code Repository</a>
            </dt>
            <dd>
              <a href="https://github.com/tdwg/tdwg-vocabulary-registry">https://github.com/tdwg/tdwg-vocabulary-registry</a>
            </dd>
          </div>
        """
    ) in de_space_html(fix_html), "Code Repository information not included"
