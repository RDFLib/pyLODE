import argparse
import os.path
import requests
import io
import rdflib


RDF_FILE_EXTENSIONS = [
    '.rdf',
    '.owl',
    '.ttl',
    '.n3',
    '.nt',
    '.json'
]

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


# used to determine whether or not a fiven path is actually a real file
def is_valid_file(parser, arg):
    try:
        return open(arg, 'r')
    except:
        parser.error('The file %s does not exist!' % arg)


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
            g = rdflib.Graph().parse(data=data, foramt=fmt)
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


    # # generate the graph
    # try:
    #     g = rdflib.Graph().parse(format=rdflib.util.guess_format(args.inputfile))