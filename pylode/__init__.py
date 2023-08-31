try:
    from pylode._version import __version__
except ImportError:
    __version__ = "0.0.0"

from .common import *
from .profiles import OntDoc, Prof, VocPub, NMPF, PROFILES, RDF_MEDIA_TYPES

__all__ = [
    "__version__",
    "OntDoc",
    "Prof",
    "VocPub",
    "NMPF",
    "PROFILES",
    "RDF_MEDIA_TYPES",
    "MakeDocco"
]
