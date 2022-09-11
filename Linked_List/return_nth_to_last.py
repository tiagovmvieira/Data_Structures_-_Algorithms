from re import S
from linked_list_generic import GenericLinkedList
from termcolor import colored

"""
Quizz

Implement an algorithm to find the nth to last element of a singly linked list
"""

class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()

    # trivial solution
    def find_nth_to_last_trivial(self, nth: int)-> int:
        if (nth < 2 or nth > len(self) - 1):
            raise ValueError(f"n: The value for the nth element should be between 2 and {len(self) - 1}") 

        iterator = self.head
        i = 1
        while iterator:
            if len(self) - i == nth - 1:
                return iterator.value
            i += 1
            iterator = iterator.next

    def find_nth_to_last(self, nth)-> int:
        if (nth < 2 or nth > len(self) - 1):
            raise ValueError(f"n: The value for the nth element should be between 2 and {len(self) -1}")

        pointer_1 = self.head
        pointer_2 = self.head

        for i in range(nth):
            pointer_2 = pointer_2.next

        while pointer_2:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

        return pointer_1.value

    
            


if __name__ == '__main__':
    print(colored('-------------------- LINKED LIST --------------------', 'red'))
    print(colored('---------------- RETURN nth TO LAST -----------------', 'red'))
    solution_linked_list = SolutionLinkedList()
    solution_linked_list.generate(10, 0, 10)
    print(solution_linked_list)
    print(solution_linked_list.find_nth_to_last_trivial(5))
    print(solution_linked_list.find_nth_to_last(5))