from os import path
from model.entity import *
from jinja2 import Environment, FileSystemLoader
from rdflib import URIRef


class Properties(Entities):
    def __init__(self, g, existing_fids):
        super().__init__(g, existing_fids)

        self.op_instances = []
        self.dp_instances = []
        self.ap_instances = []

        q = '''
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX dct:  <http://purl.org/dc/terms/>
            SELECT * 
            WHERE {                    
                ?uri    a   ?property_type . 
    
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
        '''

        for r in self.g.query(q):
            p = Property(self.g, str(r.uri), self.existing_fids, r.property_type)

            if r.property_type == URIRef('http://www.w3.org/2002/07/owl#ObjectProperty'):
                self.op_instances.append(p)
            elif r.property_type == URIRef('http://www.w3.org/2002/07/owl#DatatypeProperty'):
                self.dp_instances.append(p)
            else:  # AnnotationProperty
                self.ap_instances.append(p)

    @property
    def html(self):
        template_dir = path.join(path.dirname(path.dirname(path.realpath(__file__))), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('properties.html')

        return template.render(
            op_instances=self.op_instances,
            dp_instances=self.dp_instances,
            ap_instances=self.ap_instances
        )


class Property(Entity):
    def __init__(self, g, uri, existing_fids, property_type):
        super().__init__(g, uri, existing_fids)

        self.property_type = property_type

        self._get_domains()
        self._get_ranges()

    def _get_domains(self):
        self.domains = []
        self.domainIncludes = []

        q = '''
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX dct:  <http://purl.org/dc/terms/>        

            SELECT ?domain ?name
            WHERE {{
                <{}> rdfs:domain ?domain .  

                OPTIONAL {{
                    {{ ?domain  rdfs:label     ?name . }}
                    UNION
                    {{ ?domain  dct:title      ?name . }}
                    UNION
                    {{ ?domain  skos:prefLabel ?name . }}            
                }}                    

                FILTER NOT EXISTS {{ 
                    FILTER(regex(STR(?domain), "http://www.w3.org/2002/07/owl#"))
                }}
                FILTER NOT EXISTS {{
                    FILTER(regex(STR(?domain), "http://www.w3.org/2000/01/rdf-schema#"))
                }}                      
            }} 
        '''.format(self.uri)

        for r in self.g.query(q):
            if type(r.domain) == URIRef:
                self.domains.append({
                    'uri': r.domain,
                    'type': 'uri',
                    'name': r.name if r.name is not None else super().get_element_name_from_uri(self, str(r.domain))
                })
            else:  # Blank Node, i.e. a restriction
                self.domains.append({
                    'uri': r.domain,
                    'type': 'bn'
                    # TODO: add in all the other options for restrictions
                })

        q = '''
            PREFIX sdo:  <http://schema.org/>
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX dct:  <http://purl.org/dc/terms/>  

            SELECT ?domainIncludes ?name
            WHERE {{
                <{}> sdo:domainIncludes ?domainIncludes .  

                OPTIONAL {{
                    {{ ?domainIncludes  rdfs:label     ?name . }}
                    UNION
                    {{ ?domainIncludes  dct:title      ?name . }}
                    UNION
                    {{ ?domainIncludes  skos:prefLabel ?name . }}            
                }}                     
            }} 
        '''.format(self.uri)

        for r in self.g.query(q):
            self.domainIncludes.append({
                'uri': r.domainIncludes,
                'name': r.name if r.name is not None else super().get_element_name_from_uri(self, str(r.range))
            })

    def _get_ranges(self):
        self.ranges = []
        self.rangeIncludes = []

        q = '''
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX dct:  <http://purl.org/dc/terms/>     

            SELECT ?range ?name
            WHERE {{
                <{}> rdfs:range ?range .  

                OPTIONAL {{
                    {{ ?range  rdfs:label     ?name . }}
                    UNION
                    {{ ?range  dct:title      ?name . }}
                    UNION
                    {{ ?range  skos:prefLabel ?name . }}            
                }}                     

                FILTER NOT EXISTS {{ 
                    FILTER(regex(STR(?range), "http://www.w3.org/2002/07/owl#"))
                }}
                FILTER NOT EXISTS {{
                    FILTER(regex(STR(?range), "http://www.w3.org/2000/01/rdf-schema#"))
                }}                    
            }} 
        '''.format(self.uri)

        for r in self.g.query(q):
            self.ranges.append({
                'uri': r.range,
                'name': r.name if r.name is not None else super().get_element_name_from_uri(self, str(r.range))
            })

        q = '''
            PREFIX sdo:  <http://schema.org/>
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX dct:  <http://purl.org/dc/terms/>  

            SELECT ?rangeIncludes ?name
            WHERE {{
              <{}> sdo:rangeIncludes ?rangeIncludes .  

                OPTIONAL {{
                    {{ ?rangeIncludes  rdfs:label     ?name . }}
                    UNION
                    {{ ?rangeIncludes  dct:title      ?name . }}
                    UNION
                    {{ ?rangeIncludes  skos:prefLabel ?name . }}            
                }}                   
            }} 
        '''.format(self.uri)

        for r in self.g.query(q):
            self.rangeIncludes.append({
                'uri': r.rangeIncludes,
                'name': r.name if r.name is not None else super().get_element_name_from_uri(self, str(r.rangeIncludes))
            })

    @property
    def html(self):
        template_dir = path.join(path.dirname(path.dirname(path.realpath(__file__))), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('property.html')

        return template.render(
            uri=self.uri,
            fid=self.fid,
            name=self.name,
            description=self.description,
            usage=self.usage,
            domains=self.domains,
            domainIncludes=self.domainIncludes,
            ranges=self.ranges,
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

    g = Graph().parse(path.join(path.dirname(path.dirname(path.realpath(__file__))), 'examples', 'borehole.ttl'), format='turtle')

    # expand the graph using OWL-RL
    try:
        owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)
    except Exception as e:
        raise RdfGraphError(
            'Error while running OWL-RL Deductive Closure\n{}'.format(str(e.args[0]))
        )

    with open(path.join(path.dirname(path.dirname(path.realpath(__file__))), 'examples', 'borehole-expanded.ttl'), 'w') as f:
        f.write(g.serialize(format='turtle').decode('utf-8'))

    ps = Properties(g, existing_fids)

    print(ps.html)
