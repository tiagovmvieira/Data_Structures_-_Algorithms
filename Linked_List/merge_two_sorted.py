from typing import Generic
from linked_list_generic import GenericLinkedList
from termcolor import colored

"""
Quizz

Merge two sorted lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()

    def merge_two_lists(self, linked_list_1: GenericLinkedList, linked_list_2: GenericLinkedList):
        iterator_1 = linked_list_1.head
        iterator_2 = linked_list_2.head

        while iterator_1 and iterator_2:
            if iterator_1.value <= iterator_2.value:
                self.insert(iterator_1.value)
                iterator_1 = iterator_1.next 
            else:
                self.insert(iterator_2.value)
                iterator_2 = iterator_2.next

        while iterator_1:
            self.insert(iterator_1.value)
            iterator_1 = iterator_1.next
        
        while iterator_2:
            self.insert(iterator_2.value)
            iterator_2 = iterator_2.next

if __name__ == '__main__':
    print(colored('-------------------- LINKED LIST --------------------', 'red'))
    print(colored('--------------- MERGE TWO SORTED LISTS --------------', 'red'))
    linked_list_1 = SolutionLinkedList()
    linked_list_1.insert(1)
    linked_list_1.insert(2)
    linked_list_1.insert(4)
    print(linked_list_1)

    linked_list_2 = SolutionLinkedList()
    linked_list_2.insert(1)
    linked_list_2.insert(3)
    linked_list_2.insert(4)
    print(linked_list_2)

    merged_linked_list = SolutionLinkedList()
    merged_linked_list.merge_two_lists(linked_list_1, linked_list_2)
    print(merged_linked_list)

