from typing import Union
from rdflib import Dataset, URIRef, Graph


def get_graph_from_dataset(d: Dataset, graph_identifier: URIRef) -> Union[Graph, None]:
    return [x for x in d.contexts() if x.identifier == graph_identifier][0]
