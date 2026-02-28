from rdflib import Namespace
from rdflib.namespace import (
    DCTERMS,
    OWL,
    RDF,
    RDFS,
    SDO,
    SKOS,
    VANN,
)

ONTDOC = Namespace("https://w3id.org/profile/ontdoc/")

# metadata properties for OWL Ontology instances
ONT_PROPS = [
    DCTERMS.title,
    DCTERMS.publisher,
    DCTERMS.creator,
    DCTERMS.contributor,
    DCTERMS.created,
    DCTERMS.dateAccepted,
    DCTERMS.modified,
    DCTERMS.issued,
    DCTERMS.license,
    DCTERMS.rights,
    SDO.category,
    OWL.versionIRI,
    OWL.versionInfo,
    OWL.priorVersion,
    SDO.identifier,
    VANN.preferredNamespacePrefix,
    VANN.preferredNamespaceUri,
    SKOS.historyNote,
    SKOS.scopeNote,
    DCTERMS.source,
    DCTERMS.provenance,
    SKOS.note,
    DCTERMS.description,
    ONTDOC.restriction,
]

# properties for OWL Class instances
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

# properties for instances of RDF Property and OWL specialised
# forms, such as ObjectProperty etc.
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

# properties for Agents
AGENT_PROPS = [
    SDO.name,
    SDO.affiliation,
    SDO.identifier,
    SDO.email,
    SDO.honorificPrefix,
    SDO.url,
]

# properties for OWL restriction instances
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

# all known properties
PROPS = set(ONT_PROPS + CLASS_PROPS + PROP_PROPS + AGENT_PROPS + RESTRICTION_PROPS)

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

OWL_SET_TYPES = [OWL.unionOf, OWL.intersectionOf]
