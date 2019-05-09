from os import path
from jinja2 import Environment, FileSystemLoader
import markdown


class Ontology:
    def __init__(self, g):
        self.uri = None
        self.name = None
        self.description = None
        self.created = None
        self.modified = None
        self.version_info = None
        self.version_uri = None
        self.publishers = []
        self.creators = []
        self.contributors = []
        self.has_classes = False
        self.has_ops = False
        self.has_dps = False
        self.has_aps = False
        self.has_nis = False

        # get basic ontology properties
        q = '''
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX dct:  <http://purl.org/dc/terms/>
            PREFIX dc:  <http://purl.org/dc/elements/1.1/>
            SELECT * 
            WHERE {
                ?uri    a               owl:Ontology .
                
                # name / label
                OPTIONAL {
                    { ?uri  rdfs:label     ?name . }
                    UNION
                    { ?uri  dct:title      ?name . }
                    UNION
                    { ?uri  skos:prefLabel ?name . }               
                }
    
                # description / definitions
                OPTIONAL {
                    { ?uri rdfs:comment       ?description . }
                    UNION
                    { ?uri skos:definition    ?description . }
                    UNION
                    { ?uri dct:description    ?description . }
                }                               
                
                OPTIONAL { ?uri    dct:created     ?created . }
                OPTIONAL { ?uri    dct:modified    ?modified . }
                OPTIONAL { ?uri    owl:versionInfo ?version_info . }
                OPTIONAL { ?uri    owl:versionIRI  ?version_uri . }
            }
        '''

        for r in g.query(q):
            self.uri = r.uri
            self.name = r.name
            self.description = markdown.markdown(r.description) if r.description is not None else None
            self.created = r.created
            self.modified = r.modified
            self.version_info = r.version_info
            self.version_uri = r.version_uri

        # get agents
        # TODO: replace for loops in ontology.html with list joins
        q = '''
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX dc:  <http://purl.org/dc/elements/1.1/>
            PREFIX dct:  <http://purl.org/dc/terms/>
            SELECT * 
            WHERE {
                ?uri    a               owl:Ontology .

                OPTIONAL {
                    { ?uri  dc:publisher      ?publisher . }
                    UNION
                    { ?uri  dct:publisher     ?publisher . }           
                }
            }
        '''
        for r in g.query(q):
            if r.publisher is not None:
                self.publishers.append(r.publisher)

        q = '''
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX dc:  <http://purl.org/dc/elements/1.1/>
            PREFIX dct:  <http://purl.org/dc/terms/>
            SELECT * 
            WHERE {
                ?uri    a               owl:Ontology .

                OPTIONAL {
                    { ?uri  dc:creator     ?creator . }
                    UNION
                    { ?uri  dct:creator     ?creator . }          
                }
            }
        '''
        for r in g.query(q):
            if r.creator is not None:
                self.creators.append(r.creator)

        q = '''
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX dc:  <http://purl.org/dc/elements/1.1/>
            PREFIX dct:  <http://purl.org/dc/terms/>
            SELECT * 
            WHERE {
                ?uri    a               owl:Ontology .

                OPTIONAL {
                    { ?uri  dc:contributor      ?contributor . }
                    UNION
                    { ?uri  dct:contributor     ?contributor . }          
                }
            }
        '''
        for r in g.query(q):
            if r.contributor is not None:
                self.contributors.append(r.contributor)

        # check for classes, ops, dp, ap & nis
        q = '''
        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
        SELECT (COUNT(?uri) AS ?count)
        WHERE {
            ?uri a owl:Class .
            
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2002/07/owl#"))
            }           
        }
        '''
        for r in g.query(q):
            if int(r[0]) > 0:
                self.has_classes = True

        q = '''
        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
        SELECT (COUNT(?uri) AS ?count)
        WHERE {
            ?uri    a   owl:ObjectProperty . 

            # removing upper ontology properties
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2002/07/owl#"))
            }    
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2000/01/rdf-schema#"))
            }      
        }
        '''
        for r in g.query(q):
            if int(r[0]) > 0:
                self.has_ops = True

        q = '''
        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
        SELECT (COUNT(?uri) AS ?count)
        WHERE {
            ?uri    a   owl:DatatypeProperty . 

            # removing upper ontology properties
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2002/07/owl#"))
            }    
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2000/01/rdf-schema#"))
            }      
        }
        '''
        for r in g.query(q):
            if int(r[0]) > 0:
                self.has_dps = True

        q = '''
        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
        SELECT (COUNT(?uri) AS ?count)
        WHERE {
            ?uri    a   owl:AnnotationProperty . 

            # removing upper ontology properties
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2002/07/owl#"))
            }    
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2000/01/rdf-schema#"))
            }      
        }
        '''
        for r in g.query(q):
            if int(r[0]) > 0:
                self.has_aps = True

        q = '''
        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
        SELECT (COUNT(?uri) AS ?count)
        WHERE {
            ?uri    a   owl:NamedIndividual .     
        }
        '''
        for r in g.query(q):
            if int(r[0]) > 0:
                self.has_nis = True

        self.html = self.render_html()

    def render_html(self):
        template_dir = path.join(path.dirname(path.dirname(path.realpath(__file__))), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('ontology.html')
        return template.render(
            uri=self.uri,
            name=self.name,
            description=self.description,
            publishers=self.publishers,
            creators=self.creators,
            contributors=self.contributors,
            created=self.created,
            modified=self.modified,
            version_info=self.version_info,
            version_uri=self.version_uri,
            has_classes=self.has_classes,
            has_ops=self.has_ops,
            has_dps=self.has_dps,
            has_aps=self.has_aps,
            has_nis=self.has_nis
        )


if __name__ == '__main__':
    from rdflib import Graph
    import owlrl

    # used to capture graph parsing and content errors
    class RdfGraphError(Exception):
        pass

    existing_fids = []

    g = Graph().parse(path.join(path.dirname(path.dirname(path.realpath(__file__))), 'examples', 'prof.ttl'),
                      format='turtle')

    # expand the graph using OWL-RL
    try:
        owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)
    except Exception as e:
        raise RdfGraphError(
            'Error while running OWL-RL Deductive Closure\n{}'.format(str(e.args[0]))
        )

    o = Ontology(g)

    print(o.html)
