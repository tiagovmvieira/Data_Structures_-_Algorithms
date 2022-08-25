from termcolor import colored

class Graph():
    def __init__(self, graph_dictionary: dict = None):
        if graph_dictionary is None:
            graph_dictionary = {}
        self.graph_dictionary = graph_dictionary
    
    def __str__(self)-> str:
        return str(self.graph_dictionary)

    def _arrange_graph(self):
        visited_vertices = []
        visited_keys = []
        for key in self.graph_dictionary:
            visited_keys.append(key)
            visited_vertices.append(key) if key not in visited_vertices else None
            for value in self.graph_dictionary.get(key):
                visited_vertices.append(value) if value not in visited_vertices else None
    
        a = set(visited_keys).union(set(visited_vertices))
        b = set(visited_keys).intersection(set(visited_vertices))
        c = list(a - b)

        auxiliar_graph = dict.fromkeys(c, [])
        self.graph_dictionary.update(auxiliar_graph)

    def add_edge(self, vertex: str, edge: str):
        try:
            self.graph_dictionary[vertex].append(edge)
        except KeyError:
            self.graph_dictionary[vertex] = [edge]        

    def check_route(self, start_node: str, end_node: str)-> bool:
        self._arrange_graph()
        visited_nodes = [start_node]
        queue = [start_node]
        path = False
        while queue:
            dequeue_vertex = queue.pop(0) #dequeue first element
            for adjacent_vertex in self.graph_dictionary.get(dequeue_vertex):
                if adjacent_vertex not in visited_nodes:
                    if adjacent_vertex == end_node:
                        path = True
                        break
                    else:
                        visited_nodes.append(adjacent_vertex)
                        queue.append(adjacent_vertex)
        return path

if __name__ == '__main__':
    print(colored('----------------- GRAPH ALGORITHMS ----------------', 'red'))
    graph = Graph()

    print(colored('----------------- GRAPH CREATION ------------------', 'red'))
    graph.add_edge('E', 'F')
    graph.add_edge('E', 'A')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('A', 'B')
    graph.add_edge('F', 'I')
    graph.add_edge('C', 'G')
    graph.add_edge('G', 'D')
    graph.add_edge('G', 'H')
    graph.add_edge('B', 'J')
    print(graph)

    print(colored('--- CHECK IF THERE IS A ROUTE BETWEEN TWO NODES ---', 'red'))
    print(graph.check_route('A', 'H'))