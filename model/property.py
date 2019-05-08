from os import path
from model.entity import *
from jinja2 import Environment, FileSystemLoader
from rdflib import URIRef


class Properties(Entities):
    def __init__(self, g, existing_fids):
        self.op_instances = []
        self.dtp_instances = []
        self.ap_instances = []

        q = '''
        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX dct:  <http://purl.org/dc/terms/>
        PREFIX sdo:  <https://schema.org/>
        SELECT * 
        WHERE {                    
            ?uri    a   ?property_type . 
            
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

            # usage notes
            OPTIONAL {
                ?uri skos:scopeNote       ?usage .
            }

            # domain
            OPTIONAL {
                ?uri rdfs:domain          ?domain .
            }  

            # domainIncludes
            OPTIONAL {
                ?uri sdo:domainIncludes   ?domainIncludes .
            }         

            # range
            OPTIONAL {
                ?uri rdfs:range           ?range .
            }           

            # rangeIncludes
            OPTIONAL {
                ?uri rdfs:rangeIncludes   ?rangeIncludes .
            }            

            # removing upper ontology properties
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2002/07/owl#"))
            }    
            FILTER NOT EXISTS { 
                FILTER(regex(STR(?uri), "http://www.w3.org/2000/01/rdf-schema#"))
            }
            VALUES ?property_type {
                owl:ObjectProperty
                owl:DatatypeProperty
                owl:AnnotationProperty
            }             
        }          
        ORDER BY ?name
        '''

        p = Property([], 'http://fake.com.au.nothing', None, None, None, None, None, None, None, None)

        for r in g.query(q):
            if r.uri != p.uri:
                # save the old p
                if p.fid is not None:
                    if p.property_type == URIRef('http://www.w3.org/2002/07/owl#ObjectProperty'):
                        self.op_instances.append(p)
                    elif p.property_type == URIRef('http://www.w3.org/2002/07/owl#DatatypeProperty'):
                        self.dtp_instances.append(p)
                    else:  # AnnotationProperty
                        self.ap_instances.append(p)

                # create a new p
                p = Property(
                    existing_fids,
                    r.uri,
                    r.name if r.name is not None else None,
                    r.description,
                    r.usage,
                    [],
                    [],
                    [],
                    [],
                    r.property_type
                )
                p.domains.append(r.domain)
                p.domainIncludes.append(r.domainIncludes)
                p.ranges.append(r.range)
                p.rangeIncludes.append(r.rangeIncludes)
            else:  # r.uri == uri:
                p.domains.append(r.domain)
                p.domainIncludes.append(r.domainIncludes)
                p.ranges.append(r.range)
                p.rangeIncludes.append(r.rangeIncludes)

        self.html = self.render_html()

    def render_html(self):
        template_dir = path.join(path.dirname(path.dirname(path.realpath(__file__))), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('properties.html')
        return template.render(
            op_instances=self.op_instances,
            dtp_instances=self.dtp_instances,
            ap_instances=self.ap_instances
        )


class Property(Entity):
    def __init__(self, existing_fids, uri, name, description, usage, domains, domainIncludes, ranges, rangeIncludes, property_type):
        super().__init__(existing_fids, uri, name, description, usage)

        self.domains = domains
        self.domainIncludes = domainIncludes
        self.ranges = ranges
        self.rangeIncludes = rangeIncludes
        self.property_type = property_type

        self.html = self.render_html()

    def render_html(self):
        template_dir = path.join(path.dirname(path.dirname(path.realpath(__file__))), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('property.html')
        return template.render(
            uri=self.uri,
            fid=self.fid,
            name=self.name,
            description=self.description,
            usage=self.usage,
            domain=self.domains,
            domainIncludes=self.domainIncludes,
            range=self.ranges,
            rangeIncludes=self.rangeIncludes,
            property_type=str(self.property_type)
        )


if __name__ == '__main__':
    from rdflib import Graph
    import owlrl

    # used to capture graph parsing and content errors
    class RdfGraphError(Exception):
        pass

    existing_fids = []

    g = Graph().parse(path.join(path.dirname(path.dirname(path.realpath(__file__))), 'examples', 'prof.ttl'), format='turtle')

    # expand the graph using OWL-RL
    try:
        owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)
    except Exception as e:
        raise RdfGraphError(
            'Error while running OWL-RL Deductive Closure\n{}'.format(str(e.args[0]))
        )

    ps = Properties(g, existing_fids)

    print(ps.html)
