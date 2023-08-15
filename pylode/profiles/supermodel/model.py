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
    cardinality_min: int = None
    cardinality_max: int = None
    value_type: "Class" = None
    value_class_type: "Class" = None


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
    images: list[Image] = field(default_factory=list)
    examples: list[Literal] = field(default_factory=list)
    notes: list[Note] = field(default_factory=list)

    def __eq__(self, other):
        if not isinstance(other, Class):
            return False

        return self.iri == other.iri


@dataclass
class ComponentModel:
    iri: URIRef
    name: str
    description: str = None
    classes: list[Class] = field(default_factory=list)
    top_level_classes: list[Class] = field(default_factory=list)
    images: list[Image] = field(default_factory=list)
    order: int = None
    ignored_classes: list[URIRef] = field(default_factory=list)

    def __post_init__(self):
        if self.order is None:
            self.order = 9999
