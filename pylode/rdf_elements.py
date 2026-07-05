from rdflib import Namespace
from rdflib.namespace import *

ONTPUB = Namespace("https://linked.data.gov.au/def/ontpub/")

# OntPub
ONTOLOGY_PROPS = [
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
    ONTPUB.restriction,
    OWL.imports,
    SDO.codeRepository,
    #SKOS.hasTopConcept, -- catered for in Concept Hierarchy
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
    ONTPUB.inDomainOf,
    ONTPUB.inDomainIncludesOf,
    ONTPUB.inRangeOf,
    ONTPUB.inRangeIncludesOf,
    ONTPUB.restriction,
    ONTPUB.hasInstance,
    ONTPUB.superClassOf,
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
    ONTPUB.superPropertyOf,
    RDFS.domain,
    SDO.domainIncludes,
    RDFS.range,
    SDO.rangeIncludes,
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

DATATYPE_CARDINALITIES = {
    XSD.minInclusive: ">=",
    XSD.minExclusive: ">",
    XSD.maxInclusive: "<=",
    XSD.maxExclusive: "<",
}

# VocPub
CONCEPT_SCHEME_PROPS = [
    SKOS.prefLabel,
    SKOS.definition,
    DCTERMS.publisher,
    DCTERMS.creator,
    DCTERMS.contributor,
    DCTERMS.created,
    DCTERMS.modified,
    DCTERMS.issued,
    DCTERMS.license,
    SDO.copyrightNotice,
    SDO.copyrightYear,
    SDO.version,
    SKOS.historyNote,
    DCTERMS.source,
    DCTERMS.provenance,
    SDO.codeRepository,
    SDO.identifier,
    SDO.citation,
    SDO.keywords,
    DCAT.theme,
    SDO.status,
]

COLLECTION_PROPS = [
    SKOS.prefLabel,
    SKOS.definition,
    SKOS.altLabel,
    SKOS.inScheme,
    RDFS.isDefinedBy,
    SKOS.example,
    SKOS.broader,
    SKOS.narrower,
    SKOS.related,
    SKOS.scopeNote,
    SKOS.note,
    DCTERMS.source,
    DCTERMS.provenance,
    SDO.citation,
    SDO.status,
]

CONCEPT_PROPS = [
    SKOS.prefLabel,
    SKOS.definition,
    SKOS.altLabel,
    SKOS.inScheme,
    RDFS.isDefinedBy,
    SKOS.example,
    SKOS.broader,
    SKOS.narrower,
    SKOS.related,
    SKOS.scopeNote,
    SKOS.note,
    DCTERMS.source,
    DCTERMS.provenance,
    SDO.citation,
    SDO.status,
]

# VocPub
SHAPES_GRAPH_PROPS = [
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
    OWL.imports,
    SDO.codeRepository,
    RDFS.member,
    ONTPUB.defines
]

NODE_SHAPE_PROPS = [
    DCTERMS.title,
    DCTERMS.description,

    RDFS.isDefinedBy,
    SDO.memberOf,
    SH.message,
    SH.property
]

PROPERTY_SHAPE_PROPS = [
    DCTERMS.title,
    DCTERMS.description,

    RDFS.isDefinedBy,
    SDO.memberOf,
    SH.message,
    SH.path,
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

# all known properties
PROPS = set(
    ONTOLOGY_PROPS
    + CLASS_PROPS
    + PROP_PROPS
    + RESTRICTION_PROPS

    + CONCEPT_SCHEME_PROPS
    + COLLECTION_PROPS
    + CONCEPT_PROPS

    + SHAPES_GRAPH_PROPS
    + NODE_SHAPE_PROPS
    + PROPERTY_SHAPE_PROPS

    + AGENT_PROPS
)

ELEMENT_TYPES = {
    OWL.Class: ("c", "OWL/RDFS Class"),
    RDF.Property: ("p", "RDF Property"),
    OWL.ObjectProperty: ("op", "OWL Object Property"),
    OWL.DatatypeProperty: ("dp", "OWL Datatype Property"),
    OWL.AnnotationProperty: ("ap", "OWL Annotation Property"),
    OWL.FunctionalProperty: ("fp", "OWL Functional Property"),
    OWL.InverseFunctionalProperty: ("ifp", "OWL Inverse Functional Property"),
    RDFS.Datatype: ("dt", "RDFS Datatypes"),
    OWL.NamedIndividual: ("ni", "OWL Named Individual"),
    SKOS.ConceptScheme: ("cs", "SKOS Concept Scheme"),
    SKOS.Collection: ("col", "SKOS Collection"),
    SKOS.Concept: ("co", "SKOS Concept"),
    SH.NodeShape: ("ns", "SH NodeShape"),
    SH.PropertyShape: ("ps", "SH PropertyShape"),
}