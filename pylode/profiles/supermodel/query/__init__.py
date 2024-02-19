import math
import logging
from textwrap import dedent
from collections import defaultdict
from itertools import chain

from rdflib import Graph, Literal, URIRef, Dataset
from rdflib.graph import DATASET_DEFAULT_GRAPH_ID
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
    QB,
)


from pylode.profiles.supermodel.namespace import LODE
from pylode.profiles.supermodel.model import (
    ComponentModel,
    Class,
    ImageObject,
    Property,
    Note,
    RDFProperty,
    MediaObject,
    TextObject,
    Profile,
    ProfileType,
    ProfileHierarchyItem,
    CodedProperty,
    Resource,
    SimpleCodedProperty,
)
from pylode.profiles.supermodel.query.common import (
    get_class,
    get_descriptions,
    get_name,
    get_values,
    get_subclasses,
    get_is_defined_by,
)
from pylode.profiles.supermodel.query.property_shape import get_class_properties_by_sh
from pylode.rdf_elements import AGENT_PROPS, ONT_PROPS, ONTDOC
from pylode.utils import (
    back_onts_label_props,
    load_background_onts,
    load_background_onts_titles,
)
from pylode.profiles.supermodel.loader import load_profiles

logger = logging.getLogger(__name__)


def get_value(
    iri: URIRef, predicate: URIRef, graph: Graph
) -> str | int | float | bool | None:
    """Get the value as a Python data type."""
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


def get_notes(iri: URIRef, graph: Graph) -> list[Note]:
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
    return list(graph.objects(iri, LODE.ignoreClass))


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


def get_super_properties(iri: URIRef, graph: Graph, db: Dataset) -> list[RDFProperty]:
    super_property_iris = get_values(iri, graph, [RDFS.subPropertyOf])
    properties = []
    for super_property_iri in super_property_iris:
        prop = get_rdf_property(super_property_iri, graph, db)
        properties.append(prop)

    return properties


def get_domain_includes(iri: URIRef, graph: Graph, db: Dataset) -> list[Class]:
    domain_includes_iris = graph.objects(iri, SDO.domainIncludes)
    domain_includes = []
    for domain_includes_iri in domain_includes_iris:
        c = get_class(domain_includes_iri, graph, db,[])
        domain_includes.append(c)

    return domain_includes


def get_range_includes(iri: URIRef, graph: Graph, db: Dataset) -> list[Class]:
    range_includes_iris = graph.objects(iri, SDO.rangeIncludes)
    range_includes = []
    for range_includes_iri in range_includes_iris:
        c = get_class(range_includes_iri, graph, db,[])
        range_includes.append(c)

    return range_includes


def get_rdf_property(iri, graph, db: Dataset) -> RDFProperty:
    name = get_name(iri, graph, db)
    description = get_descriptions(iri, graph)
    notes = get_notes(iri, graph)
    is_defined_by = get_is_defined_by(iri, graph, db)
    super_properties = get_super_properties(iri, graph, db)
    domain_includes = get_domain_includes(iri, graph, db)
    range_includes = get_range_includes(iri, graph, db)

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


def get_rdf_properties(rdf_property_type: URIRef, graph: Graph, db: Dataset) -> list[RDFProperty]:
    property_iris = graph.subjects(RDF.type, rdf_property_type)
    properties = []
    for property_iri in property_iris:
        prop = get_rdf_property(property_iri, graph, db)

        properties.append(prop)

    return sorted(properties, key=lambda x: x.name)


def get_root_profile_iri(graph: Graph) -> URIRef:
    """Get the root profile IRI in the initial document.

    This also ensures there is only 1 profile in the initial document.
    """
    profiles = list(graph.subjects(RDF.type, PROF.Profile, unique=True))
    count = len(profiles)
    if count > 1:
        raise ValueError(
            f"There is more than 1 prof:Profile defined in the input document. Expected only 1 prof:Profile definition but found {[str(p) for p in profiles]}."
        )
    elif count < 1:
        profiles = list(graph.subjects(RDF.type, OWL.Ontology, unique=True))

        if len(profiles) != 1:
            raise ValueError(
                f"There can only be one owl:Ontology defined in the document."
            )

    return profiles[0]


def get_super_profiles(iri: URIRef, graph: Graph) -> list[ProfileHierarchyItem]:
    super_profile_iris = graph.objects(iri, PROF.isProfileOf)
    super_profiles = []
    for super_profile_iri in super_profile_iris:
        super_profiles.append(
            ProfileHierarchyItem(
                iri=super_profile_iri,
                name=get_name(super_profile_iri, graph),
                is_profile_of=get_super_profiles(super_profile_iri, graph),
            )
        )
    return super_profiles


class Query:
    def add_to_graph(self, graph: Graph, graph_identifier: str) -> None:
        _graph = Graph(identifier=graph_identifier)
        for s, p, o in graph:
            self.db.add((s, p, o, _graph))

    def get_profiles_hierarchy(self) -> ProfileHierarchyItem:
        def _get_profile_hierarchy_item(iri: URIRef):
            return ProfileHierarchyItem(
                iri=iri,
                name=get_name(iri, self.db),
                is_profile_of=get_super_profiles(iri, self.db),
            )

        return _get_profile_hierarchy_item(self.root_profile_iri)

    def get_profiles_order(
        self, profiles_hierarchy: ProfileHierarchyItem
    ) -> list[URIRef]:
        profiles = []
        focus = profiles_hierarchy

        def _add(profile: ProfileHierarchyItem):
            profiles.append(profile.iri)
            if profile.is_profile_of:
                for _super_profile in profile.is_profile_of:
                    _add(_super_profile)

        _add(focus)

        return profiles

    def get_summary_vocabularies(self):
        coded_properties = defaultdict(list)

        for graph in self.db.graphs():
            props = list(graph.subjects(RDF.type, QB.CodedProperty))
            for prop in props:
                codelist = [
                    Resource(
                        x,
                        get_name(x, graph),
                        get_descriptions(x, graph),
                    )
                    for x in graph.objects(prop, QB.codeList)
                ]
                simple_coded_property = SimpleCodedProperty(
                    prop,
                    get_name(prop, graph, self.db),
                    get_descriptions(prop, graph),
                    codelist,
                )
                if simple_coded_property not in coded_properties[prop]:
                    coded_properties[prop].append(simple_coded_property)

        # Sort by label of the first value.
        coded_properties = dict(
            sorted(coded_properties.items(), key=lambda v: v[1][0].name.lower())
        )

        vocab_class_index = defaultdict(list)
        for component_model in self.component_models:
            for cls in component_model.classes:
                for properties in cls.properties.values():
                    for prop in properties:
                        if isinstance(prop, CodedProperty):
                            if prop.belongs_to_class not in vocab_class_index[prop.iri]:
                                vocab_class_index[prop.iri].append(
                                    prop.belongs_to_class
                                )

        for vocab in vocab_class_index:
            vocab_class_index[vocab] = sorted(
                vocab_class_index[vocab], key=lambda x: x.name
            )

        # Collapse by combining codelist values.
        for prop in coded_properties:
            codelist = []
            for coded_property in coded_properties[prop]:
                codelist += coded_property.codelist

            # Copy the codelist values to the first coded property.
            coded_properties[prop][0].codelist = codelist

            # Add classes to coded property.
            coded_properties[prop][0].classes = vocab_class_index[prop]

            # Only have one copy that has all the codelist values combined.
            coded_properties[prop] = [coded_properties[prop][0]]

        return coded_properties

    def __init__(self, graph: Graph) -> None:
        self.root_profile_iri = get_root_profile_iri(graph)
        self.db = load_profiles(self.root_profile_iri, graph.serialize())
        self.graph = self.db.root_graph
        self.debug = True if (None, LODE.debug, None) in self.db.config_graph else False

        # An IRI index of classes that 'exist' within this documentation.
        # TODO: may not need this anymore since we are now working with a dataset object.
        self.class_index: set[URIRef] = set()

        self.ns = self.get_ns()

        self.profiles_hierarchy = self.get_profiles_hierarchy()
        # This order is mainly used to sort the properties for a class by their profile's specificity.
        self.profiles_order = self.get_profiles_order(self.profiles_hierarchy)

        self.component_models = self.load_component_models()
        if not self.component_models:
            self.component_models = [
                self.load_component_model(URIRef(self.ns[1]), self.db)
            ]
        self.ontdoc_inference()

        self.coded_properties = self.get_summary_vocabularies()

        print("Named graphs")
        print([str(g.identifier) for g in self.db.graphs()])

        self.back_onts = load_background_onts()
        self.back_onts_titles = load_background_onts_titles(self.back_onts)
        self.props_labeled = back_onts_label_props(self.back_onts)
        self.onts_props = self.get_onts_props()
        self.examples = get_examples(self.get_supermodel_iri(), self.graph)

    def import_profile(self, iri: str):
        db = self.db
        qualified_profile_nodes = db.objects(
            subject=iri, predicate=LODE.isQualifiedProfileOf
        )

        for node in qualified_profile_nodes:
            resources = list(self.db.objects(node, RDF.value / PROF.hasResource))
            for resource in resources:
                graph = Graph()
                path = self.db.value(resource, PROF.hasArtifact)
                mimetype = self.db.value(resource, DCTERMS.format) or "text/turtle"
                graph.parse(path, mimetype)

                profile_iri = graph.value(
                    predicate=RDF.type, object=PROF.Profile
                ) or graph.value(predicate=RDF.type, object=OWL.Ontology)

                if profile_iri is not None:
                    if node not in self.imported_profiles:
                        self.imported_profiles.append(node)
                    self.add_to_graph(graph, node)

                    self.import_profile(profile_iri)

    def import_profiles(self):
        """Recursively import all profiles referenced by the root profile.

        Only imports profiles referenced with lode:isQualifiedProfileOf.
        """
        iri = self.root_profile_iri
        self.imported_profiles.append(iri)
        self.import_profile(iri)

    def get_supermodel_iri(self) -> URIRef:
        iri = None
        for s in self.graph.subjects(RDF.type, PROF.Profile, unique=True):
            iri = s

        if iri is None:
            raise ValueError("No profile found.")

        return iri

    def get_title(self, iri: str) -> str | None:
        for o2 in self.graph.objects(iri, DCTERMS.title):
            return str(o2)

    def get_onts_props(self) -> dict[str, list]:
        # get all ONT_PROPS props and their (multiple) values
        this_onts_props = defaultdict(list)
        for s_ in self.graph.subjects(predicate=RDF.type, object=PROF.Profile):
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

            for s_ in ont.subjects(predicate=RDF.type, object=PROF.Profile):
                default_iri = str(s_)

            if default_iri is None:
                for s_ in ont.subjects(predicate=RDF.type, object=OWL.Ontology):
                    default_iri = str(s_)
                    if default_iri is not None:
                        ont.add((s_, RDF.type, PROF.Profile))

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

    def load_component_model(self, iri: URIRef, db: Dataset) -> ComponentModel:
        name = get_name(iri, db)
        descriptions = get_descriptions(iri, db)
        ignored_classes = get_component_model_ignored_classes(iri, db)
        profile_graph = db.get_graph(iri)
        classes = self.get_component_model_classes(profile_graph, ignored_classes)
        top_level_classes = get_top_level_component_classes(classes)
        examples = get_examples(iri, db)
        order = db.value(iri, SH.order)
        annotation_properties = get_rdf_properties(
            OWL.AnnotationProperty, profile_graph, db
        )
        datatype_properties = get_rdf_properties(OWL.DatatypeProperty, profile_graph, db)
        object_properties = get_rdf_properties(OWL.ObjectProperty, profile_graph, db)
        ontology_properties = get_rdf_properties(OWL.OntologyProperty, profile_graph, db)

        coded_properties = defaultdict(list)
        for cls in classes:
            for properties in cls.properties.values():
                for prop in properties:
                    if isinstance(prop, CodedProperty):
                        # Always get the base name, that's why we use properties[-1].name.
                        _prop = SimpleCodedProperty(
                            prop.iri,
                            properties[-1].name,
                            prop.description,
                            prop.codelist,
                        )
                        if _prop.codelist and _prop not in coded_properties[prop.iri]:
                            coded_properties[prop.iri].append(_prop)

        return ComponentModel(
            iri,
            name,
            coded_properties,
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
        component_models = self.db.config_graph.subjects(RDF.type, LODE.Module)
        result = []

        for iri in component_models:
            component_model = self.load_component_model(iri, self.db)
            result.append(component_model)

        return sorted(result, key=lambda x: x.order)

    def get_class_properties_from_schema_domain_includes(
        self,
        iri: URIRef,
        properties: dict[URIRef, list[Property]],
        ignored_classes: list[URIRef],
    ) -> list[Property]:

        for _graph in self.db.graphs():
            graph = self.db.get_graph(_graph.identifier)

            schema_domain_includes_iris = graph.subjects(SDO.domainIncludes, iri)
            for schema_domain_includes_iri in schema_domain_includes_iris:
                name = get_name(schema_domain_includes_iri, graph)
                description = get_descriptions(schema_domain_includes_iri, graph)
                value_class_types = [
                    get_class(c, graph, self.db, ignored_classes)
                    for c in get_values(
                        schema_domain_includes_iri, graph, [SDO.rangeIncludes]
                    )
                ]

                properties[schema_domain_includes_iri].append(
                    Property(
                        iri=schema_domain_includes_iri,
                        name=name,
                        description=description,
                        profile=Profile(
                            graph.identifier,
                            get_name(graph.identifier, self.db),
                        ),
                        value_class_types=value_class_types,
                    )
                )

        return properties

    def get_coded_properties(
        self, cls_iri: URIRef, properties: dict[str, list[Property]]
    ) -> dict[str, list[Property]]:
        for prop in properties.copy():
            _graphs = list(
                filter(
                    lambda g: g.identifier != DATASET_DEFAULT_GRAPH_ID,
                    self.db.contexts((prop, RDF.type, QB.CodedProperty)),
                )
            )

            if _graphs:
                for _graph in _graphs:
                    graph = self.db.get_graph(_graph.identifier)
                    expected_value_iris = graph.objects(prop, RDFS.range)
                    value_class_types = [
                        get_class(expected_value_iri, self.db, self.db, [])
                        for expected_value_iri in expected_value_iris
                    ]

                    name = get_name(prop, graph, self.db)
                    description = (
                        get_descriptions(prop, graph)
                        or get_descriptions(prop, self.db)
                        or ""
                    )

                    new_prop = CodedProperty(
                        prop,
                        name,
                        description,
                        Profile(
                            graph.identifier,
                            get_name(graph.identifier, self.db),
                        ),
                        belongs_to_class=get_class(cls_iri, self.db, self.db,[]),
                        value_class_types=value_class_types,
                        method="qb:CodedProperty",
                        codelist=[
                            Resource(
                                x,
                                get_name(x, graph),
                                get_descriptions(x, graph),
                            )
                            for x in graph.objects(prop, QB.codeList)
                        ],
                    )
                    properties[prop].append(new_prop)

        return properties

    def sort_properties_by_profile(self, properties: list[Property]) -> list[Property]:
        """Sort each property based on most specific profile to most broad."""
        order_dict = {profile: i for i, profile in enumerate(self.profiles_order)}
        order_dict.update({None: math.inf})
        return sorted(
            properties,
            key=lambda p: order_dict[
                next(
                    (
                        profile
                        for profile in self.profiles_order
                        if p.profile.iri == profile
                    ),
                    None,
                )
            ],
        )

    def sort_properties(self, iri: URIRef, properties: dict[str, list[Property]]):
        is_defined_by = get_is_defined_by(iri, self.db, self.db)

        for property_iri in properties:
            properties[property_iri] = self.sort_properties_by_profile(
                properties[property_iri]
            )

            for p in properties[property_iri]:
                if p.profile.iri == self.root_profile_iri:
                    # Defined by entrypoint profile.
                    p.profile.type = ProfileType.ROOT
                elif is_defined_by is not None and p.profile.iri == is_defined_by.iri:
                    # Defined in current module.
                    p.profile.type = ProfileType.BASE
                elif (
                    is_defined_by is None
                    and (p.profile.iri, RDF.type, LODE.Module) in self.db
                ):
                    # Defined by another module within the overall model.
                    p.profile.type = ProfileType.BASE
                else:
                    # Defined by one of the intermediary profiles.
                    p.profile.type = ProfileType.INTERMEDIARY

    def get_component_model_class_properties(
        self, iri: URIRef, ignored_classes: list[URIRef]
    ) -> dict[str, list[Property]]:
        """Get the properties of a class.

        Object property - range is Any

        Object and datatype properties - output shows "Not specified" instead of empty string.

        Below are the different methods to extract properties of a class.

        SHACL:
        [x] - sh:property via a sh:NodeShape, which may also be an owl:Class or rdfs:Class
        [x] - sh:targetClass
        [x] - implicit target class (contains rdfs:Class and sh:NodeShape)
        [x] - sh:targetObjectsOf
        [x] - sh:targetSubjectsOf
        [x] - all above should support sh:path as a sequence path
        [x] - sh:path property for a single value can have its label overridden by sh:name
        [ ] - sh:path sequence path should not use sh:name to override property names - they are additional title for the constraints

        Other:
        [ ] - rdfs:domain and rdfs:range - consider only when there's no sh:class in the property shape
        [x] - schema:domainIncludes and schema:rangeIncludes
        [x] - RDF data cube - vocabulary binding
        """

        properties = get_class_properties_by_sh(iri, self.db)

        properties = self.get_coded_properties(iri, properties)

        properties = self.get_class_properties_from_schema_domain_includes(
            iri, properties, ignored_classes
        )

        self.sort_properties(iri, properties)

        # TODO: Need to refactor the properties data structure to a dict of list[Property].
        # properties += self.get_class_properties_from_schema_domain_includes(
        #     iri, ignored_classes
        # )

        return dict(sorted(properties.items(), key=lambda t: get_name(t[0], self.db)))

    def get_superclasses(
        self, iri: URIRef, graph: Graph, ignored_classes: list[URIRef]
    ) -> list[Class]:
        superclasses = filter(
            lambda x: x not in ignored_classes and isinstance(x, URIRef),
            list(graph.objects(iri, RDFS.subClassOf)),
        )
        return sorted(
            [
                self.get_component_model_class(superclass, graph, ignored_classes)
                for superclass in superclasses
            ],
            key=lambda x: x.name,
        )

    def get_component_model_class(
        self, iri: URIRef, graph: Graph, ignored_classes: list[URIRef]
    ):
        name = get_name(iri, graph, self.db)
        descriptions = get_descriptions(iri, graph)
        subclasses = get_subclasses(iri, graph, self.db, ignored_classes)
        # TODO: Add memoization to remove the need to recalculate the same classes.
        #       Reuse self.class_index or something similar for memoize data structure.
        superclasses = self.get_superclasses(iri, graph, ignored_classes)
        properties = self.get_component_model_class_properties(iri, ignored_classes)

        def _merge_superclass_properties(superclasses: list[Class]):
            for superclass in superclasses:
                for (
                    property_iri,
                    superclass_properties,
                ) in superclass.properties.items():
                    for superclass_property in superclass_properties:
                        if properties.get(property_iri):
                            if superclass_property not in properties[property_iri]:
                                properties[property_iri].append(superclass_property)
                        else:
                            properties[property_iri] = []
                            properties[property_iri].append(superclass_property)

                if superclass.superclasses:
                    _merge_superclass_properties(superclass.superclasses)

        _merge_superclass_properties(superclasses)
        examples = get_examples(iri, graph)
        notes = get_notes(iri, graph)
        is_defined_by = get_is_defined_by(iri, graph, self.db)

        return Class(
            iri=iri,
            name=name,
            description=descriptions,
            subclasses=subclasses,
            superclasses=superclasses,
            properties=properties,
            examples=examples,
            notes=notes,
            is_defined_by=is_defined_by,
        )

    def get_component_model_classes(
        self, graph: Graph, ignored_classes: list[URIRef]
    ) -> list[Class]:
        classes = graph.subjects(RDF.type, OWL.Class)

        result = []
        for c in filter(lambda x: x not in ignored_classes, classes):
            result.append(self.get_component_model_class(c, graph, ignored_classes))
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
