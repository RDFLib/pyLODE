from rdflib import Graph, RDF, RDFS, OWL, Namespace, util
from rdflib.namespace import SKOS, DC, DCTERMS, FOAF, DOAP, PROV, SDO, XSD
from rdflib.term import URIRef, Literal, BNode
from os import path
import requests
import collections
import dateutil.parser
from jinja2 import Environment, FileSystemLoader
from rdflib import plugin
from rdflib.plugin import register, Serializer
from rdflib_jsonld import serializer
from profiles import PROFILES
import markdown

register("json-ld", Serializer, "rdflib_jsonld.serializer", "JsonLDSerializer")

RDF_FILE_EXTENSIONS = [".rdf", ".owl", ".ttl", ".n3", ".nt", ".json"]

RDF_SERIALIZER_MAP = {
    "text/turtle": "turtle",
    "text/n3": "n3",
    "application/n-triples": "nt",
    "application/ld+json": "json-ld",
    "application/rdf+xml": "xml",
    # Some common but incorrect mimetypes
    "application/rdf": "xml",
    "application/rdf xml": "xml",
    "application/json": "json-ld",
    "application/ld json": "json-ld",
    "text/ttl": "turtle",
    "text/turtle;charset=UTF-8": "turtle",
    "text/ntriples": "nt",
    "text/n-triples": "nt",
    "text/plain": "nt",  # text/plain is the old/deprecated mimetype for n-triples
}


class MakeDocco:
    def __init__(self, input_data_file=None, input_uri=None, outputformat="html", profile="owl"):
        self.profile_selected = profile
        self.default_language = "en"

        if outputformat not in ["html", "md"]:
            self.outputformat = "html"
        else:
            self.outputformat = outputformat

        if profile not in PROFILES.keys():
            self.profile_selected = "owl"
        else:
            self.profile_selected = profile

        # shared variables
        if input_data_file is not None:
            self._parse_input_data_file(input_data_file)
        elif input_uri is not None:
            self._parse_input_uri(input_uri)
        else:
            raise Exception("You must supply either an input file or a URI for your ontology's RDF")

        self.NAMESPACES = collections.OrderedDict()
        self.FIDS = {}
        self.METADATA = {}
        self.G.bind("sdo", SDO)
        self.SDO2 = Namespace("http://schema.org/")
        self.G.bind("sdo2", self.SDO2)
        self.G.bind("prov", PROV)

        if self.profile_selected == "owl":
            self.CLASSES = collections.OrderedDict()
            self.PROPERTIES = collections.OrderedDict()
            self.NAMED_INDIVIDUALS = collections.OrderedDict()
        elif self.profile_selected == "skos":
            self.CONCEPTS = collections.OrderedDict()
            self.COLLECTIONS = collections.OrderedDict()

    def _parse_input_data_file(self, input_data_file):
        if not str(input_data_file).endswith(tuple(RDF_FILE_EXTENSIONS)):
            raise Exception(
                "If supplying an input RDF file, it must end with one of the following file type extensions: {}."
                    .format(
                        ", ".join(RDF_FILE_EXTENSIONS)
                    )
                )
        else:
            fmt = (
                "json-ld"
                if input_data_file.endswith(".json") or input_data_file.endswith(".jsonld")
                else util.guess_format(input_data_file)
            )
            with open(input_data_file, 'r') as f:
                data = f.read()
            self.G = Graph().parse(data=data, format=fmt)
            self.source_info = (input_data_file, fmt)
            self.publication_dir = path.dirname(input_data_file)

    def _parse_input_uri(self, uri):
        r = requests.get(
            uri, headers={"Accept": ", ".join(RDF_SERIALIZER_MAP.keys())}
        )
        # get RDF format from Media Type
        media_type = r.headers.get("Content-Type").split(";")[0]  # splitting off any ;charset=...
        if RDF_SERIALIZER_MAP.get(media_type):
            fmt = RDF_SERIALIZER_MAP.get(media_type)
        else:
            fmt = (
                "json-ld"
                if media_type == "application/ld+json"
                   or media_type == "application/json"
                else None
            )

        if fmt is None:
            raise Exception(
                "Could not parse the supplied URI. The RDF format could not be determined from Media Type "
                "({} was given) or from a file extension".format(media_type)
            )

        self.G = Graph().parse(data=r.text, format=fmt)
        self.source_info = (uri, fmt)
        self.publication_dir = path.join(
            path.dirname(path.realpath(__file__)), "output_files"
        )

    @classmethod
    def list_profiles(cls):
        s = ""
        for k, v in PROFILES.items():
            s += "{}: {}\n".format(k, v)

        return s

    @classmethod
    def is_supported_profile(cls, profile_key):
        is_supported = False
        for k, v in PROFILES.items():
            if profile_key == k or profile_key == v.uri:
                is_supported = True

        return is_supported

    #
    #   Item utilities
    #
    def _load_template(self, template_file):
        return Environment(
            loader=FileSystemLoader(path.join(path.dirname(path.realpath(__file__)), "templates"))
        ).get_template(template_file)

    def _get_namespace_from_uri(self, uri):
        # split on hash
        segments = uri.split("#")
        if len(segments) == 2:
            return segments[0] + "#"
        else:
            segments = uri.split("/")
            if len(segments) > 1:
                return "/".join(segments[0:-1]) + "/"
            else:
                return None

    def _get_curie_prefix(uself, uri, existing_curies):
        ns_count = 0

        from .curies import CURIES

        # TODO: replace this with a once-per run update CURIES function
        def get_curie_online(uri):
            try:
                r = requests.get(
                    "http://prefix.cc/reverse", params={"uri": uri, "format": "txt"}
                )
                if r.status_code == 200:
                    # primitive check to see if it really is prefix.cc replying with a text/plain response
                    if r.headers["Content-Type"] == "text/plain":
                        return r.text.split("\t")[0]
                    else:
                        return None
                else:
                    return None
            except requests.exceptions.ConnectionError:
                # presumably this module can't access the internet or prefix.cc is down
                return None

        def get_curie_from_namespace(uri, existing_curies, ns_count):
            # strip off trailing hash or slash and return last path segment
            c = uri.rstrip("#/").split("/")[-1]

            # prevent CURIE collision = return nsX (X int) if we already have this one
            if c in existing_curies:
                ns_count += 1
                return "ns" + str(ns_count)

            return c

        # attempt to look up the well-known curie for this Namespace in http://prefix.cc dump
        for k, v in CURIES.items():
            if v == uri:
                return k

        # attempt to look up the well-known CURIE for this Namespace using http://prefix.cc online (more up-to-date)
        c = get_curie_online(uri)
        if c is not None:
            return c

        # can't find CURIE online so make up one
        c = get_curie_from_namespace(uri, existing_curies, ns_count)
        return c if c is not None else ""

    def _extract_namespaces(self):
        """
        First we get the namespaces from rdflib

        Then we cycle through all the URIs in the graph (all s, p & o),
            create a set of them,
            extract their base URIS (i.e. a non-duplicative list of them)
            see if they are in the namespaces,
                if not, generate their CURIE and add them to namespaces
        """
        # get declared namespaces, keyed by URI
        ns = {}
        uri_bases = set()
        for k, v in self.G.namespaces():
            ns[str(v)] = k

        # get other namespaces by extracting base URIs from all URIs
        for s, p, o in self.G:
            # exclude certain annotation URIs
            # and individuals (SDO.identifier)
            # exclude known annoying URIs (ORCID)
            if (
                p == OWL.versionIRI
                or p == OWL.imports
                or p == SDO.identifier
                or self.SDO2.identifier
                or str(o).startswith("https://orcid")
            ):
                pass
            else:
                # add only URI subjects (not Blank Nodes)
                if type(s) == URIRef:
                    uri_bases.add(self._get_namespace_from_uri(str(s)))

                # predicates are always URIs so add them all
                uri_bases.add(self._get_namespace_from_uri(str(p)))

                # add only URI objects (not Blank Nodes or Literals), exclude emails
                if type(o) == URIRef and "@" not in str(o):
                    uri_bases.add(self._get_namespace_from_uri(str(o)))

        # for the de-duplicated URIs, if the uri_base is not in namespaces, get CURIE and add it
        for uri_base in uri_bases:
            if ns.get(uri_base) is None:
                uri_prefix = self._get_curie_prefix(uri_base, [x for x in ns.values()])
                ns[uri_base] = uri_prefix

        # invert the key/values in instances
        for k, v in sorted(ns.items(), key=lambda x: x[1]):
            if v == "":  # can't use empty dict keys in Python
                self.NAMESPACES[":"] = k
            else:
                self.NAMESPACES[v] = k

    def _make_title_from_uri(self, uri):
        # can't tolerate any URI faults so return None if anything is wrong

        # URIs with no path segments or ending in slash
        segments = uri.split("/")
        if len(segments[-1]) < 1:
            return None

        # URIs with only a domain - no path segments
        if len(segments) < 4:
            return None

        # URIs ending in hash
        if segments[-1].endswith("#"):
            return None

        return (
            segments[-1].split("#")[-1]
            if segments[-1].split("#")[-1] != ""
            else segments[-1].split("#")[-2]
        )

    # makes the fragment ID for a class, property, Named Individual (any entity) based on URI or name
    def _make_fid(self, title, uri):
        # does this URI already have a fid?
        existing_fid = self.FIDS.get(uri)
        if existing_fid is not None:
            return existing_fid

        # no, so make one
        def _remove_non_ascii_chars(s):
            return "".join(j for j in s if ord(j) < 128).replace("&", "").lower()

        # try creating an ID from label
        # lowercase, remove spaces, escape all non-ASCII chars
        if title is not None:
            fid = _remove_non_ascii_chars(title.replace(" ", ""))

            # do not return fid if it's already in use
            if fid not in self.FIDS.values():
                self.FIDS[uri] = fid
                return fid

        # this fid is already present so generate a new one from the URI instead

        # split URI for last slash segment
        segments = uri.split("/")
        # return None for empty string - URI ends in slash
        if len(segments[-1]) < 1:
            return None

        # return None for domains, i.e. ['http:', '', '{domain}'] - no path segments
        if len(segments) < 4:
            return None

        # split out hash URIs
        # remove any training hashes
        if segments[-1].endswith("#"):
            return None

        fid = (
            segments[-1].split("#")[-1]
            if segments[-1].split("#")[-1] != ""
            else segments[-1].split("#")[-2]
        )
        # fid = fid.lower()

        # do not return fid if it's already in use
        if fid not in self.FIDS.values():
            self.FIDS[uri] = fid
            return fid
        else:
            # since it's in use but we've exhausted generation options, just add 1 to existing fid name
            self.FIDS[uri] = fid + "1"
            return fid + "1"  # yeah yeah, there could be more than one but unlikely

    def _get_default_namespace(self):
        self.METADATA["default_namespace"] = None

        # if this ontology declares a preferred URI, use that
        if self.METADATA.get("preferredNamespaceUri"):
            self.METADATA["default_namespace"] = self.METADATA.get(
                "preferredNamespaceUri"
            )

        # if not, try the URI of the ontology compared to all prefixes
        for s in self.G.subjects(predicate=RDF.type, object=OWL.Ontology):
            ont_uri = str(s)

        for s in self.G.subjects(predicate=RDF.type, object=SKOS.ConceptScheme):
            ont_uri = str(s)

        for k, v in self.NAMESPACES.items():
            # i.e. the ontology URI is the same as the default namespace + / or #
            if v == ont_uri + "/" or v == ont_uri + "#":
                self.METADATA["default_namespace"] = v

        if self.NAMESPACES.get("") is not None:
            del self.NAMESPACES[""]

    def _get_curie(self, uri):
        n = self._get_namespace_from_uri(str(uri))
        for k, v in self.NAMESPACES.items():
            if v == n or v.strip("/#") == n:
                if k == ":":
                    return "{}".format(self._get_uri_id(uri))
                else:
                    return "{}:{}".format(k, self._get_uri_id(uri))

        # if no match, return the original URI
        return uri

    def _get_uri_id(self, uri):
        # split on hash
        segments = uri.split("#")
        if len(segments) == 2:
            return segments[1]
        else:
            return uri.split("/")[-1]  # could return None if URI ends in /

    def _make_agent_link(self, name, url=None, email=None):
        if url is not None and email is not None:
            agent = '<a href="{0}">{1}</a> (<a href="mailto:{2}">{2}</a>)'.format(
                url, name, email.replace("mailto:", "")
            )
        elif url is not None and email is None:
            agent = '<a href="{0}">{1}</a>'.format(url, name)
        elif url is None and email is not None:
            agent = '<a href="{0}">{1}</a>'.format(email.split("/")[-1], name)
        elif url is not None:
            agent = '<a href="{}">{}</a>'.format(url, name)
        else:
            agent = name

        return agent

    def _make_source_file_link(self, source_info):
        return '<a href="{}">RDF ({})</a>'.format(
            source_info[0].split("/")[-1], source_info[1]
        )

    #
    #   All profiles
    #
    def _make_namespaces(self, outputformat="html"):
        return self._load_template("namespaces." + outputformat).render(
            namespaces=self.NAMESPACES,
            default_namespace=self.METADATA["default_namespace"],
        )

    def _make_schemaorg_metadata(self):
        uri = URIRef(self.METADATA.get("uri"))
        name = Literal(self.METADATA.get("title"))
        publishers = ""
        creators = ""
        if self.METADATA.get("created") is not None:
            date_created = Literal(self.METADATA.get("created"), datatype=XSD.date)
        if self.METADATA.get("modified") is not None:
            date_modified = Literal(self.METADATA.get("modified"), datatype=XSD.date)
        if self.METADATA.get("description") is not None:
            description = Literal(self.METADATA.get("description"))
        if self.METADATA.get("license") is not None:
            license = URIRef(self.METADATA.get("license").split('>')[1].split('<')[0])
        else:
            license = None
        if self.METADATA.get("rights") is not None:
            rights = Literal(self.METADATA.get("rights"))
        copyright_holder = ""
        if self.METADATA.get("created") is not None:
            copyright_year = Literal(
                self.METADATA.get("created").split("-")[0], datatype=XSD.int
            )
        if self.METADATA.get("repository") is not None:
            repository = URIRef(self.METADATA.get("repository"))

        """
        @prefix sdo: <https://schema.org/> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

        <http://linked.data.gov.au/def/crs> a sdo:DigitalDocument ;
            sdo:name "CRS Ontology" ;
            sdo:publisher <http://catalogue.linked.data.gov.au/org/naa> ;
            sdo:creator [
                sdo:name "Nicholas J. Car" ;
                sdo:identifier <http://orcid.org/0000-0002-8742-7730> ;
                sdo:email <nicholas.car@csiro.au> ;
                sdo:memberOf [
                    sdo:name "CSIRO" ;
                    sdo:identifier <http://catalogue.linked.data.gov.au/org/csiro> ;
                ] ;
            ] ;
            sdo:date_created "2018-09-10"^^xsd:date ;
            sdo:date_modified "2019-05-31"^^xsd:date ;
            sdo:license <https://creativecommons.org/licenses/by/4.0/> ;

            sdo:copyrightHolder <http://catalogue.linked.data.gov.au/org/naa> ;
            sdo:copyright_year "2019"^^xsd:gYear ;
            sdo:encodingFormat <https://w3id.org/mediatype/text/html> ;
        .

        <http://catalogue.linked.data.gov.au/org/naa>
            a sdo:Organization ;
            sdo:name "National Archives of Australia" ;
            sdo:identifier <http://catalogue.linked.data.gov.au/org/naa> ;
        .        
        """
        g = Graph()
        SDO = Namespace("https://schema.org/")
        g.bind("sdo", SDO)
        g.bind("xsd", XSD)

        g.add((uri, RDF.type, SDO.DefinedTermSet))
        g.add((uri, SDO.name, name))
        # g.add((uri, SDO.publishers, SDO.DigitalDocument))
        # g.add((uri, SDO.creators, SDO.DigitalDocument))
        if self.METADATA.get("date_created") is not None:
            g.add((uri, SDO.dateCreated, date_created))
        if self.METADATA.get("date_modified") is not None:
            g.add((uri, SDO.dateModified, date_modified))
        if self.METADATA.get("description") is not None:
            g.add((uri, SDO.description, description))
        if license is not None:
            g.add((uri, SDO.license, license))
        if self.METADATA.get("rights") is not None:
            g.add((uri, SDO.rights, rights))
        # g.add((uri, SDO.copyrightHolder, copyrightHolder))
        if self.METADATA.get("copyright_year") is not None:
            g.add((uri, SDO.copyrightYear, copyright_year))
        if self.METADATA.get("repository") is not None:
            g.add((uri, SDO.codeRepository, repository))

        return g.serialize(format="json-ld").decode("utf-8")

    #
    #   OWL
    #
    def _expand_graph_for_owl(self):
        # name
        for s, o in self.G.subject_objects(predicate=DC.title):
            self.G.add((s, RDFS.label, o))

        for s, o in self.G.subject_objects(predicate=DCTERMS.title):
            self.G.add((s, RDFS.label, o))

        for s, o in self.G.subject_objects(predicate=SKOS.prefLabel):
            self.G.add((s, RDFS.label, o))

        for s, o in self.G.subject_objects(predicate=SDO.name):
            self.G.add((s, RDFS.label, o))

        # description
        for s, o in self.G.subject_objects(predicate=DC.description):
            self.G.add((s, RDFS.comment, o))

        for s, o in self.G.subject_objects(predicate=DCTERMS.description):
            self.G.add((s, RDFS.comment, o))

        for s, o in self.G.subject_objects(predicate=SKOS.definition):
            self.G.add((s, RDFS.comment, o))

        # property types
        for s in self.G.subjects(predicate=RDF.type, object=OWL.ObjectProperty):
            self.G.add((s, RDF.type, RDF.Property))

        for s in self.G.subjects(predicate=RDF.type, object=OWL.FunctionalProperty):
            self.G.add((s, RDF.type, RDF.Property))

        for s in self.G.subjects(predicate=RDF.type, object=OWL.DatatypeProperty):
            self.G.add((s, RDF.type, RDF.Property))

        for s in self.G.subjects(predicate=RDF.type, object=OWL.AnnotationProperty):
            self.G.add((s, RDF.type, RDF.Property))

        # class types
        for s in self.G.subjects(predicate=RDF.type, object=OWL.Class):
            self.G.add((s, RDF.type, RDFS.Class))

        # owl:Restrictions from Blank Nodes
        for s in self.G.subjects(predicate=OWL.onProperty):
            self.G.add((s, RDF.type, OWL.Restriction))

    def _extract_metadata_for_owl(self):
        if len(self.CLASSES.keys()) > 0:
            self.METADATA["has_classes"] = True

        self.METADATA["has_ops"] = False
        self.METADATA["has_fps"] = False
        self.METADATA["has_dps"] = False
        self.METADATA["has_aps"] = False
        self.METADATA["has_ps"] = False

        if len(self.NAMED_INDIVIDUALS.keys()) > 0:
            self.METADATA["has_nis"] = True

        for k, v in self.PROPERTIES.items():
            if v.get("prop_type") == "op":
                self.METADATA["has_ops"] = True
            if v.get("prop_type") == "fp":
                self.METADATA["has_fps"] = True
            if v.get("prop_type") == "dp":
                self.METADATA["has_dps"] = True
            if v.get("prop_type") == "ap":
                self.METADATA["has_aps"] = True
            if v.get("prop_type") == "p":
                self.METADATA["has_ps"] = True

        s_str = None
        self.METADATA["imports"] = set()
        self.METADATA["creators"] = set()
        self.METADATA["contributors"] = set()
        self.METADATA["publishers"] = set()
        for s in self.G.subjects(predicate=RDF.type, object=OWL.Ontology):
            s_str = str(s)  # this is the Ontology's URI
            self.METADATA["uri"] = s_str

            for p, o in self.G.predicate_objects(subject=s):
                if p == OWL.imports:
                    self.METADATA["imports"].add(self._make_uri_html(o))

                if p == RDFS.label:
                    self.METADATA["title"] = str(o)

                if p == RDFS.comment:
                    import markdown

                    self.METADATA["description"] = markdown.markdown(str(o))

                if p == SKOS.historyNote:
                    self.METADATA["historyNote"] = str(o)

                if p == DCTERMS.created:
                    self.METADATA["created"] = dateutil.parser.parse(str(o)).strftime(
                        "%Y-%m-%d"
                    )

                if p == DCTERMS.modified:
                    self.METADATA["modified"] = dateutil.parser.parse(str(o)).strftime(
                        "%Y-%m-%d"
                    )

                if p == DCTERMS.issued:
                    self.METADATA["issued"] = dateutil.parser.parse(str(o)).strftime(
                        "%Y-%m-%d"
                    )

                if p == DCTERMS.source:
                    if str(o).startswith('http'):
                        self.METADATA["source"] = self._make_uri_html(o)  # '<a href="{0}">{0}</a>'.format(str(o))
                    else:
                        self.METADATA["source"] = str(o)

                if p == OWL.versionIRI:
                    self.METADATA["versionIRI"] = '<a href="{0}">{0}</a>'.format(str(o))

                if p == OWL.versionInfo:
                    self.METADATA["versionInfo"] = str(o)

                if p == URIRef("http://purl.org/vocab/vann/preferredNamespacePrefix"):
                    self.METADATA["preferredNamespacePrefix"] = str(o)

                if p == URIRef("http://purl.org/vocab/vann/preferredNamespaceUri"):
                    self.METADATA["preferredNamespaceUri"] = str(o)

                if p == DCTERMS.license:
                    self.METADATA["license"] = (
                        '<a href="{0}">{0}</a>'.format(str(o))
                        if str(o).startswith("http")
                        else str(o)
                    )

                if p == DCTERMS.rights:
                    self.METADATA["rights"] = (
                        str(o)
                        .replace("Copyright", "&copy;")
                        .replace("copyright", "&copy;")
                    )

                # Agents
                if p == DC.creator:
                    if type(o) == URIRef:
                        self.METADATA["creators"].add(
                            '<a href="{0}">{0}</a>'.format(str(o))
                        )
                    else:
                        self.METADATA["creators"].add(str(o))

                if p == DCTERMS.creator:
                    if type(o) == Literal:
                        self.METADATA["creators"].add(str(o))
                    else:  # Blank Node or URI
                        self.METADATA["creators"].add(self._make_agent_html(o))

                if p == DC.contributor:
                    if type(o) == URIRef:
                        self.METADATA["contributors"].add(
                            '<a href="{0}">{0}</a>'.format(str(o))
                        )
                    else:
                        self.METADATA["contributors"].add(str(o))

                if p == DCTERMS.contributor:
                    if type(o) == Literal:
                        self.METADATA["contributors"].add(str(o))
                    else:  # Blank Node or URI
                        self.METADATA["contributors"].add(self._make_agent_html(o))

                if p == DC.publisher:
                    if type(o) == URIRef:
                        self.METADATA["publishers"].add(
                            '<a href="{0}">{0}</a>'.format(str(o))
                        )
                    else:
                        self.METADATA["publishers"].add(str(o))

                if p == DCTERMS.publisher:
                    if type(o) == Literal:
                        self.METADATA["publishers"].add(str(o))
                    else:  # Blank Node or URI
                        self.METADATA["publishers"].add(self._make_agent_html(o))

                # TODO: cater for other Agent representations

                if p == PROV.wasGeneratedBy:
                    for o2 in self.G.objects(subject=o, predicate=DOAP.repository):
                        self.METADATA["repository"] = str(o2)

                if p == SDO.codeRepository:
                    self.METADATA["repository"] = str(o)

            if self.METADATA.get("title") is None:
                raise ValueError(
                    "Your ontology does not indicate any form of label or title. "
                    "You must declare one of the following for your ontology: rdfs:label, dct:title, skos:prefLabel"
                )

        if s_str is None:
            raise Exception(
                "Your RDF file does not define an ontology. "
                "It must contains a declaration such as <...> rdf:type owl:Ontology ."
            )

    def _extract_classes_uris(self):
        classes = []
        for s in self.G.subjects(predicate=RDF.type, object=RDFS.Class):
            # ignore blank nodes for things like [ owl:unionOf ( ... ) ]
            if type(s) == BNode:
                pass
            else:
                classes.append(str(s))

        for p in sorted(classes):
            self.CLASSES[p] = {}

    def _extract_classes(self):
        for cls in self.CLASSES.keys():
            s = URIRef(cls)
            # create Python dict for each class
            self.CLASSES[cls] = {}

            # basic class properties
            self.CLASSES[cls]["title"] = None
            self.CLASSES[cls]["description"] = None
            self.CLASSES[cls]["scopeNote"] = None
            self.CLASSES[cls]["example"] = None
            self.CLASSES[cls]["isDefinedBy"] = None
            self.CLASSES[cls]["source"] = None

            for p, o in self.G.predicate_objects(subject=s):
                if p == RDFS.label:
                    self.CLASSES[cls]["title"] = str(o)

                if p == RDFS.comment:
                    self.CLASSES[cls]["description"] = str(o)

                if p == SKOS.scopeNote:
                    self.CLASSES[cls]["scopeNote"] = str(o)

                if p == SKOS.example:
                    self.CLASSES[cls]["example"] = str(o)

                if p == RDFS.isDefinedBy:
                    self.CLASSES[cls]["isDefinedBy"] = str(o)

                if p == DCTERMS.source or p == DC.source:
                    if str(o).startswith('http'):
                        self.CLASSES[cls]["source"] = self._make_uri_html(o)  # '<a href="{0}">{0}</a>'.format(str(o))
                    else:
                        self.CLASSES[cls]["source"] = str(o)

            # patch title from URI if we haven't got one
            if self.CLASSES[cls]["title"] is None:
                self.CLASSES[cls]["title"] = self._make_title_from_uri(cls)

            # make fid
            self.CLASSES[cls]["fid"] = self._make_fid(self.CLASSES[cls]["title"], cls)

            # equivalent classes
            equivalent_classes = []
            for o in self.G.objects(subject=s, predicate=OWL.equivalentClass):
                if type(o) != BNode:
                    equivalent_classes.append(
                        self._get_curie(str(o))
                    )  # ranges that are just classes
                else:
                    # equivalent classes collections (unionOf | intersectionOf
                    q = """
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  

                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> owl:equivalentClass ?eq .  
                            ?eq owl:unionOf|owl:intersectionOf ?collection .
                            ?eq ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    """.format(
                        s
                    )
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(self._get_curie(str(r.col_member)))
                    equivalent_classes.append((collection_type, collection_members))
            self.CLASSES[cls]["equivalents"] = equivalent_classes

            # super classes
            supers = []
            restrictions = []
            for o in self.G.objects(subject=s, predicate=RDFS.subClassOf):
                if (o, RDF.type, OWL.Restriction) not in self.G:
                    if type(o) != BNode:
                        supers.append(str(o))  # supers that are just classes
                    else:
                        # super collections (unionOf | intersectionOf
                        q = """
                            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  

                            SELECT ?col_type ?col_member
                            WHERE {{
                                <{}> rdfs:subClassOf ?sup .  
                                ?sup owl:unionOf|owl:intersectionOf ?collection .
                                ?sup ?col_type ?collection . 
                                ?collection rdf:rest*/rdf:first ?col_member .              
                            }} 
                        """.format(
                            s
                        )
                        collection_type = None
                        collection_members = []
                        for r in self.G.query(q):
                            collection_type = self._get_curie(str(r.col_type))
                            collection_members.append(str(r.col_member))
                        supers.append((collection_type, collection_members))
                else:
                    restrictions.append(o)

            self.CLASSES[cls]["supers"] = supers
            self.CLASSES[cls]["restrictions"] = restrictions

            # sub classes
            subs = []
            for o in self.G.subjects(predicate=RDFS.subClassOf, object=s):
                if type(o) != BNode:
                    subs.append(str(o))
                else:
                    # sub classes collections (unionOf | intersectionOf
                    q = """
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  

                        SELECT ?col_type ?col_member
                        WHERE {{
                            ?sub rdfs:subClassOf <{}> . 
                            ?sub owl:unionOf|owl:intersectionOf ?collection .
                            ?sub ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    """.format(
                        s
                    )
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(self._get_curie(str(r.col_member)))
                    subs.append((collection_type, collection_members))
            self.CLASSES[cls]["subs"] = subs

            in_domain_of = []
            for o in self.G.subjects(predicate=RDFS.domain, object=s):
                in_domain_of.append(str(o))
            self.CLASSES[cls]["in_domain_of"] = in_domain_of

            in_domain_includes_of = []
            for o in self.G.subjects(predicate=SDO.domainIncludes, object=s):
                in_domain_includes_of.append(str(o))
            self.CLASSES[cls]["in_domain_includes_of"] = in_domain_includes_of

            in_range_of = []
            for o in self.G.subjects(predicate=RDFS.range, object=s):
                in_range_of.append(str(o))
            self.CLASSES[cls]["in_range_of"] = in_range_of

            in_range_includes_of = []
            for o in self.G.subjects(predicate=SDO.rangeIncludes, object=s):
                in_range_includes_of.append(str(o))
            self.CLASSES[cls]["in_range_includes_of"] = in_range_includes_of

            # TODO: cater for Named Individuals of this class - "has members"

        # # sort properties by title
        # x = sorted([(k, v) for k, v in classes.items()], key=lambda tup: tup[1]['title'])
        # y = collections.OrderedDict()
        # for n in x:
        #     y[n[0]] = n[1]
        #
        # return y

    def _extract_properties_uris(self):
        properties = []
        for s in self.G.subjects(predicate=RDF.type, object=RDF.Property):
            properties.append(str(s))

        for p in sorted(properties):
            self.PROPERTIES[p] = {}

    def _extract_properties(self):
        for prop in self.PROPERTIES.keys():
            s = URIRef(prop)
            # property type
            if (s, RDF.type, OWL.ObjectProperty) in self.G:
                self.PROPERTIES[prop]["prop_type"] = "op"
            elif (s, RDF.type, OWL.FunctionalProperty) in self.G:
                self.PROPERTIES[prop]["prop_type"] = "fp"
            elif (s, RDF.type, OWL.DatatypeProperty) in self.G:
                self.PROPERTIES[prop]["prop_type"] = "dp"
            elif (s, RDF.type, OWL.AnnotationProperty) in self.G:
                self.PROPERTIES[prop]["prop_type"] = "ap"
            else:
                self.PROPERTIES[prop]["prop_type"] = "p"

            self.PROPERTIES[prop]["title"] = None
            self.PROPERTIES[prop]["description"] = None
            self.PROPERTIES[prop]["scopeNote"] = None
            self.PROPERTIES[prop]["example"] = None
            self.PROPERTIES[prop]["isDefinedBy"] = None
            self.PROPERTIES[prop]["source"] = None
            self.PROPERTIES[prop]["supers"] = []
            self.PROPERTIES[prop]["subs"] = []
            self.PROPERTIES[prop]["equivs"] = []
            self.PROPERTIES[prop]["invs"] = []
            self.PROPERTIES[prop]["domains"] = []
            self.PROPERTIES[prop]["domainIncludes"] = []
            self.PROPERTIES[prop]["ranges"] = []
            self.PROPERTIES[prop]["rangeIncludes"] = []

            for p, o in self.G.predicate_objects(subject=s):
                if p == RDFS.label:
                    self.PROPERTIES[prop]["title"] = str(o)

                if p == RDFS.comment:
                    self.PROPERTIES[prop]["description"] = str(o)

                if p == SKOS.scopeNote:
                    self.PROPERTIES[prop]["scopeNote"] = str(o)

                if p == SKOS.example:
                    self.PROPERTIES[prop]["example"] = \
                        '<pre>' + str(o).replace("<", "&lt;").replace("\t", "    ").replace("\n", "<br />") + '</pre>'

                if p == RDFS.isDefinedBy:
                    self.PROPERTIES[prop]["isDefinedBy"] = str(o)

                if p == DCTERMS.source or p == DC.source:
                    if str(o).startswith('http'):
                        self.PROPERTIES[prop]["source"] = self._make_uri_html(o)  # '<a href="{0}">{0}</a>'.format(str(o))
                    else:
                        self.PROPERTIES[prop]["source"] = str(o)

            # patch title from URI if we haven't got one
            if self.PROPERTIES[prop]["title"] is None:
                self.PROPERTIES[prop]["title"] = self._make_title_from_uri(prop)

            # make fid
            self.PROPERTIES[prop]["fid"] = self._make_fid(
                self.PROPERTIES[prop]["title"], prop
            )

            # super properties
            for o in self.G.objects(subject=s, predicate=RDFS.subPropertyOf):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["supers"].append(str(o))  # self._make_uri_html

            # sub properties
            for o in self.G.subjects(predicate=RDFS.subPropertyOf, object=s):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["subs"].append(str(o))

            # equivalent properties
            for o in self.G.objects(subject=s, predicate=OWL.equivalentProperty):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["equivs"].append(str(o))

            # inverse properties
            for o in self.G.objects(subject=s, predicate=OWL.inverseOf):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["invs"].append(str(o))

            # domains
            for o in self.G.objects(subject=s, predicate=RDFS.domain):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["domains"].append(str(o))  # domains that are just classes
                else:
                    # domain collections (unionOf | intersectionOf
                    q = """
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> rdfs:domain ?domain .  
                            ?domain owl:unionOf|owl:intersectionOf ?collection .
                            ?domain ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    """.format(
                        s
                    )
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    self.PROPERTIES[prop]["domains"].append((collection_type, collection_members))

            # domainIncludes
            for o in self.G.objects(subject=s, predicate=SDO.domainIncludes):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["domainIncludes"].append(
                        str(o)
                    )  # domainIncludes that are just classes
                else:
                    # domainIncludes collections (unionOf | intersectionOf
                    q = """
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX sdo: <https://schema.org/>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> sdo:domainIncludes ?domainIncludes .  
                            ?domainIncludes owl:unionOf|owl:intersectionOf ?collection .
                            ?domainIncludes ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    """.format(
                        s
                    )
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    self.PROPERTIES[prop]["domainIncludes"].append((collection_type, collection_members))

            for o in self.G.objects(subject=s, predicate=self.SDO2.domainIncludes):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["domainIncludes"].append(
                        str(o)
                    )  # domainIncludes that are just classes
                else:
                    # domainIncludes collections (unionOf | intersectionOf
                    q = """
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX sdo2: <https://schema.org/>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> sdo2:domainIncludes ?domainIncludes .  
                            ?domainIncludes owl:unionOf|owl:intersectionOf ?collection .
                            ?domainIncludes ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    """.format(
                        s
                    )
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    self.PROPERTIES[prop]["domainIncludes"].append((collection_type, collection_members))

            # ranges
            for o in self.G.objects(subject=s, predicate=RDFS.range):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["ranges"].append(str(o))  # ranges that are just classes
                else:
                    # range collections (unionOf | intersectionOf
                    q = """
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> rdfs:range ?range .  
                            ?range owl:unionOf|owl:intersectionOf ?collection .
                            ?range ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    """.format(
                        s
                    )
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    self.PROPERTIES[prop]["ranges"].append((collection_type, collection_members))

            # rangeIncludes
            for o in self.G.objects(subject=s, predicate=SDO.rangeIncludes):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["rangeIncludes"].append(str(o))  # rangeIncludes that are just classes
                else:
                    # rangeIncludes collections (unionOf | intersectionOf
                    q = """
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX sdo: <https://schema.org/>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> sdo:rangeIncludes ?rangeIncludes .  
                            ?rangeIncludes owl:unionOf|owl:intersectionOf ?collection .
                            ?rangeIncludes ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    """.format(
                        s
                    )
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    self.PROPERTIES[prop]["rangeIncludes"].append((collection_type, collection_members))

            for o in self.G.objects(subject=s, predicate=self.SDO2.rangeIncludes):
                if type(o) != BNode:
                    self.PROPERTIES[prop]["rangeIncludes"].append(str(o))  # rangeIncludes that are just classes
                else:
                    # rangeIncludes collections (unionOf | intersectionOf
                    q = """
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX sdo2: <http://schema.org/>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> sdo2:rangeIncludes ?rangeIncludes .  
                            ?rangeIncludes owl:unionOf|owl:intersectionOf ?collection .
                            ?rangeIncludes ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    """.format(
                        s
                    )
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    self.PROPERTIES[prop]["rangeIncludes"].append((collection_type, collection_members))

            # TODO: cater for sub property chains

        # # sort properties by title
        # x = sorted([(k, v) for k, v in self.PROPERTIES.items()], key=lambda tup: tup[1]['title'])
        # y = collections.OrderedDict()
        # for n in x:
        #     y[n[0]] = n[1]
        #
        # return y

    def _extract_named_individuals_uris(self):
        named_individuals = []
        for s in self.G.subjects(predicate=RDF.type, object=OWL.NamedIndividual):
            named_individuals.append(str(s))

        for ni in sorted(named_individuals):
            self.NAMED_INDIVIDUALS[ni] = {}

    def _extract_named_individuals(self):
        for ni in self.NAMED_INDIVIDUALS.keys():
            if ni.startswith("http"):
                s = URIRef(ni)
            else:
                s = BNode(ni)
            # create Python dict for each NI
            self.NAMED_INDIVIDUALS[ni] = {}

            # basic NI properties
            self.NAMED_INDIVIDUALS[ni]["classes"] = set()
            self.NAMED_INDIVIDUALS[ni]["title"] = None
            self.NAMED_INDIVIDUALS[ni]["description"] = None
            self.NAMED_INDIVIDUALS[ni]["isDefinedBy"] = None
            self.NAMED_INDIVIDUALS[ni]["source"] = None
            self.NAMED_INDIVIDUALS[ni]["seeAlso"] = None
            self.NAMED_INDIVIDUALS[ni]["sameAs"] = None

            for p, o in self.G.predicate_objects(subject=s):
                # list all the other classes of this NI
                if p == RDF.type:
                    if o != OWL.NamedIndividual:
                        self.NAMED_INDIVIDUALS[ni]["classes"].add(self._make_uri_html(o))

                if p == RDFS.label:
                    self.NAMED_INDIVIDUALS[ni]["title"] = str(o)

                if p == RDFS.comment:
                    self.NAMED_INDIVIDUALS[ni]["description"] = str(o)

                if p == RDFS.isDefinedBy:
                    self.NAMED_INDIVIDUALS[ni]["isDefinedBy"] = str(o)

                if p == DCTERMS.source or p == DC.source:
                    if str(o).startswith('http'):
                        self.NAMED_INDIVIDUALS[ni]["source"] = self._make_uri_html(o)  # '<a href="{0}">{0}</a>'.format(str(o))
                    else:
                        self.NAMED_INDIVIDUALS[ni]["source"] = str(o)

                if p == RDFS.seeAlso:
                    self.NAMED_INDIVIDUALS[ni]["seeAlso"] = self._make_uri_html(o)

                if p == OWL.sameAs:
                    self.NAMED_INDIVIDUALS[ni]["sameAs"] = self._make_uri_html(o)

            # patch title from URI if we haven't got one
            if self.NAMED_INDIVIDUALS[ni].get("title") is None:
                self.NAMED_INDIVIDUALS[ni]["title"] = self._make_title_from_uri(ni)

            # make fid
            self.NAMED_INDIVIDUALS[ni]["fid"] = self._make_fid(self.NAMED_INDIVIDUALS[ni]["title"], ni)

    def _make_metadata(self, source_info, outputformat="html"):
        return self._load_template("owl_metadata." + outputformat).render(
            imports=self.METADATA["imports"],
            title=self.METADATA.get("title"),
            uri=self.METADATA.get("uri"),
            version_uri=self.METADATA.get("versionIRI"),
            publishers=self.METADATA["publishers"],
            creators=self.METADATA["creators"],
            contributors=self.METADATA["contributors"],
            created=self.METADATA.get("created"),  # TODO: auto-detect format
            modified=self.METADATA.get("modified"),
            issued=self.METADATA.get("issued"),
            source=self.METADATA.get("source"),
            description=self.METADATA.get("description"),
            historyNote=self.METADATA.get("historyNote"),
            version_info=self.METADATA.get("versionInfo"),
            license=self.METADATA.get("license"),
            rights=self.METADATA.get("rights"),
            repository=self.METADATA.get("repository"),
            ont_rdf=self._make_source_file_link(source_info),
            has_classes=self.METADATA.get("has_classes"),
            has_ops=self.METADATA.get("has_ops"),
            has_fps=self.METADATA.get("has_fps"),
            has_dps=self.METADATA.get("has_dps"),
            has_aps=self.METADATA.get("has_aps"),
            has_ps=self.METADATA.get("has_ps"),
            has_nis=self.METADATA.get("has_nis"),
        )

    def _make_classes(self, outputformat="html"):
        # make all Classes
        class_template = self._load_template("owl_class." + outputformat)
        classes_list = []
        for k, v in self.CLASSES.items():
            classes_list.append(
                class_template.render(
                    uri=k,
                    fid=v["fid"],
                    title=v["title"],
                    description=v["description"],
                    supers=v["supers"],
                    restrictions=v["restrictions"],
                    scopeNote=v["scopeNote"],
                    example=v["example"],
                    is_defined_by=v["isDefinedBy"],
                    source=v["source"],
                    subs=v["subs"],
                    in_domain_of=v["in_domain_of"],
                    in_domain_includes_of=v["in_domain_includes_of"],
                    in_range_of=v["in_range_of"],
                    in_range_includes_of=v["in_range_includes_of"],
                )
            )

        # make the template for all Classes
        classes_template = self._load_template("owl_classes." + outputformat)
        # add in Class index
        fids = sorted(
            [(v.get("fid"), v.get("title")) for k, v in self.CLASSES.items()],
            key=lambda tup: tup[1],
        )
        return classes_template.render(fids=fids, classes=classes_list, )

    def _make_property(self, property, outputformat="html"):
        return self._load_template("owl_property." + outputformat).render(
            uri=property[0],
            fid=property[1].get("fid"),
            property_type=property[1].get("prop_type"),
            title=property[1].get("title"),
            description=property[1].get("description"),
            scopeNote=property[1].get("scopeNote"),
            example=property[1].get("example"),
            is_defined_by=property[1].get("isDefinedBy"),
            source=property[1].get("source"),
            supers=property[1].get("supers"),
            subs=property[1].get("subs"),
            equivs=property[1].get("equivs"),
            invs=property[1].get("invs"),
            domains=property[1]["domains"],
            domainIncludes=property[1]["domainIncludes"],
            ranges=property[1]["ranges"],
            rangeIncludes=property[1]["rangeIncludes"],
        )

    def _make_properties(self, outputformat="html"):
        # make all properties, grouped by OWL type
        op_instances = []
        fp_instances = []
        dp_instances = []
        ap_instances = []
        p_instances = []

        for k, v in self.PROPERTIES.items():
            if v.get("prop_type") == "op":
                op_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v), outputformat=outputformat),
                    )
                )
            elif v.get("prop_type") == "fp":
                fp_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v), outputformat=outputformat),
                    )
                )
            elif v.get("prop_type") == "dp":
                dp_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v), outputformat=outputformat),
                    )
                )
            elif v.get("prop_type") == "ap":
                ap_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v), outputformat=outputformat),
                    )
                )
            elif v.get("prop_type") == "p":
                p_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v), outputformat=outputformat),
                    )
                )

        # make the template for all properties
        return self._load_template("owl_properties." + outputformat).render(
            op_instances=op_instances,
            fp_instances=fp_instances,
            dp_instances=dp_instances,
            ap_instances=ap_instances,
            p_instances=p_instances,
        )

    def _make_named_individual(self, named_individual, outputformat="html"):
        return self._load_template("owl_named_individual." + outputformat).render(
            uri=named_individual[0],
            fid=named_individual[1].get("fid"),
            classes=named_individual[1].get("classes"),
            title=named_individual[1].get("title"),
            description=named_individual[1].get("description"),
            is_defined_by=named_individual[1].get("isDefinedBy"),
            source=named_individual[1].get("source"),
            see_also=named_individual[1].get("seeAlso"),
            same_as=named_individual[1].get("sameAs")
        )

    def _make_named_individuals(self, outputformat="html"):
        # make all NIs
        named_individuals_list = []
        for k, v in self.NAMED_INDIVIDUALS.items():
            named_individuals_list.append(
                self._make_named_individual((k, v), outputformat=outputformat)
            )

        # add in NIs index
        fids = sorted(
            [(v.get("fid"), v.get("title")) for k, v in self.NAMED_INDIVIDUALS.items()],
            key=lambda tup: tup[1],
        )
        return self._load_template("owl_named_individuals." + outputformat).render(
            fids=fids,
            named_individuals=named_individuals_list
        )

    def _make_document_owl(
        self,
        title,
        metadata,
        classes,
        properties,
        named_individuals,
        default_namespace,
        namespaces,
        outputformat="html",
        exclude_css=False,
    ):
        css = None
        if outputformat == "html":
            if not exclude_css:
                pylode_css = path.join(
                    path.dirname(path.realpath(__file__)), "style", "pylode.css"
                )
                css = open(pylode_css).read()

        return self._load_template("owl_document." + outputformat).render(
            schemaorg=self._make_schemaorg_metadata(),  # only does something for the HTML templates
            title=title,
            metadata=metadata,
            classes=classes,
            properties=properties,
            named_individuals=named_individuals,
            default_namespace=default_namespace,
            namespaces=namespaces,
            css=css,
        )

    #
    #   SKOS
    #
    def _expand_graph_for_skos(self):
        # name
        for s, o in self.G.subject_objects(predicate=DC.title):
            self.G.add((s, SKOS.prefLabel, o))

        for s, o in self.G.subject_objects(predicate=RDFS.label):
            self.G.add((s, SKOS.prefLabel, o))

        for s, o in self.G.subject_objects(predicate=DCTERMS.title):
            self.G.add((s, SKOS.prefLabel, o))

        # description
        for s, o in self.G.subject_objects(predicate=DC.description):
            self.G.add((s, RDFS.comment, o))

        for s, o in self.G.subject_objects(predicate=DCTERMS.description):
            self.G.add((s, RDFS.comment, o))

        for s, o in self.G.subject_objects(predicate=SKOS.definition):
            self.G.add((s, RDFS.comment, o))

        # OWL -> SKOS
        # classes as Concepts types
        for s in self.G.subjects(predicate=RDF.type, object=RDFS.Class):
            self.G.add((s, RDF.type, SKOS.Concept))

        for s in self.G.subjects(predicate=RDF.type, object=OWL.Class):
            self.G.add((s, RDF.type, SKOS.Concept))

        # SKOS Concept Hierarchy from Class subsumption
        for s, o in self.G.subject_objects(predicate=RDFS.subClassOf):
            if type(o) != BNode:  # stops restrictions being seen as broader/narrower
                self.G.add((s, SKOS.broader, o))
                self.G.add((o, SKOS.narrower, s))

        for s, o in self.G.subject_objects(predicate=OWL.equivalentClass):
            self.G.add((s, SKOS.exactMatch, o))
            self.G.add((o, SKOS.exactMatch, s))

        # the ontology is now a ConceptScheme
        for s in self.G.subjects(predicate=RDF.type, object=OWL.Ontology):
            self.G.add((s, RDF.type, SKOS.ConceptScheme))

            # top concepts
            # if the class is declared here and has no subClassOf
            for s2 in self.G.subjects(predicate=RDF.type, object=SKOS.Concept):
                if (s2, RDFS.subClassOf, None) not in self.G:
                    self.G.add((s2, SKOS.topConceptOf, s))

        # SKOS -> SKOS
        # broader / narrower buildout
        for s, o in self.G.subject_objects(predicate=SKOS.broader):
            self.G.add((o, SKOS.narrower, s))

        for s, o in self.G.subject_objects(predicate=SKOS.narrower):
            self.G.add((o, SKOS.broader, s))

        for s, o in self.G.subject_objects(predicate=SKOS.topConceptOf):
            self.G.add((o, SKOS.hasTopConcept, s))

        for s, o in self.G.subject_objects(predicate=SKOS.hasTopConcept):
            self.G.add((o, SKOS.topConceptOf, s))

    def _extract_concept_scheme_for_skos(self):
        """Extracts standard SKOS ConceptScheme metadata

        Will interpret an owl:Ontology as a skos:ConceptScheme if run against an OWL document
        """

        self.METADATA["creators"] = set()
        self.METADATA["contributors"] = set()
        self.METADATA["publishers"] = set()
        for s in self.G.subjects(predicate=RDF.type, object=SKOS.ConceptScheme):
            self.METADATA["uri"] = str(s)
            for p, o in self.G.predicate_objects(subject=s):
                if p == SKOS.prefLabel:
                    self.METADATA["title"] = str(o)

                if p == SKOS.definition:
                    import markdown

                    self.METADATA["description"] = markdown.markdown(str(o))

                if p == SKOS.historyNote:
                    self.METADATA["historyNote"] = str(o)

                if p == DCTERMS.created:
                    self.METADATA["created"] = dateutil.parser.parse(str(o)).strftime(
                        "%Y-%m-%d"
                    )

                if p == DCTERMS.modified:
                    self.METADATA["modified"] = dateutil.parser.parse(str(o)).strftime(
                        "%Y-%m-%d"
                    )

                if p == DCTERMS.issued:
                    self.METADATA["issued"] = dateutil.parser.parse(str(o)).strftime(
                        "%Y-%m-%d"
                    )

                if p == DCTERMS.source:
                    if str(o).startswith('http'):
                        self.METADATA["source"] = self._make_uri_html(o)  # '<a href="{0}">{0}</a>'.format(str(o))
                    else:
                        self.METADATA["source"] = str(o)

                if p == OWL.versionIRI:
                    self.METADATA["versionIRI"] = '<a href="{0}">{0}</a>'.format(str(o))

                if p == OWL.versionInfo:
                    self.METADATA["versionInfo"] = str(o)

                if p == URIRef("http://purl.org/vocab/vann/preferredNamespacePrefix"):
                    self.METADATA["preferredNamespacePrefix"] = str(o)

                if p == URIRef("http://purl.org/vocab/vann/preferredNamespaceUri"):
                    self.METADATA["preferredNamespaceUri"] = str(o)

                if p == DCTERMS.license:
                    self.METADATA["license"] = (
                        '<a href="{0}">{0}</a>'.format(str(o))
                        if str(o).startswith("http")
                        else str(o)
                    )

                if p == DCTERMS.rights:
                    self.METADATA["rights"] = (
                        str(o)
                            .replace("Copyright", "&copy;")
                            .replace("copyright", "&copy;")
                    )

                # Agents
                if p == DC.creator:
                    if type(o) == URIRef:
                        self.METADATA["creators"].add(
                            '<a href="{0}">{0}</a>'.format(str(o))
                        )
                    else:
                        self.METADATA["creators"].add(str(o))

                if p == DCTERMS.creator:
                    if type(o) == Literal:
                        self.METADATA["creators"].add(str(o))
                    else:  # Blank Node or URI
                        self.METADATA["creators"].add(self._make_agent_html(o))

                if p == DC.contributor:
                    if type(o) == URIRef:
                        self.METADATA["contributors"].add(
                            '<a href="{0}">{0}</a>'.format(str(o))
                        )
                    else:
                        self.METADATA["contributors"].add(str(o))

                if p == DCTERMS.contributor:
                    if type(o) == Literal:
                        self.METADATA["contributors"].add(str(o))
                    else:  # Blank Node or URI
                        self.METADATA["contributors"].add(self._make_agent_html(o))

                if p == DC.publisher:
                    if type(o) == URIRef:
                        self.METADATA["publishers"].add(
                            '<a href="{0}">{0}</a>'.format(str(o))
                        )
                    else:
                        self.METADATA["publishers"].add(str(o))

                if p == DCTERMS.publisher:
                    if type(o) == Literal:
                        self.METADATA["publishers"].add(str(o))
                    else:  # Blank Node or URI
                        self.METADATA["publishers"].add(self._make_agent_html(o))

                # TODO: cater for other Agent representations

                if p == PROV.wasGeneratedBy:
                    for o2 in self.G.objects(subject=o, predicate=DOAP.repository):
                        self.METADATA["repository"] = str(o2)

                if p == SDO.codeRepository:
                    self.METADATA["repository"] = str(o)

        if self.METADATA.get("title") is None:
            raise ValueError(
                "Your taxonomy's ConceptScheme does not indicate any form of title. "
                "You must declare one of the following for it: rdfs:label, dct:title, skos:prefLabel"
            )

        if len(self.COLLECTIONS.keys()) > 0:
            self.METADATA["has_collections"] = True

        if len(self.CONCEPTS.keys()) > 0:
            self.METADATA["has_concepts"] = True

    def _extract_collections_for_skos(self):
        """Extracts standard SKOS Collection metadata"""
        collections = []
        # TODO: handle OrderedCollections
        for s in self.G.subjects(predicate=RDF.type, object=SKOS.Collection):
            collections.append(str(s))

        # keeping the OrderedDict ordered
        for c in sorted(collections):
            self.COLLECTIONS[c] = {}

        # fill in each Collection's details from the graph
        for c in self.COLLECTIONS.keys():
            s = URIRef(c)  # for use in Graph() loops

            self.COLLECTIONS[c]["fid"] = None
            self.COLLECTIONS[c]["prefLabels"] = set()
            self.COLLECTIONS[c]["altLabels"] = []
            self.COLLECTIONS[c]["definitions"] = []
            self.COLLECTIONS[c]["scopeNotes"] = []
            self.COLLECTIONS[c]["source"] = None

            self.COLLECTIONS[c]["members"] = []

            for p, o in self.G.predicate_objects(subject=s):
                if p == SKOS.prefLabel:
                    self.COLLECTIONS[c]["prefLabels"].add((o.value, 'en'))  # TODO: add in language

                elif p == SKOS.altLabel:
                    self.COLLECTIONS[c]["altLabels"].append(str(o))  # TODO: add in language

                elif p == SKOS.definition:
                    self.COLLECTIONS[c]["definitions"].append(str(o))  # TODO: add in language

                elif p == SKOS.scopeNote:
                    self.COLLECTIONS[c]["scopeNotes"].append(str(o))  # TODO: add in language

                elif p == DCTERMS.source:
                    self.COLLECTIONS[c]["source"] = str(o)

                elif p == SKOS.topConceptOf:
                    self.COLLECTIONS[c]["topConceptOfs"].append(str(o))

                elif p == SKOS.member:
                    self.COLLECTIONS[c]["members"].append(self._make_uri_html(str(o), type="cp"))
                    # TODO: handle members that are other Collections, not Concepts

            self.COLLECTIONS[c]["prefLabels"] = list(self.COLLECTIONS[c]["prefLabels"])
            self.COLLECTIONS[c]["members"] = list(self.COLLECTIONS[c]["members"])

            # make fid
            # TODO: update to use default language label, not [0]
            self.COLLECTIONS[c]["fid"] = self._make_fid(
                self.COLLECTIONS[c]["prefLabels"][0][0], c
            )

    def _extract_concepts_for_skos(self):
        """Extracts standard SKOS Concepts and their metadata

        Will interpret an owl:Class and rdfs:Class instances as skos:Concepts if run against an OWL document
        """
        concepts = []
        for s in self.G.subjects(predicate=RDF.type, object=SKOS.Concept):
            concepts.append(str(s))

        # keeping the OrderedDict ordered
        for c in sorted(concepts):
            self.CONCEPTS[c] = {}

        # fill in each Concept's details from the graph
        for c in self.CONCEPTS.keys():
            s = URIRef(c)  # for use in Graph() loops

            self.CONCEPTS[c]["fid"] = None
            self.CONCEPTS[c]["prefLabels"] = set()
            self.CONCEPTS[c]["default_prefLabel"] = None
            self.CONCEPTS[c]["altLabels"] = set()
            self.CONCEPTS[c]["definitions"] = set()
            self.CONCEPTS[c]["scopeNotes"] = set()
            self.CONCEPTS[c]["examples"] = set()
            self.CONCEPTS[c]["inSchemes"] = set()
            self.CONCEPTS[c]["topConceptOfs"] = set()
            self.CONCEPTS[c]["source"] = None
            self.CONCEPTS[c]["broaders"] = set()
            self.CONCEPTS[c]["narrowers"] = set()
            self.CONCEPTS[c]["exactMatches"] = set()
            self.CONCEPTS[c]["closeMatches"] = set()
            self.CONCEPTS[c]["broadMatches"] = set()
            self.CONCEPTS[c]["narrowMatches"] = set()

            for p, o in self.G.predicate_objects(subject=s):
                if p == SKOS.prefLabel:
                    self.CONCEPTS[c]["prefLabels"].add((o.value, o.language))  # TODO: add in language
                    if o.language == self.default_language:
                        self.CONCEPTS[c]["default_prefLabel"] = o.value

                elif p == SKOS.altLabel:
                    self.CONCEPTS[c]["altLabels"].add(str(o))  # TODO: add in language

                elif p == SKOS.definition:
                    self.CONCEPTS[c]["definitions"].add(str(o))  # TODO: add in language

                elif p == SKOS.scopeNote:
                    self.CONCEPTS[c]["scopeNotes"].add(str(o))  # TODO: add in language

                elif p == SKOS.example:
                    self.CONCEPTS[c]["examples"].add(str(o))  # TODO: add in language

                elif p == SKOS.inScheme:
                    self.CONCEPTS[c]["inSchemes"].add(str(o))

                elif p == DCTERMS.source:
                    self.CONCEPTS[c]["source"] = str(o)

                elif p == SKOS.topConceptOf:
                    self.CONCEPTS[c]["topConceptOfs"].add(str(o))

                elif p == SKOS.broader:
                    self.CONCEPTS[c]["broaders"].add(str(o))

                elif p == SKOS.narrower:
                    self.CONCEPTS[c]["narrowers"].add(str(o))

                elif p == SKOS.exactMatch:
                    self.CONCEPTS[c]["exactMatches"].add(str(o))

                elif p == SKOS.closeMatch:
                    self.CONCEPTS[c]["closeMatches"].add(str(o))

                elif p == SKOS.broadMatch:
                    self.CONCEPTS[c]["broadMatches"].add(str(o))

                elif p == SKOS.narrowMatch:
                    self.CONCEPTS[c]["narrowMatches"].add(str(o))

            # listify the sets
            self.CONCEPTS[c]["prefLabels"] = list(self.CONCEPTS[c]["prefLabels"])
            self.CONCEPTS[c]["altLabels"] = list(self.CONCEPTS[c]["altLabels"])
            self.CONCEPTS[c]["definitions"] = list(self.CONCEPTS[c]["definitions"])
            self.CONCEPTS[c]["scopeNotes"] = list(self.CONCEPTS[c]["scopeNotes"])
            self.CONCEPTS[c]["examples"] = list(self.CONCEPTS[c]["examples"])
            self.CONCEPTS[c]["inSchemes"] = list(self.CONCEPTS[c]["inSchemes"])
            self.CONCEPTS[c]["topConceptOfs"] = list(self.CONCEPTS[c]["topConceptOfs"])
            self.CONCEPTS[c]["broaders"] = list(self.CONCEPTS[c]["broaders"])
            self.CONCEPTS[c]["narrowers"] = list(self.CONCEPTS[c]["narrowers"])
            self.CONCEPTS[c]["exactMatches"] = list(self.CONCEPTS[c]["exactMatches"])
            self.CONCEPTS[c]["closeMatches"] = list(self.CONCEPTS[c]["closeMatches"])
            self.CONCEPTS[c]["broadMatches"] = list(self.CONCEPTS[c]["broadMatches"])
            self.CONCEPTS[c]["narrowMatches"] = list(self.CONCEPTS[c]["narrowMatches"])

            # make fid
            # TODO: update to use default language label, not [0]
            self.CONCEPTS[c]["fid"] = self._make_fid(
                self.CONCEPTS[c]["default_prefLabel"], c
            )

    def _make_uri_html(self, uri, type=None):
        # set display to CURIE
        short = self._get_curie(uri)
        # if the URI base is within the default namespace of this ontology
        #   use the fragment URI
        # else
        #   use the given URI
        uri_base = self._get_namespace_from_uri(uri)
        if uri_base == self.METADATA.get("default_namespace"):
            if self.profile_selected == "owl":
                if self.PROPERTIES.get(uri):
                    html = '<a href="#{}">{}</a>'.format(self.PROPERTIES[uri]["fid"], short)
                elif self.CLASSES.get(uri):
                    html = '<a href="#{}">{}</a>'.format(self.CLASSES[uri]["fid"], short)
                else:
                    html = '<a href="{}">{}</a>'.format(uri, short)
            elif self.profile_selected == "skos":
                if self.CONCEPTS.get(uri):
                    html = '<a href="#{}">{}</a>'.format(self.CONCEPTS[uri]["fid"], self.CONCEPTS[uri]["default_prefLabel"])
                elif self.COLLECTIONS.get(uri):
                    html = '<a href="#{}">{}</a>'.format(self.COLLECTIONS[uri]["fid"], short)
                else:
                    html = '<a href="{}">{}</a>'.format(uri, short)
            else:
                html = '<a href="{}">{}</a>'.format(uri, short)
        else:
            html = '<a href="{}">{}</a>'.format(uri, short)

        # OWL
        if type == "c":
            return html + '<sup class="sup-c" title="class">c</sup>'
        elif type == "op":
            return html + '<sup class="sup-op" title="object property">op</sup>'
        elif type == "fp":
            return html + '<sup class="sup-fp" title="functional property">fp</sup>'
        elif type == "dp":
            return html + '<sup class="sup-dp" title="datatype property">dp</sup>'
        elif type == "ap":
            return html + '<sup class="sup-ap" title="annotation property">ap</sup>'
        elif type == "ni":
            return html + '<sup class="sup-ni" title="named individual">ni</sup>'
        # SKOS
        elif type == "cp":
            return html + '<sup class="sup-cp" title="concept">cp</sup>'
        elif type == "cl":
            return html + '<sup class="sup-cl" title="collection">cl</sup>'
        # None
        else:
            return html

    def _make_collection_class_html(self, col_type, col_members):
        if col_type == "owl:unionOf":
            j = " or "
        elif col_type == "owl:intersectionOf":
            j = " and "
        else:
            j = " ? "
        # others...
        return "({})".format(
            j.join([self._make_uri_html(x, type="c") for x in col_members])
        )

    def _make_restriction_html(self, subject, restriction_bn):
        prop = None
        card = None
        cls = None

        for p2, o2 in self.G.predicate_objects(subject=restriction_bn):
            if p2 != RDF.type:
                if p2 == OWL.onProperty:
                    # TODO: add the property type for HTML
                    t = None
                    if str(o2) in self.PROPERTIES.keys():
                        t = self.PROPERTIES[str(o2)]["prop_type"]
                    prop = self._make_uri_html(str(o2), t)
                elif p2 == OWL.onClass:
                    """
                    domains = []
                    for o in self.G.objects(subject=s, predicate=RDFS.domain):
                        if type(o) != BNode:
                            domains.append(str(o))  # domains that are just classes
                        else:
                            # domain collections (unionOf | intersectionOf
                            q = '''
                                PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
            
                                SELECT ?col_type ?col_member
                                WHERE {{
                                    <{}> rdfs:domain ?domain .  
                                    ?domain owl:unionOf|owl:intersectionOf ?collection .
                                    ?domain ?col_type ?collection . 
                                    ?collection rdf:rest*/rdf:first ?col_member .              
                                }} 
                            '''.format(s)
                            collection_type = None
                            collection_members = []
                            for r in self.G.query(q):
                                collection_type = self._get_curie(str(r.col_type))
                                collection_members.append(str(r.col_member))
                            domains.append((collection_type, collection_members))
                    self.PROPERTIES[prop]['domains'] = domains                
                    
                    """
                    if type(o2) == BNode:
                        # onClass collections (unionOf | intersectionOf
                        q = """
                            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
                            SELECT ?col_type ?col_member
                            WHERE {{
                                <{}> owl:onClass ?onClass .  
                                ?onClass owl:unionOf|owl:intersectionOf ?collection .
                                ?onClass ?col_type ?collection . 
                                ?collection rdf:rest*/rdf:first ?col_member .              
                            }} 
                        """.format(
                            str(subject)
                        )
                        collection_type = None
                        collection_members = []
                        for r in self.G.query(q):
                            collection_type = self._get_curie(str(r.col_type))
                            collection_members.append(str(r.col_member))

                        cls = self._make_collection_class_html(
                            collection_type, collection_members
                        )
                    else:
                        cls = self._make_uri_html(str(o2), type="c")
                elif p2 in [
                    OWL.cardinality,
                    OWL.qualifiedCardinality,
                    OWL.minCardinality,
                    OWL.minQualifiedCardinality,
                    OWL.maxCardinality,
                    OWL.maxQualifiedCardinality,
                ]:
                    if p2 in [OWL.minCardinality, OWL.minQualifiedCardinality]:
                        card = "min"
                    elif p2 in [OWL.maxCardinality, OWL.maxQualifiedCardinality]:
                        card = "max"
                    elif p2 in [OWL.cardinality, OWL.qualifiedCardinality]:
                        card = "exactly"

                    card = '<span class="cardinality">{}</span> {}'.format(
                        card, str(o2)
                    )
                elif p2 in [OWL.allValuesFrom, OWL.someValuesFrom]:
                    if p2 == OWL.allValuesFrom:
                        card = "only"
                    else:  # p2 == OWL.someValuesFrom
                        card = "some"

                    if type(o2) == BNode:
                        # someValuesFrom collections (unionOf | intersectionOf
                        q = """
                            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
                            SELECT ?col_type ?col_member
                            WHERE {{
                                <{0}> ?x _:{1} .
                                _:{1} owl:someValuesFrom|owl:allValuesFrom ?bn2 .
                                ?bn2 owl:unionOf|owl:intersectionOf ?collection .
                                ?s ?col_type ?collection . 
                                ?collection rdf:rest*/rdf:first ?col_member .              
                            }} 
                        """.format(
                            str(subject), str(o2)
                        )
                        collection_type = None
                        collection_members = []
                        for r in self.G.query(q):
                            collection_type = self._get_curie(str(r.col_type))
                            collection_members.append(str(r.col_member))

                        c = self._make_collection_class_html(
                            collection_type, collection_members
                        )
                    else:
                        c = self._make_uri_html(str(o2), type="c")
                    card = '<span class="cardinality">{}</span> {}'.format(card, c)
                elif p2 == OWL.hasValue:
                    card = '<span class="cardinality">value</span> {}'.format(
                        self._make_uri_html(str(o2), type="c")
                    )

        restriction = prop + " " + card if card is not None else prop
        restriction = restriction + " " + cls if cls is not None else restriction

        return restriction

    def _make_agent_html(self, agent_node):
        # we understand foaf:name, foaf:homepage & sdo:name & sdo:identifier & sdo:email (as a URI)
        # TODO: cater for other Agent representations

        name = None
        url = None
        email = None
        org_name = None
        org_url = None
        org_email = None
        for p, o in self.G.predicate_objects(subject=agent_node):
            if (
                p == FOAF.homepage
                or p == SDO.identifier
                or p == self.SDO2.identifier
            ):
                url = str(o)
            elif p == FOAF.name or p == SDO.name or p == self.SDO2.name:
                name = str(o)
            elif p == FOAF.mbox or p == SDO.email or p == self.SDO2.email:
                email = (
                    str(o).split("/")[-1].split("#")[-1]
                )  # remove base URI leaving only email address
            elif (
                p == SDO.memberOf
                or p == self.SDO2.memberOf
                or p == SDO.affiliation
                or p == self.SDO2.affiliation
            ):
                for p2, o2 in self.G.predicate_objects(subject=o):
                    if (
                        p2 == FOAF.homepage
                        or p2 == SDO.identifier
                        or p2 == self.SDO2.identifier
                        or p2 == SDO.url
                        or p2 == self.SDO2.url
                    ):  # TODO: split homepage form IDs, cater for rdfs:seeAlso
                        org_url = str(o2)
                    elif p2 == FOAF.name or p2 == SDO.name or p2 == self.SDO2.name:
                        org_name = str(o2)
                    elif p == FOAF.mbox or p == SDO.email or p == self.SDO2.email:
                        org_email = (
                            str(o2).split("/")[-1].split("#")[-1]
                        )  # remove base URI leaving only email address

        agent = self._make_agent_link(name, url=url, email=email)

        if org_name is not None:
            org = self._make_agent_link(org_name, url=org_url, email=org_email)
            agent += " of " + org

        return agent

    def _make_skos_concept_scheme(self, source_info, outputformat="html"):
        return self._load_template("skos_concept_scheme." + outputformat).render(
            title=self.METADATA.get("title"),
            uri=self.METADATA.get("uri"),
            version_uri=self.METADATA.get("versionIRI"),
            publishers=self.METADATA["publishers"],
            creators=self.METADATA["creators"],
            contributors=self.METADATA["contributors"],
            created=self.METADATA.get("created"),
            modified=self.METADATA.get("modified"),
            issued=self.METADATA.get("issued"),
            source=self.METADATA.get("source"),
            description=self.METADATA.get("description"),
            historyNote=self.METADATA.get("historyNote"),
            version_info=self.METADATA.get("versionInfo"),
            license=self.METADATA.get("license"),
            rights=self.METADATA.get("rights"),
            repository=self.METADATA.get("repository"),
            ont_rdf=self._make_source_file_link(source_info),
            has_collections=True if len(self.COLLECTIONS) > 0 else False,
            has_concepts=True if len(self.CONCEPTS) > 0 else False,
        )

    def _make_skos_collection(self, collection, outputformat="html"):
        return self._load_template("skos_collection." + outputformat).render(
            uri=collection[0],
            fid=collection[1].get("fid"),
            prefLabels=collection[1].get("prefLabels"),
            altLabels=collection[1].get("altLabels"),
            definitions=collection[1].get("definitions"),
            scopeNotes=collection[1].get("scopeNotes"),
            source=collection[1].get("source"),
            members=[self._make_uri_html(x, type="cp") for x in collection[1].get("members")],
        )

    def _make_skos_collections(self, outputformat="html"):
        collections = []
        for k, v in self.COLLECTIONS.items():
            collections.append(
                (
                    list(v["prefLabels"])[0][0],
                    v["fid"],
                    self._make_skos_collection((k, v), outputformat=outputformat),
                )
            )

        return self._load_template("skos_collections." + outputformat).render(collections=collections)

    # def _make_concept_hierarchy(self):
    #     # same as parent query, only:
    #     #   running against rdflib in-memory graph, not SPARQL endpoint
    #     #   a single graph, not a multi-graph (since it's an RDF/XML or Turtle file)
    #     """
    #     Function to draw concept hierarchy for vocabulary
    #     """
    #
    #     def build_hierarchy(bindings_list, broader_concept=None, level=0):
    #         """
    #         Recursive helper function to build hierarchy list from a bindings list
    #         Returns list of tuples: (<level>, <concept>, <concept_preflabel>, <broader_concept>)
    #         """
    #         level += 1  # Start with level 1 for top concepts
    #         hierarchy = []
    #
    #         narrower_list = sorted(
    #             [
    #                 binding_dict
    #                 for binding_dict in bindings_list
    #                 if
    #                 # Top concept
    #                 (
    #                     (broader_concept is None)
    #                     and (binding_dict.get("broader_concept") is None)
    #                 )
    #                 or
    #                 # Narrower concept
    #                 (
    #                     (binding_dict.get("broader_concept") is not None)
    #                     and (binding_dict["broader_concept"] == broader_concept)
    #                 )
    #             ],
    #             key=lambda binding_dict: binding_dict["concept_preflabel"],
    #         )
    #
    #         for binding_dict in narrower_list:
    #             concept = binding_dict["concept"]
    #             hierarchy += [
    #                 (
    #                     level,
    #                     concept,
    #                     binding_dict["concept_preflabel"],
    #                     binding_dict["broader_concept"]
    #                     if binding_dict.get("broader_concept")
    #                     else None,
    #                 )
    #             ] + build_hierarchy(bindings_list, concept, level)
    #
    #         return hierarchy
    #
    #     q = """
    #         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    #         PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    #         PREFIX dct: <http://purl.org/dc/terms/>
    #         SELECT DISTINCT ?concept ?concept_preflabel ?broader_concept
    #         WHERE {{
    #             {{ ?concept skos:inScheme ?cs . }}
    #             UNION
    #             {{ ?concept skos:topConceptOf ?cs . }}
    #             UNION
    #             {{ ?cs skos:hasTopConcept ?concept . }}
    #             ?concept skos:prefLabel ?concept_preflabel .
    #             OPTIONAL {{ ?concept skos:broader ?broader_concept .
    #                 ?broader_concept skos:inScheme ?cs .
    #                 }}
    #             FILTER(lang(?concept_preflabel) = "{language}" || lang(?concept_preflabel) = "")
    #         }}
    #         ORDER BY ?concept_preflabel""".format(
    #         language='en'
    #     )
    #
    #     bindings_list = []
    #     for r in self.G.query(q):
    #         bindings_list.append(
    #             {
    #                 # ?concept ?concept_preflabel ?broader_concept
    #                 "concept": r[0],
    #                 "concept_preflabel": r[1],
    #                 "broader_concept": r[2],
    #             }
    #         )
    #
    #     assert bindings_list is not None, "FILE concept hierarchy query failed"
    #
    #     hierarchy = build_hierarchy(bindings_list)
    #
    #     return self._draw_concept_hierarchy(hierarchy)
    #
    # def _draw_concept_hierarchy(self, hierarchy):
    #     tab = "\t"
    #     previous_length = 1
    #
    #     text = ""
    #     tracked_items = []
    #     for item in hierarchy:
    #         mult = None
    #
    #         if item[0] > previous_length + 2:  # SPARQL query error on length value
    #             for tracked_item in tracked_items:
    #                 if tracked_item["name"] == item[3]:
    #                     mult = tracked_item["indent"] + 1
    #
    #         if mult is None:
    #             found = False
    #             for tracked_item in tracked_items:
    #                 if tracked_item["name"] == item[3]:
    #                     found = True
    #             if not found:
    #                 mult = 0
    #
    #         if mult is None:  # else: # everything is normal
    #             mult = item[0] - 1
    #
    #         uri = item[1]
    #
    #         t = tab * mult + "* [" + item[2] + "](" + uri + ")\n"
    #         text += t
    #         previous_length = mult
    #         tracked_items.append({"name": item[1], "indent": mult})
    #
    #     return markdown.markdown(text)
    #
    # def render_concept_tree(html_doc):
    #     soup = BeautifulSoup(html_doc, "html.parser")
    #
    #     # concept_hierarchy = soup.find(id='concept-hierarchy')
    #
    #     uls = soup.find_all("ul")
    #
    #     for i, ul in enumerate(uls):
    #         # Don't add HTML class nested to the first 'ul' found.
    #         if not i == 0:
    #             ul["class"] = "nested"
    #             if ul.parent.name == "li":
    #                 temp = BeautifulSoup(str(ul.parent.a.extract()), "html.parser")
    #                 ul.parent.insert(
    #                     0, BeautifulSoup('<span class="caret">', "html.parser")
    #                 )
    #                 ul.parent.span.insert(0, temp)
    #     return soup

    def _make_concept_hierarchy(self, outputformat="html"):
        # render concept
        def _render(c, children, level=0):
            if outputformat == "md":
                md = level*"\t" + "* [{}]({})".format(self.CONCEPTS.get(c).get("default_prefLabel"), c)
                if len(children) > 0:
                    for ch in sorted(children):
                        md += "\n" + _render(ch, self.CONCEPTS.get(ch).get("narrowers"), level=level + 1)
                return md
            else:  # HTML
                html = "<li>{}".format(self._make_uri_html(c))
                if len(children) > 0:
                    for ch in sorted(children):
                        html += "\n<ul>" + _render(ch, self.CONCEPTS.get(ch).get("narrowers"), level=level + 1) + "</ul>"
                html += "</li>"
                return html

        # start with a topConcept
        tcs = []
        for s, o in self.G.subject_objects(predicate=SKOS.hasTopConcept):
            tcs.append(str(o))

        txt = ""
        for tc in sorted(tcs):
            txt += _render(tc, self.CONCEPTS.get(tc).get("narrowers"), 0)

        return "<ul class=\"hierarchy\">\n" + txt + "\n</ul>"

    def _make_skos_concept(self, concept, outputformat="html"):
        return self._load_template("skos_concept." + outputformat).render(
            uri=concept[0],
            fid=concept[1].get("fid"),
            default_prefLabel=concept[1].get("default_prefLabel"),
            prefLabels=concept[1].get("prefLabels"),
            altLabels=concept[1].get("altLabels"),
            definitions=concept[1].get("definitions"),
            scopeNotes=concept[1].get("scopeNotes"),
            examples=concept[1].get("examples"),
            source=concept[1].get("source"),
            broaders=[self._make_uri_html(x, type="cp") for x in concept[1].get("broaders")],
            narrowers=[self._make_uri_html(x, type="cp") for x in concept[1].get("narrowers")],
            exactMatches=[self._make_uri_html(x, type="cp") for x in concept[1].get("exactMatches")],
            closeMatches=[self._make_uri_html(x, type="cp") for x in concept[1].get("closeMatches")],
            broadMatches=[self._make_uri_html(x, type="cp") for x in concept[1].get("broadMatches")],
            narrowMatches=[self._make_uri_html(x, type="cp") for x in concept[1].get("narrowMatches")],
        )

    def _make_skos_concepts(self, outputformat="html"):
        # TODO: make Concept hierarchy (URIs)

        # TODO: list all Concepts, alphabetically by prefLabel
        concepts = []
        for k, v in self.CONCEPTS.items():
            concepts.append(
                (
                    v["default_prefLabel"],
                    v["fid"],
                    self._make_skos_concept((k, v), outputformat=outputformat),
                )
            )

        return self._load_template("skos_concepts." + outputformat).render(
            concept_hierarchy=self._make_concept_hierarchy(),
            concepts=concepts
        )

    def _make_document_skos(
            self,
            title,
            outputformat="html",
            exclude_css=False,
    ):
        css = None
        if outputformat == "html":
            if not exclude_css:
                pylode_css = path.join(
                    path.dirname(path.realpath(__file__)), "style", "pylode.css"
                )
                css = open(pylode_css).read()

        return self._load_template("skos_taxonomy." + outputformat).render(
            schemaorg=self._make_schemaorg_metadata(),  # only does something for the HTML template
            title=title,
            concept_scheme=self._make_skos_concept_scheme(self.source_info, outputformat=outputformat),
            has_collections=True if len(self.COLLECTIONS) > 0 else False,
            collections=self._make_skos_collections(outputformat=outputformat),
            has_concepts=True if len(self.CONCEPTS) > 0 else False,
            concepts=self._make_skos_concepts(outputformat=outputformat),
            namespaces=self._make_namespaces(outputformat=outputformat),
            css=css
        )

    def document(self, exclude_css=False):
        if self.profile_selected == "skos":
            # expand the graph using pre-defined rules to make querying easier (poor man's inference)
            self._expand_graph_for_skos()
            # get all the namespaces using several methods
            self._extract_namespaces()
            # get the default namespace
            self._get_default_namespace()
            # extract all the SKOS things
            self._extract_collections_for_skos()
            self._extract_concepts_for_skos()
            self._make_concept_hierarchy()
            self._extract_concept_scheme_for_skos()

            return self._make_document_skos(
                self.METADATA["title"],
                outputformat=self.outputformat,
                exclude_css=exclude_css,
            )
        else:
            # expand the graph using pre-defined rules to make querying easier (poor man's inference)
            self._expand_graph_for_owl()
            # get all the namespaces using several methods
            self._extract_namespaces()
            # get the default namespace
            self._get_default_namespace()
            # get the IDs (URIs) of all properties -> self.PROPERTIES
            self._extract_properties_uris()
            # get the IDs (URIs) of all classes -> CLASSES
            self._extract_classes_uris()
            # get the IDs (URIs) of all Named Individuals -> NAMED_INDIVIDUALS
            self._extract_named_individuals_uris()
            # get all the properties' details
            self._extract_properties()
            # get all the classes' details
            self._extract_classes()
            # get all the Named Individuals' details
            self._extract_named_individuals()
            # get the ontology's metadata
            self._extract_metadata_for_owl()
            # create fragment URIs for default namespace classes & properties
            # for each CURIE, if it's in the default namespace, i.e. this ontology, use its fragment URI

            # crosslinking properties
            for uri, prop in self.PROPERTIES.items():
                html = []
                for p in prop["supers"]:
                    prop_type = (
                        self.PROPERTIES.get(p).get("prop_type")
                        if self.PROPERTIES.get(p)
                        else None
                    )
                    html.append(self._make_uri_html(p, type=prop_type))
                self.PROPERTIES[uri]["supers"] = html

                html = []
                for p in prop["subs"]:
                    prop_type = (
                        self.PROPERTIES.get(p).get("prop_type")
                        if self.PROPERTIES.get(p)
                        else None
                    )
                    html.append(self._make_uri_html(p, type=prop_type))
                self.PROPERTIES[uri]["subs"] = html

                html = []
                for p in prop["equivs"]:
                    prop_type = (
                        self.PROPERTIES.get(p).get("prop_type")
                        if self.PROPERTIES.get(p)
                        else None
                    )
                    html.append(self._make_uri_html(p, type=prop_type))
                self.PROPERTIES[uri]["equivs"] = html

                html = []
                for p in prop["invs"]:
                    prop_type = (
                        self.PROPERTIES.get(p).get("prop_type")
                        if self.PROPERTIES.get(p)
                        else None
                    )
                    html.append(self._make_uri_html(p, type=prop_type))
                self.PROPERTIES[uri]["invs"] = html

                html = []
                for d in prop["domains"]:
                    if type(d) == tuple:
                        html.append(self._make_collection_class_html(d[0], d[1]))
                    else:
                        html.append(self._make_uri_html(d, type="c"))
                self.PROPERTIES[uri]["domains"] = html

                html = []
                for d in prop["domainIncludes"]:
                    if type(d) == tuple:
                        for m in d[1]:
                            html.append(self._make_uri_html(m, type="c"))
                    else:
                        html.append(self._make_uri_html(d, type="c"))
                self.PROPERTIES[uri]["domainIncludes"] = html

                html = []
                for d in prop["ranges"]:
                    if type(d) == tuple:
                        for m in d[1]:
                            html.append(self._make_uri_html(m, type="c"))
                    else:
                        html.append(self._make_uri_html(d, type="c"))
                self.PROPERTIES[uri]["ranges"] = html

                html = []
                for d in prop["rangeIncludes"]:
                    if type(d) == tuple:
                        for m in d[1]:
                            html.append(self._make_uri_html(m, type="c"))
                    else:
                        html.append(self._make_uri_html(d, type="c"))
                self.PROPERTIES[uri]["rangeIncludes"] = html

            # crosslinking classes
            for uri, cls in self.CLASSES.items():
                html = []
                for d in cls["equivalents"]:
                    if type(d) == tuple:
                        for m in d[1]:
                            html.append(self._make_uri_html(m, type="c"))
                    else:
                        html.append(self._make_uri_html(d, type="c"))
                self.CLASSES[uri]["equivalents"] = html

                html = []
                for d in cls["supers"]:
                    if type(d) == tuple:
                        html.append(self._make_collection_class_html(d[0], d[1]))
                    else:
                        html.append(self._make_uri_html(d, type="c"))
                self.CLASSES[uri]["supers"] = html

                html = []
                for d in cls["restrictions"]:
                    html.append(self._make_restriction_html(uri, d))
                self.CLASSES[uri]["restrictions"] = html

                html = []
                for d in cls["subs"]:
                    if type(d) == tuple:
                        for m in d[1]:
                            html.append(self._make_uri_html(m, type="c"))
                    else:
                        html.append(self._make_uri_html(d, type="c"))
                self.CLASSES[uri]["subs"] = html

                html = []
                for p in cls["in_domain_of"]:
                    prop_type = (
                        self.PROPERTIES.get(p).get("prop_type")
                        if self.PROPERTIES.get(p)
                        else None
                    )
                    html.append(self._make_uri_html(p, type=prop_type))
                self.CLASSES[uri]["in_domain_of"] = html

                html = []
                for p in cls["in_domain_includes_of"]:
                    prop_type = (
                        self.PROPERTIES.get(p).get("prop_type")
                        if self.PROPERTIES.get(p)
                        else None
                    )
                    html.append(self._make_uri_html(p, type=prop_type))
                self.CLASSES[uri]["in_domain_includes_of"] = html

                html = []
                for p in cls["in_range_of"]:
                    prop_type = (
                        self.PROPERTIES.get(p).get("prop_type")
                        if self.PROPERTIES.get(p)
                        else None
                    )
                    html.append(self._make_uri_html(p, type=prop_type))
                self.CLASSES[uri]["in_range_of"] = html

                html = []
                for p in cls["in_range_includes_of"]:
                    prop_type = (
                        self.PROPERTIES.get(p).get("prop_type")
                        if self.PROPERTIES.get(p)
                        else None
                    )
                    html.append(self._make_uri_html(p, type=prop_type))
                self.CLASSES[uri]["in_range_includes_of"] = html

            elements = {
                "metadata": self._make_metadata(self.source_info, outputformat=self.outputformat),
                "classes": self._make_classes(outputformat=self.outputformat),
                "properties": self._make_properties(outputformat=self.outputformat),
                "named_individuals": self._make_named_individuals(outputformat=self.outputformat),
                "default_namespace": self.METADATA["default_namespace"],
                "namespaces": self._make_namespaces(outputformat=self.outputformat)
            }

            return self._make_document_owl(
                self.METADATA["title"],
                **elements,
                outputformat=self.outputformat,
                exclude_css=exclude_css,
            )


if __name__ == "__main__":
    m = MakeDocco(input_data_file="examples/agrif.ttl")

    with open("examples/agrif.html", "w") as f:
        f.write(m.document())
