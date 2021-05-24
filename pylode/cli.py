import argparse
from sys import exit
import sys
from os.path import dirname, realpath
sys.path.insert(0, dirname(dirname(realpath(__file__))))
from pylode import RDF_FILE_EXTENSIONS, MakeDocco
import logging


# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)  # start with minimal logging
fh = logging.FileHandler("pylode.log")
fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(name)s - %(message)s"))
logger.addHandler(fh)


def is_valid_file(parser, arg):
    try:
        return open(arg, "r")
    except:
        parser.error("The file %s does not exist!" % arg)


# used to capture graph parsing and content errors
class RdfGraphError(Exception):
    pass


def main(args=None):
    # read the input ontology file into a graph
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    overarching_group = parser.add_mutually_exclusive_group()
    inputs_group = overarching_group.add_mutually_exclusive_group()

    inputs_group.add_argument(
        "-i",
        "--inputfile",
        help="The RDF ontology file you wish to generate HTML for. "
        "Must be in either Turtle, RDF/XML, JSON-LD or N-Triples formats indicated by the file type extensions:"
        "{} respectively.".format(", ".join(RDF_FILE_EXTENSIONS)),
        type=lambda x: is_valid_file(parser, x),
    )

    inputs_group.add_argument(
        "-u",
        "--url",
        help="The RDF ontology you wish to generate HTML for, online. "
        "Must be an absolute URL that can be resolved to RDF, preferably via Content Negotiation.",
    )

    overarching_group.add_argument(
        "-lp",
        "--listprofiles",
        help="This flag, if used, must be the only flag supplied. It will cause the program to list all the ontology"
        " documentation profiles that it supports, indicating both their URI and their short token for use with the"
        " -p (--profile) flag when creating HTML documentation",
        action="store_true",
    )

    parser.add_argument(
        "-p",
        "--profile",
        help="A profile - a specified information model - for an ontology. You can indicate this via the profile's URI"
        "or its token. The list of profiles - URIs and their corresponding tokens - supported by pyLODE, can be "
        "found by running the program with the flag -lp or --listprofiles.",
        default="ontdoc",
    )

    parser.add_argument(
        "-c",
        "--css",
        help="Whether (true) or not (false) to include CSS within an output HTML file.",
        choices=["true", "false"],
        default="true",
    )

    parser.add_argument(
        "-cs",
        "--usecuriesstored",
        help="Whether (true) or not (false) to look up CURIEs for unknown namespaces using the stored CURIE list.",
        choices=["true", "false"],
        default="true",
    )
    parser.add_argument(
        "-co",
        "--getcuriesonline",
        help="Whether (true) or not (false) to look up CURIEs for unknown namespaces using http://prefix.cc.",
        choices=["true", "false"],
        default="false",
    )

    parser.add_argument(
        "-o",
        "--outputfile",
        help="A name you wish to assign to the output file. Will be postfixed with .html/.md/.adoc if not already "
             "added. If no output file is given, output will be printed to screen",
        default=None
    )

    parser.add_argument(
        "-f",
        "--outputformat",
        help="The output format of the documentation. HTML, Markdown and ASCIIDOC are supported",
        choices=["html", "md", "adoc"],
        default="html",
    )

    parser.add_argument(
        "-log", "--loglevel",
        help="Log level for pylode.log.",
        choices=["debug", "info", "warning", "error"],
        default="error"
    )

    parser.add_argument(
        "-l",
        "--language",
        help="The ISO 639 language code for the desired output language.",
        default="en",
    )

    parser.add_argument(
        "-v",
        "--version",
        help="The version of this copy of pyLODE.",
        action="store_true"
    )

    args = parser.parse_args()

    if args.loglevel:
        if args.loglevel == "debug":
            logger.setLevel(logging.DEBUG)
            logger.log(logging.DEBUG, "logger set to DEBUG")
            print("logger set to DEBUG")
        elif args.loglevel == "info":
            logger.setLevel(logging.INFO)
            logger.log(logging.DEBUG, "logger set to INFO")
            print("logger set to INFO")
        elif args.loglevel == "warning":
            logger.setLevel(logging.WARNING)
        else:
            logger.setLevel(logging.ERROR)

    if args.listprofiles:
        print(MakeDocco.list_profiles())
        exit()
    elif args.version:
        from pylode import __version__
        print(__version__)
        exit()
    elif args.inputfile or args.url:
        if args.outputformat == "adoc" and args.profile != "ontdoc":
            raise NotImplementedError("Sorry, ASCIIDOC format is currently only available for the OntDoc profile")

        include_css = True if args.css == "true" else False
        use_curies_stored = True if args.usecuriesstored == "true" else False
        get_curies_online = True if args.getcuriesonline == "true" else False

        # args are present so getting RDF from input file or uri into an rdflib Graph
        if args.inputfile:
            logger.log(logging.DEBUG, f"args.inputfile: {args.inputfile.name}")
            h = MakeDocco(
                input_data_file=args.inputfile,
                outputformat=args.outputformat,
                profile=args.profile,
                include_css=include_css,
                language=args.language,
                use_curies_stored=use_curies_stored,
                get_curies_online=get_curies_online,
            )
        elif args.url:
            logger.log(logging.DEBUG, f"args.url: {args.url.name}")
            h = MakeDocco(
                input_uri=args.url,
                outputformat=args.outputformat,
                profile=args.profile,
                include_css=include_css,
                language=args.language,
                use_curies_stored=use_curies_stored,
                get_curies_online=get_curies_online,
            )
        else:
            # we have neither an input file or a URI supplied
            parser.error(
                "Either an input file or a url is required to access the ontology's RDF"
            )

        if args.profile:
            if not MakeDocco.is_supported_profile(args.profile):
                parser.error("The profile you requested, '{}', is not supported. "
                             "Please choose from those given by List Profiles (-lp)".format(args.profile))
    else:
        parser.error("An ontology source (-i/--inputfile or -u/--url) is required")

    # here we have a parsed graph from either a local file or a URI

    # name the output file
    if args.outputfile is not None:
        output_file_name = args.outputfile

        if not output_file_name.endswith(args.outputformat):
            output_file_name += "." + args.outputformat

        # generate the HTML doc
        h.document(destination=output_file_name)

        print("Finished. {} documentation in {}".format(args.profile, output_file_name))
    else:
        print(h.document())


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
