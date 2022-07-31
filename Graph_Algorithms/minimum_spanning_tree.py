from termcolor import colored

class DisjointSet():
    def __init__(self, vertices, parent):
        self.vertices = vertices
        self.parent = parent
        self.rank = dict.fromkeys(vertices, 0)

if __name__ == '__main__':
    print(colored('----------------- GRAPH ALGORITHMS ----------------', 'red'))
    