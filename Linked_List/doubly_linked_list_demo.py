from termcolor import colored
from typing import Union

class Node():
    def __init__(self, value: int = None):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def _get_length(self)-> int:
        if self.head is None:
            return 0

        result = 1
        iterator = self.head
        while iterator != self.tail:
            result += 1
            iterator = iterator.next
        return result

    def print(self)-> list:
        print([node.value for node in self])

    # creation of a doubly linked list
    def create(self, value: int)-> str:
        node = Node(value)
        node.next = None
        node.previous = None
        self.head = node
        self.tail = node

        return "The Doubly Linked List has been created"

    # insertion of a node in a doubly linked list
    def insert(self, value: int, location: Union[str, int] = 'last')-> str:
        if self.head is None:
            return 'The Doubly Linked List does not exist'
        else:
            node = Node(value)
            if location == 'first': #beginning?
                node.previous = None #node connection
                node.next = self.head #node connection
                self.head.previous = node #node connection
                self.head = node #tag
            elif location == 'last': #end?
                node.next = None #node connection
                node.previous = self.tail #node connection
                self.tail.next = node #node connection
                self.tail = node #tag
            elif location == 'middle': #middle?
                iterator = self.head
                index = 0
                while index < (self._get_length() // 2) - 1:
                    iterator = iterator.next
                    index += 1
                next_node = iterator.next
                node.next = next_node
                node.previous = iterator
                node.next.previous = node
                iterator.next = node
            else:
                pass
        return "The node has been successfully inserted"

if __name__ == '__main__':
    print(colored('---------------- DOUBLY LINKED LIST -----------------', 'red'))
    print(colored('------------------- LIST CREATION -------------------', 'red'))
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.create(5)
    doubly_linked_list.insert(2, 'first')
    doubly_linked_list.insert(3)
    doubly_linked_list.insert(4, 'middle')
    doubly_linked_list.insert(6, 'middle')
    doubly_linked_list.print()
    print(doubly_linked_list._get_length())