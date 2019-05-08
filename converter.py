import argparse
import requests
import rdflib
import owlrl
import collections
from jinja2 import Environment, FileSystemLoader


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


# used to determine whether or not a given path is actually a real file
def is_valid_file(parser, arg):
    try:
        return open(arg, 'r')
    except:
        parser.error('The file %s does not exist!' % arg)


# used to capture graph parsing and content errors
class RdfGraphError(Exception):
    pass


# assists get_classes when no name is given for an element
def _get_element_name_from_uri(uri):
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


# get all Classes from graph
def get_classes(g, html_document):
    q = '''
    PREFIX owl:  <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX dct:  <http://purl.org/dc/terms/>
    SELECT * 
    WHERE {
        # only need this one type call since OWL-RL is expanding all subclasses to this
        ?c  a               rdfs:Class . 
        
        # name / label
        OPTIONAL {
            { ?c  rdfs:label      ?name . }
            UNION
            { ?c  dct:title      ?name . }
        }
        
        # description / definitions
        OPTIONAL {
            { ?c rdfs:comment       ?description . }
            UNION
            { ?c skos:definition    ?description . }
        }
        
        # usage notes
        OPTIONAL {
            ?c skos:scopeNote     ?usage .
        }
        
        # removing upper ontology class declarations by filtering out specifics
        FILTER (?c NOT IN (
            <http://www.w3.org/2002/07/owl#Nothing>,
            <http://www.w3.org/2002/07/owl#Thing>
            )
        )     
    }    
    '''
    html = ''
    for r in g.query(q):
        template = Environment(loader=FileSystemLoader('templates')).get_template('class.html')
        output = template.render({
            'id': make_fragment_id(r.c, r.name, html_document),
            'iri': r.c,
            'name': r.name if r.name is not None else _get_element_name_from_uri(r.c),
            'description': r.description
        })
        html += output + '\n'

    with open('classes.html', 'w') as f:
        f.write(html)


# assists other methods by removing non-ASCII chars from a string
def _remove_non_ascii(s):
    return ''.join(i for i in s if ord(i) < 128)


# TODO: complete make_fragment_id
# makes the fragment ID for a class, property, Named Individual (any entity) based on URI & label
def make_fragment_id(uri, name, html_document):
    # try creating an ID from label
    # lowercase, remove spaces, escape all non-ASCII chars
    if name is not None:
        fid = _remove_non_ascii(name.lower().replace(' ', ''))

        if fid not in html_document.fragment_ids:
            html_document.fragment_ids.append(fid)
            return fid

    # this fid is already present in fragment ids so generate a fid from the URI instead

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

    return fid


# TODO: make_listing
def make_listing(entities):
    # makes Classes / Properties / Named Individuals listings like:
    # driller hasDiameter hadDrillingMethod hadDrillingTime hasElevation hasInclination hasPurpose...
    # at the start of each section
    pass


def make_domain():
    # don't forget to include domainIncludes
    pass


def make_range():
    # don't forget to include domainIncludes
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

    # render_ontology(None)
