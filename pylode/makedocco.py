from rdflib import Graph, util
from os import path
import requests
from rdflib.plugin import register, Serializer
from rdflib_jsonld import serializer
from docprofiles import PROFILES
from docprofile import DocProfile
from docprofile_owlp import Owlp
from docprofile_skosp import Skosp


register("json-ld", Serializer, "rdflib_jsonld.serializer", "JsonLDSerializer")

RDF_FILE_EXTENSIONS = [".rdf", ".owl", ".ttl", ".n3", ".nt", ".json"]

RDF_SERIALIZER_MAP = {
    "text/turtle": "turtle",
    "text/n3": "n3",
    "application/n-triples": "nt",
    "application/ld+json": "json-ld",
    "application/rdf+xml": "xml",
    # Some common but incorrect mimetypes
    "application/rdf": "xml",
    "application/rdf xml": "xml",
    "application/json": "json-ld",
    "application/ld json": "json-ld",
    "text/ttl": "turtle",
    "text/turtle;charset=UTF-8": "turtle",
    "text/ntriples": "nt",
    "text/n-triples": "nt",
    "text/plain": "nt",  # text/plain is the old/deprecated mimetype for n-triples
}


class MakeDocco:
    def __init__(self, input_data_file=None, input_uri=None, outputformat="html", exclude_css=False, get_curies_online=False, profile="owlp"):
        self.profile_selected = profile

        if outputformat not in ["html", "md"]:
            self.outputformat = "html"
        else:
            self.outputformat = outputformat

        self.exclude_css = exclude_css
        self.get_curies_online = get_curies_online

        if profile not in PROFILES.keys():
            self.profile_selected = "owlp"
        else:
            self.profile_selected = profile

        # shared variables
        if input_data_file is not None:
            self._parse_input_data_file(input_data_file)
        elif input_uri is not None:
            self._parse_input_uri(input_uri)
        else:
            raise Exception("You must supply either an input file or a URI for your ontology's RDF")

    def _parse_input_data_file(self, input_data_file):
        if not str(input_data_file).endswith(tuple(RDF_FILE_EXTENSIONS)):
            raise Exception(
                "If supplying an input RDF file, it must end with one of the following file type extensions: {}."
                    .format(
                        ", ".join(RDF_FILE_EXTENSIONS)
                    )
                )
        else:
            fmt = (
                "json-ld"
                if input_data_file.endswith(".json") or input_data_file.endswith(".jsonld")
                else util.guess_format(input_data_file)
            )
            with open(input_data_file, 'r') as f:
                data = f.read()
            self.G = Graph().parse(data=data, format=fmt)
            self.source_info = (input_data_file, fmt)
            self.publication_dir = path.dirname(input_data_file)

    def _parse_input_uri(self, uri):
        r = requests.get(
            uri, headers={"Accept": ", ".join(RDF_SERIALIZER_MAP.keys())}
        )
        # get RDF format from Media Type
        media_type = r.headers.get("Content-Type").split(";")[0]  # splitting off any ;charset=...
        if RDF_SERIALIZER_MAP.get(media_type):
            fmt = RDF_SERIALIZER_MAP.get(media_type)
        else:
            fmt = (
                "json-ld"
                if media_type == "application/ld+json"
                   or media_type == "application/json"
                else None
            )

        if fmt is None:
            raise Exception(
                "Could not parse the supplied URI. The RDF format could not be determined from Media Type "
                "({} was given) or from a file extension".format(media_type)
            )

        self.G = Graph().parse(data=r.text, format=fmt)
        self.source_info = (uri, fmt)
        self.publication_dir = path.join(
            path.dirname(path.realpath(__file__)), "output_files"
        )

    @classmethod
    def list_profiles(cls):
        s = ""
        for k, v in PROFILES.items():
            s += "{}: {}\n".format(k, v)

        return s

    @classmethod
    def is_supported_profile(cls, profile_key):
        is_supported = False
        for k, v in PROFILES.items():
            if profile_key == k or profile_key == v.uri:
                is_supported = True

        return is_supported

    def document(self, destination=None):
        if self.profile_selected == "skosp":
            p = Skosp(
                self.G,
                self.source_info,
                outputformat=self.outputformat,
                exclude_css=self.exclude_css,
                default_language="en",
                get_curies_online=self.get_curies_online
            )
        else:
            p = Owlp(
                self.G,
                self.source_info,
                outputformat=self.outputformat,
                exclude_css=self.exclude_css,
                default_language="en",
                get_curies_online=self.get_curies_online
            )

        if destination is not None:
            try:
                with open(destination, "w") as f:
                    f.write(m.document())
            except Exception as e:
                print(e)
                raise Exception("The file you specified as 'destination' could not be written to.")

        else:
            return p.generate_document()


if __name__ == "__main__":
    m = MakeDocco(input_data_file="examples/agrif.ttl", profile="owlp", outputformat="html")

    m.document(destination="examples/agrif.html")
