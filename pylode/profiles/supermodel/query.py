from textwrap import dedent
from collections import defaultdict
from itertools import chain

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import (
    RDF,
    OWL,
    RDFS,
    DC,
    SKOS,
    SDO,
    DCTERMS,
    PROV,
    FOAF,
    ORG,
    VANN,
    PROF,
    SH,
)


from pylode.profiles.supermodel.namespace import SM
from pylode.profiles.supermodel.model import (
    ComponentModel,
    Class,
    ImageObject,
    Property,
    Note,
    Ontology,
    RDFProperty,
    MediaObject,
    TextObject,
)
from pylode.rdf_elements import AGENT_PROPS, ONT_PROPS, ONTDOC
from pylode.utils import (
    back_onts_label_props,
    load_background_onts,
    load_background_onts_titles,
)


def get_value(
    iri: URIRef, predicate: URIRef, graph: Graph
) -> str | int | float | bool | None:
    value = graph.value(iri, predicate)
    if value is None:
        return None
    if isinstance(value, Literal):
        return value.value
    elif isinstance(value, URIRef):
        return str(value)
    else:
        raise TypeError(f"Unhandled type {type(value)}. Expected URIRef or Literal.")


def get_examples(iri: URIRef, graph: Graph) -> list[MediaObject]:
    example_iris = graph.objects(iri, SDO.workExample)
    examples = []
    for example_iri in example_iris:
        class_types = list(graph.objects(example_iri, RDF.type))
        if SDO.TextObject in class_types:
            text_object = get_text_object(example_iri, graph)
            examples.append(text_object)
        elif SDO.ImageObject in class_types:
            image_object = get_image_object(example_iri, graph)
            examples.append(image_object)
        else:
            raise ValueError(
                f"Examples must be either an sdo:TextObject or an sdo:ImageObject."
            )

    return sorted(examples, key=lambda x: x.order)


def get_text_object(iri: URIRef, graph: Graph) -> TextObject:
    name = get_value(iri, SDO.name, graph)
    description = get_value(iri, SDO.description, graph)
    encoding_format = get_value(iri, SDO.encodingFormat, graph)
    source = get_value(iri, DCTERMS.source, graph)
    order = get_value(iri, SH.order, graph)
    text = get_value(iri, SDO.text, graph)

    if not text:
        raise ValueError("Text examples must have a value encoded using sdo:text.")

    return TextObject(
        name, description, encoding_format, source, order, dedent(text).strip()
    )


def get_image_object(iri: URIRef, graph: Graph) -> ImageObject:
    name = get_value(iri, SDO.name, graph)
    description = get_value(iri, SDO.description, graph)
    encoding_format = get_value(iri, SDO.encodingFormat, graph)
    source = get_value(iri, DCTERMS.source, graph)
    order = get_value(iri, SH.order, graph)
    url = get_value(iri, SDO.contentUrl, graph)
    caption = get_value(iri, SDO.caption, graph)

    return ImageObject(
        name,
        description,
        encoding_format,
        source,
        order,
        url,
        caption,
    )


def get_images(iri: URIRef, graph: Graph) -> list[ImageObject]:
    """Get images from a subject in the graph.

    Example data:
    ```
    container:CSD
      schema:workExample [
        a schema:ImageObject ;
        schema:caption "Diagram for Cadastral Survey Dataset." ;
        schema:contentUrl "https://icsm-au.github.io/3d-csdm-design/2022/spec_files/CSD_logical.png"^^xsd:anyURI ;
        sh:order 0 ;
      ] ;
    .
    ```
    """
    images = []
    image_ids = graph.objects(iri, SDO.image)

    for image_id in image_ids:
        name = graph.value(image_id, SDO.name)
        description = get_descriptions(image_id, graph)
        encoding_format = graph.value(image_id, SDO.encodingFormat)
        source = graph.value(image_id, DCTERMS.source)
        caption = graph.value(image_id, SDO.caption)
        url = graph.value(image_id, SDO.contentUrl)
        order = graph.value(image_id, SH.order)

        images.append(
            ImageObject(name, description, encoding_format, source, caption, url, order)
        )

    return sorted(set(images), key=lambda x: x.order)


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


def get_name(iri: URIRef, graph: Graph) -> str:
    names = get_values(iri, graph, [RDFS.label, SKOS.prefLabel, SDO.name])
    names.append(graph.qname(iri))
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


def get_class(iri: URIRef, graph: Graph, ignored_classes: list[URIRef]) -> Class:
    name = get_name(iri, graph)
    subclasses = get_subclasses(iri, graph, ignored_classes)
    return Class(iri, name, subclasses=subclasses)


def get_superclasses(
    iri: URIRef, graph: Graph, ignored_classes: list[URIRef]
) -> list[Class]:
    superclasses = filter(
        lambda x: x not in ignored_classes and isinstance(x, URIRef),
        list(graph.objects(iri, RDFS.subClassOf)),
    )
    return sorted(
        [get_class(superclass, graph, ignored_classes) for superclass in superclasses],
        key=lambda x: x.name,
    )


def get_subclasses(
    iri: URIRef, graph: Graph, ignored_classes: list[URIRef]
) -> list[Class]:
    subclasses = filter(
        lambda x: x not in ignored_classes and isinstance(x, URIRef),
        list(graph.subjects(RDFS.subClassOf, iri)),
    )
    return sorted(
        [get_class(subclass, graph, ignored_classes) for subclass in subclasses],
        key=lambda x: x.name,
    )


def get_is_defined_by(iri: URIRef, graph: Graph) -> Ontology | None:
    is_defined_by = get_values(iri, graph, [RDFS.isDefinedBy])
    ontology = is_defined_by[0] if len(is_defined_by) > 0 else None
    if ontology is not None:
        name = get_name(ontology, graph)
        return Ontology(iri=ontology, name=name)
    return None


def get_class_properties_from_sh_nodeshape_sh_property(
    iri: URIRef, graph: Graph, ignored_classes: list[URIRef]
) -> list[Property]:
    properties = []
    classes = list(graph.objects(iri, RDF.type))

    if SH.NodeShape in classes:
        sh_properties = list(graph.objects(iri, SH.property))
        for sh_property in sh_properties:
            sh_path = graph.value(sh_property, SH.path)
            sh_class = graph.value(sh_property, SH["class"])
            sh_description = (
                graph.value(sh_property, SH.description)
                or get_descriptions(sh_path, graph)
                or ""
            )
            sh_name = graph.value(sh_property, SH.name) or get_name(sh_path, graph)
            sh_nodekind = graph.value(sh_property, SH.nodeKind)
            sh_min = graph.value(sh_property, SH.minCount)
            sh_max = graph.value(sh_property, SH.maxCount)
            belongs_to_class = get_class(iri, graph, ignored_classes)
            value_type = (
                get_class(sh_nodekind, graph, ignored_classes)
                if sh_nodekind is not None
                else None
            )
            value_class_type = (
                get_class(sh_class, graph, ignored_classes)
                if sh_class is not None
                else None
            )

            properties.append(
                Property(
                    iri=graph.qname(sh_path),
                    name=sh_name,
                    description=sh_description,
                    belongs_to_class=belongs_to_class,
                    cardinality_min=int(sh_min) if sh_min is not None else None,
                    cardinality_max=int(sh_max) if sh_max is not None else None,
                    value_type=value_type,
                    value_class_types=[value_class_type]
                    if value_class_type is not None
                    else [],
                )
            )

    return sorted(properties, key=lambda x: x.name)


def get_class_properties_from_schema_domain_includes(
    iri: URIRef, graph: Graph, ignored_classes: list[URIRef]
) -> list[Property]:
    properties = []
    schema_domain_includes_iris = graph.subjects(SDO.domainIncludes, iri)
    for schema_domain_includes_iri in schema_domain_includes_iris:
        name = get_name(schema_domain_includes_iri, graph)
        description = get_descriptions(schema_domain_includes_iri, graph)
        value_class_types = [
            get_class(c, graph, ignored_classes)
            for c in get_values(schema_domain_includes_iri, graph, [SDO.rangeIncludes])
        ]

        properties.append(
            Property(
                iri=schema_domain_includes_iri,
                name=name,
                description=description,
                belongs_to_class=None,
                value_class_types=value_class_types,
            )
        )

    return sorted(properties, key=lambda x: x.name)


def get_component_model_class_properties(
    iri: URIRef, graph: Graph, ignored_classes: list[URIRef]
):
    """Get the properties of a class.

    Object property - range is Any

    Object and datatype properties - output shows "Not specified" instead of empty string.

    Ways to extract properties of a class:
      [x] - sh:property via an sh:NodeShape, which may also be an owl:Class or rdfs:Class
      [ ] - sh:targetClass
      [ ] - rdfs:domain and rdfs:range - consider only when there's no sh:class in the property shape
      [x] - schema:domainIncludes and schema:rangeIncludes
      [ ] - check for other ways in the SHACL spec...
      [ ] - concrete data to models - example JSON-LD instance document
      [ ] - JSON schema and JSON context binding
      [ ] - RDF data cube - vocabulary binding
    """
    properties = []

    properties += get_class_properties_from_sh_nodeshape_sh_property(
        iri, graph, ignored_classes
    )

    properties += get_class_properties_from_schema_domain_includes(
        iri, graph, ignored_classes
    )

    return properties


def get_notes(iri: URIRef, graph: Graph) -> list[str]:
    notes = []

    skos_notes = get_values(iri, graph, [SKOS.note])
    for note in skos_notes:
        notes.append(Note(str(note), "note"))

    change_notes = get_values(iri, graph, [SKOS.changeNote])
    for note in change_notes:
        notes.append(Note(str(note), "Change Note"))

    editorial_notes = get_values(iri, graph, [SKOS.editorialNote])
    for note in editorial_notes:
        notes.append(Note(str(note), "Editorial Note"))

    history_notes = get_values(iri, graph, [SKOS.historyNote])
    for note in history_notes:
        notes.append(Note(str(note), "History Note"))

    scope_notes = get_values(iri, graph, [SKOS.scopeNote])
    for note in scope_notes:
        notes.append(Note(str(note), "Scope Note"))

    return sorted(notes, key=lambda note: note.type)


def get_component_model_ignored_classes(iri: URIRef, graph: Graph) -> list[URIRef]:
    return list(graph.objects(iri, SM.ignoreClass))


def get_top_level_component_classes(classes: list[Class]) -> list[Class]:
    top_level_classes = []

    for cls in classes:
        has_superclass = False
        for superclass in cls.superclasses:
            if superclass in classes:
                has_superclass = True
        if not has_superclass:
            top_level_classes.append(cls)

    return top_level_classes


def get_super_properties(iri: URIRef, graph: Graph) -> list[RDFProperty]:
    super_property_iris = get_values(iri, graph, [RDFS.subPropertyOf])
    properties = []
    for super_property_iri in super_property_iris:
        prop = get_rdf_property(super_property_iri, graph)
        properties.append(prop)

    return properties


def get_domain_includes(iri: URIRef, graph: Graph) -> list[Class]:
    domain_includes_iris = graph.objects(iri, SDO.domainIncludes)
    domain_includes = []
    for domain_includes_iri in domain_includes_iris:
        c = get_class(domain_includes_iri, graph, [])
        domain_includes.append(c)

    return domain_includes


def get_range_includes(iri: URIRef, graph: Graph) -> list[Class]:
    range_includes_iris = graph.objects(iri, SDO.rangeIncludes)
    range_includes = []
    for range_includes_iri in range_includes_iris:
        c = get_class(range_includes_iri, graph, [])
        range_includes.append(c)

    return range_includes


def get_rdf_property(iri, graph) -> RDFProperty:
    name = get_name(iri, graph)
    description = get_descriptions(iri, graph)
    notes = get_notes(iri, graph)
    is_defined_by = get_is_defined_by(iri, graph)
    super_properties = get_super_properties(iri, graph)
    domain_includes = get_domain_includes(iri, graph)
    range_includes = get_range_includes(iri, graph)

    return RDFProperty(
        iri,
        name,
        description,
        notes,
        is_defined_by,
        super_properties,
        domain_includes,
        range_includes,
    )


def get_rdf_properties(rdf_property_type: URIRef, graph: Graph) -> list[RDFProperty]:
    property_iris = graph.subjects(RDF.type, rdf_property_type)
    properties = []
    for property_iri in property_iris:
        prop = get_rdf_property(property_iri, graph)

        properties.append(prop)

    return properties


class Query:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph

        # An IRI index of classes that 'exist' within this documentation.
        self.class_index: set[URIRef] = set()

        self.ns = self.get_ns()
        self.component_models = self.load_component_models()
        if not self.component_models:
            self.component_models = [
                self.load_component_model(URIRef(self.ns[1]), self.graph)
            ]
        self.ontdoc_inference()

        self.back_onts = load_background_onts()
        self.back_onts_titles = load_background_onts_titles(self.back_onts)
        self.props_labeled = back_onts_label_props(self.back_onts)
        self.onts_props = self.get_onts_props()
        self.examples = get_examples(self.get_supermodel_iri(), self.graph)

    def get_supermodel_iri(self) -> URIRef:
        for s in self.graph.subjects(RDF.type, SM.Supermodel):
            return s

    def get_title(self, iri: str) -> str | None:
        for o2 in self.graph.objects(iri, DCTERMS.title):
            return str(o2)

    def get_onts_props(self) -> dict[str, list]:
        # get all ONT_PROPS props and their (multiple) values
        this_onts_props = defaultdict(list)
        for s_ in self.graph.subjects(predicate=RDF.type, object=SM.Supermodel):
            for p_, o in self.graph.predicate_objects(s_):
                if p_ in ONT_PROPS:
                    this_onts_props[p_].append(o)

        return this_onts_props

    def ontdoc_inference(self):
        """Expands the ontology's graph to make OntDoc querying easier.

        Uses axioms made up for OntDoc, but they are simple and obvious
        and don't collide with well-known ontologies"""
        g = self.graph
        # class types
        for s_ in g.subjects(RDF.type, OWL.Class):
            g.add((s_, RDF.type, RDFS.Class))

        # # property types
        # for s_ in chain(
        #     g.subjects(RDF.type, OWL.ObjectProperty),
        #     g.subjects(RDF.type, OWL.FunctionalProperty),
        #     g.subjects(RDF.type, OWL.DatatypeProperty),
        #     g.subjects(RDF.type, OWL.AnnotationProperty),
        # ):
        #     g.add((s_, RDF.type, RDF.Property))

        # name
        for s_, o in chain(
            g.subject_objects(DC.title),
            g.subject_objects(RDFS.label),
            g.subject_objects(SKOS.prefLabel),
            g.subject_objects(SDO.name),
        ):
            g.add((s_, DCTERMS.title, o))

        # description
        for s_, o in chain(
            g.subject_objects(DC.description),
            g.subject_objects(RDFS.comment),
            g.subject_objects(SKOS.definition),
            g.subject_objects(SDO.description),
        ):
            g.add((s_, DCTERMS.description, o))

        # date modified
        for s_, o in chain(
            g.subject_objects(SDO.dateModified),
        ):
            g.add((s_, DCTERMS.modified, o))

        # date issued
        for s_, o in chain(
            g.subject_objects(SDO.dateIssued),
        ):
            g.add((s_, DCTERMS.issued, o))

        # source
        for s_, o in g.subject_objects(DC.source):
            g.add((s_, DCTERMS.source, o))

        # license
        for s_, o in g.subject_objects(SDO.license):
            g.add((s_, DCTERMS.license, o))

        #
        #   Blank Node Types
        #
        for s_ in g.subjects(OWL.onProperty, None):
            g.add((s_, RDF.type, OWL.Restriction))

        for s_ in chain(
            g.subjects(OWL.unionOf, None), g.subjects(OWL.intersectionOf, None)
        ):
            g.add((s_, RDF.type, OWL.Class))

        # we do these next few so we only need to loop through
        # Class & Property properties once: single subject
        for s_, o in g.subject_objects(RDFS.subClassOf):
            g.add((o, ONTDOC.superClassOf, s_))

        for s_, o in g.subject_objects(RDFS.subPropertyOf):
            g.add((o, ONTDOC.superPropertyOf, s_))

        for s_, o in g.subject_objects(RDFS.domain):
            g.add((o, ONTDOC.inDomainOf, s_))

        for s_, o in g.subject_objects(SDO.domainIncludes):
            g.add((o, ONTDOC.inDomainIncludesOf, s_))

        for s_, o in g.subject_objects(RDFS.range):
            g.add((o, ONTDOC.inRangeOf, s_))

        for s_, o in g.subject_objects(SDO.rangeIncludes):
            g.add((o, ONTDOC.inRangeIncludesOf, s_))

        for s_, o in g.subject_objects(RDF.type):
            g.add((o, ONTDOC.hasMember, s_))

        #
        #   Agents
        #
        # creator
        for s_, o in chain(
            g.subject_objects(DC.creator),
            g.subject_objects(SDO.creator),
            g.subject_objects(SDO.author),
        ):
            g.remove((s_, DC.creator, o))
            g.remove((s_, SDO.creator, o))
            g.remove((s_, SDO.author, o))
            g.add((s_, DCTERMS.creator, o))

        # contributor
        for s_, o in chain(
            g.subject_objects(DC.contributor),
            g.subject_objects(SDO.contributor),
        ):
            g.remove((s_, DC.contributor, o))
            g.remove((s_, SDO.contributor, o))
            g.add((s_, DCTERMS.contributor, o))

        # publisher
        for s_, o in chain(
            g.subject_objects(DC.publisher), g.subject_objects(SDO.publisher)
        ):
            g.remove((s_, DC.publisher, o))
            g.remove((s_, SDO.publisher, o))
            g.add((s_, DCTERMS.publisher, o))

        # indicate Agent instances from properties
        for o in chain(
            g.objects(None, DCTERMS.publisher),
            g.objects(None, DCTERMS.creator),
            g.objects(None, DCTERMS.contributor),
        ):
            g.add((o, RDF.type, PROV.Agent))

        # Agent annotations
        for s_, o in g.subject_objects(FOAF.name):
            g.add((s_, SDO.name, o))

        for s_, o in g.subject_objects(FOAF.mbox):
            g.add((s_, SDO.email, o))

        for s_, o in g.subject_objects(ORG.memberOf):
            g.add((s_, SDO.affiliation, o))

    def get_ns(self) -> tuple[str, str]:
        ont = self.graph
        """Gets the default Namespace for the given graph (ontology)"""
        # if this ontology declares a preferred URI, use that
        pref_iri = None
        for s_, o in ont.subject_objects(predicate=VANN.preferredNamespaceUri):
            pref_iri = str(o)

        pref_prefix = None
        for s_, o in ont.subject_objects(predicate=VANN.preferredNamespacePrefix):
            pref_prefix = str(o)
        if pref_prefix is None:
            pref_prefix = ""

        if pref_iri is not None:
            return pref_prefix, pref_iri

        # if not, try the URI of the main object, compared to all prefixes
        else:
            default_iri = None

            for s_ in ont.subjects(predicate=RDF.type, object=SM.Supermodel):
                default_iri = str(s_)

            if default_iri is None:
                for s_ in ont.subjects(predicate=RDF.type, object=OWL.Ontology):
                    default_iri = str(s_)
                    if default_iri is not None:
                        ont.add((s_, RDF.type, SM.Supermodel))

            if default_iri is not None:
                prefix = ont.compute_qname(default_iri, True)[0]
                if prefix is not None:
                    return prefix, default_iri
            else:
                # can't find either a declared or default namespace
                # so we have an error
                raise Exception(
                    "pyLODE can't detect a URI for an owl:Ontology, "
                    "a skos:ConceptScheme or a prof:Profile"
                )

    def load_component_model(self, iri: URIRef, graph: Graph) -> ComponentModel:
        name = get_name(iri, graph)
        descriptions = get_descriptions(iri, graph)
        ignored_classes = get_component_model_ignored_classes(iri, self.graph)
        classes = self.get_component_model_classes(graph, ignored_classes)
        top_level_classes = get_top_level_component_classes(classes)
        examples = get_examples(iri, graph)
        order = self.graph.value(iri, SH.order)
        annotation_properties = get_rdf_properties(OWL.AnnotationProperty, graph)
        datatype_properties = get_rdf_properties(OWL.DatatypeProperty, graph)
        object_properties = get_rdf_properties(OWL.ObjectProperty, graph)
        ontology_properties = get_rdf_properties(OWL.OntologyProperty, graph)

        return ComponentModel(
            iri,
            name,
            descriptions,
            classes,
            top_level_classes,
            examples,
            int(order) if order is not None else None,
            ignored_classes,
            annotation_properties,
            datatype_properties,
            object_properties,
            ontology_properties,
        )

    def load_component_models(self) -> list[ComponentModel]:
        supermodel = self.get_supermodel_iri()
        component_models = list(self.graph.objects(supermodel, SM.componentModel))
        result = []

        for iri in component_models:
            component_model_files = list(
                self.graph.objects(iri, SDO.encoding / SDO.contentUrl)
            )
            graph = Graph()
            for file in component_model_files:
                graph.parse(file)

            component_model = self.load_component_model(iri, graph)
            result.append(component_model)

            self.graph += graph

        return sorted(result, key=lambda x: x.order)

    def get_component_model_classes(
        self, graph: Graph, ignored_classes: list[URIRef]
    ) -> list[Class]:
        classes = graph.subjects(RDF.type, OWL.Class)

        result = []
        for c in filter(lambda x: x not in ignored_classes, classes):
            name = get_name(c, graph)
            descriptions = get_descriptions(c, graph)
            subclasses = get_subclasses(c, graph, ignored_classes)
            superclasses = get_superclasses(c, graph, ignored_classes)
            properties = get_component_model_class_properties(c, graph, ignored_classes)
            examples = get_examples(c, graph)
            notes = get_notes(c, graph)
            is_defined_by = get_is_defined_by(c, graph)

            result.append(
                Class(
                    iri=c,
                    name=name,
                    description=descriptions,
                    subclasses=subclasses,
                    superclasses=superclasses,
                    properties=properties,
                    examples=examples,
                    notes=notes,
                    is_defined_by=is_defined_by,
                )
            )
            self.class_index.add(c)

        return sorted(result, key=lambda x: x.name)

    def get_schema_org_metadata_graph(self):
        graph = Graph()
        for ont_iri in chain(
            self.graph.subjects(predicate=RDF.type, object=OWL.Ontology),
            self.graph.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
            self.graph.subjects(predicate=RDF.type, object=PROF.Profile),
        ):
            graph.add((ont_iri, RDF.type, SDO.DefinedTermSet))
            for p_, o in self.graph.predicate_objects(ont_iri):
                if p_ == DCTERMS.title:
                    graph.add((ont_iri, SDO.name, o))
                elif p_ == DCTERMS.description:
                    graph.add((ont_iri, SDO.description, o))
                elif p_ == DCTERMS.publisher:
                    graph.add((ont_iri, SDO.publisher, o))
                    if not isinstance(o, Literal):
                        for p2, o2 in self.graph.predicate_objects(o):
                            if p2 in AGENT_PROPS:
                                graph.add((o, p2, o2))
                elif p_ == DCTERMS.creator:
                    graph.add((ont_iri, SDO.creator, o))
                    if not isinstance(o, Literal):
                        for p2, o2 in self.graph.predicate_objects(o):
                            if p2 in AGENT_PROPS:
                                graph.add((o, p2, o2))
                elif p_ == DCTERMS.contributor:
                    graph.add((ont_iri, SDO.contributor, o))
                    if not isinstance(o, Literal):
                        for p2, o2 in self.graph.predicate_objects(o):
                            if p2 in AGENT_PROPS:
                                graph.add((o, p2, o2))
                elif p_ == DCTERMS.created:
                    graph.add((ont_iri, SDO.dateCreated, o))
                elif p_ == DCTERMS.modified:
                    graph.add((ont_iri, SDO.dateModified, o))
                elif p_ == DCTERMS.issued:
                    graph.add((ont_iri, SDO.dateIssued, o))
                elif p_ == DCTERMS.license:
                    graph.add((ont_iri, SDO.license, o))
                elif p_ == DCTERMS.rights:
                    graph.add((ont_iri, SDO.copyrightNotice, o))

        return graph
