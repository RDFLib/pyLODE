import argparse
import os
from os import path
import shutil
import requests
import rdflib
from makehtml import MakeHtml


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
    'text/turtle;charset=UTF-8': 'turtle',
    'text/ntriples': 'nt',
    'text/n-triples': 'nt',
    'text/plain': 'nt',  # text/plain is the old/deprecated mimetype for n-triples
}


# used to determine whether or not a given path is actually a real file
def is_valid_file(parser, arg):
    try:
        return open(arg, 'r')
    except:
        parser.error('The file %s does not exist!' % arg)


# used to capture graph parsing and content errors
class RdfGraphError(Exception):
    pass


def main(args):
    # read the input ontology file into a graph
    parser = argparse.ArgumentParser()
    overarching_group = parser.add_mutually_exclusive_group()
    inputs_group = overarching_group.add_mutually_exclusive_group()

    inputs_group.add_argument(
        '-i', '--inputfile',
        help='The RDF ontology file you wish to generate HTML for. '
             'Must be in either Turtle, RDF/XML, JSON-LD or N-Triples formats indicated by the file type extensions:'
             '{} respectively.'.format(', '.join(RDF_FILE_EXTENSIONS)),
        type=lambda x: is_valid_file(parser, x)
    )
    inputs_group.add_argument(
        '-u', '--url',
        help='The RDF ontology you wish to generate HTML for, online. '
             'Must be an absolute URL that can be resolved to RDF, preferably via Content Negotiation.'
    )

    # TODO: remove requirement to have an input arg with -lp
    overarching_group.add_argument(
        '-lp', '--listprofiles',
        help='This flag, if used, must be the only flag supplied. It will cause the program to list all the ontology'
             ' documentation profiles that it supprts, indicating both their URI and their short token for use with the'
             ' -p (--profile) flag when creating HTML documentation'
    )

    parser.add_argument(
        '-c', '--css',
        help='Whether (true) or not (false) to copy the default CSS file to the output directory.',
        choices=['true', 'false'],
        default='false'
    )

    parser.add_argument(
        '-p', '--profile',
        help='A profile - a specified information model - for an ontology. You can indicate this via the profile\'s URI'
             'or via the profile\'s token. The list of profiles, URIs and tokens, that this application supports can be'
             'found by running the program with the flag -lp or --listprofiles only.'
    )

    parser.add_argument(
        '-o', '--outputfile',
        help='A name you wish to assign to the output file. Will be postfixed with .html. If not specified, '
             'the name of the input file or last segment of RDF URI will be used, + .html.'
    )

    parser.add_argument(
        '-f', '--outputformat',
        help='The output format of the documentation. HTML is working fully, markdown is in test mode only.',
        choices=['html', 'markdown'],
        default='html'
    )

    args = parser.parse_args()

    if args.listprofiles:
        print('list profiles')
        exit()
    elif args.inputfile or args.url:
        # args are present so getting RDF from input file or uri into an rdflid Graph
        if args.inputfile:
            if not args.inputfile.name.endswith(tuple(RDF_FILE_EXTENSIONS)):
                parser.error(
                    'If supplying an input RDF file, it must end with one of the following file type extensions: {}.'
                    .format(', '.join(RDF_FILE_EXTENSIONS))
                )
            else:
                fmt = 'json-ld' \
                    if args.inputfile.name.endswith('.json') or args.inputfile.name.endswith('.jsonld') \
                    else rdflib.util.guess_format(args.inputfile.name)
                data = args.inputfile.read()
                g = rdflib.Graph().parse(data=data, format=fmt)
                source_info = (args.inputfile.name, fmt)
                publication_dir = path.dirname(args.inputfile.name)
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
                fmt = 'json-ld' if media_type == 'application/ld+json' or media_type == 'application/json' else None

            if fmt is None:
                parser.error(
                    'Could not parse the supplied URI. The RDF format could not be determined from Media Type '
                    '({} was given) or from a file extension'.format(media_type)
                )

            g = rdflib.Graph().parse(data=r.text, format=fmt)
            source_info = (args.url, fmt)
            publication_dir = path.join(path.dirname(path.realpath(__file__)), 'output_files')
        else:
            # we have neither an input file or a URI supplied
            parser.error('Either an inputfile or a url is required to access the ontology\'s RDF')
    else:
        parser.error('Either an ontology source (-i/--inputfile or a -u/--url) is required or one of the documentation '
                     'commands, such as -lp (--listprofiles)')

    # here we have a parsed graph from either a local file or a URI

    # set up output directories and resources
    main_dir = path.dirname(path.realpath(__file__))
    style_dir = path.join(main_dir, 'style')
    os.makedirs(publication_dir, exist_ok=True)

    # include CSS
    msg_css = ''
    if args.css == 'true':
        shutil.copyfile(path.join(style_dir, 'pylode.css'), path.join(publication_dir, 'style.css'))
        msg_css = ' and CSS'

    output_filename = os.path.basename(args.outputfile) if args.outputfile else 'doc.html'

    if args.outputformat == 'html':
        if not output_filename.endswith('.html'):
            output_filename += '.html'
    elif args.outputformat == 'markdown':
        if not output_filename.endswith('.md'):
            output_filename += '.md'

    h = MakeHtml(args.outputformat)
    h.G = g

    # generate the HTML doc
    with open(path.join(publication_dir, output_filename), 'w') as f:
        f.write(h.document(source_info))

    if args.outputformat == 'html':
        msg_template = 'Finished. HTML{} file in {}/.'
    else:
        msg_template = 'Finished. Markdown{} file in {}/.'
    msg = msg_template.format(msg_css, publication_dir)
    print(msg)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
