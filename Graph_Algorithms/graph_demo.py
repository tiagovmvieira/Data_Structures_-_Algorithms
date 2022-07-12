class Graph():
    def __init__(self, graph_dictionary: dict = None):
        if graph_dictionary is None:
            graph_dictionary = {}
        self.graph_dictionary = graph_dictionary

    def add_edge(self, vertex: str, edge: str):
        self.graph_dictionary[vertex].append(edge)

graph = Graph()
try:
    graph.add_edge('A', 'B')
except KeyError:
    print('Vertice A does not exist already')