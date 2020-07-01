from rdflib.plugin import register, Serializer
register("json-ld", Serializer, "rdflib_jsonld.serializer", "JsonLDSerializer")

from .common import *
from .profiles import OntDoc, Prof, VocPub, PROFILES, RDF_MEDIA_TYPES
