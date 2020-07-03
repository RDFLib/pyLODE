from os import path
import requests
from rdflib import util, Graph

VERSION = "2.8.3"
APP_DIR = path.dirname(path.realpath(__file__))
TEMPLATES_DIR = path.join(path.dirname(path.realpath(__file__)), "templates")
STYLE_DIR = path.join(path.dirname(path.realpath(__file__)), "style")
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


from .profiles import OntDoc, Prof, VocPub, PROFILES


class MakeDocco:
    def __init__(self, input_data_file=None, input_uri=None, data=None, outputformat="html", exclude_css=False, get_curies_online=False, profile="ontdoc"):
        """This class receives all of the variables needed to specify how to make documentation from an input RDF source

        :param input_data_file: An RDF file
        :type input_data_file: path (string)
        :param input_uri: A URI resolving to RDF data
        :type input_uri: A URI (string)
        :param data: RDF data
        :type data: Python varaible (string)
        :param outputformat: The desired output format form the list of supported formats (currently either "html" (default) or "md" for Markdown
        :type outputformat: string (one of "html" or "md")
        :param exclude_css: Whether (True, default) or not (False) to include styling CSS within HTML outputs (as oposed to producing a separate style.css file)
        :type exclude_css: boolean
        :param get_curies_online: Whether (True) or not (False, default) to search prefix.cc online for additional URI prefixes
        :type get_curies_online: boolean
        :param profile: When document profile, from a supported set, to use. Currently supported is "ontdoc" (profile of OWL) or "skosp" (profile of SKOS). See `list_profiles()` for full list of profiles.
        :type profile: string (one of "ontdoc" or "skosp")
        """
        self.profile_selected = profile

        if outputformat not in ["html", "md"]:
            self.outputformat = "html"
        else:
            self.outputformat = outputformat

        self.exclude_css = exclude_css
        self.get_curies_online = get_curies_online

        if profile not in PROFILES.keys():
            print("The profile you've selected, {}, is not recognised so the default profile, {} is being used. "
                  "Known profiles are: {}".format(profile, "ontdoc", ", ".join(PROFILES.keys())))
            self.profile_selected = "ontdoc"
        else:
            self.profile_selected = profile

        # shared variables
        if input_data_file is not None:
            self._parse_input_data_file(input_data_file)
        elif input_uri is not None:
            self._parse_input_uri(input_uri)
        elif data is not None:
            self._parse_data(data)
        else:
            raise Exception("You must supply either an input file or a URI for your ontology's RDF")

    def _parse_input_data_file(self, input_data_file):
        if hasattr(input_data_file, "name"):
            file_name = str(input_data_file.name)
        elif input_data_file is not None:
            file_name = str(input_data_file)

        if not file_name.endswith(tuple(RDF_FILE_EXTENSIONS)):
            raise Exception(
                "If supplying an input RDF file, it must end with one of the following file type extensions: {}."
                    .format(
                        ", ".join(RDF_FILE_EXTENSIONS)
                    )
                )
        else:
            fmt = (
                "json-ld"
                if file_name.endswith(".json") or file_name.endswith(".jsonld")
                else util.guess_format(file_name)
            )

            self.G = Graph().parse(file_name, format=fmt)
            self.source_info = (file_name, fmt)
            self.publication_dir = path.dirname(file_name)

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

    def _parse_data(self, data):
        self.G = Graph().parse(data=data, format="turtle")
        self.source_info = ("input.ttl", "turtle")
        self.publication_dir = path.dirname(path.realpath(__file__))

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
        if self.profile_selected == "prof":
            p = Prof(
                self.G,
                self.source_info,
                outputformat=self.outputformat,
                exclude_css=self.exclude_css,
                default_language="en",
                get_curies_online=self.get_curies_online
            )
        elif self.profile_selected == "vocpub":
            p = VocPub(
                self.G,
                self.source_info,
                outputformat=self.outputformat,
                exclude_css=self.exclude_css,
                default_language="en",
                get_curies_online=self.get_curies_online
            )
        else:
            p = OntDoc(
                self.G,
                self.source_info,
                outputformat=self.outputformat,
                exclude_css=self.exclude_css,
                default_language="en",
                get_curies_online=self.get_curies_online
            )

        if destination is not None:
            doc = p.generate_document()
            try:
                with open(destination, "w") as f:
                    f.write(doc)
            except Exception as e:
                print(e)
                raise Exception("The file you specified as 'destination' could not be written to. You specified {}.".format(destination))

        else:
            return p.generate_document()
