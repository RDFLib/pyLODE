from os import path
from model.entity import *
from jinja2 import Environment, FileSystemLoader


class Ontology():
    def __init__(self, g):
        self.uri = None
        self.name = None
        self.description = None
        self.publishers = None
        self.creators = None
        self.contributors = None
        self.created = None
        self.modified = None
        self.version_info = None
        self.version_uri = None

        self.has_classes = False
        self.has_ops = False
        self.has_dps = False
        self.has_aps = False
        self.has_nis = False

        q = '''
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX dct:  <http://purl.org/dc/terms/>
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
                }
                
                OPTIONAL { ?uri    dct:publisher   ?publishers . }
                OPTIONAL { ?uri    dct:creator     ?creators . }
                OPTIONAL { ?uri    dct:contributor ?contributors . }
                OPTIONAL { ?uri    dct:created     ?created . }
                OPTIONAL { ?uri    dct:modified    ?modified . }
                OPTIONAL { ?uri    owl:versionInfo ?version_info . }
                OPTIONAL { ?uri    owl:versionIRI  ?version_uri . }
            }
        '''
        for r in g.query(q):
            self.uri = r.uri
            self.name = r.name
            self.description = r.description
            self.publishers = r.publishers
            self.creators = r.creators
            self.contributors = r.contributors
            self.created = r.created
            self.modified = r.modified
            self.version_info = r.version_info
            self.version_uri = r.version_uri

        # check for classes, ops, dp, ap & nis

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


class OwlClass(Entity):
    def __init__(self, existing_fids, uri, name, description, usage):
        super().__init__(existing_fids, uri, name, description, usage)

        self.html = self.render_html()

    def render_html(self):
        template_dir = path.join(path.dirname(path.dirname(path.realpath(__file__))), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('class.html')
        return template.render(
            uri=self.uri,
            fid=self.fid,
            name=self.name,
            description=self.description,  # TODO: handle Markdown in description
            usage=self.usage
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
