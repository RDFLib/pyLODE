class Profile:
    """A Profile is a specification that constrains, extends, combines, or provides guidance or explanation about
    the usage of other specifications.

    This definition includes what are sometimes called "application profiles", "metadata application profiles", or
    "metadata profiles". In this document, "data profile" and these other variants are all referred to as just
    "profiles".

    This definition of Profiles is from The Profiles Vocabulary: https://www.w3.org/TR/dx-prof/ and objects created
    using this class are intended for use as prof:Profile instances.
    """
    def __init__(
            self,
            uri,
            label,
            comment,
            mediatypes,
            default_mediatype,
            languages=None,
            default_language='en',
            is_profile_of=None
    ):
        """
        Constructor

        :param uri: The namespace URI for the *profile* view.
        :type uri: str
        :param label: The human-readable label for the Profile.
        :type label: str
        :param comment: A description of the Profile.
        :type comment: str
        :param mediatypes: The list of IANA MediaTypes that this Profile supports.
        :type mediatypes: list
        :param default_mediatype: The default MediaType that this Profile is delivered in.
        :type default_mediatype: str
        :param languages: A list of languages this Profile supports. Identified by ISO 639-1 2-letter language codes.
        :type languages: list
        :param default_language: The default language, by default it is 'en': English.
        :type default_language: str
        :param is_profile_of: A list of URIs (strings) that this Profile is a Profile of
        :type is_profile_of: list
        """
        self.uri = uri
        self.label = label
        self.comment = comment
        self.mediatypes = mediatypes
        self.default_mediatype = default_mediatype
        self.languages = languages if languages is not None else ['en']
        self.default_language = default_language
        self.is_profile_of = is_profile_of

    def __str__(self):
        return self.uri


RDF_MEDIA_TYPES = [
    'text/turtle',
    'application/rdf+xml',
    'application/ld+json',
    'text/n3',
    'application/n-triples'
]
HTML_MEDIA_TYPE = "text/html"
PROF_PROFILE = Profile(
    "https://www.w3.org/TR/dx-prof/",
    "The Profiles Vocabulary",
    "The Profiles Vocabulary is an RDF vocabulary created to allow the machine-readable description of profiles of "
    "specifications for information resources.",
    [HTML_MEDIA_TYPE, "text/markdown"],
    HTML_MEDIA_TYPE,
    languages=["en"],
    default_language="en"
)
PROF_FLAT_PROFILE = Profile(
    "https://w3id.org/profile/prof-flat",
    "Flattened PROF Hierarchy",
    "A profile of the Profiles Vocabulary for documentation purposes that requires all details of profiles within a "
    "profile hierarchy to be documented be present within a single graph (or file)."
    "through profile hierarchy.",
    [HTML_MEDIA_TYPE, "text/markdown"],
    HTML_MEDIA_TYPE,
    languages=["en"],
    default_language="en"
)
OWL_PROFILE = Profile(
    "https://www.w3.org/TR/owl2-rdf-based-semantics/",
    "Web Ontology Language (OWL)",
    "The OWL 2 Web Ontology Language, informally OWL 2, is an ontology language for the Semantic Web with formally "
    "defined meaning. OWL 2 ontologies provide classes, properties, individuals, and data values and are stored as "
    "Semantic Web documents.",
    [HTML_MEDIA_TYPE, "text/markdown"],
    HTML_MEDIA_TYPE,
    languages=["en"],
    default_language="en"
)
ONT_DOC_PROFILE = Profile(
    "https://w3id.org/profile/ontdoc",
    "Ontology Documentation Profile",
    "OWL Classes and Properties as well as additional SKOS, Dublin Core Terms and schema.org annotation "
    "properties to be used to document ontologies.",
    [HTML_MEDIA_TYPE, "text/markdown"],
    HTML_MEDIA_TYPE,
    languages=["en"],
    default_language="en",
    is_profile_of=["https://www.w3.org/TR/owl2-rdf-based-semantics/"]
)
NMPF_PROFILE = Profile(
    "https://w3id.org/profile/nmpf",
    "Ireland's National Marine Planning Framework Ontology Documentation Profile",
    "OWL Classes and Properties as well as additional SKOS, Dublin Core Terms and schema.org annotation "
    "properties to be used to document ontologies.",
    [HTML_MEDIA_TYPE, "text/markdown"],
    HTML_MEDIA_TYPE,
    languages=["en"],
    default_language="en",
    is_profile_of=["https://www.w3.org/TR/owl2-rdf-based-semantics/"]
)
SKOS_PROFILE = Profile(
    "https://www.w3.org/TR/skos-reference/",
    "Simple Knowledge Organization System (SKOS)",
    "A common data model for sharing and linking knowledge organization systems, such as thesauri, taxonomies, "
    "classification schemes and subject heading systems.",
    RDF_MEDIA_TYPES + [HTML_MEDIA_TYPE, "text/markdown"],
    HTML_MEDIA_TYPE,
    languages=["en"],
    default_language="en",
    is_profile_of=["https://www.w3.org/TR/owl2-rdf-based-semantics/"]
)
VOC_PUB_PROFILE = Profile(
    "https://w3id.org/profile/vocpub",
    "Vocabulary Publication Profile",
    "SKOS ConceptSchemes, Collections & Concepts as well as additional Dublin Core Terms & schema.org "
    "annotation properties to be used to publish vocabularies.",
    RDF_MEDIA_TYPES + [HTML_MEDIA_TYPE, "text/markdown"],
    HTML_MEDIA_TYPE,
    languages=["en"],
    default_language="en",
    is_profile_of=["https://www.w3.org/TR/skos-reference/"]
)

# MOD_PROFILE = Profile(
#     "http://www.isibang.ac.in/ns/mod#MetadataForOntologyDescriptionAndPublication",
#     "Metadata for Ontology Description and Publication (MOD)",
#     "To describe the vocabularies, e.g., ontology, classification, metadata, etc.",
#     RDF_MEDIA_TYPES + [HTML_MEDIA_TYPE, "text/markdown"],
#     HTML_MEDIA_TYPE,
#     languages=["en"],
#     default_language="en",
#     is_profile_of=["https://www.w3.org/TR/owl2-rdf-based-semantics/", "http://purl.org/dc/terms/"]
# )

PROFILES = {
    "prof": PROF_PROFILE,
    "ontdoc": ONT_DOC_PROFILE,
    "vocpub": VOC_PUB_PROFILE,
    "nmpf": NMPF_PROFILE
    # "modp": MOD_PROFILE
}
