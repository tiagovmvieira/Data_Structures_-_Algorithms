from re import I
from linked_list_generic import GenericLinkedList
from termcolor import colored

"""
Given a linked list, and an integer 'val', remove all the nodes of the linked list that has 'Node.vall = val',
and return the new linked_list.

"""
class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()

    def remove_linked_list_elements(self, val: int)-> GenericLinkedList:
        iterator = self.head

        while iterator:
            if iterator.value == val: # head or single value linked list
                if iterator == self.head:
                    if self.head.next == None:
                        self.head = None
                        self.tail = None
                    else: # more than one node
                        self.head = self.head.next
            elif iterator.next.value == val: ## middle or tail
                if iterator.next == self.tail:
                    iterator.next = None
                    self.tail = iterator
                else: # middle
                    historic = iterator.next
                    iterator.next = historic.next
            iterator = iterator.next
        return self
        
if __name__ == '__main__':
    solution_linked_list = SolutionLinkedList()
    solution_linked_list.insert(1)
    solution_linked_list.insert(2)
    solution_linked_list.insert(6)
    solution_linked_list.insert(3)
    solution_linked_list.insert(4)
    solution_linked_list.insert(5)
    solution_linked_list.insert(6)
    print(solution_linked_list)
    print('After removal:',solution_linked_list.remove_linked_list_elements(6))

    another_linked_list = SolutionLinkedList()
    print('After removal:', another_linked_list.remove_linked_list_elements(1))

    final_linked_list = SolutionLinkedList()
    final_linked_list.insert(7)
    final_linked_list.insert(7)
    final_linked_list.insert(7)
    final_linked_list.insert(7)
    print('After removal:', final_linked_list.remove_linked_list_elements(7))


