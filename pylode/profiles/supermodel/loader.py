import logging
import time

import httpx
from rdflib import Graph, URIRef, OWL, PROF, RDF, DCTERMS

from pylode.profiles.supermodel.dataset import Dataset
from pylode.profiles.supermodel.namespace import LODE

# TODO: Set up logging elsewhere
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

httpcore_logger = logging.getLogger("httpcore")
httpcore_logger.setLevel(logging.WARNING)

PYLODE_CONFIG_GRAPH = "urn:graph:pylode-config"


MEDIA_TYPES = {
    "text/turtle": "text/turtle",
    "application/n-triples": "application/n-triples",
    "application/n-quads": "application/n-quads",
}


def fetch(
    url: str, client: httpx.Client, content_type: str = "text/turtle"
) -> tuple[str, str]:
    # TODO: Remove proxies
    # http://localhost:8001/profiles/nz-profile.ttl
    # http://localhost:8000/csdm.ttl
    proxies = {
        # "https://linked.data.gov.au/def/csdm/geometryprim": "http://localhost:8000/geometryprim.ttl",
        # "http://www.opengis.net/ont/geosparql": "https://cdn.jsdelivr.net/gh/opengeospatial/ogc-geosparql@master/1.1/geo.ttl",
        # "http://datashapes.org/dash": "https://cdn.jsdelivr.net/gh/zazuko/rdf-vocabularies@master/ontologies/dash/dash.nq",
        # "https://linked.data.gov.au/def/csdm/container": "http://localhost:8000/container.ttl",
        # "https://linked.data.gov.au/def/csdm/parcels": "http://localhost:8000/parcels.ttl",
        # "https://linked.data.gov.au/def/csdm/commonpatterns": "http://localhost:8000/commonpatterns.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/icsm-common.ttl": "http://localhost:8001/profiles/icsm-common.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/icsm-profile-shacl.ttl": "http://localhost:8001/profiles/icsm-profile-shacl.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/nz-vocab-bindings.ttl": "http://localhost:8001/profiles/nz-vocab-bindings.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/nz-profile-shacl.ttl": "http://localhost:8001/profiles/nz-profile-shacl.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/nz-vocabs-shacl.ttl": "http://localhost:8001/profiles/nz-vocabs-shacl.ttl",
        # "https://icsm-au.github.io/3d-csdm/csdm.ttl": "http://localhost:8000/csdm.ttl",
        # "https://icsm-au.github.io/3d-csdm/pylode.ttl": "http://localhost:8000/pylode.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/jurisdictional-codelist-types.shacl": "http://localhost:8001/profiles/jurisdictional-codelist-types.shacl",
        # "https://icsm-au.github.io/3d-csdm/shapes/survey_features.shapes.ttl": "http://localhost:8000/shapes/survey_features.shapes.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/wa-vocab-bindings.ttl": "http://localhost:8001/profiles/wa-vocab-bindings.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/icsm-vocab-bindings.ttl": "http://localhost:8001/profiles/icsm-vocab-bindings.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/wa-profile-shacl.ttl": "http://localhost:8001/profiles/wa-profile-shacl.ttl",
        # "https://icsm-au.github.io/3d-csdm/commonpatterns.ttl": "http://localhost:8000/commonpatterns.ttl",
        # "https://icsm-au.github.io/3d-csdm/shapes/common_patterns.shapes.ttl": "http://localhost:8000/shapes/common_patterns.shapes.ttl",
        # "https://icsm-au.github.io/3d-csdm-profiles/profiles/nz-pointnames-shacl.ttl": "http://localhost:8001/profiles/nz-pointnames-shacl.ttl",
        # "https://icsm-au.github.io/3d-csdm/shapes/container.shapes.ttl": "http://localhost:8000/shapes/container.shapes.ttl",
    }
    if url in proxies:
        logger.debug(f"Using proxy URL {url} to {proxies[url]}")
        url = proxies[url]
    response = client.get(url, headers={"Accept": content_type})
    if response.status_code != 200:
        raise httpx.HTTPError(
            f"HTTP {response.status_code}: Failed to fetch remote resource from {url}. {response.text}"
        )

    content_type_headers = response.headers.get("Content-Type")
    for media_type in MEDIA_TYPES:
        if media_type in content_type_headers:
            content_type = media_type
    return response.text, content_type


class ProfilesDataset(Dataset):
    def load_owl_imports(self, graph: Graph):
        """Load all owl:imports values recursively."""
        import_values = [
            str(v)
            for v in graph.objects(None, OWL.imports)
            if str(v) not in self.external_resources
        ]
        if import_values:
            for remote_resource in import_values:
                if str(remote_resource) not in self.external_resources:
                    logger.debug(
                        f"Fetching remote resource {remote_resource} from owl:imports."
                    )
                    _graph = Graph()
                    try:
                        data, content_type = fetch(str(remote_resource), self.client)
                        _graph.parse(data=data, format=content_type)
                        # _graph.parse(str(remote_resource))
                        self.external_resources.add(str(remote_resource))
                        graph.__iadd__(self.load_owl_imports(_graph))
                    except Exception as err:
                        raise RuntimeError(
                            f"Failed to parse data from {remote_resource}. {err}"
                        )

        return graph

    def load_profiles(self, graph: Graph, prev_graph: Graph):
        profiles = graph.subjects(RDF.type, PROF.Profile)
        for profile in profiles:
            cbd = graph.cbd(profile)
            profile_graph = Graph(identifier=str(profile))
            profile_graph.__iadd__(cbd)

            prof_resource_descriptors = profile_graph.objects(None, PROF.hasResource)
            for prof_resource_descriptor in prof_resource_descriptors:
                mediatype = profile_graph.value(
                    prof_resource_descriptor, DCTERMS.format
                )
                role = profile_graph.value(prof_resource_descriptor, PROF.hasRole)
                remote_resource = profile_graph.value(
                    prof_resource_descriptor, PROF.hasArtifact
                )

                if role == LODE.config:
                    config_graph = self.get_graph(URIRef(PYLODE_CONFIG_GRAPH))
                    logger.debug(
                        f"Fetching remote resource {remote_resource} from PROF resource descriptor. A pylode config."
                    )
                    data, content_type = fetch(
                        str(remote_resource), self.client, str(mediatype)
                    )
                    config_graph.parse(data=data, format=content_type)

                    _config_graph = Graph().parse(data=data, format=content_type)
                    _config_graph = self.load_owl_imports(_config_graph)
                    self.load_profiles(_config_graph, graph)
                elif str(mediatype) in MEDIA_TYPES:
                    logger.debug(
                        f"Fetching remote resource {remote_resource} from PROF resource descriptor."
                    )
                    new_graph = Graph()
                    data, content_type = fetch(
                        str(remote_resource), self.client, str(mediatype)
                    )
                    new_graph.parse(data=data, format=content_type)
                    new_graph = self.load_owl_imports(new_graph)

                    if new_graph.value(None, RDF.type, PROF.Profile):
                        self.load_profiles(new_graph, profile_graph)
                    else:
                        profile_graph.__iadd__(new_graph)
            self.add_graph(profile_graph)

    def __init__(self, root_profile_iri: str, data: str):
        super().__init__(default_union=True)
        self.root_profile_iri = root_profile_iri
        self.client = httpx.Client(follow_redirects=True)

        # Tracks what we have loaded so far.
        self.external_resources = set()

        graph = Graph()
        graph.parse(data=data)
        graph = self.load_owl_imports(graph)
        initial_profiles_graph = Graph()
        for profile in graph.subjects(RDF.type, PROF.Profile):
            cbd = graph.cbd(profile)
            initial_profiles_graph.__iadd__(cbd)
            graph = graph - cbd

        self.add_graph(Graph(identifier=PYLODE_CONFIG_GRAPH))
        self.load_profiles(initial_profiles_graph, graph)

        root_graph = Graph(identifier=root_profile_iri)
        root_graph.__iadd__(graph)
        self.add_graph(root_graph)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    @property
    def root_graph(self) -> Graph:
        return self.get_graph(URIRef(self.root_profile_iri))

    @property
    def config_graph(self) -> Graph:
        return self.get_graph(URIRef(PYLODE_CONFIG_GRAPH))


def load_profiles(root_profile_iri: str, data: str) -> ProfilesDataset:
    """Create an RDF Dataset by expanding the initial profile data.

    Profiles are mapped to a named graph in the dataset.
    This function loads statements from owl:imports and PROF resources.
    These statements are loaded into their profile's named graphs.
    """
    start_time = time.time()
    with ProfilesDataset(root_profile_iri, data) as db:
        logger.debug(
            f"Finished loading profiles in {time.time() - start_time:.2f} seconds."
        )
        logger.debug(f"Named graphs:")
        logger.debug([str(g.identifier) for g in db.graphs()])
        logger.debug(
            f"pylode config:\n{db.get_graph(URIRef(PYLODE_CONFIG_GRAPH)).serialize(format='longturtle')}"
        )
        return db
