import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
from pylode.common import MakeDocco


def test_issue_110():
    m = MakeDocco(input_data_file=str(Path(__file__).absolute().parent / "test_issue_110_input.ttl"))
    assert "balance between £1,000 and £1,000,000 GBP" in m.document()
