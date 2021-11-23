import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
from pylode.common import MakeDocco


def test_issue_155():
    m = MakeDocco(input_data_file=str(Path(__file__).parent.parent / "pylode" / "examples" / "examples-ont" / "examples.ttl"))
    html = m.document()

    assert '<a href="https://linked.data.gov.au/org/surround">surround</a>' in html


if __name__ == "__main__":
    test_issue_155()
