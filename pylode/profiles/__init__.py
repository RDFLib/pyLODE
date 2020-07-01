from os import path
import sys
sys.path.insert(0, path.dirname(path.dirname(path.realpath(__file__))))  # pylode module
import pprint
pprint.pprint(sys.path)
from .ontdoc import OntDoc
from .prof import Prof
from .vocpub import VocPub
