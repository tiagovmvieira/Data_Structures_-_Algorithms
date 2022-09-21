from linked_list_generic import GenericLinkedList
from termcolor import colored
from typing import Tuple, Union
"""
Quizz

Given a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the 'next' pointer. Internally, 'pos' is used to denote the index of the node that tail's 'next' pointer is connected to.
Note that 'pos' is not passed as a paramater.

Return True if there is a cycle in the linked list. Otherwise, return False.
"""

class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()


    def check_cycle(self)-> Union[Tuple[bool, int], bool]:
        visited = set()
        
        iterator = self.head
        while iterator:
            if iterator not in visited:
                visited.add(iterator)
            else:
                return True
        
            iterator = iterator.next
        return False

if __name__ == '__main__':
    solution_linked_list = SolutionLinkedList()
    solution_linked_list.insert(3)
    solution_linked_list.insert(2)
    solution_linked_list.insert(0)
    solution_linked_list.insert(-4)
    solution_linked_list.tail.next = solution_linked_list.head.next
    print(solution_linked_list.check_cycle())

    another_linked_list = SolutionLinkedList()
    another_linked_list.insert(1)
    another_linked_list.insert(2)
    another_linked_list.tail.next = another_linked_list.head
    print(another_linked_list.check_cycle())

    final_linked_list = SolutionLinkedList()
    final_linked_list.insert(1)
    print(final_linked_list.check_cycle())