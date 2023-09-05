from abc import ABC
from datetime import date
from dataclasses import dataclass, field

from rdflib import URIRef, Literal


DEFAULT_ORDER_VALUE = 999999


@dataclass
class MediaObject(ABC):
    name: str
    description: str
    encoding_format: str
    source: str
    # TODO: had role
    order: int | float

    def __post_init__(self):
        if self.name is None:
            self.name = ""
        if self.description is None:
            self.description = ""
        if self.order is None:
            self.order = DEFAULT_ORDER_VALUE


@dataclass
class ImageObject(MediaObject):
    url: str
    caption: str

    def __hash__(self) -> int:
        return hash(self.url)


@dataclass
class TextObject(MediaObject):
    text: str


@dataclass
class Property:
    iri: URIRef
    name: str
    description: str
    belongs_to_class: "Class" = None
    cardinality_min: int = None
    cardinality_max: int = None
    value_type: "Class" = None
    value_class_types: list["Class"] = field(default_factory=list)


@dataclass
class Note:
    value: str
    type: str

    def __post_init__(self):
        note_types = (
            "note",
            "Change Note",
            "Editorial Note",
            "History Note",
            "Scope Note",
        )
        if self.type not in note_types:
            raise ValueError(
                f"An instance of Note's 'type' attribute must have one of the following values: {note_types}. Received '{self.type}' instead."
            )


@dataclass
class Class:
    iri: URIRef
    name: str
    description: str = None
    subclasses: list["Class"] = field(default_factory=list)
    superclasses: list["Class"] = field(default_factory=list)
    properties: list[Property] = field(default_factory=list)
    examples: list[MediaObject] = field(default_factory=list)
    examples: list[Literal] = field(default_factory=list)
    notes: list[Note] = field(default_factory=list)
    is_defined_by: "Ontology" = None

    def __eq__(self, other):
        if not isinstance(other, Class):
            return False

        return self.iri == other.iri


@dataclass
class RDFProperty:
    iri: URIRef
    name: str
    description: str = None
    notes: list[Note] = field(default_factory=list)
    is_defined_by: "Ontology" = None
    super_properties: list["RDFProperty"] = field(default_factory=list)
    domain_includes: list[Class] = field(default_factory=list)
    range_includes: list[Class] = field(default_factory=list)


@dataclass
class ComponentModel:
    iri: URIRef
    name: str
    description: str = None
    classes: list[Class] = field(default_factory=list)
    top_level_classes: list[Class] = field(default_factory=list)
    examples: list[MediaObject] = field(default_factory=list)
    order: int = None
    ignored_classes: list[URIRef] = field(default_factory=list)
    annotation_properties: list[RDFProperty] = field(default_factory=list)
    datatype_properties: list[RDFProperty] = field(default_factory=list)
    object_properties: list[RDFProperty] = field(default_factory=list)
    ontology_properties: list[RDFProperty] = field(default_factory=list)

    def __post_init__(self):
        if self.order is None:
            self.order = DEFAULT_ORDER_VALUE


@dataclass
class Metadata:
    name: str
    date_created: date
    date_modified: date
    date_accepted: date
    date_issued: date
    version_info: str
    categories: list[str]
    contributors: list[str]
    creators: list[str]
    property_values: dict[str, str]
    publisher: str


@dataclass
class Ontology:
    iri: str
    name: str
