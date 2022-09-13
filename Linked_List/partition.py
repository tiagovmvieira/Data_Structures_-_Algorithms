from linked_list_generic import GenericLinkedList
from termcolor import colored

"""
Quizz

Partition: Write code to a partition linked list around a value x, such that all nodes less than x
come before all nodes greater than or equal to x.
"""

class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()

    def partition(self, value: int):
        current_node = self.head
        self.tail = self.head

        while current_node:
            next_node = current_node.next #next node
            current_node.next = None 
            if current_node.value > value:
                self.tail.next = current_node
                self.tail = current_node
            else:
                current_node.next = self.head
                self.head = current_node
            current_node = next_node # looping

        if self.tail.next is not None:
            self.tail.next = None

        return self

if __name__ == '__main__':
    print(colored('-------------------- LINKED LIST --------------------', 'red'))
    print(colored('-------------------- PARTITION ----------------------', 'red'))
    solution_linked_list = SolutionLinkedList()
    solution_linked_list.generate(10, 0, 99)
    print(solution_linked_list)
    print(solution_linked_list.partition(30))

