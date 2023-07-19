from dataclasses import dataclass, field

from rdflib import URIRef, Literal


@dataclass
class Image:
    url: str
    name: str
    description: str
    order: int

    def __post_init__(self):
        if self.name is None:
            self.name = ""
        if self.description is None:
            self.description = ""
        if self.order is None:
            self.order = 9999


@dataclass
class Property:
    iri: URIRef
    name: str
    description: str
    belongs_to_class: "Class"
    cardinality: str = None
    value_type: str = None
    value_class_type: URIRef = None

    def __post_init__(self):
        if self.cardinality is None:
            self.cardinality = "0..*"


@dataclass
class Class:
    iri: URIRef
    name: str
    description: str = None
    superclasses: list["Class"] = field(default_factory=list)
    properties: list[Property] = field(default_factory=list)
    images: list[Image] = field(default_factory=list)
    examples: list[Literal] = field(default_factory=list)


@dataclass
class ComponentModel:
    iri: URIRef
    name: str
    description: str = None
    classes: list[Class] = field(default_factory=list)
    images: list[Image] = field(default_factory=list)
    order: int = None

    def __post_init__(self):
        if self.order is None:
            self.order = 9999
