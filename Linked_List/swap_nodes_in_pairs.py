from re import S
from typing import Generic
from linked_list_generic import GenericLinkedList
from termcolor import colored

"""
Quizz

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
the values in the list's nodes (i.e., only nodes themselves may be changed.)

"""
class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()

    def swap_nodes_in_pairs(self):
        # creation of an auxiliar linked list
        dummy_linked_list = GenericLinkedList() 
        dummy_linked_list.insert(0)
        dummy_linked_list.head.next = self.head
        
        previous = dummy_linked_list # original historic
        iterator = self.head

        while iterator and iterator.next:
            # save pointers
            next_pair = iterator.next.next
            second = iterator.next

            # reverse the current pair
            second.next = iterator
            iterator.next = next_pair
            previous.next = second #original second node is now reversed

            # update pointers
            previous = iterator
            iterator = next_pair

        print(dummy_linked_list)
        return dummy_linked_list.head.next

if __name__ == '__main__':
    print(colored('-------------------- LINKED LIST --------------------', 'red'))
    print(colored('---------------- SWAP NODES IN PAIRS ----------------', 'red'))
    linked_list = SolutionLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    print(linked_list)
    print(linked_list.swap_nodes_in_pairs())







