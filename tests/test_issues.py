import sys
from pathlib import Path

sys.path.append(str(Path().parent.parent.resolve() / "pylode"))
import pytest
from rdflib import Literal, URIRef
from rdflib.namespace import DCTERMS, RDFS, XSD

from pylode.profiles import OntPub
from pylode.utils import *

current_dir = Path(__file__).parent


# scope="session" so that this is reused without regeneration in this testing session
@pytest.fixture(scope="session")
def fix_ont():
    od = OntPub(Path(__file__).parent / "data" / "prof.ttl")
    return od.ont

