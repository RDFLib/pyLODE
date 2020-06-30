from pylode.common import VERSION, STYLE_DIR, TEMPLATES_DIR
import collections
from os import path
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import DC, DCTERMS, DOAP, OWL, PROF, PROV, RDF, RDFS, SDO, SKOS
import dateutil.parser
from itertools import chain
import markdown
from jinja2 import Environment, FileSystemLoader
from os.path import join
from pylode.profiles import BaseProfile


class Prof(BaseProfile):
    def __init__(self, g, source_info, outputformat="html", exclude_css=False, default_language="en", get_curies_online=False):
        super().__init__(g, source_info, outputformat=outputformat, exclude_css=exclude_css, get_curies_online=False, default_language=default_language)
        self.RESOURCE_DESCRIPTORS = collections.OrderedDict()

    def _load_template(self, template_file):
        return Environment(loader=FileSystemLoader(join(TEMPLATES_DIR, "prof"))).get_template(template_file)

    def _get_default_namespace(self):
        self.METADATA["default_namespace"] = None

        # if this ontology declares a preferred URI, use that
        if self.METADATA.get("preferredNamespaceUri"):
            self.METADATA["default_namespace"] = self.METADATA.get(
                "preferredNamespaceUri"
            )

        # if not, try the URI of the ontology compared to all prefixes
        for s in self.G.subjects(predicate=RDF.type, object=PROF.Profile):
            ont_uri = str(s)

        for k, v in self.NAMESPACES.items():
            # i.e. the ontology URI is the same as the default namespace + / or #
            if v == ont_uri + "/" or v == ont_uri + "#":
                self.METADATA["default_namespace"] = v

        if self.NAMESPACES.get("") is not None:
            del self.NAMESPACES[""]

    def _make_formatted_uri(self, uri, type=None):
        # set display to CURIE
        short = self._get_curie(uri)
        # if the URI base is within the default namespace of this ontology
        #   use the fragment URI
        # else
        #   use the given URI
        uri_base = self._get_namespace_from_uri(uri)
        link = None
        if uri_base == self.METADATA.get("default_namespace"):
            if self.CONCEPTS.get(uri):
                link = "[{}]({})".format(self.CONCEPTS[uri]["default_prefLabel"], self.CONCEPTS[uri]["fid"]) \
                    if self.outputformat == "md" \
                    else '<a href="#{}">{}</a>'.format(self.CONCEPTS[uri]["fid"], self.CONCEPTS[uri]["default_prefLabel"])
            elif self.COLLECTIONS.get(uri):
                    link = "[{}]({})".format(self.COLLECTIONS[uri]["default_prefLabel"], self.COLLECTIONS[uri]["fid"]) \
                        if self.outputformat == "md" \
                        else '<a href="#{}">{}</a>'.format(self.COLLECTIONS[uri]["fid"], self.COLLECTIONS[uri]["default_prefLabel"])

        if link is None:
            link = "[{}]({})".format(short, uri) \
                if self.outputformat == "md" \
                else '<a href="{}">{}</a>'.format(uri, short)

        if type == "cp":
            if self.outputformat == "md":
                suffix = ' (cp)'
            else:
                suffix = '<sup class="sup-cp" title="concept">cp</sup>'
        elif type == "cl":
            if self.outputformat == "md":
                suffix = ' (cl)'
            else:
                suffix = '<sup class="sup-cl" title="collection">cl</sup>'
        # None
        else:
            suffix = ''

        return link + suffix

    def _expand_graph(self):
        # label
        for s, o in chain(
                self.G.subject_objects(DC.title),
                self.G.subject_objects(SKOS.prefLabel),
                self.G.subject_objects(DCTERMS.title)
        ):
            self.G.remove((s, DC.title, o))
            self.G.remove((s, SKOS.prefLabel, o))
            self.G.remove((s, DCTERMS.title, o))
            self.G.add((s, RDFS.label, o))

        # comment
        for s, o in chain(
                self.G.subject_objects(DC.description),
                self.G.subject_objects(DCTERMS.description),
                self.G.subject_objects(SDO.description),
                self.G.subject_objects(SKOS.definition),
        ):
            self.G.remove((s, DC.description, o))
            self.G.remove((s, DCTERMS.description, o))
            self.G.remove((s, SDO.description, o))
            self.G.remove((s, SKOS.definition, o))
            self.G.add((s, RDFS.comment, o))

        # Agents
        # creator
        for s, o in chain(
                self.G.subject_objects(DC.creator),
                self.G.subject_objects(SDO.creator),
                self.G.subject_objects(SDO.author)  # conflate SDO.author with DCTERMS.creator
        ):
            self.G.remove((s, DC.creator, o))
            self.G.remove((s, SDO.creator, o))
            self.G.remove((s, SDO.author, o))
            self.G.add((s, DCTERMS.creator, o))

        # contributor
        for s, o in chain(
                self.G.subject_objects(DC.contributor),
                self.G.subject_objects(SDO.contributor)
        ):
            self.G.remove((s, DC.contributor, o))
            self.G.remove((s, SDO.contributor, o))
            self.G.add((s, DCTERMS.contributor, o))

        # publisher
        for s, o in chain(
                self.G.subject_objects(DC.publisher),
                self.G.subject_objects(SDO.publisher)
        ):
            self.G.remove((s, DC.publisher, o))
            self.G.remove((s, SDO.publisher, o))
            self.G.add((s, DCTERMS.publisher, o))

        # Resource Descriptors
        for s, o in self.G.subject_objects(PROF.hasResource):
            self.G.add((o, RDF.type, PROF.ResourceDescriptor))

    def _extract_resource_descriptors(self):
        """Extracts Resource Descriptors"""
        resource_descriptors = []
        # TODO: handle OrderedCollections
        for s in self.G.subjects(predicate=RDF.type, object=PROF.ResourceDescriptor):
            print("RD: " + str(s))
            resource_descriptors.append(str(s))  # could be a URI or a BNode

        # keeping the OrderedDict ordered
        for rd in sorted(resource_descriptors):
            self.RESOURCE_DESCRIPTORS[rd] = {}

        # fill in each Resource Descriptor's details from the graph
        for rd in self.RESOURCE_DESCRIPTORS.keys():
            s = URIRef(rd)  # for use in Graph() loops

            self.RESOURCE_DESCRIPTORS[rd]["fid"] = None
            self.RESOURCE_DESCRIPTORS[rd]["label"] = None
            self.RESOURCE_DESCRIPTORS[rd]["comment"] = None
            self.RESOURCE_DESCRIPTORS[rd]["artifact"] = None
            self.RESOURCE_DESCRIPTORS[rd]["roles"] = set()
            self.RESOURCE_DESCRIPTORS[rd]["conforms"] = set()
            self.RESOURCE_DESCRIPTORS[rd]["format"] = None

            for p, o in self.G.predicate_objects(subject=s):
                if p == RDFS.label:
                    self.RESOURCE_DESCRIPTORS[rd]["label"] = str(o)
                elif p == RDFS.comment:
                    self.RESOURCE_DESCRIPTORS[rd]["comment"] = str(o)
                elif p == PROF.hasArtifact:
                    self.RESOURCE_DESCRIPTORS[rd]["artifact"] = str(o)
                elif p == PROF.hasRole:
                    self.RESOURCE_DESCRIPTORS[rd]["roles"].add(str(o))
                elif p == DCTERMS.conformsTo:
                    self.RESOURCE_DESCRIPTORS[rd]["conforms"].add(str(o))
                elif p == DCTERMS.format:
                    self.RESOURCE_DESCRIPTORS[rd]["format"] = str(o)

            self.RESOURCE_DESCRIPTORS[rd]["roles"] = list(self.RESOURCE_DESCRIPTORS[rd]["roles"])
            self.RESOURCE_DESCRIPTORS[rd]["conforms"] = list(self.RESOURCE_DESCRIPTORS[rd]["conforms"])

            # make fid
            self.RESOURCE_DESCRIPTORS[rd]["fid"] = self._make_fid(None, rd)

    def _extract_profile(self):
        """Extracts standard prof:Profile metadata
        """

        self.METADATA["creators"] = set()
        self.METADATA["contributors"] = set()
        self.METADATA["publishers"] = set()
        for s in self.G.subjects(predicate=RDF.type, object=PROF.Profile):
            self.METADATA["uri"] = str(s)
            for p, o in self.G.predicate_objects(subject=s):
                if p == RDFS.label:
                    self.METADATA["label"] = str(o)

                if p == RDFS.comment:
                    self.METADATA["comment"] = markdown.markdown(str(o))

                # dates
                if p in [DCTERMS.created, DCTERMS.modified, DCTERMS.issued]:
                    date_type = p.split("/")[-1]
                    self.METADATA[date_type] = dateutil.parser.parse(str(o)).strftime("%Y-%m-%d")

                if p == OWL.versionIRI:
                    self.METADATA["versionIRI"] = self._make_formatted_uri(o)

                if p == OWL.versionInfo:
                    self.METADATA["versionInfo"] = str(o)

                if p == URIRef("http://purl.org/vocab/vann/preferredNamespacePrefix"):
                    self.METADATA["preferredNamespacePrefix"] = str(o)

                if p == URIRef("http://purl.org/vocab/vann/preferredNamespaceUri"):
                    self.METADATA["preferredNamespaceUri"] = str(o)

                if p == DCTERMS.license:
                    self.METADATA["license"] = (
                        self._make_formatted_uri(o)
                        if str(o).startswith("http")
                        else str(o)
                    )

                if p == DCTERMS.rights:
                    self.METADATA["rights"] = (
                        str(o)
                            .replace("Copyright", "&copy;")
                            .replace("copyright", "&copy;")
                            .replace("(c)", "&copy;")
                    )

                # Agents
                if p in [DCTERMS.creator, DCTERMS.contributor, DCTERMS.publisher]:
                    agent_type = p.split("/")[-1] + "s"
                    if type(o) == Literal:
                        self.METADATA[agent_type].add(str(o))
                    else:  # Blank Node or URI
                        self.METADATA[agent_type].add(self._make_agent_html(o))

                # TODO: cater for other Agent representations

        if self.METADATA.get("label") is None:
            raise ValueError(
                "Your profile does not indicate any form of title. "
                "You must declare one of the following for it: rdfs:label, dct:title, skos:prefLabel"
            )

    def _make_profile(self):
        return self._load_template("profile." + self.outputformat).render(
            title=self.METADATA.get("title"),
            uri=self.METADATA.get("uri"),
            version_uri=self.METADATA.get("versionIRI"),
            publishers=sorted(self.METADATA["publishers"]),
            creators=sorted(self.METADATA["creators"]),
            contributors=sorted(self.METADATA["contributors"]),
            created=self.METADATA.get("created"),
            modified=self.METADATA.get("modified"),
            issued=self.METADATA.get("issued"),
            comment=self.METADATA.get("comment"),
            version_info=self.METADATA.get("versionInfo"),
            license=self.METADATA.get("license"),
            rights=self.METADATA.get("rights"),
            repository=self.METADATA.get("repository"),
            prof_rdf=self._make_source_file_link(),
            has_resource_descriptors=True if len(self.RESOURCE_DESCRIPTORS) > 0 else False,
        )

    def _make_resource_descriptor(self, rd):
        return self._load_template("resource_descriptor." + self.outputformat).render(
            uri=rd[0],
            fid=rd[1].get("fid"),
            label=rd[1].get("label"),
            comment=rd[1].get("comment"),
            artifact=rd[1].get("artifact"),
            roles=rd[1].get("roles"),
            conforms=rd[1].get("conforms"),
            format=rd[1].get("format"),
        )

    def _make_resource_descriptors(self):
        rds = []
        for k, v in self.RESOURCE_DESCRIPTORS.items():
            rds.append(
                (
                    v["label"],
                    v["fid"],
                    self._make_resource_descriptor((k, v)),
                )
            )

        return self._load_template("resource_descriptors." + self.outputformat).render(rds=rds)

    def _make_document(self):
        css = None
        if self.outputformat == "html":
            if not self.exclude_css:
                css = open(path.join(STYLE_DIR, "pylode.css")).read()

        print(True if len(self.RESOURCE_DESCRIPTORS) > 0 else False)
        print(self._make_resource_descriptors())

        return self._load_template("prof." + self.outputformat).render(
            schemaorg=self._make_schemaorg_metadata(),  # only does something for the HTML template
            title=self.METADATA["label"],
            has_resource_descriptors=True if len(self.RESOURCE_DESCRIPTORS) > 0 else False,
            resource_descriptors=self._make_resource_descriptors(),
            namespaces=self._make_namespaces(),
            css=css,
            pylode_version=VERSION
        )

    def generate_document(self):
        self._expand_graph()
        self._extract_namespaces()
        self._get_default_namespace()
        self._extract_profile()
        self._extract_resource_descriptors()

        return self._make_document()
