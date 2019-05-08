from abc import ABC


class Entities(ABC):
    def __init__(self):
        self.instances = []

    def render_html(self):
        pass


class Entity(ABC):
    def __init__(self, existing_fids, uri, name, description, usage):
        self.uri = uri
        self.name = name if name is not None else self._get_element_name_from_uri()
        self.fid = self._make_fid(existing_fids)
        self.description = description
        self.usage = usage

    def render_html(self):
        pass

    def _get_element_name_from_uri(self):
        # can't tolerate any URI faults so return None if anything is wrong

        # URIs with no path segments or ending in slash
        segments = self.uri.split('/')
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
    def _make_fid(self, existing_fids):
        # try creating an ID from label
        # lowercase, remove spaces, escape all non-ASCII chars
        if self.name is not None:
            fid = self._remove_non_ascii_chars(self.name.lower().replace(' ', ''))

            if fid not in existing_fids:
                existing_fids.append(fid)
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
