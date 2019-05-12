import rdflib

g = rdflib.Graph().parse('../examples/borehole-expanded.ttl', format='turtle')

q = '''
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX : <http://linked.data.gov.au/def/borehole/>        
    SELECT ?domain 
    WHERE {{
        <{}> rdfs:domain ?domain .
        
        FILTER NOT EXISTS {{ 
            FILTER(regex(STR(?domain), "http://www.w3.org/2002/07/owl#"))
        }}
        FILTER NOT EXISTS {{
            FILTER(regex(STR(?domain), "http://www.w3.org/2000/01/rdf-schema#"))
        }}        
    }} 
'''.format('http://linked.data.gov.au/def/borehole/hasSurfaceCircumstance')

for r in g.query(q):
    if type(r[0]) is rdflib.term.URIRef:
        print(r[0])

