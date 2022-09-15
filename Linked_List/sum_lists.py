from linked_list_generic import GenericLinkedList
from termcolor import colored

import random
"""
Quizz

You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list

"""

def sum_lists(linked_list_1: GenericLinkedList, linked_list_2: GenericLinkedList)-> GenericLinkedList:
    iterator_1 = linked_list_1.head
    iterator_2 = linked_list_2.head
    carry = 0

    solution_linked_list = GenericLinkedList()

    while iterator_1 or iterator_2:
        result = carry
        result += iterator_1.value if iterator_1 else 0
        result += iterator_2.value if iterator_2 else 0
        iterator_1 = iterator_1.next if iterator_1 else None
        iterator_2 = iterator_2.next if iterator_2 else None
        solution_linked_list.insert((int(result % 10)))
        carry = result / 10

    return solution_linked_list

if __name__ == '__main__':
    print(colored('-------------------- LINKED LIST --------------------', 'red'))
    print(colored('--------------------- SUM LISTS ---------------------', 'red'))
    linked_list_1 = GenericLinkedList()
    linked_list_1.insert(7)
    linked_list_1.insert(1)
    linked_list_1.insert(6)

    linked_list_2 = GenericLinkedList()
    linked_list_2.insert(5)
    linked_list_2.insert(9)
    linked_list_2.insert(2)
    print(linked_list_1)
    print(linked_list_2)
    print(sum_lists(linked_list_1, linked_list_2))