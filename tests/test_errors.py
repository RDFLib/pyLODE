import sys
from pathlib import Path

sys.path.append(str(Path().absolute().parent.parent / "pylode"))

from pylode.ontdoc import OntDoc, PylodeError

import pytest


def test_no_title():
    ont_notitle = """
        @prefix : <http://example.com/minimal/> .
        @prefix owl: <http://www.w3.org/2002/07/owl#> .
        
        <http://example.com/minimal>
            a owl:Ontology ;
        .
        """
    with pytest.raises(PylodeError) as ctx:
        od = OntDoc(ont_notitle).ont


def test_invalid_rdf():
    invalid_rdf = """
        @prefix : <http://example.com/minimal/> .
        # @prefix owl: <http://www.w3.org/2002/07/owl#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

        <http://example.com/minimal>
            a owl:Ontology ;
            rdfs:label "Minimal Ontology" ;
        .
        """
    with pytest.raises(SystemExit):
        od = OntDoc(invalid_rdf)


def test_no_file():
    with pytest.raises(SystemExit):
        od = OntDoc("this-is-not-a-file.ttl")


if __name__ == "__main__":
    od = OntDoc("this-is-not-a-file.ttl")
