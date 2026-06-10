import sys
from pathlib import Path

sys.path.append(str(Path().absolute().parent / "pylode"))

from pylode.profiles.ontpub import OntPub
from pylode.profiles.vocpub import VocPub

EXAMPLES_DIR = Path(__file__).parent / "ontpub"

for f in sorted(Path(EXAMPLES_DIR).glob("*.ttl")):
    html_file = Path(EXAMPLES_DIR / Path(f.stem + ".html")).absolute()
    print(f"regenerating {html_file}")

    OntPub(f).make_html(destination=html_file)

EXAMPLES_DIR = Path(__file__).parent / "vocpub"

for f in sorted(Path(EXAMPLES_DIR).glob("*.ttl")):
    html_file = Path(EXAMPLES_DIR / Path(f.stem + ".html")).absolute()
    print(f"regenerating {html_file}")

    VocPub(f).make_html(destination=html_file)