from rdflib import URIRef
from rdflib.namespace import Namespace, DefinedNamespace


class SM(DefinedNamespace):
    _fail = True
    _underscore_num = True
    _NS = Namespace("https://linked.data.gov.au/def/supermodel/")

    Supermodel: URIRef
    ComponentModel: URIRef
    componentModel: URIRef
