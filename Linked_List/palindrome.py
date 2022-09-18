from linked_list_generic import GenericLinkedList, Node
from termcolor import colored

"""
Quizz

Palindrome: Implement a method to check if a linked list is a palindrome
"""

class SolutionLinkedList(GenericLinkedList):
    def __init__(self):
        super().__init__()

    def check_palindrome(self)-> bool:
        iterator = self.head
        N = 0
        while iterator:
            N += 1
            iterator = iterator.next
        middle = N // 2
        i = 0
        
        first = second = self.head
        while i < middle:
            second = second.next
            i += 1
        second = reverse_linked_list(second)

        while first and second:
            if first.value != second.value:
                return False
            first = first.next
            second = second.next
        return True

def reverse_linked_list(head: Node)-> Node:
    iterator = head
    previous_node = None

    while iterator:
        historic = iterator.next
        iterator.next = previous_node

        previous_node = iterator
        iterator = historic
    return previous_node

if __name__ == '__main__':
    print(colored('-------------------- LINKED LIST --------------------', 'red'))
    print(colored('-------------------- PALINDROME ---------------------', 'red'))
    palindrome = SolutionLinkedList()
    palindrome.insert(1)
    palindrome.insert(2)
    palindrome.insert(3)
    palindrome.insert(2)
    palindrome.insert(1)
    print(palindrome)
    print(palindrome.check_palindrome())

    not_palindrome = SolutionLinkedList()
    not_palindrome.insert(1)
    not_palindrome.insert(2)
    not_palindrome.insert(3)
    not_palindrome.insert(4)
    not_palindrome.insert(5)
    print(not_palindrome)
    print(not_palindrome.check_palindrome())
