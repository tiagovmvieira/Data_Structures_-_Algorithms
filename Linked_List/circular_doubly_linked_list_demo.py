from termcolor import colored
from typing import Union

class Node():
    def __init__(self, value: int = None):
        self.value = value
        self.next = None
        self.previous = None

class CircularDoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def __get_length(self)-> int:
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

    # creation of a circular doubly linked list
    def create(self, value: int)-> str:
        node = Node(value)
        self.head = node
        self.tail = node
        node.previous = node
        node.next = node

        return "The Doubly Linked List has been created"

    # insertion of a node in a circular doubly linked list
    def insert(self, value: int, location: Union[str, int] = 'last')-> str:
        if self.head is None:
            return 'The Circular Doubly Linked List does not exist'

        node = Node(value)
        if location == 'first':
            node.next = self.head
            node.previous = self.tail
            self.head.previous = node
            self.head = node #tag
            self.tail.next = node
        elif location == 'last':
            node.next = self.head
            node.previous = self.tail
            self.head.previous = node
            self.tail.next = node
            self.tail = node
        elif location == 'middle':
            if (self.__get_length() % 2) == 0:
                return 'The Circular Doubly Linked List does not a middle position to insert into the node'
            iterator = self.head
            index = 0
            while index < (self.__get_length() // 2) - 1:
                iterator = iterator.next
                index += 1
            node.next = iterator.next
            node.previous = iterator
            node.next.previous = iterator
            node.next = iterator
        else:
            if location == 1:
                node.next = self.head
                node.previous = self.tail
                self.head.previous = node
                self.head = node
                self.tail.next = node
            elif location == self.__get_length():
                node.next = self.head
                node.previous = self.tail
                self.head.previous = node
                self.tail.next = node
                self.tail = node
            else:
                iterator = self.head
                index = 0
                while index < location - 1:
                    iterator = iterator.next
                    index += 1
                node.next = iterator.next
                node.previous = iterator
                node.next.previous = node
                iterator.next = node
        return "The node has been successfully inserted"

if __name__ == '__main__':
    print(colored('----------- CIRCULAR DOUBLY LINKED LIST -------------', 'red'))
    print(colored('------------------- LIST CREATION -------------------', 'red'))
    circular_doubly_linked_list = CircularDoublyLinkedList()
    print(circular_doubly_linked_list.create(1))
    circular_doubly_linked_list.print()
    print(colored('------------------- LIST INSERTION ------------------', 'red'))
    circular_doubly_linked_list.insert(4, 'last')
    circular_doubly_linked_list.insert(0, 'first')
    circular_doubly_linked_list.insert(3, 2)
    circular_doubly_linked_list.insert(5)
    print(circular_doubly_linked_list.insert(2, 'middle'))
    circular_doubly_linked_list.print()
    print(circular_doubly_linked_list.insert(2, 'middle'))
    circular_doubly_linked_list.print()

