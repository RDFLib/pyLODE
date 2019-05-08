from os import path
import collections
from model.ontology import *
from model.owl_class import *
from model.property import *
from jinja2 import Environment, FileSystemLoader


class HtmlDocument:
    def __init__(self, g):
        existing_fids = []

        o = Ontology(g)
        c = OwlClasses(g, existing_fids)
        p = Properties(g, existing_fids)
        # TODO: replace static namespaces with real ones, try call from rdflib + prefix.cc
        test_namespaces = {
            ':': 'http://linked.data.gov.au/def/borehole/',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'dct': 'http://purl.org/dc/terms/',
            'geo': 'http://www.opengis.net/ont/geosparql#',
            'geox': 'http://linked.data.gov.au/def/geox/',
            'loci': 'http://linked.data.gov.au/def/loci/',
            'owl': 'http://www.w3.org/2002/07/owl#',
            'prov': 'http://www.w3.org/ns/prov#',
            'qudt': 'http://qudt.org/schema/qudt/',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'skos': 'http://www.w3.org/2004/02/skos/core#',
            'sdo': 'https://schema.org/',
            'xsd': 'http://www.w3.org/2001/XMLSchema#',
            'time': 'http://www.w3.org/2006/time#'
        }
        n = collections.OrderedDict(sorted(test_namespaces.items(), key=lambda x: x[0]))

        self.html = self.render_html(o, c, p, n)

    def render_html(self, ontology, classes, properties, namespaces):
        template_dir = path.join(path.dirname(path.dirname(path.realpath(__file__))), 'templates')
        template = Environment(loader=FileSystemLoader(template_dir)).get_template('document.html')
        return template.render(
            ontology=ontology.html,
            classes=classes.html,
            properties=properties.html,
            namespaces=namespaces
        )


if __name__ == '__main__':
    from rdflib import Graph
    import owlrl

    # used to capture graph parsing and content errors
    class RdfGraphError(Exception):
        pass

    existing_fids = []

    g = Graph().parse(
        path.join(path.dirname(path.dirname(path.realpath(__file__))), 'examples', 'prof.ttl'),
        format='turtle'
    )

    # expand the graph using OWL-RL
    try:
        owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)
    except Exception as e:
        raise RdfGraphError(
            'Error while running OWL-RL Deductive Closure\n{}'.format(str(e.args[0]))
        )


