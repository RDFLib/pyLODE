from typing import Optional, Union

from rdflib import Dataset as _Dataset, Graph, URIRef, BNode
from rdflib.graph import _ContextIdentifierType, _ContextType


class Dataset(_Dataset):
    def add_graph(
        self, g: Optional[Union[_ContextIdentifierType, _ContextType, str]]
    ) -> Graph:
        """Add a graph to dataset with correct context set.

        If we use self.add_graph(graph), it doesn't add the context correctly. Then if we
        try and query the default graph like, self.objects(None, None), it returns nothing.

        This function fixes the above issue.
        """
        identifier = URIRef(g.identifier) or BNode()
        if identifier in self.graphs():
            _graph = self.get_graph(identifier)
        else:
            _graph = Graph(identifier=identifier)
            _graph.__iadd__(g)
            super().add_graph(_graph)
        for s, p, o in g:
            self.add((s, p, o, _graph))

        return self.get_graph(identifier)
