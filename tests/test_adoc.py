import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))
import pylode
from pathlib import Path


def test_adoc():
    examples_ont_path = str(Path(__file__).parent.parent / "pylode" / "examples" / "examples-ont" / "examples.ttl")
    adoc = pylode.MakeDocco(examples_ont_path, outputformat="adoc").document()
    assert(adoc.startswith("= Examples Ontology"))

