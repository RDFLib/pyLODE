from pylode import __version__
from pylode.common import TEMPLATES_DIR, STYLE_DIR
import collections
from os import path
from itertools import chain
import markdown
from jinja2 import Environment, FileSystemLoader
from os.path import join
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import DC, DCTERMS, DOAP, OWL, PROV, RDF, RDFS, SDO, SKOS
from pylode.profiles.base import BaseProfile


class NMPF(BaseProfile):
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
        self.G.bind("prov", PROV)
        self.CLASSES = collections.OrderedDict()
        self.PROPERTIES = collections.OrderedDict()
        self.NAMED_INDIVIDUALS = collections.OrderedDict()

    def _make_collection_class_html(self, col_type, col_members):
        if col_type == "owl:unionOf":
            j = " or "
        elif col_type == "owl:intersectionOf":
            j = " and "
        else:
            j = " ? "
        # others...
        return "({})".format(
            j.join([self._make_formatted_uri(x, type="c") for x in col_members])
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
                    prop = self._make_formatted_uri(str(o2), t)
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
                        cls = self._make_formatted_uri(str(o2), type="c")
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

                    if self.outputformat == "md":
                        card = '**{}** {}'.format(
                            card, str(o2)
                        )
                    else:
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
                        c = self._make_formatted_uri(str(o2), type="c")

                    if self.outputformat == "md":
                        card = '**{}** {}'.format(card, c)
                    else:
                        card = '<span class="cardinality">{}</span> {}'.format(card, c)
                elif p2 == OWL.hasValue:
                    if self.outputformat == "md":
                        card = '**value** {}'.format(
                            self._make_formatted_uri(str(o2), type="c")
                        )
                    else:
                        card = '<span class="cardinality">value</span> {}'.format(
                            self._make_formatted_uri(str(o2), type="c")
                        )

        restriction = prop + " " + card if card is not None else prop
        restriction = restriction + " " + cls if cls is not None else restriction

        return restriction

    def _load_template(self, template_file):
        return Environment(loader=FileSystemLoader(join(TEMPLATES_DIR, "ontdoc"))).get_template(template_file)

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
            if self.PROPERTIES.get(uri):
                link = "[{}]({})".format(short, self.PROPERTIES[uri]["fid"]) \
                    if self.outputformat == "md" \
                    else '<a href="#{}">{}</a>'.format(self.PROPERTIES[uri]["fid"], short)
            elif self.CLASSES.get(uri):
                link = "[{}]({})".format(short, self.CLASSES[uri]["fid"]) \
                    if self.outputformat == "md" \
                    else '<a href="#{}">{}</a>'.format(self.CLASSES[uri]["fid"], short)
            else:
                link = "[{}]({})".format(short, uri) \
                    if self.outputformat == "md" \
                    else '<a href="{}">{}</a>'.format(uri, short)

        if link is None:
            link = "[{}]({})".format(short, uri) \
                if self.outputformat == "md" \
                else '<a href="{}">{}</a>'.format(uri, short)

        if type == "c":
            if self.outputformat == "md":
                suffix = ' (c)'
            else:
                suffix = '<sup class="sup-c" title="class">c</sup>'
        elif type == "op":
            if self.outputformat == "md":
                suffix = ' (op)'
            else:
                suffix = '<sup class="sup-op" title="object property">op</sup>'
        elif type == "fp":
            if self.outputformat == "md":
                suffix = ' (fp)'
            else:
                suffix = '<sup class="sup-fp" title="functional property">fp</sup>'
        elif type == "dp":
            if self.outputformat == "md":
                suffix = ' (dp)'
            else:
                suffix = '<sup class="sup-dp" title="datatype property">dp</sup>'
        elif type == "ap":
            if self.outputformat == "md":
                suffix = ' (ap)'
            else:
                suffix = '<sup class="sup-ap" title="annotation property">ap</sup>'
        elif type == "ni":
            if self.outputformat == "md":
                suffix = ' (ni)'
            else:
                suffix = '<sup class="sup-ni" title="named individual">ni</sup>'
        else:
            suffix = ''

        return link + suffix

    def _expand_graph(self):
        # name
        for s, o in chain(
                self.G.subject_objects(DC.title),
                self.G.subject_objects(RDFS.label),
                self.G.subject_objects(SKOS.prefLabel),
                self.G.subject_objects(SDO.name)
        ):
            self.G.add((s, DCTERMS.title, o))

        # description
        for s, o in chain(
                self.G.subject_objects(DC.description),
                self.G.subject_objects(RDFS.comment),
                self.G.subject_objects(SKOS.definition),
                self.G.subject_objects(SDO.description)
        ):
            self.G.add((s, DCTERMS.description, o))

        # property types
        for s in chain(
                self.G.subjects(RDF.type, OWL.ObjectProperty),
                self.G.subjects(RDF.type, OWL.FunctionalProperty),
                self.G.subjects(RDF.type, OWL.DatatypeProperty),
                self.G.subjects(RDF.type, OWL.AnnotationProperty)
        ):
            self.G.add((s, RDF.type, RDF.Property))

        # class types
        for s in self.G.subjects(RDF.type, OWL.Class):
            self.G.add((s, RDF.type, RDFS.Class))

        # owl:Restrictions from Blank Nodes
        for s in self.G.subjects(OWL.onProperty):
            self.G.add((s, RDF.type, OWL.Restriction))

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

    def _extract_metadata(self):
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
        self.METADATA["editors"] = set()
        self.METADATA["funders"] = set()
        self.METADATA["translators"] = set()
        for s in self.G.subjects(predicate=RDF.type, object=OWL.Ontology):
            s_str = str(s)  # this is the Ontology's URI
            self.METADATA["uri"] = s_str

            for p, o in self.G.predicate_objects(subject=s):
                if p == OWL.imports:
                    self.METADATA["imports"].add(self._make_formatted_uri(o))

                if p == DCTERMS.title:
                    self.METADATA["title"] = str(o)

                if p == DCTERMS.description:
                    self.METADATA["description"] = markdown.markdown(str(o))

                if p == SKOS.historyNote:
                    self.METADATA["historyNote"] = markdown.markdown(str(o))

                # dates
                if p in [DCTERMS.created, DCTERMS.modified, DCTERMS.issued]:
                    date_type = p.split("/")[-1]
                    self.METADATA[date_type] = str(o)

                if p == DCTERMS.source:
                    if str(o).startswith('http'):
                        self.METADATA["source"] = self._make_formatted_uri(o)
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
                if p in [
                    DCTERMS.creator, DCTERMS.contributor, DCTERMS.publisher, SDO.editor, SDO.funder, SDO.translator
                ]:
                    agent_type = p.split("/")[-1] + "s"
                    if type(o) == Literal:
                        self.METADATA[agent_type].add(str(o))
                    else:  # Blank Node or URI
                        self.METADATA[agent_type].add(self._make_agent(o))

                if p == PROV.wasGeneratedBy:
                    for o2 in self.G.objects(subject=o, predicate=DOAP.repository):
                        self.METADATA["repository"] = self._make_formatted_uri(o2)

                if p == SDO.codeRepository:
                    self.METADATA["repository"] = self._make_formatted_uri(o)

            if self.METADATA.get("title") is None:
                self.METADATA["title"] = "{no title found}"
                # raise ValueError(
                #     "Your ontology does not indicate any form of label or title. "
                #     "You must declare one of the following for your ontology: rdfs:label, dct:title, skos:prefLabel"
                # )

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
                if p == DCTERMS.title:
                    self.CLASSES[cls]["title"] = str(o)

                if p == DCTERMS.description:
                    self.CLASSES[cls]["description"] = markdown.markdown(str(o))

                if p == SKOS.scopeNote:
                    self.CLASSES[cls]["scopeNote"] = markdown.markdown(str(o))

                if p == SKOS.example:
                    self.CLASSES[cls]["example"] = str(o)

                if p == RDFS.isDefinedBy:
                    self.CLASSES[cls]["isDefinedBy"] = str(o)

                if p == DCTERMS.source or p == DC.source:
                    if str(o).startswith('http'):
                        self.CLASSES[cls]["source"] = self._make_formatted_uri(o)  # '<a href="{0}">{0}</a>'.format(str(o))
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
            has_members = []
            for o in self.G.subjects(predicate=RDF.type, object=s):
                has_members.append(str(o))
            self.CLASSES[cls]["has_members"] = has_members

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

                if p == DCTERMS.description:
                    self.PROPERTIES[prop]["description"] = markdown.markdown(str(o))

                if p == SKOS.scopeNote:
                    self.PROPERTIES[prop]["scopeNote"] = markdown.markdown(str(o))

                if p == SKOS.example:
                    self.PROPERTIES[prop]["example"] = str(o)

                if p == RDFS.isDefinedBy:
                    self.PROPERTIES[prop]["isDefinedBy"] = str(o)

                if p == DCTERMS.source or p == DC.source:
                    if str(o).startswith('http'):
                        self.PROPERTIES[prop]["source"] = self._make_formatted_uri(
                            o)  # '<a href="{0}">{0}</a>'.format(str(o))
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
            self.NAMED_INDIVIDUALS[ni]["appliesToWholeMaritimeArea"] = None
            self.NAMED_INDIVIDUALS[ni]["policyCode"] = None
            self.NAMED_INDIVIDUALS[ni]["directsOther"] = None
            self.NAMED_INDIVIDUALS[ni]["directsChapter"] = None

            for p, o in self.G.predicate_objects(subject=s):
                # list all the other classes of this NI
                if p == RDF.type:
                    if o != OWL.NamedIndividual:
                        self.NAMED_INDIVIDUALS[ni]["classes"].add(self._make_formatted_uri(o))

                if p == RDFS.label:
                    self.NAMED_INDIVIDUALS[ni]["title"] = str(o)

                if p == RDFS.comment:
                    self.NAMED_INDIVIDUALS[ni]["description"] = str(o)

                if p == RDFS.isDefinedBy:
                    self.NAMED_INDIVIDUALS[ni]["isDefinedBy"] = str(o)

                if p == DCTERMS.source or p == DC.source:
                    if str(o).startswith('http'):
                        self.NAMED_INDIVIDUALS[ni]["source"] = self._make_formatted_uri(
                            o)  # '<a href="{0}">{0}</a>'.format(str(o))
                    else:
                        self.NAMED_INDIVIDUALS[ni]["source"] = str(o)

                if p == RDFS.seeAlso:
                    self.NAMED_INDIVIDUALS[ni]["seeAlso"] = self._make_formatted_uri(o)

                if p == OWL.sameAs:
                    self.NAMED_INDIVIDUALS[ni]["sameAs"] = self._make_formatted_uri(o)

                if p == URIRef('http://something/national-marine-planning-framework-policies#appliesToWholeMaritimeArea'):
                    self.NAMED_INDIVIDUALS[ni]['appliesToWholeMaritimeArea'] = str(o)

                if p == URIRef('http://something/national-marine-planning-framework-policies#policyCode'):
                    self.NAMED_INDIVIDUALS[ni]['policyCode'] = str(o)

                if p == URIRef('http://something/national-marine-planning-framework-policies#directsOtherProposalsInRelationToTopicActivity'):
                    self.NAMED_INDIVIDUALS[ni]['directsOther'] = str(o)

                if p == URIRef('http://something/national-marine-planning-framework-policies#directsChapterTopicActivityProposals'):
                    self.NAMED_INDIVIDUALS[ni]['directsChapter'] = str(o)

            # patch title from URI if we haven't got one
            if self.NAMED_INDIVIDUALS[ni].get("title") is None:
                self.NAMED_INDIVIDUALS[ni]["title"] = self._make_title_from_uri(ni)

            # make fid
            self.NAMED_INDIVIDUALS[ni]["fid"] = self._make_fid(self.NAMED_INDIVIDUALS[ni]["title"], ni)

    def _make_metadata(self):
        return self._load_template("metadata." + self.outputformat).render(
            imports=sorted(self.METADATA["imports"]),
            title=self.METADATA.get("title"),
            uri=self.METADATA.get("uri"),
            version_uri=self.METADATA.get("versionIRI"),
            publishers=sorted(self.METADATA["publishers"]),
            creators=sorted(self.METADATA["creators"]),
            contributors=sorted(self.METADATA["contributors"]),
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
            ont_rdf=self._make_source_file_link(),
            has_classes=self.METADATA.get("has_classes"),
            has_ops=self.METADATA.get("has_ops"),
            has_fps=self.METADATA.get("has_fps"),
            has_dps=self.METADATA.get("has_dps"),
            has_aps=self.METADATA.get("has_aps"),
            has_ps=self.METADATA.get("has_ps"),
            has_nis=self.METADATA.get("has_nis"),
        )

    def _make_classes(self):
        # make all Classes
        class_template = self._load_template("class." + self.outputformat)
        classes_list = []
        for k, v in self.CLASSES.items():
            # handling Markdown formatting within a table
            if self.outputformat == "md":
                desc = v["description"].replace("\n", " ") if v.get("description") is not None else None
                if v.get("example") is not None:
                    eg = v["example"].strip().replace("\t", "    ").split("\n")
                    eg2 = ""
                    for line in eg:
                        eg2 += "`" + line + "`<br />"
                    eg = eg2
                else:
                    eg = None
            else:
                desc = v["description"]
                eg = v["example"].replace("<", "&lt;").replace(">", "&gt;") if v.get("example") is not None else None

            classes_list.append(
                class_template.render(
                    uri=k,
                    fid=v["fid"],
                    title=v["title"],
                    description=desc,
                    supers=v["supers"],
                    restrictions=v["restrictions"],
                    scopeNote=v["scopeNote"],
                    example=eg,
                    is_defined_by=v["isDefinedBy"],
                    source=v["source"],
                    subs=v["subs"],
                    in_domain_of=v["in_domain_of"],
                    in_domain_includes_of=v["in_domain_includes_of"],
                    in_range_of=v["in_range_of"],
                    in_range_includes_of=v["in_range_includes_of"],
                    has_members=v["has_members"]
                )
            )

        # make the template for all Classes
        classes_template = self._load_template("classes." + self.outputformat)
        # add in Class index
        fids = sorted(
            [(v.get("fid"), v.get("title")) for k, v in self.CLASSES.items()],
            key=lambda tup: tup[1],
        )
        return classes_template.render(fids=fids, classes=classes_list, )

    def _make_property(self, property):
        # handling Markdown formatting within a table
        if self.outputformat == "md":
            desc = property[1].get("description").replace("\n", " ") \
                if property[1].get("description") is not None else None
            if property[1].get("example") is not None:
                eg = property[1].get("example").strip().replace("\t", "    ").split("\n")
                eg2 = ""
                for line in eg:
                    eg2 += "`" + line + "`<br />"
                eg = eg2
            else:
                eg = None
        else:
            desc = property[1].get("description")
            eg = property[1].get("example")

        return self._load_template("property." + self.outputformat).render(
            uri=property[0],
            fid=property[1].get("fid"),
            property_type=property[1].get("prop_type"),
            title=property[1].get("title"),
            description=desc,
            scopeNote=property[1].get("scopeNote"),
            example=eg,
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

    def _make_properties(self):
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
                        self._make_property((k, v)),
                    )
                )
            elif v.get("prop_type") == "fp":
                fp_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v)),
                    )
                )
            elif v.get("prop_type") == "dp":
                dp_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v)),
                    )
                )
            elif v.get("prop_type") == "ap":
                ap_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v)),
                    )
                )
            elif v.get("prop_type") == "p":
                p_instances.append(
                    (
                        v["title"],
                        v["fid"],
                        self._make_property((k, v)),
                    )
                )

        # make the template for all properties
        return self._load_template("properties." + self.outputformat).render(
            op_instances=op_instances,
            fp_instances=fp_instances,
            dp_instances=dp_instances,
            ap_instances=ap_instances,
            p_instances=p_instances,
        )

    def _make_named_individual(self, named_individual):
        return self._load_template("named_individual." + self.outputformat).render(
            uri=named_individual[0],
            fid=named_individual[1].get("fid"),
            classes=named_individual[1].get("classes"),
            title=named_individual[1].get("title"),
            description=named_individual[1].get("description"),
            is_defined_by=named_individual[1].get("isDefinedBy"),
            source=named_individual[1].get("source"),
            see_also=named_individual[1].get("seeAlso"),
            same_as=named_individual[1].get("sameAs"),
            applies_whole=named_individual[1].get("appliesToWholeMaritimeArea"),
            policy_code=named_individual[1].get("policyCode"),
            directs_other=named_individual[1].get("directsOther"),
            directs_chapter=named_individual[1].get("directsChapter")
        )

    def _make_named_individuals(self):
        # make all NIs
        named_individuals_list = []
        for k, v in self.NAMED_INDIVIDUALS.items():
            named_individuals_list.append(
                self._make_named_individual((k, v))
            )

        # add in NIs index
        fids = []
        for k, v in self.NAMED_INDIVIDUALS.items():
            if v.get("fid") is not None:  # ensure BNodes not added
                fids.append((v.get("fid"), v.get("title")))
        fids = sorted(fids, key=lambda tup: tup[1])
        return self._load_template("named_individuals." + self.outputformat).render(
            fids=fids,
            named_individuals=named_individuals_list
        )

    def _make_document(self):
        css = None
        if self.outputformat == "html":
            if self.include_css:
                css = open(path.join(STYLE_DIR, "pylode.css")).read()

        return self._load_template("document." + self.outputformat).render(
            schemaorg=self._make_schemaorg_metadata(),  # only does something for the HTML templates
            title=self.METADATA["title"],
            metadata=self._make_metadata(),
            classes=self._make_classes(),
            properties=self._make_properties(),
            named_individuals=self._make_named_individuals(),
            default_namespace=self.METADATA["default_namespace"],
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
        self._extract_metadata()
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
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.PROPERTIES[uri]["supers"] = html

            html = []
            for p in prop["subs"]:
                prop_type = (
                    self.PROPERTIES.get(p).get("prop_type")
                    if self.PROPERTIES.get(p)
                    else None
                )
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.PROPERTIES[uri]["subs"] = html

            html = []
            for p in prop["equivs"]:
                prop_type = (
                    self.PROPERTIES.get(p).get("prop_type")
                    if self.PROPERTIES.get(p)
                    else None
                )
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.PROPERTIES[uri]["equivs"] = html

            html = []
            for p in prop["invs"]:
                prop_type = (
                    self.PROPERTIES.get(p).get("prop_type")
                    if self.PROPERTIES.get(p)
                    else None
                )
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.PROPERTIES[uri]["invs"] = html

            html = []
            for d in prop["domains"]:
                if type(d) == tuple:
                    html.append(self._make_collection_class_html(d[0], d[1]))
                else:
                    html.append(self._make_formatted_uri(d, type="c"))
            self.PROPERTIES[uri]["domains"] = html

            html = []
            for d in prop["domainIncludes"]:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_formatted_uri(m, type="c"))
                else:
                    html.append(self._make_formatted_uri(d, type="c"))
            self.PROPERTIES[uri]["domainIncludes"] = html

            html = []
            for d in prop["ranges"]:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_formatted_uri(m, type="c"))
                else:
                    html.append(self._make_formatted_uri(d, type="c"))
            self.PROPERTIES[uri]["ranges"] = html

            html = []
            for d in prop["rangeIncludes"]:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_formatted_uri(m, type="c"))
                else:
                    html.append(self._make_formatted_uri(d, type="c"))
            self.PROPERTIES[uri]["rangeIncludes"] = html

        # crosslinking classes
        for uri, cls in self.CLASSES.items():
            html = []
            for d in cls["equivalents"]:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_formatted_uri(m, type="c"))
                else:
                    html.append(self._make_formatted_uri(d, type="c"))
            self.CLASSES[uri]["equivalents"] = html

            html = []
            for d in cls["supers"]:
                if type(d) == tuple:
                    html.append(self._make_collection_class_html(d[0], d[1]))
                else:
                    html.append(self._make_formatted_uri(d, type="c"))
            self.CLASSES[uri]["supers"] = html

            html = []
            for d in cls["restrictions"]:
                html.append(self._make_restriction_html(uri, d))
            self.CLASSES[uri]["restrictions"] = html

            html = []
            for d in cls["subs"]:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_formatted_uri(m, type="c"))
                else:
                    html.append(self._make_formatted_uri(d, type="c"))
            self.CLASSES[uri]["subs"] = html

            html = []
            for p in cls["in_domain_of"]:
                prop_type = (
                    self.PROPERTIES.get(p).get("prop_type")
                    if self.PROPERTIES.get(p)
                    else None
                )
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.CLASSES[uri]["in_domain_of"] = html

            html = []
            for p in cls["in_domain_includes_of"]:
                prop_type = (
                    self.PROPERTIES.get(p).get("prop_type")
                    if self.PROPERTIES.get(p)
                    else None
                )
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.CLASSES[uri]["in_domain_includes_of"] = html

            html = []
            for p in cls["in_range_of"]:
                prop_type = (
                    self.PROPERTIES.get(p).get("prop_type")
                    if self.PROPERTIES.get(p)
                    else None
                )
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.CLASSES[uri]["in_range_of"] = html

            html = []
            for p in cls["in_range_includes_of"]:
                prop_type = (
                    self.PROPERTIES.get(p).get("prop_type")
                    if self.PROPERTIES.get(p)
                    else None
                )
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.CLASSES[uri]["in_range_includes_of"] = html

            html = []
            for p in cls["has_members"]:
                prop_type = (
                    self.PROPERTIES.get(p).get("prop_type")
                    if self.PROPERTIES.get(p)
                    else None
                )
                html.append(self._make_formatted_uri(p, type=prop_type))
            self.CLASSES[uri]["has_members"] = html

        return self._make_document()
