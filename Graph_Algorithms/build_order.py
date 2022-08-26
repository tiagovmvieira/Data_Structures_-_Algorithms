from typing import List
from termcolor import colored

def create_graph(projects: list, dependencies: List[set])-> list:
    project_graph = {}
    for project in projects:
        project_graph[project] = []

    for dependency in dependencies:
        project_graph[dependency[0]].extend(dependency[1])
    
    return project_graph

def get_projects_with_dependecies(project_graph: dict)-> set:
    projects_with_dependecies = set()
    for project in project_graph:
        projects_with_dependecies = projects_with_dependecies.union(set(project_graph[project]))

    return projects_with_dependecies

def get_projects_without_dependecies(projects_with_dependecies: set, project_graph: dict)-> set:
    projects_without_dependecies = set()
    for project in project_graph:
        if project in projects_with_dependecies:
            continue
        else:
            projects_without_dependecies.add(project)

    return projects_without_dependecies

def find_build_order(projects: list, dependecies: List[set])-> list:
    build_order = []
    project_graph = create_graph(projects, dependecies)
    while project_graph:
        projects_with_dependecies = get_projects_with_dependecies(project_graph)
        projects_without_dependecies = get_projects_without_dependecies(projects_with_dependecies, project_graph)
        
        if len(projects_without_dependecies) == 0 and project_graph:
            raise ValueError('There is a cycle in the build order')
       
        for project in projects_without_dependecies:
            build_order.append(project)
            project_graph.pop(project, None)
    
    return build_order

if __name__ == '__main__':
    print(colored('----------------- GRAPH ALGORITHMS ----------------', 'red'))
    print(colored('------------------- BUILD ORDER -------------------', 'red'))
    print(find_build_order(['a', 'b', 'c', 'd', 'e', 'f'],
                    [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
                    ))