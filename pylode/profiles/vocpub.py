from pylode import __version__
from pylode.common import STYLE_DIR, TEMPLATES_DIR
import collections
from os import path
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import DC, DCTERMS, DOAP, OWL, PROV, RDF, RDFS, SDO, SKOS
from itertools import chain
import markdown
from jinja2 import Environment, FileSystemLoader
from os.path import join
from pylode.profiles.base import BaseProfile


class VocPub(BaseProfile):
    def __init__(
            self,
            g,
            source_info,
            outputformat="html",
            include_css=False,
            default_language="en",
            use_curies_stored=True,
            get_curies_online=False
    ):
        super().__init__(
            g,
            source_info,
            outputformat=outputformat,
            include_css=include_css,
            use_curies_stored=use_curies_stored,
            get_curies_online=get_curies_online,
            default_language=default_language)
        self.CONCEPTS = collections.OrderedDict()
        self.COLLECTIONS = collections.OrderedDict()

    def _load_template(self, template_file):
        return Environment(loader=FileSystemLoader(join(TEMPLATES_DIR, "vocpub"))).get_template(template_file)

    def _make_fragment_uri(self, uri):
        """VocPub Profile allows fragment URIs for Concepts & Collections"""
        if self.CONCEPTS.get(uri) or self.COLLECTIONS.get(uri):
            if self.CONCEPTS.get(uri):
                title = self.CONCEPTS[uri]["default_prefLabel"]
                uri = self.CONCEPTS[uri]["fid"]
            elif self.COLLECTIONS.get(uri):
                title = self.COLLECTIONS[uri]["default_prefLabel"]
                uri = self.COLLECTIONS[uri]["fid"]

            links = {
                "md": f"[{title}](#{uri})",
                "adoc": f"link:#{uri}[{title}]",
                "html": f'<a href="#{uri}">{title}</a>'
            }
            return links[self.outputformat]
        else:
            return self._make_formatted_uri_basic(uri)

    def _make_formatted_uri(self, uri, type=None):
        link = super()._make_formatted_uri(uri)

        types = {
            "con": "concept",
            "col": "collection",
        }

        if type not in types.keys():
            return link

        suffixes = {
            "md": f' ({type})',
            "adoc": f' ^{type}^',
            "html": f'<sup class="sup-{type}" title="{types[type]}">{type}</sup>'
        }

        return link + suffixes[self.outputformat]

    def _expand_graph(self):
        # name
        for s, o in chain(
                self.G.subject_objects(DC.title),
                self.G.subject_objects(RDFS.label),
                self.G.subject_objects(DCTERMS.title)
        ):
            self.G.add((s, SKOS.prefLabel, o))

        # description
        for s, o in chain(
                self.G.subject_objects(DC.description),
                self.G.subject_objects(DCTERMS.description),
                self.G.subject_objects(RDFS.comment),
                self.G.subject_objects(SDO.description)
        ):
            self.G.add((s, SKOS.definition, o))

        # OWL -> SKOS
        # classes as Concepts types
        for s in chain(
                self.G.subjects(RDF.type, RDFS.Class),
                self.G.subjects(RDF.type, OWL.Class)
        ):
            self.G.add((s, RDF.type, SKOS.Concept))

        # SKOS Concept Hierarchy from Class subsumption
        for s, o in self.G.subject_objects(RDFS.subClassOf):
            if type(o) != BNode:  # stops restrictions being seen as broader/narrower
                self.G.add((s, SKOS.broader, o))
                self.G.add((o, SKOS.narrower, s))

        for s, o in self.G.subject_objects(OWL.equivalentClass):
            self.G.add((s, SKOS.exactMatch, o))
            self.G.add((o, SKOS.exactMatch, s))

        # the ontology is now a ConceptScheme
        for s in self.G.subjects(RDF.type, OWL.Ontology):
            self.G.add((s, RDF.type, SKOS.ConceptScheme))

            # top concepts
            # if the class (now typed a Concept) is declared here and
            #   has no subClassOf
            #   or is subClassOf skos:Concept
            #   or is only a subClassOf BNodes (restrictions)
            for s2 in self.G.subjects(RDF.type, SKOS.Concept):
                if (s2, RDFS.subClassOf, None) not in self.G:
                    self.G.add((s2, SKOS.topConceptOf, s))

                only_bn = True
                for o3 in self.G.objects(s2, RDFS.subClassOf):
                    if type(o3) != BNode:
                        only_bn = False
                if only_bn:
                    self.G.add((s2, SKOS.topConceptOf, s))


        # SKOS -> SKOS
        # broader / narrower buildout
        for s, o in self.G.subject_objects(SKOS.broader):
            self.G.add((o, SKOS.narrower, s))

        for s, o in self.G.subject_objects(SKOS.narrower):
            self.G.add((o, SKOS.broader, s))

        for s, o in self.G.subject_objects(SKOS.topConceptOf):
            self.G.add((o, SKOS.hasTopConcept, s))

        for s, o in self.G.subject_objects(SKOS.hasTopConcept):
            self.G.add((o, SKOS.topConceptOf, s))

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

    def _extract_collections(self):
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
            self.COLLECTIONS[c]["default_prefLabel"] = None
            self.COLLECTIONS[c]["prefLabels"] = set()
            self.COLLECTIONS[c]["altLabels"] = set()
            self.COLLECTIONS[c]["definitions"] = set()
            self.COLLECTIONS[c]["scopeNotes"] = set()
            self.COLLECTIONS[c]["source"] = None
            self.COLLECTIONS[c]["members"] = set()

            for p, o in self.G.predicate_objects(subject=s):
                if p == SKOS.prefLabel:
                    self.COLLECTIONS[c]["prefLabels"].add((str(o), o.language))  # TODO: add in language
                    if o.language == self.default_language:
                        self.COLLECTIONS[c]["default_prefLabel"] = str(o)

                elif p == SKOS.altLabel:
                    self.COLLECTIONS[c]["altLabels"].add(str(o))  # TODO: add in language

                elif p == SKOS.definition:
                    # TODO: add in language
                    if self.outputformat == "md":
                        self.COLLECTIONS[c]["definitions"].add(str(o))
                    else:
                        self.COLLECTIONS[c]["definitions"].add(markdown.markdown(str(o)))

                elif p == SKOS.scopeNote:
                    # TODO: add in language
                    if self.outputformat == "md":
                        self.COLLECTIONS[c]["scopeNotes"].add(str(o))
                    else:
                        self.COLLECTIONS[c]["scopeNotes"].add(markdown.markdown(str(o)))

                elif p == DCTERMS.source:
                    self.COLLECTIONS[c]["source"] = str(o)

                elif p == SKOS.topConceptOf:
                    self.COLLECTIONS[c]["topConceptOfs"].add(str(o))

                elif p == SKOS.member:
                    self.COLLECTIONS[c]["members"].add(str(o))
                    # TODO: handle members that are other Collections, not Concepts

            # listify the sets
            self.COLLECTIONS[c]["prefLabels"] = list(self.COLLECTIONS[c]["prefLabels"])
            self.COLLECTIONS[c]["altLabels"] = list(self.COLLECTIONS[c]["altLabels"])
            self.COLLECTIONS[c]["definitions"] = list(self.COLLECTIONS[c]["definitions"])
            self.COLLECTIONS[c]["scopeNotes"] = list(self.COLLECTIONS[c]["scopeNotes"])
            self.COLLECTIONS[c]["members"] = list(self.COLLECTIONS[c]["members"])

            # make fid
            # TODO: update to use default language label, not [0]
            try:
                pl = self.COLLECTIONS[c]["prefLabels"][0][0]

                self.COLLECTIONS[c]["fid"] = self._make_fid(
                    pl, c
                )
            except Exception as e:
                print(e)
                raise Exception("You Collection {}  doesn't have a label but it needs one!".format(c))

    def _extract_concepts(self):
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
                    self.CONCEPTS[c]["prefLabels"].add((str(o), o.language))  # TODO: add in language
                    if o.language == self.default_language:
                        self.CONCEPTS[c]["default_prefLabel"] = str(o)

                elif p == SKOS.altLabel:
                    self.CONCEPTS[c]["altLabels"].add(str(o))  # TODO: add in language

                elif p == SKOS.definition:
                    # TODO: add in language
                    if self.outputformat == "md":
                        self.CONCEPTS[c]["definitions"].add(str(o))
                    else:
                        self.CONCEPTS[c]["definitions"].add(markdown.markdown(str(o)))

                elif p == SKOS.scopeNote:
                    # TODO: add in language
                    if self.outputformat == "md":
                        self.CONCEPTS[c]["scopeNotes"].add(str(o))
                    else:
                        self.CONCEPTS[c]["scopeNotes"].add(markdown.markdown(str(o)))

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

            # patch title from URI if we haven't got one
            if len(self.CONCEPTS[c]["prefLabels"]) < 1:
                pl = self._make_title_from_uri(c)
                self.CONCEPTS[c]["prefLabels"].add((pl, 'en'))
                self.CONCEPTS[c]["default_prefLabel"] = pl

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

    def _extract_concept_scheme(self):
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
                    if self.outputformat == "md":
                        self.METADATA["description"] = str(o)
                    else:
                        self.METADATA["description"] = markdown.markdown(str(o))

                if p == SKOS.historyNote:
                    if self.outputformat == "md":
                        self.METADATA["historyNote"] = str(o)
                    else:
                        self.METADATA["historyNote"] = markdown.markdown(str(o))

                # dates
                if p in [DCTERMS.created, DCTERMS.modified, DCTERMS.issued]:
                    date_type = p.split("/")[-1]
                    self.METADATA[date_type] = str(o)

                if p == DCTERMS.source:
                    if str(o).startswith('http'):
                        self.METADATA["source"] = self._make_formatted_uri(o)  # '<a href="{0}">{0}</a>'.format(str(o))
                    else:
                        self.METADATA["source"] = str(o)

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
                        self.METADATA[agent_type].add(self._make_agent(o))

                # TODO: cater for other Agent representations

                if p == PROV.wasGeneratedBy:
                    for o2 in self.G.objects(subject=o, predicate=DOAP.repository):
                        self.METADATA["repository"] = self._make_formatted_uri(o2)

                if p == SDO.codeRepository:
                    self.METADATA["repository"] = self._make_formatted_uri(o)

        if self.METADATA.get("title") is None:
            raise ValueError(
                "Your taxonomy's ConceptScheme does not indicate any form of title. "
                "You must declare one of the following for it: rdfs:label, dct:title, skos:prefLabel"
            )

        if len(self.COLLECTIONS.keys()) > 0:
            self.METADATA["has_collections"] = True

        if len(self.CONCEPTS.keys()) > 0:
            self.METADATA["has_concepts"] = True

    def _make_skos_concept_scheme(self):
        return self._load_template("concept_scheme." + self.outputformat).render(
            title=self.METADATA.get("title"),
            uri=self.METADATA.get("uri"),
            version_uri=self.METADATA.get("versionIRI"),
            publishers=sorted(self.METADATA["publishers"]),
            creators=sorted(self.METADATA["creators"]),
            contributors=sorted(self.METADATA["contributors"]),
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
            ont_rdf=self._make_source_file_link(),
            has_collections=True if len(self.COLLECTIONS) > 0 else False,
            has_concepts=True if len(self.CONCEPTS) > 0 else False,
        )

    def _make_skos_collection(self, collection):
        return self._load_template("collection." + self.outputformat).render(
            uri=collection[0],
            fid=collection[1].get("fid"),
            default_prefLabel=collection[1].get("default_prefLabel"),
            prefLabels=collection[1].get("prefLabels"),
            altLabels=collection[1].get("altLabels"),
            definitions=collection[1].get("definitions"),
            scopeNotes=collection[1].get("scopeNotes"),
            source=collection[1].get("source"),
            members=[self._make_formatted_uri(x, type="con") for x in collection[1].get("members")],
        )

    def _make_skos_collections(self):
        collections = []
        for k, v in self.COLLECTIONS.items():
            collections.append(
                (
                    v["default_prefLabel"],
                    v["fid"],
                    self._make_skos_collection((k, v)),
                )
            )

        return self._load_template("collections." + self.outputformat).render(collections=collections)

    def _make_concept_hierarchy(self):
        of = self.outputformat
        # render concept
        def _render(c, children, of, level=0):
            if of == "md":
                md = level*"\t" + "* " + self._make_formatted_uri(c, type="con")
                if len(children) > 0:
                    for ch in sorted(children):
                        md += _render(ch, self.CONCEPTS.get(ch).get("narrowers"), of, level=level + 1)
                return md
            else:  # HTML
                html = "<li>{}".format(self._make_formatted_uri(c))
                if len(children) > 0:
                    for ch in sorted(children):
                        html += "\n<ul>" + \
                                _render(ch, self.CONCEPTS.get(ch).get("narrowers"), of, level=level + 1) + \
                                "</ul>"
                html += "</li>"
                return html

        # start with a topConcept
        tcs = []
        for s, o in self.G.subject_objects(predicate=SKOS.hasTopConcept):
            tcs.append(str(o))

        txt = ""
        for tc in sorted(tcs):
            txt += _render(tc, self.CONCEPTS.get(tc).get("narrowers"), self.outputformat, 0)

        if self.outputformat == "md":
            return txt
        else:
            return "<ul class=\"hierarchy\">\n" + txt + "\n</ul>"

    def _make_skos_concept(self, concept):
        # handling Markdown formatting within a table
        if self.outputformat == "md":
            if len(concept[1].get("definitions")) > 0:
                defs = [d.replace("\n", " ") for d in concept[1].get("definitions")]
            else:
                defs = []
            if len(concept[1].get("examples")) > 0:
                egs = [eg.strip().replace("\t", "    ") for eg in concept[1].get("examples")]
                egs2 = []
                for ee in egs:
                    ee2 = ""
                    for line in ee.split("\n"):
                        ee2 += "`" + line + "`<br />"
                    egs2.append(ee2)
                egs = egs2
            else:
                egs = []
        else:
            defs = concept[1].get("definitions")
            if len(concept[1].get("examples")) > 1:
                egs = [x.replace("<", "&lt;").replace(">", "&gt;") for x in concept[1].get("examples")]
            else:
                egs = []

        return self._load_template("concept." + self.outputformat).render(
            uri=concept[0],
            fid=concept[1].get("fid"),
            default_prefLabel=concept[1].get("default_prefLabel"),
            prefLabels=concept[1].get("prefLabels"),
            altLabels=concept[1].get("altLabels"),
            definitions=defs,
            scopeNotes=concept[1].get("scopeNotes"),
            examples=egs,
            source=concept[1].get("source"),
            broaders=[self._make_formatted_uri(x, type="con") for x in concept[1].get("broaders")],
            narrowers=[self._make_formatted_uri(x, type="con") for x in concept[1].get("narrowers")],
            exactMatches=[self._make_formatted_uri(x, type="con") for x in concept[1].get("exactMatches")],
            closeMatches=[self._make_formatted_uri(x, type="con") for x in concept[1].get("closeMatches")],
            broadMatches=[self._make_formatted_uri(x, type="con") for x in concept[1].get("broadMatches")],
            narrowMatches=[self._make_formatted_uri(x, type="con") for x in concept[1].get("narrowMatches")],
        )

    def _make_skos_concepts(self):
        # TODO: make Concept hierarchy (URIs)

        # TODO: list all Concepts, alphabetically by prefLabel
        concepts = []
        for k, v in self.CONCEPTS.items():
            concepts.append(
                (
                    v["default_prefLabel"],
                    v["fid"],
                    self._make_skos_concept((k, v)),
                )
            )

        return self._load_template("concepts." + self.outputformat).render(
            concept_hierarchy=self._make_concept_hierarchy(),
            concepts=concepts
        )

    def _make_document(self):
        css = None
        if self.outputformat == "html":
            if self.include_css:
                css = open(path.join(STYLE_DIR, "pylode.css")).read()

        return self._load_template("taxonomy." + self.outputformat).render(
            schemaorg=self._make_schemaorg_metadata(),  # only does something for the HTML template
            title=self.METADATA["title"],
            concept_scheme=self._make_skos_concept_scheme(),
            has_collections=True if len(self.COLLECTIONS) > 0 else False,
            collections=self._make_skos_collections(),
            has_concepts=True if len(self.CONCEPTS) > 0 else False,
            concepts=self._make_skos_concepts(),
            namespaces=self._make_namespaces(),
            css=css,
            pylode_version=__version__
        )

    def generate_document(self):
        # expand the graph using pre-defined rules to make querying easier (poor man's inference)
        self._expand_graph()
        # get all the namespaces using several methods
        self._extract_namespaces()
        # get the default namespace
        self._get_default_namespace()
        # extract all the SKOS things
        self._extract_collections()
        self._extract_concepts()
        self._make_concept_hierarchy()
        self._extract_concept_scheme()

        return self._make_document()
