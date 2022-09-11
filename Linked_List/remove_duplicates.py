from linked_list_generic import GenericLinkedList
from termcolor import colored

"""
Quizz

Remove Duplicates: Write code to remove duplicates from an unsorted singly linked list
"""

class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()

    def __delete_node(self, location: int):
        if location == 1: # begginning
            if len(self) == 1: #only one node
                self.head = None
                self.tail = None
            else: #more than one node
                self.head = self.head.next
        elif location == len(self): #end
            if len(self) == 1: #only one node
                self.head = None
                self.tail = None
            else: #more than one node
                iterator = self.head
                while iterator is not None:
                    if iterator.next == self.tail:
                        break
                    iterator = iterator.next
                iterator.next = None
                self.tail = iterator
        else: #specific position
            iterator = self.head 
            i = 1
            while i < location - 1:
                iterator = iterator.next
                i += 1
            next_node = iterator.next
            iterator.next = next_node.next

    def remove_duplicates(self):
        iterator = self.head
        visited = []
        i = 1
        while iterator:
            if iterator.value in visited:
                self.__delete_node(i)
                i -= 1
            else:
                visited.append(iterator.value)
                i += 1
            iterator = iterator.next

if __name__ == '__main__':
    print(colored('-------------------- LINKED LIST --------------------', 'red'))
    print(colored('----------------- REMOVE DUPLICATES -----------------', 'red'))
    solution_linked_list = SolutionLinkedList()
    solution_linked_list.generate(20, 0, 10)
    print(solution_linked_list)
    solution_linked_list.remove_duplicates()
    print(solution_linked_list)

