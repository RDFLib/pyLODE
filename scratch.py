from rdflib import Graph
from rdflib.namespace import RDF, OWL, DCTERMS
from itertools import chain


g = Graph().parse("pylode/examples/agrif.ttl", format="turtle")

p = 0
for s in g.subjects(predicate=RDF.type, object=OWL.ObjectProperty):
    p += 1

print(p)

p = 0
for s in g.subjects(predicate=RDF.type, object=OWL.AnnotationProperty):
    p += 1

print(p)

p = 0
for s in chain(
        g.subjects(predicate=RDF.type, object=OWL.ObjectProperty),
        g.subjects(predicate=RDF.type, object=OWL.AnnotationProperty)
):
    p += 1

print(p)

for s, o in g.subject_objects(DCTERMS.creator):
    print(o)




