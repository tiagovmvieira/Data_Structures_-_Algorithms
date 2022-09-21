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


    def o_n_check_cycle(self)-> bool:
        visited = set()
        
        iterator = self.head
        while iterator:
            if iterator not in visited:
                visited.add(iterator)
            else:
                return True
        
            iterator = iterator.next
        return False

    def o_1_check_cycle(self)-> bool:
        slow_pointer = fast_pointer = self.head

        while slow_pointer and fast_pointer and fast_pointer.next: #fast_pointer.next to avoid a one node linked_list -> direct to False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False


if __name__ == '__main__':
    solution_linked_list = SolutionLinkedList()
    solution_linked_list.insert(3)
    solution_linked_list.insert(2)
    solution_linked_list.insert(0)
    solution_linked_list.insert(-4)
    solution_linked_list.tail.next = solution_linked_list.head.next
    print(solution_linked_list.o_1_check_cycle())

    another_linked_list = SolutionLinkedList()
    another_linked_list.insert(1)
    another_linked_list.insert(2)
    another_linked_list.tail.next = another_linked_list.head
    print(another_linked_list.o_1_check_cycle())

    final_linked_list = SolutionLinkedList()
    final_linked_list.insert(1)
    print(final_linked_list.o_1_check_cycle())