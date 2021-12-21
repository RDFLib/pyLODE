import collections
from itertools import chain
from jinja2 import Environment, FileSystemLoader
from rdflib import SDO, SKOS, OWL, URIRef, RDF, PROF, Literal, XSD, Graph, Namespace, FOAF, Graph

from pylode.common import TEMPLATES_DIR


class BaseProfile:
    def __init__(
            self,
            g,
            source_info,
            outputformat="html",
            include_css=False,
            default_language="en",
            use_curies_stored=True,
            get_curies_online=False):
        self.outputformat = outputformat
        self.include_css = include_css
        self.default_language = default_language
        self.use_curies_stored = use_curies_stored
        self.get_curies_online = get_curies_online
        self.default_namespace = None
        self.G = self._filter_graph_by_language(g, default_language)
        self.source_info = source_info
        self.G.bind("sdo", SDO)
        self.G.bind("skos", SKOS)
        self.NAMESPACES = collections.OrderedDict()
        self.FIDS = {}
        self.METADATA = {}

    def _filter_graph_by_language(self, g, language):
        filtered = Graph()

        for s, p, o in g:
            if not type(o) is Literal or not o.language or o.language == language:
                filtered.add((s, p, o))

        for k, v in g.namespaces():
            filtered.bind(k, v)

        return filtered

    def _load_template(self, template_file):
        return Environment(loader=FileSystemLoader(TEMPLATES_DIR)).get_template(template_file)

    def _expand_graph(self):
        """Abstract method"""

    # TODO: replace this with rdflib native method
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

    def _get_uri_id(self, uri):
        # split on hash
        segments = uri.split("#")
        if len(segments) == 2:
            return segments[1]
        else:
            return uri.split("/")[-1]  # could return None if URI ends in /

    def _make_formatted_uri_basic(self, uri):
        curie = self._get_curie(uri)

        links = {
            "md": f"[{curie}]({uri})",
            "adoc": f"link:{uri}[{curie}]",
            "html": f'<a href="{uri}">{curie}</a>'
        }

        return links[self.outputformat]

    def _make_fragment_uri(self, uri):
        """This function should be overriden with profile-specific implementations
        """
        return self._make_formatted_uri_basic(uri)

    def _make_formatted_uri(self, uri):
        if uri.startswith(self.METADATA.get("default_namespace")):
            return self._make_fragment_uri(uri)
        else:
            # URI isn't in the default namespace, so use an absolut URI
            return self._make_formatted_uri_basic(uri)

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

    def _get_curie_prefix(uself, uri, existing_curies):
        ns_count = 0

        from curies import CURIES

        # TODO: replace this with a once-per run update CURIES function
        def get_curie_online(uri):
            import requests
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
                found = False
                # try to match uri_base to stored CURIES first
                if self.use_curies_stored:
                    from pylode.curies import CURIES

                    try:
                        ns[uri_base] = list(CURIES.keys())[list(CURIES.values()).index(uri_base)]
                        found = True
                    except ValueError:
                        pass

                if not found:
                    if self.get_curies_online:
                        print(f"getting CURIE for {uri_base} online")
                        uri_prefix = self._get_curie_prefix(uri_base, [x for x in ns.values()])
                        ns[uri_base] = uri_prefix
                        found = True

                # if not found:
                #     ns[uri_base] = "ns" + str(len(ns))

        # invert the key/values in instances
        for k, v in sorted(ns.items(), key=lambda x: x[1]):
            if v == "":  # can't use empty dict keys in Python
                self.NAMESPACES[":"] = k
            else:
                self.NAMESPACES[v] = k

        del(self.NAMESPACES["xml"])  # that bloody XML namespace has to go!

    def _get_default_namespace(self):
        self.METADATA["default_namespace"] = None

        # if this ontology declares a preferred URI, use that
        preferred_namespace_uri = None
        for s, o in self.G.subject_objects(predicate=URIRef("http://purl.org/vocab/vann/preferredNamespaceUri")):
            preferred_namespace_uri = str(o)

        preferred_namespace_prefix = None
        for s, o in self.G.subject_objects(predicate=URIRef("http://purl.org/vocab/vann/preferredNamespacePrefix")):
            preferred_namespace_prefix = str(o)

        if preferred_namespace_uri is not None:
            self.METADATA["default_namespace"] = preferred_namespace_uri

            if preferred_namespace_prefix is not None:
                self.NAMESPACES[preferred_namespace_prefix] = preferred_namespace_uri
                self.METADATA["default_prefix"] = preferred_namespace_prefix
            else:
                self.NAMESPACES[":"] = preferred_namespace_uri
                self.METADATA["default_prefix"] = ":"
        # if not, try the URI of the main object, compared to all prefixes
        else:
            default_uri = None

            for s in chain(
                self.G.subjects(predicate=RDF.type, object=OWL.Ontology),
                self.G.subjects(predicate=RDF.type, object=SKOS.ConceptScheme),
                self.G.subjects(predicate=RDF.type, object=PROF.Profile)
            ):
                default_uri = str(s)

            if default_uri is not None:
                self.METADATA["default_namespace"] = default_uri
                self.METADATA["default_prefix"] = ":"

                default_prefix = None
                for k, v in self.NAMESPACES.items():
                    # i.e. the default_uri is the same as the default namespace + / or #
                    if str(v).startswith(default_uri):
                        default_prefix = k

                if default_prefix is not None:
                    self.NAMESPACES[default_prefix] = default_uri
                else:
                    self.NAMESPACES[":"] = default_uri
            else:
                # can't find either a declared or default namespace so we have an error
                raise Exception("pyLODE can't detect a URI for an owl:Ontology, a skos:ConceptScheme or a prof:Profile")

    def _make_namespaces(self):
        # if the default namespace is also listed in NAMESPACES, remove it and replace the default key (:) with its key
        default_ns_prefix = self.METADATA.get("default_prefix")
        for_removal = []
        for k, v in self.NAMESPACES.items():
            if v == self.METADATA["default_namespace"]:
                for_removal.append(k)

        for r in for_removal:
            del(self.NAMESPACES[r])

        return BaseProfile._load_template(self, "namespaces." + self.outputformat).render(
            namespaces=self.NAMESPACES,
            default_namespace_prefix=default_ns_prefix if default_ns_prefix is not None else ":",
            default_namespace=self.METADATA["default_namespace"],
        )

    # makes the fragment ID for a class, property, Named Individual (any entity) based on URI or name
    def _make_fid(self, title, uri):
        # does this URI already have a fid?
        existing_fid = self.FIDS.get(uri)
        if existing_fid is not None:
            return existing_fid

        # if we get here, there is no fid, so make one
        def _remove_non_ascii_chars(s):
            return "".join(j for j in s if ord(j) < 128).replace("&", "")

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
            if self.outputformat == "md":
                license = URIRef(self.METADATA.get("license").split('(')[0].strip('[]'))
            elif self.outputformat == "adoc":
                license = URIRef(self.METADATA.get("license").replace("link:", "").split("[")[0])
            else:
                license = URIRef(self.METADATA.get("license").split('"')[1])
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
            if self.outputformat == "md":
                repository = URIRef(self.METADATA.get("repository").split('(')[0].strip('[]'))
            if self.outputformat == "adoc":
                repository = URIRef(self.METADATA.get("repository").replace("link:", "").split("[")[0])
            else:
                repository = URIRef(self.METADATA.get("repository").split('"')[1])

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

        return g.serialize(format="json-ld")

    def _make_agent_link(self, name, url=None, email=None, affiliation=None):
        if self.outputformat == "md":
            orcid = None
            if url is not None:
                if "orcid.org" in url:
                    orcid = BaseProfile._load_template(self, "orcid.md").render(
                        orcid_url=url,
                        orcid_id=url.replace("http://orcid.org/", "").replace("https://orcid.org/", "").strip("/")
                    )

            return BaseProfile._load_template(self, "agent.md").render(
                url=url,
                name=name,
                orcid=orcid,
                email=email.replace("mailto:", "") if email is not None else None,
                affiliation=affiliation
            )
        elif self.outputformat == "adoc":
            orcid = None
            if url is not None:
                if "orcid.org" in url:
                    orcid = BaseProfile._load_template(self, "orcid.adoc").render(
                        orcid_url=url,
                        orcid_id=url.replace("http://orcid.org/", "").replace("https://orcid.org/", "").strip("/")
                    )

            return BaseProfile._load_template(self, "agent.adoc").render(
                url=url,
                name=name,
                orcid=orcid,
                email=email.replace("mailto:", "") if email is not None else None,
                affiliation=affiliation
            )
        else:  # self.outputformat == "html":
            orcid = None
            if url is not None:
                if "orcid.org" in url:
                    orcid = BaseProfile._load_template(self, "orcid.html").render(
                        orcid_url=url,
                    )

            return BaseProfile._load_template(self, "agent.html").render(
                url=url,
                name=name,
                orcid=orcid,
                email=email.replace("mailto:", "") if email is not None else None,
                affiliation=affiliation
            )

    def _make_agent(self, agent_node):
        # we understand foaf:name, foaf:homepage & sdo:name & sdo:identifier & sdo:email (as a URI)
        # TODO: cater for other Agent representations

        name = None
        url = None
        email = None
        org_name = None
        org_url = None
        org_email = None
        for p, o in self.G.predicate_objects(subject=agent_node):
            print(p, o)
            if p in [FOAF.homepage, SDO.identifier]:
                url = str(o)
            elif p in [FOAF.name, SDO.name]:
                name = str(o)
            elif p in [FOAF.mbox, SDO.email]:
                email = str(o).split("/")[-1].split("#")[-1]  # remove base URI leaving only email address
            elif p in [SDO.memberOf, SDO.affiliation]:
                for p2, o2 in self.G.predicate_objects(subject=o):
                    if p2 in [FOAF.homepage, SDO.identifier, SDO.url]:  # TODO: split homepage form IDs, cater for rdfs:seeAlso
                        org_url = str(o2)
                    elif p2 in [FOAF.name, SDO.name]:
                        org_name = str(o2)
                    elif p in [FOAF.mbox, SDO.email]:
                        org_email = str(o2).split("/")[-1].split("#")[-1]  # remove base URI leaving only email address

        # use the URI of the Agent for its URL if no FOAF.homepage or SDO.identifier has been set
        if url is None and type(agent_node) == URIRef:
            url = str(agent_node)

        if name is None:
            if type(agent_node) == Literal:
                name = agent_node
            if type(agent_node) == URIRef:
                name = agent_node.split("/")[-1].split("#")[-1]
        agent = self._make_agent_link(name, url=url, email=email)

        if org_name is not None:
            org = self._make_agent_link(org_name, url=org_url, email=org_email)
            agent += " of " + org

        return agent

    def _make_source_file_link(self):
        # if the source is a URI, use that
        # if it's a file path, only use the file name
        if self.source_info[0].startswith("http"):
            uri_of_rdf = self.source_info[0]
        else:
            uri_of_rdf = self.source_info[0].split("/")[-1]
        if self.outputformat == "md":
            return 'RDF ([{}]({}))'.format(
                uri_of_rdf, self.source_info[1]
            )
        if self.outputformat == "adoc":
            return 'RDF link:{}[{}]'.format(
                uri_of_rdf, self.source_info[1]
            )
        else:
            return '<a href="{}">RDF ({})</a>'.format(
                uri_of_rdf, self.source_info[1]
            )

    def generate_document(self):
        if self.ouputformat == "md":
            return """# Empty pyLODE output (Markdown)"""
        else:  # HTML
            return """<!DOCTYPE html>""" \
                """<html lang="en">""" \
                """ <body>""" \
                """     <h1>Empty pyLODE output (HTML)</h1>""" \
                """</body>""" \
                """</html>"""