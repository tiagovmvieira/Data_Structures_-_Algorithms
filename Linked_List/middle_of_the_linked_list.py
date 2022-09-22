from linked_list_generic import GenericLinkedList, Node
from termcolor import colored

"""
Quizz

Given a linked list, return the middle node of the linked list

If there are two middle nodes, return the second middle node.
"""

class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()


    def return_middle_node(self)-> Node:
        slow_pointer = fast_pointer = self.head
        linked_list_len = 1

        while fast_pointer and fast_pointer.next:
            linked_list_len += 2
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if fast_pointer == self.tail:
                if (linked_list_len % 2) == 0:
                    return slow_pointer.next
                else:
                    return slow_pointer
        return slow_pointer

if __name__ == '__main__':
    odd_solution_linked_list = SolutionLinkedList()
    odd_solution_linked_list.insert(1)
    odd_solution_linked_list.insert(2)
    odd_solution_linked_list.insert(3)
    odd_solution_linked_list.insert(4)
    odd_solution_linked_list.insert(5)
    print('Middle Node', odd_solution_linked_list.return_middle_node().value)

    even_solution_linked_list = SolutionLinkedList()
    even_solution_linked_list.insert(1)
    even_solution_linked_list.insert(2)
    even_solution_linked_list.insert(3)
    even_solution_linked_list.insert(4)
    even_solution_linked_list.insert(5)
    even_solution_linked_list.insert(6)

    print('Middle Node', even_solution_linked_list.return_middle_node().value)