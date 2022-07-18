from termcolor import colored
from collections import defaultdict


class Graph():
    def __init__(self, graph_dictionary: dict = None):
        if graph_dictionary is None:
            graph_dictionary = {}
        self.graph_dictionary = graph_dictionary

    def bfs(self, start_vertex: str, end_vertex: str):
        queue = []
        queue.append([start_vertex])
        
        while queue:
            path = queue.pop(0) # dequeue
            node = path[-1]
            if node == end_vertex:
                return path
            for adjacent_vertex in self.graph_dictionary.get(node, []):
                new_path = list(path) # list creation
                new_path.append(adjacent_vertex)
                queue.append(new_path)

class WeightedGraph():
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
  
    def __str__(self):
        return str(self.edges)

    def add_node(self, node: str):
        self.nodes.add(node) 

    def add_edge(self, from_node: str, to_node: str, distance: float):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance #dict with a tuple as a key

def dijkstra(graph: WeightedGraph, initial_node: str)-> tuple:
    visited = {initial_node: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)
    print('Nodes', nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
            # only min_node matters ahead this nested loop
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(min_node)

    return visited, path

if __name__ == '__main__':
    print(colored('---------------------- GRAPH ----------------------', 'red'))
    print(colored('----------- SINGLE SOURCE SHORTEST PATH -----------', 'red'))
    print(colored('-------------- BREADTH FIRST SEARCH ---------------', 'red'))
    breadth_first_search_dict = {"a": ["b", "c"],
                                 "b": ["d", "g"],
                                 "c": ["d", "e"],
                                 "d": ["b", "f"],
                                 "e": ["c", "f"],
                                 "f": ["d", "e", "g"],
                                 "g": ["b", "f"]
    }
    graph = Graph(breadth_first_search_dict)
    print(graph.bfs('a', 'e'))
    print('\n')

    print(colored('--------------- DIJKSTRA ALGORITHM ----------------', 'red'))
    custom_graph = WeightedGraph()
    custom_graph.add_node('A')
    custom_graph.add_node('B')
    custom_graph.add_node('C')
    custom_graph.add_node('D')
    custom_graph.add_node('E')
    custom_graph.add_node('F')
    custom_graph.add_node('G')

    custom_graph.add_edge('A', 'B', 2)
    custom_graph.add_edge('A', 'C', 5)
    custom_graph.add_edge('B', 'C', 6)
    custom_graph.add_edge('B', 'E', 3)
    custom_graph.add_edge('B', 'D', 1)
    custom_graph.add_edge('C', 'F', 8)
    custom_graph.add_edge('D', 'E', 4)
    custom_graph.add_edge('F', 'G', 7)
    custom_graph.add_edge('E', 'G', 9)
    print('Result', dijkstra(custom_graph, 'A'))