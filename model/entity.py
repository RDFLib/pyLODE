from abc import ABC
import markdown


class Entities(ABC):
    def __init__(self, g, existing_fids):
        self.g = g
        self.existing_fids = existing_fids
        self._html = None

    @property
    def html(self):
        pass


class Entity(ABC):
    def __init__(self, g, uri, existing_fids):
        self.g = g
        self.uri = uri
        self.existing_fids = existing_fids

        self._get_properties()

        self._html = None

    def _get_properties(self):
        q = '''
        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>     
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX dct:  <http://purl.org/dc/terms/>
        SELECT * 
        WHERE {{
            # name / label
            OPTIONAL {{
                {{ <{0}>  rdfs:label        ?name . }}
                UNION
                {{ <{0}>  dct:title         ?name . }}
                UNION
                {{ <{0}> skos:prefLabel     ?name . }}          
            }}

            # description / definitions
            OPTIONAL {{
                {{ <{0}> rdfs:comment       ?description . }}
                UNION
                {{ <{0}> skos:definition    ?description . }}
                UNION
                {{ <{0}> dct:description    ?description . }}
            }}

            # usage notes
            OPTIONAL {{
                <{0}> skos:scopeNote       ?usage .
            }}
        }}
        '''.format(self.uri)

        for r in self.g.query(q):
            self.name = r.name if r.name is not None else self.get_element_name_from_uri(self, self.uri)
            self.fid = self._make_fid()
            self.description = markdown.markdown(r.description) if r.description is not None else None
            self.usage = r.usage

    @staticmethod
    def get_element_name_from_uri(self, uri):
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

    def _remove_non_ascii_chars(self, s):
        return ''.join(i for i in s if ord(i) < 128)

    # makes the fragment ID for a class, property, Named Individual (any entity) based on URI & label
    def _make_fid(self):
        # try creating an ID from label
        # lowercase, remove spaces, escape all non-ASCII chars
        if self.name is not None:
            fid = self._remove_non_ascii_chars(self.name.lower().replace(' ', ''))

            if fid not in self.existing_fids:
                self.existing_fids.append(fid)
                return fid

        # this fid is already present in fragment ids so generate a fid from the URI instead

        # split URI for last slash segment
        segments = self.uri.split('/')
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

    @property
    def html(self):
        return self._html
