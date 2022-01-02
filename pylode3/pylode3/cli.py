import argparse
from pathlib import Path
from __init__ import __version__
from ontdoc import OntDoc


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="{version}".format(version=__version__)
    )

    parser.add_argument(
        "input",
        help="Input file location or URL",
    )

    parser.add_argument(
        "-o",
        "--outputfile",
        help="A name you wish to assign to the output file. Will be postfixed with .html if not already "
             "added. If no output file is given, output will be printed to screen",
        default=None
    )

    parser.add_argument(
        "-c",
        "--css",
        help="Whether (true) or not (false) to include CSS within an output HTML file.",
        choices=["true", "false"],
        default="true",
    )

    args = parser.parse_args()

    od = OntDoc(args.input)

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
        print(od.make_html(**pylode_kwargs))
    else:
        od.make_html(**pylode_kwargs)
