from distutils import dep_util
from termcolor import colored

class Graph():
    def __init__(self, graph_dictionary: dict = None):
        if graph_dictionary is None:
            graph_dictionary = {}
        self.graph_dictionary = graph_dictionary
    
    def __str__(self)-> str:
        return str(self.graph_dictionary)

    def add_edge(self, vertex: str, edge: str):
        try:
            self.graph_dictionary[vertex].append(edge)
        except KeyError:
            self.graph_dictionary[vertex] = [edge]        
        
    def check_route(self, start_node: str, end_node: str)-> bool:
        visited_nodes = [start_node]
        queue = [start_node]
        path = False
        while queue:
            dequeue_vertex = queue.pop(0) #dequeue first element
            try:
                for adjacent_vertex in self.graph_dictionary.get(dequeue_vertex):
                    print(adjacent_vertex)
                    if adjacent_vertex not in visited_nodes:
                        if adjacent_vertex == end_node:
                            path = True
                            break
                        else:
                            visited_nodes.append(adjacent_vertex)
                            queue.append(adjacent_vertex)
            except KeyError:
                self.graph_dictionary[adjacent_vertex] = []
                visited_nodes.append(adjacent_vertex)
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