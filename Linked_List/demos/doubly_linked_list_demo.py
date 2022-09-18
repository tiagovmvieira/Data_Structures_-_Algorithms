from termcolor import colored
from typing import Union

class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

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
        index = isinstance(location, int)
        if index and (location < 1 or location > self.__get_length() + 1):
            raise ValueError(f"location: The location must be between 1 and {self.__get_length() + 1}")

        if self.head is None:
            return 'The Doubly Linked List does not exist'
        
        node = Node(value)
        if location == 'first': #beginning
            node.previous = None #node connection
            node.next = self.head #node connection
            self.head.previous = node #node connection
            self.head = node #tag
        elif location == 'last': #end
            node.next = None #node connection
            node.previous = self.tail #node connection
            self.tail.next = node #node connection
            self.tail = node #tag
        elif location == 'middle': #middle
            if not (self.__get_length() % 2) == 0:
                return ValueError("location: The Singly Linked List does not contain a middle position to insert into the node")

            iterator = self.head
            index = 0
            while index < (self.__get_length() // 2) - 1:
                iterator = iterator.next
                index += 1
            next_node = iterator.next
            node.next = next_node
            node.previous = iterator
            node.next.previous = node
            iterator.next = node
        else: #specific location
            if location == 1:
                self.insert(node.value, 'first')
            elif location == self.__get_length() + 1:
                self.insert(node.value, 'last')
            else:
                iterator = self.head
                index = 0
                while index < location - 1:
                    iterator = iterator.next
                    index += 1
                next_node = iterator.next
                node.next = next_node
                node.previous = iterator
                node.next.previous = node
                iterator.next = node

        return "The node has been successfully inserted"

    # traversal method in doubly linked list
    def traversal(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            iterator = self.head
            while iterator:
                print(iterator.value)
                iterator = iterator.next

    # reverse traversal method in doubly linked list
    def reverse_traversal(self):
        if self.head is None:
            print("There is not any element for reverse traversal")
        else:
            iterator = self.tail
        while iterator:
            print(iterator.value)
            iterator = iterator.previous
        
    # search for a node in a doubly linked list
    def search(self, node_value: int)-> str:
        if self.head is None:
            return 'The Doubly Linked List does not exist'

        i = 1
        iterator = self.head
        while iterator:
            if iterator.value == node_value:
                return f"The node containing the value {node_value} exists and it is in the position {i}"
            iterator = iterator.next
            i += 1
        return "The node does not exist in this Doubly Linked List"

    # deletion of a node in a doubly linked list
    def delete_node(self, location: Union[str, int] = 'last')-> str:
        if self.head is None:
            return 'The Doubly Linked List does not exist'

        if location == 'first': #beginning
            if self.__get_length() == 1: #only one node
                self.head = None
                self.tail = None
            else: #more than one node 
                self.head = self.head.next
                self.head.previous = None
        elif location == 'last': #end
            if self.__get_length() == 1: #only one node
                self.head = None
                self.tail = None
            else: #more than one node
                self.tail = self.tail.previous
                self.tail.next = None
        elif location == 'middle': #middle
            iterator = self.head
            index = 0
            while index < (self.__get_length() // 2) - 1:
                iterator = iterator.next
                index += 1
            iterator.next = iterator.next.next
            iterator.next.previous = iterator
        else: #specific location
            if location == 1:
                self.delete_node('first')
            elif location == self.__get_length():
                self.delete_node('last')
            else:
                iterator = self.head
                index = 0
                while index < location - 1:
                    iterator = iterator.next
                    index += 1
                iterator.next = iterator.next.next
                iterator.next.previous = iterator
                
        return 'The node has been successfully deleted'

    def delete(self):
        if self.head is None:
            return "The Doubly Linked List does not exist"

        iterator = self.head
        while iterator:
            iterator.prev = None
            iterator = iterator.next
        self.head = None
        self.tail = None
        return 'The Doubly Linked List has been deleted'

if __name__ == '__main__':
    print(colored('---------------- DOUBLY LINKED LIST -----------------', 'red'))
    print(colored('------------------- LIST CREATION -------------------', 'red'))
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.create(1)
    doubly_linked_list.print()

    print(colored('------------------- LIST INSERTION ------------------', 'red'))
    doubly_linked_list.insert(0, 'first')
    doubly_linked_list.insert(3, 'last')
    doubly_linked_list.insert(4, 4)
    doubly_linked_list.insert(2, 'middle')
    doubly_linked_list.print()

    print(colored('------------------- LIST TRAVERSAL ------------------', 'red'))
    doubly_linked_list.traversal()

    print(colored('--------------- LIST REVERSE TRAVERSAL --------------', 'red'))
    doubly_linked_list.reverse_traversal()

    print(colored('-------------------- LIST SEARCH --------------------', 'red'))
    print(doubly_linked_list.search(3))

    print(colored('---------------- DELETION OF A NODE -----------------', 'red'))
    doubly_linked_list.print()
    doubly_linked_list.delete_node('last')
    doubly_linked_list.delete_node('first')
    doubly_linked_list.print()
    doubly_linked_list.delete_node('middle')
    doubly_linked_list.print()
    doubly_linked_list.delete_node(2)
    doubly_linked_list.print()

    print(colored('------------------- LIST DELETION -------------------', 'red'))
    doubly_linked_list.delete()
    doubly_linked_list.print()
