import sys
from pathlib import Path
sys.path.append(str(Path().absolute().parent.parent / "pylode"))
from pylode.ontdoc import OntDoc
from pylode import __version__
from rdflib import Graph
import pytest
import re
from pylode.utils import de_space_html

input_rdf = Path(__file__).parent / "abisdm.ttl"
output_html = Path(__file__).parent / "abisdm.html"

OntDoc(input_rdf).make_html(output_html)