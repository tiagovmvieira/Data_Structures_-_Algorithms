from termcolor import colored
from typing import Union

class Node():
    def __init__(self, value: int = None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    # get length of a circular singly linked list
    def _get_length(self)-> int:
        if self.head is None:
            return 0

        result = 1
        iterator = self.head

        while iterator != self.tail:
            result += 1
            iterator = iterator.next
        return result

    # creation of a circular singly linked list
    def create(self, value: int)-> str:
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular Singly Linked List has been created"

    # insertion of a node in a circular singly linked list
    def insert(self, value: int, location: Union[str,int] = 'last')-> str:
        if self.head is None:
            return 'The Circular Singly Linked List does not exist'
        else:
            node = Node(value)
            if location == 'first': #beginning
                node.next = self.head #node connection
                self.head = node #tag
                self.tail.next = node #circular connection
            elif location == 'last': #end
                node.next = self.tail.next #circular connection
                self.tail.next = node #node connection 
                self.tail = node #tag
            elif location == 'middle': #middle
                iterator = self.head
                index = 0
                while index < (self._get_length() // 2) - 1:
                    iterator = iterator.next
                    index += 1
                next_node = iterator.next
                iterator.next = node
                node.next = next_node
            else:
                iterator = self.head
                index = 0
                while index < location - 1:
                    iterator = iterator.next
                    index += 1
                next_node = iterator.next
                iterator.next = node
                node.next = next_node
            return "The node has been successfully inserted"

    # traversal of a circular singly linked list
    def traversal(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            iterator = self.head
            while iterator:
                print(iterator.value)
                iterator = iterator.next
                if iterator == self.tail.next:
                    break

    # search for a node in a circular singly linked list
    def search(self, node_value: int)-> str:
        if self.head is None:
            return 'The Circular Singly Linked List does not exist'
        
        i = 1
        iterator = self.head
        while iterator: 
            if iterator.value == node_value:
                return f"The node containing the value {node_value} exists and it is in the position {i}"
            iterator = iterator.next
            if iterator == self.tail.next:
                return 'The node does not exist in this Circular Singly Linked List'
            i += 1

    # deletion of a node in a circular singly linked list
    def delete_node(self, location: Union[str, int] = 'last')-> str:
        if self.head is None:
            return 'The Circular Singly Linked List does not exist'
        else:
            if location == 'first': #beginning
                if self._get_length() == 1: #only one node
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: #more than one node
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 'last': # end
                if self._get_length() == 1: #only one node
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: #more than one node
                    iterator = self.head
                    while iterator is not None:
                        if iterator.next == self.tail: #penultimate node?
                            penultimate_node = iterator
                            break
                        iterator = iterator.next

                    penultimate_node.next = self.head
                    self.tail = penultimate_node
            elif location == 'middle': #middle
                iterator = self.head
                index = 0
                while index < (self._get_length() // 2) - 1:
                    iterator = iterator.next
                    index += 1
                next_node = iterator.next
                iterator.next = next_node.next
            else:
                iterator = self.head
                index = 0
                while index < location - 1:
                    iterator = iterator.next
                    index += 1
                next_node = iterator.next
                iterator.next = next_node.next
        return 'The node has been successfully deleted'

    def delete(self)-> str:
        self.head = None
        self.tail.next = None
        self.tail = None

if __name__ == '__main__':
    print(colored('------------ CIRCULAR SINGLE LINKED LIST ------------', 'red'))
    circular_single_linked_list = CircularSinglyLinkedList()
    circular_single_linked_list.create(1)
    circular_single_linked_list.insert(3, 'last')
    circular_single_linked_list.insert(2)
    circular_single_linked_list.traversal()
    print(circular_single_linked_list.search(2))
    # print(circular_single_linked_list._get_length())