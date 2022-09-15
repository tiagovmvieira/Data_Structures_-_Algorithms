from linked_list_generic import GenericLinkedList
from termcolor import colored
from typing import Tuple, Union

"""
Quizz

Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value. That is, if the kth node of the
first linked list is the exact same node (by reference) as the jth node of the second linked
list, then they are intersecting.
"""

def intersection(linked_list_1: GenericLinkedList, linked_list_2: GenericLinkedList)-> Union[Tuple[bool], Tuple[bool, int]]:
    iterator_1 = linked_list_1.head
    iterator_2 = linked_list_2.head

    visited = []
    while iterator_1 or iterator_2:
        if (iterator_1.value or iterator_2.value) in visited:
            return True, iterator_1.value

        visited.append(iterator_1.value)
        visited.append(iterator_2.value)
        iterator_1 = iterator_1.next if iterator_1 else None
        iterator_2 = iterator_2.next if iterator_2 else None
    return False


if __name__ == '__main__':
    print(colored('-------------------- LINKED LIST --------------------', 'red'))
    print(colored('------------------ INTERSECT LISTS ------------------', 'red'))
    linked_list_1 = GenericLinkedList()
    linked_list_1.insert(3)
    linked_list_1.insert(1)
    linked_list_1.insert(5)
    linked_list_1.insert(9)
    linked_list_1.insert(7)
    linked_list_1.insert(2)
    linked_list_1.insert(1)

    linked_list_2 = GenericLinkedList()
    linked_list_2.insert(2)
    linked_list_2.insert(4)
    linked_list_2.insert(6)
    linked_list_2.insert(7)
    linked_list_2.insert(2)
    linked_list_2.insert(1)
    print(intersection(linked_list_1, linked_list_2))