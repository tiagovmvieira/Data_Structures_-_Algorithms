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

    def bfs(self, vertex: str):
        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeue_vertex = queue.pop(0) # dequeue first element
            print(dequeue_vertex)
            for adjacent_vertex in self.graph_dictionary.get(dequeue_vertex):
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def dfs(self, vertex: str):
        visited = [vertex]
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop() # pop last element
            print(pop_vertex)
            for adjacent_vertex in self.graph_dictionary.get(pop_vertex):
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)

  
if __name__ == '__main__':
    print(colored('---------------------- GRAPH ----------------------', 'red'))
    graph = Graph()

    print(colored('------------- EDGE TO AN EMPTY GRAPH --------------', 'red'))
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    print(graph)

    print(colored('------------ EDGE TO AN EXISTING GRAPH ------------', 'red'))
    custom_dict = { "a": ["b", "c"],
                    "b": ["a", "d", "e"],
                    "c": ["a", "e"],
                    "d": ["b", "e", "f"],
                    "e": ["d", "f"],
                    "f": ["d", "e"]
    }
    new_graph = Graph(custom_dict)
    new_graph.add_edge("e", "c")
    print(new_graph)
    
    print(colored('------------ GRAPH BREADTH FIRST SEARCH -----------', 'red'))
    new_graph.bfs('a')

    print(colored('------------- GRAPH DEPTH FIRST SEARCH ------------', 'red'))
    new_graph.dfs('a')