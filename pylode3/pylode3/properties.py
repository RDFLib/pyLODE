from rdflib import Namespace
from rdflib.namespace import (
    DC,
    DCTERMS,
    DOAP,
    FOAF,
    ORG,
    OWL,
    PROF,
    PROV,
    RDF,
    RDFS,
    SDO,
    SKOS,
    VANN,
)

ONTDOC = Namespace("https://w3id.org/profile/ontdoc/")

ONT_PROPS = [
    DCTERMS.title,
    DCTERMS.publisher,
    DCTERMS.creator,
    DCTERMS.contributor,
    DCTERMS.created,
    DCTERMS.modified,
    DCTERMS.issued,
    DCTERMS.license,
    DCTERMS.rights,
    OWL.versionIRI,
    OWL.versionInfo,
    OWL.priorVersion,
    SKOS.scopeNote,
    DCTERMS.source,
    DCTERMS.provenance,
    SKOS.note,
    DCTERMS.description,
    ONTDOC.restriction,
]

CLASS_PROPS = [
    RDFS.isDefinedBy,
    DCTERMS.title,
    DCTERMS.description,
    SKOS.scopeNote,
    SKOS.example,
    DCTERMS.source,
    DCTERMS.provenance,
    SKOS.note,
    RDFS.subClassOf,
    OWL.equivalentClass,
    # OWL.restriction,
    ONTDOC.inDomainOf,
    ONTDOC.inDomainIncludesOf,
    ONTDOC.inRangeOf,
    ONTDOC.inRangeIncludesOf,
    ONTDOC.restriction,
    ONTDOC.hasInstance,
    ONTDOC.superClassOf,
]

PROP_PROPS = [
    RDFS.isDefinedBy,
    DCTERMS.title,
    DCTERMS.description,
    SKOS.scopeNote,
    SKOS.example,
    DCTERMS.source,
    DCTERMS.provenance,
    SKOS.note,
    RDFS.subPropertyOf,
    ONTDOC.superPropertyOf,
    RDFS.domain,
    SDO.domainIncludes,
    RDFS.range,
    SDO.rangeIncludes,
]

AGENT_PROPS = [
    SDO.name,
    SDO.affiliation,
    SDO.identifier,
    SDO.email,
    SDO.honorificPrefix,
    SDO.url,
]

RESTRICTION_PROPS = [
    OWL.allValuesFrom,
    OWL.someValuesFrom,
    OWL.hasValue,
    OWL.onProperty,
    OWL.onClass,
    OWL.cardinality,
    OWL.qualifiedCardinality,
    OWL.minCardinality,
    OWL.minQualifiedCardinality,
    OWL.maxCardinality,
    OWL.maxQualifiedCardinality,
]

PROPS = set(ONT_PROPS + CLASS_PROPS + PROP_PROPS + AGENT_PROPS + RESTRICTION_PROPS)

RDF_ONT_TYPES = {
    "c": "OWL/RDFS Class",
    "p": "RDF Property",
    "op": "OWL Object Property",
    "dp": "OWL Datatype Property",
    "ap": "OWL Annotation Property",
    "fp": "OWL Functional Property",
    "ni": "OWL Named Individual",
}

ONT_TYPES = {
    OWL.Class: ("c", "OWL/RDFS Class"),
    RDF.Property: ("p", "RDF Property"),
    OWL.ObjectProperty: ("op", "OWL Object Property"),
    OWL.DatatypeProperty: ("dp", "OWL Datatype Property"),
    OWL.AnnotationProperty: ("ap", "OWL Annotation Property"),
    OWL.FunctionalProperty: ("fp", "OWL Functional Property"),
    OWL.InverseFunctionalProperty: ("ifp", "OWL Inverse Functional Property"),
    OWL.NamedIndividual: ("ni", "OWL Named Individual"),
}

RESTRICTION_TYPES = [
    OWL.cardinality,
    OWL.qualifiedCardinality,
    OWL.minCardinality,
    OWL.minQualifiedCardinality,
    OWL.maxCardinality,
    OWL.maxQualifiedCardinality,
    OWL.allValuesFrom,
    OWL.someValuesFrom,
    OWL.hasValue,
]
