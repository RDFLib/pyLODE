import argparse
import requests
import rdflib
import owlrl
import collections
from model import *


# used to know what RDF file types rdflib can handle
RDF_FILE_EXTENSIONS = [
    '.rdf',
    '.owl',
    '.ttl',
    '.n3',
    '.nt',
    '.json'
]

# used to know what RDF Media Types rdflib can handle
RDF_SERIALIZER_MAP = {
    'text/turtle': 'turtle',
    'text/n3': 'n3',
    'application/n-triples': 'nt',
    'application/ld+json': 'json-ld',
    'application/rdf+xml': 'xml',
    # Some common but incorrect mimetypes
    'application/rdf': 'xml',
    'application/rdf xml': 'xml',
    'application/json': 'json-ld',
    'application/ld json': 'json-ld',
    'text/ttl': 'turtle',
    'text/ntriples': 'nt',
    'text/n-triples': 'nt',
    'text/plain': 'nt',  # text/plain is the old/deprecated mimetype for n-triples
}


# used to ensure that in any HTML doc, no fragment IDs are duplicated
class HtmlDocument:

    def __init__(self):
        self.fragment_ids = []
        self.class_listing = []


# used to determine whether or not a given path is actually a real file
def is_valid_file(parser, arg):
    try:
        return open(arg, 'r')
    except:
        parser.error('The file %s does not exist!' % arg)


# used to capture graph parsing and content errors
class RdfGraphError(Exception):
    pass



# TODO: add prefix.cc lookups
def render_ontology(g):


    #
    #   Namespaces
    #
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
    test_namespaces_ordered = collections.OrderedDict(sorted(test_namespaces.items(), key=lambda x: x[0]))
    template = Environment(loader=FileSystemLoader('templates')).get_template('ontology.html')
    output = template.render(namespaces=test_namespaces_ordered)

    with open('my_new_html_file.html', 'w') as f:
        f.write(output)

    return


if __name__ == '__main__':
    # read the input ontology file into a graph
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-i', '--inputfile',
        help='The RDF ontology file you wish to generate HTML for. '
             'Must be in either Turtle, RDF/XML, JSON-LD or N-Triples formats indicated by the file type extensions:'
             '{} respectively.'.format(', '.join(RDF_FILE_EXTENSIONS)),
        type=lambda x: is_valid_file(parser, x)
    )
    group.add_argument(
        '-u', '--url',
        help='The RDF ontology you wish to generate HTML for, online. '
             'Must be an absolute URL that can be resolved to RDF, preferably via Content Negotiation.'
    )
    parser.add_argument(
        '-o', '--outputfile',
        help='A name you wish to assign to the output file. Will be postfixed with .html. If not specified, '
             'the name of the input file or last segment of RDF URI will be used, + .html.'
    )

    args = parser.parse_args()

    # args are present so getting RDF from input file / uri into an rdflid Graph
    if args.inputfile:
        if not args.inputfile.name.endswith(tuple(RDF_FILE_EXTENSIONS)):
            parser.error(
                'If supplying an input RDF file, it must end with one of the following file type extensions: {}.'
                .format(', '.join(RDF_FILE_EXTENSIONS))
            )
        else:
            fmt = 'json-ld' if args.inputfile.name.endswith('.json') else rdflib.util.guess_format(args.inputfile.name)
            data = args.inputfile.read()
            g = rdflib.Graph().parse(data=data, format=fmt)
    elif args.url:
        r = requests.get(
            args.url,
            headers={
                'Accept': ', '.join(RDF_SERIALIZER_MAP.keys())
            }
        )
        # get RDF format from Media Type
        media_type = r.headers.get('Content-Type')
        if RDF_SERIALIZER_MAP.get(media_type):
            fmt = RDF_SERIALIZER_MAP.get(media_type)
        else:
            fmt = 'json-ld' if args.inputfile.name.endswith('.json') else rdflib.util.guess_format(args.inputfile.name)

        if fmt is None:
            parser.error(
                'Could not parse the supplied URI. The RDF format could not be determined from Media Type '
                '({} was given) or from a file extension'.format(media_type)
            )

        g = rdflib.Graph().parse(data=r.text, format=fmt)
    else:
        # we have neither an input file or a URI supplied
        parser.error('Either an inputfile or a url is required to access the ontology\'s RDF')


    # here we have a parsed graph from either a local file or a URI

    with open('g.ttl', 'w') as f:
        f.write(g.serialize(format='turtle').decode('utf-8'))

    # expand the graph using OWL-RL
    try:
        owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)
    except Exception as e:
        raise RdfGraphError(
            'Error while running OWL-RL Deductive Closure\n{}'.format(str(e.args[0]))
        )

    with open('g-expanded.ttl', 'w') as f:
        f.write(g.serialize(format='turtle').decode('utf-8'))

    # here we have the expanded graph

    # make the document
    doc = HtmlDocument()

    # get classes
    get_classes(g, doc)
    make_listing(doc.class_listing)

    # render_ontology(None)
