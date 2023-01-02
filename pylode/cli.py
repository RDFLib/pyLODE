import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).absolute().parent.parent))
from pylode import __version__, PylodeError
from pylode import OntPub, VocPub

parser = argparse.ArgumentParser()

parser.add_argument(
    "-v", "--version", action="version", version="{version}".format(version=__version__)
)

parser.add_argument(
    "input",
    help="Input file location or URL",
)

parser.add_argument(
    "-o",
    "--outputfile",
    help="A name you wish to assign to the output file. Will be postfixed "
    "with .html if not already added. If no output file is given, "
    "output will be printed to screen",
    default=None,
)

parser.add_argument(
    "-c",
    "--css",
    help="Whether (true) or not (false) to include CSS within an output " "HTML file.",
    choices=["true", "false"],
    default="true",
)

parser.add_argument(
    "-p",
    "--profile",
    help="Which profile to use to generate HTML. Must be one of "
    "'ontpub' (https://w3id.org/profile/ontpub) - for ontologies, "
    "'vocpub' (https://w3id.org/profile/vocpub) - for SKOS vocabularies",
    choices=["ontpub", "vocpub"],
    default="ontpub",
)


def main():
    args = parser.parse_args()

    try:
        if args.profile == "ontpub":
            html = OntPub(args.input)
        elif args.profile == "vocpub":
            html = VocPub(args.input)
    except PylodeError as e:
        print("ERROR: " + str(e))
        exit()

    pylode_kwargs = {}

    if args.outputfile is not None:
        if not args.outputfile.endswith("html"):
            of = args.outputfile + ".html"
        else:
            of = args.outputfile

        pylode_kwargs["destination"] = Path(of)

    if args.css == "false":
        pylode_kwargs["include_css"] = False

    if args.outputfile is None:
        print(html.make_html(**pylode_kwargs))
    else:
        html.make_html(**pylode_kwargs)


if __name__ == "__main__":
    main()
