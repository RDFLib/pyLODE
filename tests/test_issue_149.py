import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
from pylode.common import MakeDocco


def test_issue_149():
    m = MakeDocco(input_data_file=str(Path(__file__).parent / "simpleont.ttl"))
    html = m.document()
    html_img = html.replace(
        '<div style="width:500px; height:50px; background-color: lightgrey; border:solid 2px grey; padding:10px;margin-bottom:5px; text-align:center;">Pictures say 1,000 words</div>',
        '<img src="fake.png" />'
    )
    assert '<img src="fake.png" />' in html_img
    assert '<div style="width:500px;' not in html_img


if __name__ == "__main__":
    test_issue_149()
