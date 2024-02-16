import logging
from itertools import chain

from rdflib import URIRef, Graph, Dataset, Literal, RDFS, SKOS, SDO, DCTERMS

from pylode.profiles.supermodel.model import Class, Ontology

logger = logging.getLogger(__name__)


def get_values(
    iri: URIRef, graph: Graph, properties: list[URIRef]
) -> list[URIRef | Literal]:
    result = list(
        chain.from_iterable([graph.objects(iri, prop) for prop in properties])
    )

    for value in result:
        if not isinstance(value, (URIRef, Literal)):
            raise ValueError(
                f"Expected only IRIs or literals but found type {type(value)} with value {value} for IRI {iri}"
            )

    return result


def get_name(iri: URIRef, graph: Graph, db: Dataset = None) -> str:
    """Get name for resource.

    If no name found for graph (profile context), look in
    dataset (union of all graphs). If still no name found,
    fall back to using a curie.
    """
    name_predicates = [RDFS.label, SKOS.prefLabel, SDO.name]

    names = get_values(iri, graph, name_predicates)

    if not names and db is not None:
        names = get_values(iri, db, name_predicates)

    if not names:
        try:
            names.append(graph.qname(iri))
        except ValueError as err:
            logger.warning(
                f"Failed to create a qname for IRI {iri}. Reason: {err}. Adding full IRI as name instead."
            )

    return str(names[0]) if len(names) > 0 else str(iri)


def get_descriptions(iri: URIRef, graph: Graph) -> str:
    descriptions = get_values(
        iri, graph, [SKOS.definition, DCTERMS.description, SDO.description]
    )
    return (
        " ".join(sorted(str(i) for i in descriptions))
        if len(descriptions) > 0
        else None
    )


def get_class(iri: URIRef, graph: Graph, db: Dataset, ignored_classes: list[URIRef]) -> Class:
    name = get_name(iri, graph, db)
    subclasses = get_subclasses(iri, graph, db, ignored_classes)
    return Class(iri, name, subclasses=subclasses)


def get_subclasses(
    iri: URIRef, graph: Graph, db: Dataset, ignored_classes: list[URIRef]
) -> list[Class]:
    subclasses = filter(
        lambda x: x not in ignored_classes and isinstance(x, URIRef),
        list(graph.subjects(RDFS.subClassOf, iri)),
    )
    return sorted(
        [get_class(subclass, graph, db, ignored_classes) for subclass in subclasses],
        key=lambda x: x.name,
    )


def get_is_defined_by(iri: URIRef, graph: Graph, db: Dataset) -> Ontology | None:
    is_defined_by = get_values(iri, graph, [RDFS.isDefinedBy])
    ontology = is_defined_by[0] if len(is_defined_by) > 0 else None
    if ontology is not None:
        name = get_name(ontology, graph, db)
        return Ontology(iri=ontology, name=name)
    return None
