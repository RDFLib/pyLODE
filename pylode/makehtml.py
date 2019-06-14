from rdflib import Graph, RDF, RDFS, OWL, Namespace
from rdflib.namespace import SKOS, DC, DCTERMS, FOAF
from rdflib.term import URIRef, Literal, BNode
from os import path
import requests
import collections
import dateutil.parser
from jinja2 import Environment, FileSystemLoader


class MakeHtml:
    def __init__(self):
        # shared variables
        self.APP_DIR = path.dirname(path.realpath(__file__))
        self.CLASSES = collections.OrderedDict()
        self.PROPERTIES = collections.OrderedDict()
        self.NAMESPACES = collections.OrderedDict()
        self.FIDS = {}
        self.METADATA = {}

        self.G = Graph()
        self.SDO = Namespace('https://schema.org/')
        self.G.bind('sdo', self.SDO)

        self.SDO2 = Namespace('http://schema.org/')
        self.G.bind('sdo2', self.SDO2)

    def _expand_graph_for_pylode(self):
        # name
        for s, o in self.G.subject_objects(predicate=DC.title):
            self.G.add((s, RDFS.label, o))

        for s, o in self.G.subject_objects(predicate=DCTERMS.title):
            self.G.add((s, RDFS.label, o))

        for s, o in self.G.subject_objects(predicate=SKOS.prefLabel):
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

    def _extract_properties_uris(self):
        properties = []
        for s in self.G.subjects(predicate=RDF.type, object=RDF.Property):
            properties.append(str(s))

        for p in sorted(properties):
            self.PROPERTIES[p] = {}

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

    def _get_namespace_from_uri(self, uri):
        # split on hash
        segments = uri.split('#')
        if len(segments) == 2:
            return segments[0] + '#'
        else:
            segments = uri.split('/')
            if len(segments) > 1:
                return '/'.join(segments[0:-1]) + '/'
            else:
                return None

    def _get_curie_prefix(uself, uri, existing_curies):
        ns_count = 0

        from curies import CURIES

        # TODO: replace this with a once-per run update CURIES function
        def get_curie_online(uri):
            try:
                r = requests.get(
                    'http://prefix.cc/reverse',
                    params={
                        'uri': uri,
                        'format': 'txt'
                    }
                )
                if r.status_code == 200:
                    # primitive check to see if it really is prefix.cc replying with a text/plain response
                    if r.headers['Content-Type'] == 'text/plain':
                        return r.text.split('\t')[0]
                    else:
                        return None
                else:
                    return None
            except requests.exceptions.ConnectionError:
                # presumably this module can't access the internet or prefix.cc is down
                return None

        def get_curie_from_namespace(uri, existing_curies, ns_count):
            # strip off trailing hash or slash and return last path segment
            c = uri.rstrip('#/').split('/')[-1]

            # prevent CURIE collision = return nsX (x int) if we already have this one
            if c in existing_curies:
                ns_count += 1
                return 'ns' + str(ns_count)

            return c

        # attempt to look up the well-known curie for this Namespace in http://prefix.cc dump
        for k, v in CURIES.items():
            if v == uri:
                return k

        # attempt to look up the well-known CURIE for this Namespace using http://prefix.cc online (more up-to-date)
        c = get_curie_online(uri)
        if c is not None:
            return c

        # can't fund CURIE online so make up one
        c = get_curie_from_namespace(uri, existing_curies, ns_count)
        return c if c is not None else ''

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
            # and individuals (self.SDO.identifier)
            # exclude known annoying URIs (ORCID)
            if p == OWL.versionIRI or \
                    p == OWL.imports or \
                    p == self.SDO.identifier or self.SDO2.identifier or \
                    str(o).startswith('https://orcid'):
                pass
            else:
                # add only URI subjects (not Blank Nodes)
                if type(s) == URIRef:
                    uri_bases.add(self._get_namespace_from_uri(str(s)))

                # predicates are always URIs so add them all
                uri_bases.add(self._get_namespace_from_uri(str(p)))

                # add only URI objects (not Blank Nodes or Literals), exclude emails
                if type(o) == URIRef and '@' not in str(o):
                    uri_bases.add(self._get_namespace_from_uri(str(o)))

        # for the de-duplicated URIs, if the uri_base is not in namespaces, get CURIE and add it
        for uri_base in uri_bases:
            if ns.get(uri_base) is None:
                uri_prefix = self._get_curie_prefix(uri_base, [x for x in ns.values()])
                ns[uri_base] = uri_prefix

        # invert the key/values in instances
        for k, v in sorted(ns.items(), key=lambda x: x[1]):
            self.NAMESPACES[v] = k

    def _extract_properties(self):
        for prop in self.PROPERTIES.keys():
            s = URIRef(prop)
            # property type
            if (s, RDF.type, OWL.ObjectProperty) in self.G:
                self.PROPERTIES[prop]['prop_type'] = 'op'
            elif (s, RDF.type, OWL.DatatypeProperty) in self.G:
                self.PROPERTIES[prop]['prop_type'] = 'dp'
            elif (s, RDF.type, OWL.AnnotationProperty) in self.G:
                self.PROPERTIES[prop]['prop_type'] = 'ap'
            else:
                self.PROPERTIES[prop]['prop_type'] = 'p'

            self.PROPERTIES[prop]['title'] = None
            self.PROPERTIES[prop]['description'] = None
            self.PROPERTIES[prop]['scopeNote'] = None
            self.PROPERTIES[prop]['isDefinedBy'] = None

            for p, o in self.G.predicate_objects(subject=s):
                if p == RDFS.label:
                    self.PROPERTIES[prop]['title'] = str(o)

                if p == RDFS.comment:
                    self.PROPERTIES[prop]['description'] = str(o)

                if p == SKOS.scopeNote:
                    self.PROPERTIES[prop]['scopeNote'] = str(o)

                if p == RDFS.isDefinedBy:
                    self.PROPERTIES[prop]['isDefinedBy'] = str(o)

            # patch title from URI if we haven't got one
            if self.PROPERTIES[prop]['title'] is None:
                self.PROPERTIES[prop]['title'] = self._make_title_from_uri(prop)

            # make fid
            self.PROPERTIES[prop]['fid'] = self._make_fid(self.PROPERTIES[prop]['title'], prop)

            # super properties
            supers = []
            for o in self.G.objects(subject=s, predicate=RDFS.subPropertyOf):
                if type(o) != BNode:
                    supers.append(str(o))  # self._make_uri_html
            self.PROPERTIES[prop]['supers'] = supers

            # sub properties
            subs = []
            for o in self.G.subjects(predicate=RDFS.subPropertyOf, object=s):
                if type(o) != BNode:
                    subs.append(str(o))
            self.PROPERTIES[prop]['subs'] = subs

            # TODO: cater for equvalentProperty

            # domains
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

            # domainIncludes
            domain_includes = []
            for o in self.G.objects(subject=s, predicate=self.SDO.domainIncludes):
                if type(o) != BNode:
                    domain_includes.append(str(o))  # domainIncludes that are just classes
                else:
                    # domainIncludes collections (unionOf | intersectionOf
                    q = '''
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX sdo: <https://schema.org/>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> sdo:domainIncludes ?domainIncludes .  
                            ?domainIncludes owl:unionOf|owl:intersectionOf ?collection .
                            ?domainIncludes ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    '''.format(s)
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    domain_includes.append((collection_type, collection_members))
            self.PROPERTIES[prop]['domainIncludes'] = domain_includes

            domain_includes = []
            for o in self.G.objects(subject=s, predicate=self.SDO2.domainIncludes):
                if type(o) != BNode:
                    domain_includes.append(str(o))  # domainIncludes that are just classes
                else:
                    # domainIncludes collections (unionOf | intersectionOf
                    q = '''
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX sdo2: <https://schema.org/>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> sdo2:domainIncludes ?domainIncludes .  
                            ?domainIncludes owl:unionOf|owl:intersectionOf ?collection .
                            ?domainIncludes ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    '''.format(s)
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    domain_includes.append((collection_type, collection_members))
            self.PROPERTIES[prop]['domainIncludes'] = domain_includes

            # ranges
            ranges = []
            for o in self.G.objects(subject=s, predicate=RDFS.range):
                if type(o) != BNode:
                    ranges.append(str(o))  # ranges that are just classes
                else:
                    # range collections (unionOf | intersectionOf
                    q = '''
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> rdfs:range ?range .  
                            ?range owl:unionOf|owl:intersectionOf ?collection .
                            ?range ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    '''.format(s)
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    ranges.append((collection_type, collection_members))
            self.PROPERTIES[prop]['ranges'] = ranges

            # rangeIncludes
            range_includes = []
            for o in self.G.objects(subject=s, predicate=self.SDO.rangeIncludes):
                if type(o) != BNode:
                    range_includes.append(str(o))  # rangeIncludes that are just classes
                else:
                    # rangeIncludes collections (unionOf | intersectionOf
                    q = '''
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX sdo: <https://schema.org/>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> sdo:rangeIncludes ?rangeIncludes .  
                            ?rangeIncludes owl:unionOf|owl:intersectionOf ?collection .
                            ?rangeIncludes ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    '''.format(s)
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    range_includes.append((collection_type, collection_members))
            self.PROPERTIES[prop]['rangeIncludes'] = range_includes

            range_includes = []
            for o in self.G.objects(subject=s, predicate=self.SDO2.rangeIncludes):
                if type(o) != BNode:
                    range_includes.append(str(o))  # rangeIncludes that are just classes
                else:
                    # rangeIncludes collections (unionOf | intersectionOf
                    q = '''
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX sdo2: <http://schema.org/>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> sdo2:rangeIncludes ?rangeIncludes .  
                            ?rangeIncludes owl:unionOf|owl:intersectionOf ?collection .
                            ?rangeIncludes ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    '''.format(s)
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(str(r.col_member))
                    range_includes.append((collection_type, collection_members))
            self.PROPERTIES[prop]['rangeIncludes'] = range_includes

            # TODO: cater for sub property chains

        # # sort properties by title
        # x = sorted([(k, v) for k, v in self.PROPERTIES.items()], key=lambda tup: tup[1]['title'])
        # y = collections.OrderedDict()
        # for n in x:
        #     y[n[0]] = n[1]
        #
        # return y

    def _extract_classes(self):
        for cls in self.CLASSES.keys():
            s = URIRef(cls)
            # create Python dict for each class
            self.CLASSES[cls] = {}

            # basic class properties
            self.CLASSES[cls]['title'] = None
            self.CLASSES[cls]['description'] = None
            self.CLASSES[cls]['scopeNote'] = None
            self.CLASSES[cls]['isDefinedBy'] = None

            for p, o in self.G.predicate_objects(subject=s):
                if p == RDFS.label:
                    self.CLASSES[cls]['title'] = str(o)

                if p == RDFS.comment:
                    self.CLASSES[cls]['description'] = str(o)

                if p == SKOS.scopeNote:
                    self.CLASSES[cls]['scopeNote'] = str(o)

                if p == RDFS.isDefinedBy:
                    self.CLASSES[cls]['isDefinedBy'] = str(o)

            # patch title from URI if we haven;t got one
            if self.CLASSES[cls]['title'] is None:
                self.CLASSES[cls]['title'] = self._make_title_from_uri(cls)

            # make fid
            self.CLASSES[cls]['fid'] = self._make_fid(self.CLASSES[cls]['title'], cls)

            # equivalent classes
            equivalent_classes = []
            for o in self.G.objects(subject=s, predicate=OWL.equivalentClass):
                if type(o) != BNode:
                    equivalent_classes.append(self._get_curie(str(o)))  # ranges that are just classes
                else:
                    # equivalent classes collections (unionOf | intersectionOf
                    q = '''
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            <{}> owl:equivalentClass ?eq .  
                            ?eq owl:unionOf|owl:intersectionOf ?collection .
                            ?eq ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    '''.format(s)
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(self._get_curie(str(r.col_member)))
                    equivalent_classes.append((collection_type, collection_members))
            self.CLASSES[cls]['equivalents'] = equivalent_classes

            # super classes
            supers = []
            restrictions = []
            for o in self.G.objects(subject=s, predicate=RDFS.subClassOf):
                if (o, RDF.type, OWL.Restriction) not in self.G:
                    if type(o) != BNode:
                        supers.append(str(o))  # supers that are just classes
                    else:
                        # super collections (unionOf | intersectionOf
                        q = '''
                            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
        
                            SELECT ?col_type ?col_member
                            WHERE {{
                                <{}> rdfs:subClassOf ?sup .  
                                ?sup owl:unionOf|owl:intersectionOf ?collection .
                                ?sup ?col_type ?collection . 
                                ?collection rdf:rest*/rdf:first ?col_member .              
                            }} 
                        '''.format(s)
                        collection_type = None
                        collection_members = []
                        for r in self.G.query(q):
                            collection_type = self._get_curie(str(r.col_type))
                            collection_members.append(str(r.col_member))
                        supers.append((collection_type, collection_members))
                else:
                    restrictions.append(o)

            self.CLASSES[cls]['supers'] = supers
            self.CLASSES[cls]['restrictions'] = restrictions

            # sub classes
            subs = []
            for o in self.G.subjects(predicate=RDFS.subClassOf, object=s):
                if type(o) != BNode:
                    subs.append(str(o))
                else:
                    # sub classes collections (unionOf | intersectionOf
                    q = '''
                        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
                        SELECT ?col_type ?col_member
                        WHERE {{
                            ?sub rdfs:subClassOf <{}> . 
                            ?sub owl:unionOf|owl:intersectionOf ?collection .
                            ?sub ?col_type ?collection . 
                            ?collection rdf:rest*/rdf:first ?col_member .              
                        }} 
                    '''.format(s)
                    collection_type = None
                    collection_members = []
                    for r in self.G.query(q):
                        collection_type = self._get_curie(str(r.col_type))
                        collection_members.append(self._get_curie(str(r.col_member)))
                    subs.append((collection_type, collection_members))
            self.CLASSES[cls]['subs'] = subs

            in_domain_of = []
            for o in self.G.subjects(predicate=RDFS.domain, object=s):
                in_domain_of.append(str(o))
            self.CLASSES[cls]['in_domain_of'] = in_domain_of

            in_domain_includes_of = []
            for o in self.G.subjects(predicate=self.SDO.domainIncludes, object=s):
                in_domain_includes_of.append(str(o))
            self.CLASSES[cls]['in_domain_includes_of'] = in_domain_includes_of

            in_range_of = []
            for o in self.G.subjects(predicate=RDFS.range, object=s):
                in_range_of.append(str(o))
            self.CLASSES[cls]['in_range_of'] = in_range_of

            in_range_includes_of = []
            for o in self.G.subjects(predicate=self.SDO.rangeIncludes, object=s):
                in_range_includes_of.append(str(o))
            self.CLASSES[cls]['in_range_includes_of'] = in_range_includes_of

            # TODO: cater for Named Individuals of this class - "has members"

        # # sort properties by title
        # x = sorted([(k, v) for k, v in classes.items()], key=lambda tup: tup[1]['title'])
        # y = collections.OrderedDict()
        # for n in x:
        #     y[n[0]] = n[1]
        #
        # return y

    def _extract_metadata(self):
        if len(self.CLASSES.keys()) > 0:
            self.METADATA['has_classes'] = True

        self.METADATA['has_ops'] = False
        self.METADATA['has_dps'] = False
        self.METADATA['has_aps'] = False
        self.METADATA['has_ps'] = False

        for k, v in self.PROPERTIES.items():
            if v.get('prop_type') == 'op':
                self.METADATA['has_ops'] = True
            if v.get('prop_type') == 'dp':
                self.METADATA['has_dps'] = True
            if v.get('prop_type') == 'ap':
                self.METADATA['has_aps'] = True
            if v.get('prop_type') == 'p':
                self.METADATA['has_ps'] = True

        s_str = None
        self.METADATA['imports'] = set()
        self.METADATA['creators'] = set()
        self.METADATA['contributors'] = set()
        self.METADATA['publishers'] = set()
        for s in self.G.subjects(predicate=RDF.type, object=OWL.Ontology):
            s_str = str(s)  # this is the Ontology's URI
            self.METADATA['uri'] = s_str

            for p, o in self.G.predicate_objects(subject=s):
                if p == OWL.imports:
                    self.METADATA['imports'].add(self._make_uri_html(o))

                if p == RDFS.label:
                    self.METADATA['title'] = str(o)

                if p == RDFS.comment:
                    import markdown
                    self.METADATA['description'] = markdown.markdown(str(o))

                if p == DCTERMS.created:
                    self.METADATA['created'] = dateutil.parser.parse(str(o)).strftime('%Y-%m-%d')

                if p == DCTERMS.modified:
                    self.METADATA['modified'] = dateutil.parser.parse(str(o)).strftime('%Y-%m-%d')

                if p == DCTERMS.issued:
                    self.METADATA['issued'] = dateutil.parser.parse(str(o)).strftime('%Y-%m-%d')

                if p == OWL.versionIRI:
                    self.METADATA['versionIRI'] = '<a href="{0}">{0}</a>'.format(str(o))

                if p == OWL.versionInfo:
                    self.METADATA['versionInfo'] = str(o)

                if p == URIRef('http://purl.org/vocab/vann/preferredNamespacePrefix'):
                    self.METADATA['preferredNamespacePrefix'] = str(o)

                if p == URIRef('http://purl.org/vocab/vann/preferredNamespaceUri'):
                    self.METADATA['preferredNamespaceUri'] = str(o)

                if p == DCTERMS.license:
                    self.METADATA['license'] = '<a href="{0}">{0}</a>'.format(str(o)) if str(o).startswith('http') else str(o)

                if p == DCTERMS.rights:
                    self.METADATA['rights'] = str(o).replace('Copyright', '&copy;').replace('copyright', '&copy;')

                # Agents
                if p == DC.creator:
                    if type(o) == URIRef:
                        self.METADATA['creators'].add('<a href="{0}">{0}</a>'.format(str(o)))
                    else:
                        self.METADATA['creators'].add(str(o))

                if p == DCTERMS.creator:
                    if type(o) == Literal or type(o) == URIRef:  # just treat a URI as a string
                        self.METADATA['creators'].add(str(o))
                    else:  # Blank Node
                        self.METADATA['creators'].add(self._make_agent_html(o))

                if p == DC.contributor:
                    if type(o) == URIRef:
                        self.METADATA['contributors'].add('<a href="{0}">{0}</a>'.format(str(o)))
                    else:
                        self.METADATA['contributors'].add(str(o))

                if p == DCTERMS.contributor:
                    if type(o) == Literal or type(o) == URIRef:  # just treat a URI as a string
                        self.METADATA['contributors'].add(str(o))
                    else:  # Blank Node
                        self.METADATA['contributors'].add(self._make_agent_html(o))

                if p == DC.publisher:
                    if type(o) == URIRef:
                        self.METADATA['publishers'].add('<a href="{0}">{0}</a>'.format(str(o)))
                    else:
                        self.METADATA['publishers'].add(str(o))

                if p == DCTERMS.publisher:
                    if type(o) == Literal or type(o) == URIRef:  # just treat a URI as a string
                        self.METADATA['publishers'].add(str(o))
                    else:  # Blank Node
                        self.METADATA['publishers'].add(self._make_agent_html(o))

                # TODO: cater for other Agent representations

            if self.METADATA.get('title') is None:
                raise ValueError(
                    'Your ontology does not indicate any form of label or title. '
                    'You must declare one of the following for your ontology: rdfs:label, dct:title, skos:prefLabel'
                )

        if s_str is None:
            raise Exception('Your RDF file does not define an ontology. '
                            'It must contains a declaration such as <...> rdf:type owl:Ontology .')

    def _make_title_from_uri(self, uri):
        # can't tolerate any URI faults so return None if anything is wrong

        # URIs with no path segments or ending in slash
        segments = uri.split('/')
        if len(segments[-1]) < 1:
            return None

        # URIs with only a domain - no path segments
        if len(segments) < 4:
            return None

        # URIs ending in hash
        if segments[-1].endswith('#'):
            return None

        return segments[-1].split('#')[-1] if segments[-1].split('#')[-1] != '' else segments[-1].split('#')[-2]

    # makes the fragment ID for a class, property, Named Individual (any entity) based on URI or name
    def _make_fid(self, title, uri):
        # does this URI already have a fid?
        existing_fid = self.FIDS.get(uri)
        if existing_fid is not None:
            return existing_fid

        # no, so make one
        def _remove_non_ascii_chars(s):
            return ''.join(i for i in s if ord(i) < 128)

        # try creating an ID from label
        # lowercase, remove spaces, escape all non-ASCII chars
        if title is not None:
            fid = _remove_non_ascii_chars(title.lower().replace(' ', ''))

            # do not return fid if it's already in use
            if fid not in self.FIDS.values():
                self.FIDS[uri] = fid
                return fid

        # this fid is already present so generate a new one from the URI instead

        # split URI for last slash segment
        segments = uri.split('/')
        # return None for empty string - URI ends in slash
        if len(segments[-1]) < 1:
            return None

        # return None for domains, i.e. ['http:', '', '{domain}'] - no path segments
        if len(segments) < 4:
            return None

        # split out hash URIs
        # remove any training hashes
        if segments[-1].endswith('#'):
            return None

        fid = segments[-1].split('#')[-1] if segments[-1].split('#')[-1] != '' else segments[-1].split('#')[-2]
        fid = fid.lower()

        # do not return fid if it's already in use
        if fid not in self.FIDS.values():
            self.FIDS[uri] = fid
            return fid
        else:
            # since it's in use but we've exhausted generation options, just add 1 to existing fid name
            self.FIDS[uri] = fid + '1'
            return fid + '1'  # yeah yeah, there could be more than one but unlikely

    def _get_default_namespace(self):
        self.METADATA['default_namespace'] = None

        # if this ontology declares a preferred URI, use that
        if self.METADATA.get('preferredNamespaceUri'):
           self.METADATA['default_namespace'] = self.METADATA.get('preferredNamespaceUri')

        # if not, try the URI of the ontology compared to all prefixes
        for s in self.G.subjects(predicate=RDF.type, object=OWL.Ontology):
            ont_uri = str(s)
        for k, v in self.NAMESPACES.items():
            # i.e. the ontology URI is the same as the default namespace + / or #
            if v == ont_uri + '/' or v == ont_uri + '#':
                self.METADATA['default_namespace'] = v

        if self.NAMESPACES.get('') is not None:
            del(self.NAMESPACES[''])

    def _make_namespaces_html(self):
        template_dir = path.join(path.dirname(path.realpath(__file__)), 'templates')
        namespaces_template = Environment(loader=FileSystemLoader(template_dir)).get_template('namespaces.html')
        namespaces_html = namespaces_template.render(
            namespaces=self.NAMESPACES,
            default_namespace=self.METADATA['default_namespace']
        )

        return namespaces_html

    def _make_uri_html(self, uri, type=None):
        # set display to CURIE
        short = self._get_curie(uri)
        # if the URI base is within the default namespace of this ontology
        #   use the fragment URI
        # else
        #   use the given URI
        uri_base = self._get_namespace_from_uri(uri)
        if uri_base == self.METADATA.get('default_namespace'):
            if self.PROPERTIES.get(uri):
                html = '<a href="#{}">{}</a>'.format(self.PROPERTIES[uri]['fid'], short)
            elif self.CLASSES.get(uri):
                html = '<a href="#{}">{}</a>'.format(self.CLASSES[uri]['fid'], short)
            else:
                html = '<a href="{}">{}</a>'.format(uri, short)
        else:
            html = '<a href="{}">{}</a>'.format(uri, short)

        if type == 'c':
            return html + ' <sup class="sup-c" title="class">c</sup>'
        elif type == 'op':
            return html + ' <sup class="sup-op" title="object property">op</sup>'
        elif type == 'dp':
            return html + ' <sup class="sup-dp" title="datatype property">dp</sup>'
        elif type == 'ap':
            return html + ' <sup class="sup-ap" title="annotation property">ap</sup>'
        else:
            return html

    def _make_collection_class_html(self, col_type, col_members):
        if col_type == 'owl:unionOf':
            j = ' or '
        elif col_type == 'owl:intersectionOf':
            j = ' and '
        else:
            j = ' ? '
        # others...
        return '({})'.format(j.join([self._make_uri_html(x, type='c') for x in col_members]))

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
                        t = self.PROPERTIES[str(o2)]['prop_type']
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
                        q = '''
                            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
                            SELECT ?col_type ?col_member
                            WHERE {{
                                <{}> owl:onClass ?onClass .  
                                ?onClass owl:unionOf|owl:intersectionOf ?collection .
                                ?onClass ?col_type ?collection . 
                                ?collection rdf:rest*/rdf:first ?col_member .              
                            }} 
                        '''.format(str(subject))
                        collection_type = None
                        collection_members = []
                        for r in self.G.query(q):
                            collection_type = self._get_curie(str(r.col_type))
                            collection_members.append(str(r.col_member))

                        cls = self._make_collection_class_html2(collection_type, collection_members)
                    else:
                        cls = self._make_uri_html(str(o2), type='c')
                elif p2 in [
                    OWL.cardinality,
                    OWL.qualifiedCardinality,
                    OWL.minCardinality,
                    OWL.minQualifiedCardinality,
                    OWL.maxCardinality,
                    OWL.maxQualifiedCardinality,
                ]:
                    if p2 in [OWL.minCardinality, OWL.minQualifiedCardinality]:
                        card = 'min'
                    elif p2 in [OWL.maxCardinality, OWL.maxQualifiedCardinality]:
                        card = 'max'
                    elif p2 in [OWL.cardinality, OWL.qualifiedCardinality]:
                        card = 'exactly'

                    card = '<span class="cardinality">{}</span> {}'.format(card, str(o2))
                elif p2 in [OWL.allValuesFrom, OWL.someValuesFrom]:
                    if p2 == OWL.allValuesFrom:
                        card = 'only'
                    else:  # p2 == OWL.someValuesFrom
                        card = 'some'

                    if type(o2) == BNode:
                        # someValuesFrom collections (unionOf | intersectionOf
                        q = '''
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
                        '''.format(str(subject), str(o2))
                        collection_type = None
                        collection_members = []
                        for r in self.G.query(q):
                            collection_type = self._get_curie(str(r.col_type))
                            collection_members.append(str(r.col_member))

                        c = self._make_collection_class_html(collection_type, collection_members)
                    else:
                        c = self._make_uri_html(str(o2), type='c')
                    card = '<span class="cardinality">{}</span> {}'.format(card, c)
                elif p2 == OWL.hasValue:
                    card = '<span class="cardinality">value</span> {}'.format(self._make_uri_html(str(o2), type='c'))

        restriction = prop + ' ' + card if card is not None else prop
        restriction = restriction + ' ' + cls if cls is not None else restriction

        return restriction

    def _get_curie(self, uri):
        n = self._get_namespace_from_uri(str(uri))
        for k, v in self.NAMESPACES.items():
            if v == n:
                return '{}:{}'.format(k, self._get_uri_id(uri))

            # try finding a match after removing / or # before giving up
            if v.strip('/#') == n:
                return '{}:{}'.format(k, self._get_uri_id(uri))

        # if no match, return the original URI
        return uri

    def _get_uri_id(self, uri):
        # split on hash
        segments = uri.split('#')
        if len(segments) == 2:
            return segments[1]
        else:
            return uri.split('/')[-1]  # could return None if URI ends in /

    def _make_agent_link(self, name, url=None, email=None):
        if url is not None and email is not None:
            agent = '<a href="{0}">{1}</a> (<a href="mailto:{2}">{2}</a>)'.format(url, name, email)
        elif url is not None and email is None:
            agent = '<a href="{0}">{1}</a>'.format(url, name)
        elif url is None and email is not None:
            agent = '<a href="mailto:{0}">{1}</a>'.format(email.split('/')[-1], name)
        elif url is not None:
            agent = '<a href="{}">{}</a>'.format(url, name)
        else:
            agent = name

        return agent

    def _make_agent_html(self, agent_blank_node):
        agent = None
        # we understand foaf:name, foaf:homepage & sdo:name & sdo:identifier & sdo:email (as a URI)
        # TODO: cater for other Agent representations

        name = None
        url = None
        email = None
        org_name = None
        org_url = None
        org_email = None
        for p, o in self.G.predicate_objects(subject=agent_blank_node):
            if p == FOAF.homepage or p == self.SDO.identifier or p == self.SDO2.identifier:
                url = str(o)
            elif p == FOAF.name or p == self.SDO.name or p == self.SDO2.name:
                name = str(o)
            elif p == FOAF.mbox or p == self.SDO.email or p == self.SDO2.email:
                email = str(o).split('/')[-1].split('#')[-1]  # remove base URI leaving only email address
            elif p == self.SDO.memberOf or p == self.SDO2.memberOf:
                for p2, o2 in self.G.predicate_objects(subject=o):
                    if p2 == FOAF.homepage or p2 == self.SDO.identifier or p2 == self.SDO2.identifier:  # TODO: split homepage form IDs, cater for rdfs:seeOther
                        org_url = str(o2)
                    elif p2 == FOAF.name or p2 == self.SDO.name or p2 == self.SDO2.name:
                        org_name = str(o2)
                    elif p == FOAF.mbox or p == self.SDO.email or p == self.SDO2.email:
                        org_email = str(o2).split('/')[-1].split('#')[-1]  # remove base URI leaving only email address

        agent = self._make_agent_link(name, url=url, email=email)

        if org_name is not None:
            org = self._make_agent_link(org_name, url=org_url, email=org_email)
            agent += ' of ' + org

        return agent

    def _make_source_file_link(self, source_info):
        return '<a href="{}">RDF ({})</a>'.format(source_info[0].split('/')[-1], source_info[1])

    def _make_property_html(self, property):
        template_dir = path.join(path.dirname(path.realpath(__file__)), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('property.html')

        return template.render(
            uri=property[0],
            fid=property[1].get('fid'),
            property_type=property[1].get('prop_type'),
            title=property[1].get('title'),
            description=property[1].get('description'),
            scopeNote=property[1].get('scopeNote'),
            supers=property[1].get('supers'),
            subs=property[1].get('subs'),
            domains=property[1]['domains'],
            domainIncludes=property[1]['domainIncludes'],
            ranges=property[1]['ranges'],
            rangeIncludes=property[1]['rangeIncludes'],
        )

    def _make_properties_html(self):
        template_dir = path.join(path.dirname(path.realpath(__file__)), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('properties.html')
        op_instances = []
        dp_instances = []
        ap_instances = []
        p_instances = []

        for k, v in self.PROPERTIES.items():
            if v.get('prop_type') == 'op':
                op_instances.append((v['title'], v['fid'], self._make_property_html((k, v))))
            elif v.get('prop_type') == 'dp':
                dp_instances.append((v['title'], v['fid'], self._make_property_html((k, v))))
            elif v.get('prop_type') == 'ap':
                ap_instances.append((v['title'], v['fid'], self._make_property_html((k, v))))
            elif v.get('prop_type') == 'p':
                p_instances.append((v['title'], v['fid'], self._make_property_html((k, v))))

        html = template.render(
            op_instances=op_instances,
            dp_instances=dp_instances,
            ap_instances=ap_instances,
            p_instances=p_instances
        )

        return html

    def _make_classes_html(self):
        template_dir = path.join(path.dirname(path.realpath(__file__)), 'templates')
        class_template = Environment(loader=FileSystemLoader(template_dir)).get_template('class.html')
        class_htmls = []
        for k, v in self.CLASSES.items():
            class_htmls.append(
                class_template.render(
                    uri=k,
                    fid=v['fid'],
                    title=v['title'],
                    description=v['description'],
                    supers=v['supers'],
                    restrictions=v['restrictions'],
                    subs=v['subs'],
                    in_domain_of=v['in_domain_of'],
                    in_domain_includes_of=v['in_domain_includes_of'],
                    in_range_of=v['in_range_of'],
                    in_range_includes_of=v['in_range_includes_of']
                )
            )

        classes_template = Environment(loader=FileSystemLoader(template_dir)).get_template('classes.html')
        fids = sorted([(v.get('fid'), v.get('title')) for k, v in self.CLASSES.items()], key=lambda tup: tup[1])
        classes_html = classes_template.render(
            fids=fids,
            classes=class_htmls,
        )

        return classes_html

    def _make_metadata_html(self, source_info):
        template_dir = path.join(path.dirname(path.realpath(__file__)), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('metadata.html')
        html = template.render(
            imports=self.METADATA['imports'],
            title=self.METADATA.get('title'),
            uri=self.METADATA.get('uri'),
            version_uri=self.METADATA.get('versionIRI'),
            publishers=self.METADATA['publishers'],
            creators=self.METADATA['creators'],
            contributors=self.METADATA['contributors'],
            created=self.METADATA.get('created'),  # TODO: auto-detect format
            modified=self.METADATA.get('modified'),
            issued=self.METADATA.get('issued'),
            description=self.METADATA.get('description'),
            version_info=self.METADATA.get('versionInfo'),
            license=self.METADATA.get('license'),
            rights=self.METADATA.get('rights'),
            ont_source=self._make_source_file_link(source_info),
            has_classes=self.METADATA.get('has_classes'),
            has_ops=self.METADATA.get('has_ops'),
            has_dps=self.METADATA.get('has_dps'),
            has_aps=self.METADATA.get('has_aps'),
            has_ps=self.METADATA.get('has_ps'),
            has_nis=False
        )

        return html

    def _make_document_html(self, title, metadata_html, classes_html, properties_html, default_namespace, namespaces_html):
        template_dir = path.join(path.dirname(path.realpath(__file__)), 'templates')
        document_template = Environment(loader=FileSystemLoader(template_dir)).get_template('document.html')
        html = document_template.render(
            title=title,
            metadata_html=metadata_html,
            classes_html=classes_html,
            properties_html=properties_html,
            default_namespace=default_namespace,
            namespaces_html=namespaces_html
        )

        return html

    def generate_html(self, source_info):
        # add some extra triples to the graph for easier querying
        self._expand_graph_for_pylode()
        # get the IDs (URIs) of all properties -> self.PROPERTIES
        self._extract_properties_uris()
        # get the IDs (URIs) of all classes -> CLASSES
        self._extract_classes_uris()
        # get all the namespaces using several methods
        self._extract_namespaces()
        # get all the properties' details
        self._extract_properties()
        # get all the classes' details
        self._extract_classes()
        # get the ontology's metadata
        self._extract_metadata()
        # get the default namespace
        self._get_default_namespace()
        # create fragment URIs for default namespace classes & properties
        # for each CURIE, if it's in the default namespace, i.e. this ontology, use its fragment URI

        for uri, prop in self.PROPERTIES.items():
            html = []
            for p in prop['supers']:
                prop_type = self.PROPERTIES.get(p).get('prop_type') if self.PROPERTIES.get(p) else None
                html.append(self._make_uri_html(p, type=prop_type))
            self.PROPERTIES[uri]['supers'] = html

            html = []
            for p in prop['subs']:
                prop_type = self.PROPERTIES.get(p).get('prop_type') if self.PROPERTIES.get(p) else None
                html.append(self._make_uri_html(p, type=prop_type))
            self.PROPERTIES[uri]['subs'] = html

            html = []
            for d in prop['domains']:
                if type(d) == tuple:
                    html.append(self._make_collection_class_html(d[0], d[1]))
                else:
                    html.append(self._make_uri_html(d, type='c'))
            self.PROPERTIES[uri]['domains'] = html

            html = []
            for d in prop['domainIncludes']:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_uri_html(m, type='c'))
                else:
                    html.append(self._make_uri_html(d, type='c'))
            self.PROPERTIES[uri]['domainIncludes'] = html

            html = []
            for d in prop['ranges']:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_uri_html(m, type='c'))
                else:
                    html.append(self._make_uri_html(d, type='c'))
            self.PROPERTIES[uri]['ranges'] = html

            html = []
            for d in prop['rangeIncludes']:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_uri_html(m, type='c'))
                else:
                    html.append(self._make_uri_html(d, type='c'))
            self.PROPERTIES[uri]['rangeIncludes'] = html

        for uri, cls in self.CLASSES.items():
            html = []
            for d in cls['equivalents']:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_uri_html(m, type='c'))
                else:
                    html.append(self._make_uri_html(d, type='c'))
            self.CLASSES[uri]['equivalents'] = html

            html = []
            for d in cls['supers']:
                if type(d) == tuple:
                    html.append(self._make_collection_class_html(d[0], d[1]))
                else:
                    html.append(self._make_uri_html(d, type='c'))
            self.CLASSES[uri]['supers'] = html

            html = []
            for d in cls['restrictions']:
                html.append(self._make_restriction_html(uri, d))
            self.CLASSES[uri]['restrictions'] = html

            html = []
            for d in cls['subs']:
                if type(d) == tuple:
                    for m in d[1]:
                        html.append(self._make_uri_html(m, type='c'))
                else:
                    html.append(self._make_uri_html(d, type='c'))
            self.CLASSES[uri]['subs'] = html

            html = []
            for p in cls['in_domain_of']:
                prop_type = self.PROPERTIES.get(p).get('prop_type') if self.PROPERTIES.get(p) else None
                html.append(self._make_uri_html(p, type=prop_type))
            self.CLASSES[uri]['in_domain_of'] = html

            html = []
            for p in cls['in_domain_includes_of']:
                prop_type = self.PROPERTIES.get(p).get('prop_type') if self.PROPERTIES.get(p) else None
                html.append(self._make_uri_html(p, type=prop_type))
            self.CLASSES[uri]['in_domain_includes_of'] = html

            html = []
            for p in cls['in_range_of']:
                prop_type = self.PROPERTIES.get(p).get('prop_type') if self.PROPERTIES.get(p) else None
                html.append(self._make_uri_html(p, type=prop_type))
            self.CLASSES[uri]['in_range_of'] = html

            html = []
            for p in cls['in_range_includes_of']:
                prop_type = self.PROPERTIES.get(p).get('prop_type') if self.PROPERTIES.get(p) else None
                html.append(self._make_uri_html(p, type=prop_type))
            self.CLASSES[uri]['in_range_includes_of'] = html

        properties_html = self._make_properties_html()
        classes_html = self._make_classes_html()

        namespaces_html = self._make_namespaces_html()
        metadata_html = self._make_metadata_html(source_info)

        return self._make_document_html(
            self.METADATA['title'],
            metadata_html,
            classes_html,
            properties_html,
            self.METADATA['default_namespace'],
            namespaces_html
        )


if __name__ == '__main__':
    h = MakeHtml()
    # get the input file
    i = h.APP_DIR + '/examples/placenames.ttl'
    # parse the input file into an in-memory RDF graph
    h.G.parse(i, format='turtle')

    # prepare source_info to allow for link to source file in HTML
    source_info = (i, 'turtle')
    # generate the HTML doc
    html = h.generate_html(source_info)

    # write HTML to file
    with open(i.replace('ttl', 'html'), 'w') as f:
        f.write(html)
