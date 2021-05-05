import pylode
from pathlib import Path

examples_ont_path = str(Path(__file__).parent.parent / "pylode" / "examples" / "examples-ont" / "examples.ttl")
pylode.MakeDocco(examples_ont_path, outputformat="adoc").document(destination="examples.adoc")
