from termcolor import colored
from typing import List

class DisjointSet():
    def __init__(self, vertices: List[str]):
        self.vertices = vertices
        self.parent = {}
        self.rank = dict.fromkeys(vertices, 0)
        for v in vertices:
            self.parent[v] = v

    def find(self, item: str):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x: str, y: str):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

if __name__ == '__main__':
    print(colored('----------------- GRAPH ALGORITHMS ----------------', 'red'))
    print(colored('-------------- MINIMUM SPANNING TREE --------------', 'red'))
    vertices = ['A', 'B', 'C', 'D', 'E']
    disjoint_set = DisjointSet(vertices)
    disjoint_set.union('A', 'B')
    disjoint_set.union('A', 'C')
    print(disjoint_set.find('A'))
    