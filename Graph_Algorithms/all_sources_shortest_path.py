import numpy as np
from termcolor import colored
from typing import List

inf = np.inf
def print_solution(no_vertices: int, distance: List[list]):
    for i in range(no_vertices): #2D iteration
        for j in range(no_vertices):
            print(distance[i][j], end= " ")
        print(" ")

def floyd_warshall(no_vertices: int, graph: List[list]):
    distance = graph
    for vertice in range(no_vertices):
        # print('Iteration: {}'.format(vertice + 1))
        for i in range(no_vertices): # 2D iteration
            for j in range(no_vertices):
                distance[i][j] = min(distance[i][j], 
                                     distance[i][vertice] + distance[vertice][j]
                                    )
        # print_solution(no_vertices, distance)
        # print('----------')
    # print('Solution')
    print_solution(no_vertices, distance)

if __name__ == '__main__':
    print(colored('----------------- GRAPH ALGORITHMS ----------------', 'red'))
    print(colored('------------ ALL SOURCES SHORTEST PATH ------------', 'red'))
    graph = [
        [0, 8, inf, 1],
        [inf, 0, 1, inf],
        [4, inf, 0, inf],
        [inf, 2, 9, 0],
    ]
    print(colored('------------ FLOYD WARSHALL ALGORITHM ------------', 'red'))
    print(colored('------------------- GIVEN GRAPH -------------------', 'red'))
    print_solution(len(graph), graph)
    print(colored('--------------------- SOLUTION --------------------', 'red'))
    floyd_warshall(len(graph), graph)