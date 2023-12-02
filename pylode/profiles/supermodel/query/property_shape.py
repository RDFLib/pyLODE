import math
from collections import defaultdict

from rdflib import URIRef, Dataset, RDF, SH, Graph, BNode
from rdflib.collection import Collection

from pylode.profiles.supermodel.model import Property, Profile, Class, ProfileType
from pylode.profiles.supermodel.query.common import (
    get_descriptions,
    get_class,
    get_is_defined_by,
)
from pylode.profiles.supermodel.query import get_name


def get_property_shapes(iri: URIRef, graph: Graph) -> dict[str, list[URIRef | BNode]]:
    """Get the property shapes for the given class IRI."""
    property_shapes = defaultdict(list)

    # Get property shapes from node shapes found via sh:targetClass.
    nodeshapes = list(graph.subjects(SH.targetClass, iri))
    for nodeshape in nodeshapes:
        property_shapes[nodeshape] += list(graph.objects(nodeshape, SH.property))

    # Get property shapes from node shape via implicit target class.
    property_shapes[iri] += list(graph.objects(iri, SH.property))

    return property_shapes


def get_sh_path(
    property_shape: URIRef | BNode, profile_graph: Graph, db: Dataset
) -> URIRef | None:
    """Get the sh:path value of a property shape."""
    sh_path = db.value(property_shape, SH.path)

    if sh_path is None:
        return None
    elif isinstance(sh_path, BNode):
        rdf_list = Collection(db, sh_path)
        if rdf_list:
            # If it's a rdf:List with elements, assign the first element as the sh:path value.
            sh_path = rdf_list[0]
        else:
            # sh:path value cannot be a blank node.
            # See https://www.w3.org/TR/shacl/#dfn-shacl-property-path.
            return None

    return sh_path


def get_property_by_property_shape(
    class_iri: URIRef,
    property_shape: URIRef | BNode,
    profile_graph: Graph,
    db: Dataset,
    method: str,
    **kwargs,
) -> Property:
    """Get a Property object for the given property shape."""
    sh_path = kwargs.get("sh_path") or get_sh_path(property_shape, profile_graph, db)
    name = (
        kwargs.get("name")
        or profile_graph.value(property_shape, SH.name)
        or get_name(sh_path, profile_graph, db)
    )
    description = kwargs.get("description") or (
        profile_graph.value(property_shape, SH.description)
        or get_descriptions(sh_path, profile_graph)
        or get_descriptions(sh_path, db)
        or ""
    )
    profile = kwargs.get("profile") or Profile(
        profile_graph.identifier,
        get_name(profile_graph.identifier, profile_graph, db),
    )
    belongs_to_class = kwargs.get("belongs_to_class") or get_class(class_iri, db, [])
    sh_nodekind = profile_graph.value(property_shape, SH.nodeKind)
    sh_min = profile_graph.value(property_shape, SH.minCount)
    sh_max = profile_graph.value(property_shape, SH.maxCount)
    sh_class = profile_graph.value(property_shape, SH["class"])
    value_type = (
        get_class(sh_nodekind, profile_graph, []) if sh_nodekind is not None else None
    )
    value_class_type = (
        get_class(sh_class, profile_graph, []) if sh_class is not None else None
    )
    property_source = kwargs.get("property_source") or ""

    return Property(
        iri=sh_path,
        name=name,
        description=description,
        profile=profile,
        belongs_to_class=belongs_to_class,
        cardinality_min=int(sh_min) if sh_min is not None else None,
        cardinality_max=int(sh_max) if sh_max is not None else None,
        value_type=value_type,
        value_class_types=[value_class_type] if value_class_type is not None else [],
        method=method,
        property_source=property_source,
    )


def get_properties_by_sh_target_predicate(
    iri: URIRef,
    sh_target_predicate: URIRef,
    nodeshape_property_shapes: dict[str, list[URIRef | BNode]],
    profile_graph: Graph,
    db: Dataset,
) -> dict[str, list[Property]]:
    """Get the properties by sh:targetObjectsOf or sh:targetSubjectsOf specified by sh_target_predicate.

    Note: the actual node shape or property shape used to extract the property is indicated by the variables
    that start with an underscore.
    """
    properties = defaultdict(list)

    for nodeshape, property_shapes in nodeshape_property_shapes.items():
        for nodeshape_property_shape in property_shapes:
            sh_path = get_sh_path(nodeshape_property_shape, profile_graph, db)
            if sh_path is None:
                continue

            # Get node shapes that target the sh_path variable above using sh:targetSubjectsOf.
            # We get the _profile_graph here because the profile_graph passed into this function is the profile graph for
            # the property shape.
            # We now need to get the profile graph for the shapes that target the sh_path with sh:targetSubjectsOf.
            for profile_iri in db.graphs():
                _profile_graph = db.graph(profile_iri)
                for _nodeshape in _profile_graph.subjects(sh_target_predicate, sh_path):
                    for _property_shape in db.objects(_nodeshape, SH.property):
                        _sh_path = get_sh_path(_property_shape, _profile_graph, db)
                        if sh_target_predicate == SH.targetObjectsOf:
                            _name = f"{get_name(sh_path, _profile_graph, db)} / {get_name(_sh_path, _profile_graph, db)}"
                            method = "sh:targetObjectsOf"
                        elif sh_target_predicate == SH.targetSubjectsOf:
                            _name = None
                            method = "sh:targetSubjectsOf"
                        else:
                            _name = None
                            method = get_name(sh_target_predicate, db)

                        property_source = f"Node shape: {nodeshape if isinstance(nodeshape, URIRef) else '(blank node)'} Property shape: {_property_shape if isinstance(_property_shape, URIRef) else '(blank node)'}"

                        property_ = get_property_by_property_shape(
                            iri,
                            _property_shape,
                            _profile_graph,
                            db,
                            method,
                            sh_path=_sh_path,
                            name=_name,
                            property_source=property_source,
                        )

                        if sh_target_predicate == SH.targetObjectsOf:
                            properties[sh_path].append(property_)
                        else:
                            properties[_sh_path].append(property_)

    return properties


def sort_properties_by_profile(
    profiles_order: list[URIRef], properties: list[Property]
) -> list[Property]:
    """Sort each property based on most specific profile to most broad."""
    order_dict = {profile: i for i, profile in enumerate(profiles_order)}
    order_dict.update({None: math.inf})
    return sorted(
        properties,
        key=lambda p: order_dict[
            next(
                (profile for profile in profiles_order if p.profile.iri == profile),
                None,
            )
        ],
    )


def get_class_properties_by_sh(
    iri: URIRef, db: Dataset, root_profile_iri: URIRef, profiles_order: list[URIRef]
) -> dict[str, list[Property]]:
    properties: dict[str, list[Property]] = defaultdict(list)

    # Check whether this class IRI contains an implicit class target or is targeted by sh:targetClass.
    if not (iri, RDF.type, SH.NodeShape) in db and not list(
        db.subjects(SH.targetClass, iri)
    ):
        return properties

    # Loop through each profile. Each profile is a named graph in the dataset.
    for profile_iri in db.graphs():
        profile_graph = db.graph(profile_iri)
        # TODO: We should be building a list of properties for sh:targetObjectsOf and sh:targetSubjectsOf from all
        #   property sources, not just property shapes. E.g, sdo:rangeIncluds, rdfs:range, etc.
        nodeshape_property_shapes = get_property_shapes(iri, profile_graph)

        properties.update(
            get_properties_by_sh_target_predicate(
                iri, SH.targetObjectsOf, nodeshape_property_shapes, profile_graph, db
            )
        )

        properties.update(
            get_properties_by_sh_target_predicate(
                iri, SH.targetSubjectsOf, nodeshape_property_shapes, profile_graph, db
            )
        )

        # Process the property shapes as normal.
        for nodeshape, property_shapes in nodeshape_property_shapes.items():
            for property_shape in property_shapes:
                sh_path = get_sh_path(property_shape, profile_graph, db)
                property_source = f"Node shape: {nodeshape if isinstance(nodeshape, URIRef) else '(blank node)'} Property shape: {property_shape if isinstance(property_shape, URIRef) else '(blank node)'}"
                property_ = get_property_by_property_shape(
                    iri, property_shape, profile_graph, db, "sh:path", property_source=property_source
                )
                properties[sh_path].append(property_)

    is_defined_by = get_is_defined_by(iri, db)

    for property_iri in properties:
        properties[property_iri] = sort_properties_by_profile(
            profiles_order, properties[property_iri]
        )
        # Set any intermediary properties to be of type intermediary if it is of type base.
        for p in properties[property_iri]:
            if p.profile.iri == root_profile_iri:
                p.profile.type = ProfileType.ROOT
            elif is_defined_by is not None and p.profile.iri == is_defined_by.iri:
                p.profile.type = ProfileType.BASE
            else:
                p.profile.type = ProfileType.INTERMEDIARY

    return properties
