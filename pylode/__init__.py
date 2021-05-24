from rdflib.plugin import register, Serializer
register("json-ld", Serializer, "rdflib_jsonld.serializer", "JsonLDSerializer")
__version__ = "2.9.3"

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
