from termcolor import colored
from typing import Union

class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.next = None
        
class SinglyLinkedList:
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
        
        result = 0
        iterator = self.head

        while iterator is not None:
            result += 1
            iterator = iterator.next
        return result

    def print(self)-> list:
        print([node.value for node in self])

    # creation of a singly linked list
    def create(self, value: int)-> str:
        node = Node(value)
        self.head = node
        self.tail = node
        return "The Singly Linked List has been created"

    def insert(self, value: int, location: Union[str, int] = None)-> str:
        index = isinstance(location, int)
        if index and (location < 1 or location > self.__get_length() + 1):
            raise ValueError(f"location: The location must be between 1 and {self.__get_length() + 1}")

        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if location == 'first':
                node.next = self.head
                self.head = node
            elif location == 'last':
                self.tail.next = node
                self.tail = node
            elif location == 'middle':
                if not (self.__get_length() % 2) == 0:
                    return ValueError("location: The Singly Linked List does not contain a middle position to insert into the node")
                
                iterator = self.head
                index = 0
                while index < (self.__get_length() / 2) - 1:
                    iterator = iterator.next
                    index += 1
                next_node = iterator.next
                iterator.next = node
                node.next = next_node
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
                        index  += 1
                    next_node = iterator.next
                    iterator.next = node
                    node.next = next_node
    
        return "The node has been sucessfully inserted"

    # traversal of a singly linked list
    def traversal(self)-> int:
        if self.head is None:
            print("There is not any element for traversal")
        else:
            iterator = self.head
            while iterator is not None:
                print(iterator.value)
                iterator = iterator.next

    # search for a node in a singly linked list
    def search(self, node_value: int)-> str:
        if self.head is None:
            return "The Singly Linked List does not exist"

        i = 1
        iterator = self.head
        while iterator: 
            if iterator.value == node_value:
                return f"The node containing the value {node_value} exists and it is in the position {i}"
            iterator = iterator.next
            i += 1
        return f"There is not a node containg the value {node_value}"

    def delete_node(self, location: Union[str, int] = 'last')-> str:
        if self.head is None:
            return "The Singly Linked List does not exist"
        
        index = isinstance(location, int)
        if index and (location < 1 or location > self.__get_length() + 1):
            raise ValueError(f"location: The location must be between 1 and {self.__get_length() + 1}")

        if location == 'first': #beginning
            if self.__get_length() == 1: #only one node
                self.head = None
                self.tail = None
            else: # more than one
                self.head = self.head.next
        elif location == 'last': #end
            if self.__get_length() == 1: #only one node
                self.head = None
                self.tail = None
            else: # more than one
                iterator = self.head
                while iterator is not None:
                    if iterator.next == self.tail:
                        break
                    iterator = iterator.next
                iterator.next = None
                self.tail = iterator
        elif location == 'middle': #middle
            if (self.__get_length() % 2) == 0:
                return ValueError("location: The Singly Linked List does not contain a middle node")
            iterator = self.head
            index = 1
            while index < (self.__get_length() / 2) - 1:
                iterator = iterator.next
                index += 1
            next_node = iterator.next
            iterator.next = next_node.next
        else: #specific location
            if location == 1:
                self.delete_node('first')
            elif location == self.__get_length():
                self.delete_node('last')
            else:
                iterator = self.head
                index = 1
                while index < location - 1:
                    iterator = iterator.next
                    index += 1
                next_node = iterator.next
                iterator.next = next_node.next
        
        return "The node has been successfully deleted"

    def delete(self)-> str:
        if self.head is None:
            return "The Singly Linked List does not exist"

        self.head = None
        self.tail = None

        return "The Singly List has been sucessfully deleted"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int):
        if self.head is None:
            self.head = Node(value)
        else:
            iterator = self.head #iterator starts on the head
            while iterator.next is not None:
                iterator = iterator.next # pointing 
            iterator.next = Node(value) # appending

    def append_by_position(self, node: Node, position: int):
        iterator = self.head #iterator start on the head
        if position == 0:
            self.head = node
            self.head.next = iterator
        else:
            i = 1
            while iterator is not None:
                if i == position:
                    historic = iterator.next
                    iterator.next = node
                    iterator.next.next = historic
                i += 1
                iterator = iterator.next

    def print(self)-> str:
        if self.head is None:
            print('Linked list is empty')
            return

        iterator = self.head # iterator starts on the head
        linked_list_string = '' # starts empty
        
        while iterator is not None:
            linked_list_string += str(iterator.value) + '-->'
            iterator = iterator.next
        
        linked_list_string = linked_list_string[:-3]
        print(linked_list_string)

    def get_length(self)-> int:
        result = 0
        if self.head is None:
            return result

        iterator = self.head
        while iterator is not None:
            result += 1
            iterator = iterator.next
        return result

    def find_element(self, position: int)-> int:
        i = 0
        iterator = self.head 
        while iterator is not None:
            if i == position:
                return iterator.value
            iterator = iterator.next 
            i += 1

    def reverse_linked_list(self): #iteratively
        if self.head is None:
            print('Linked List is empty')
            return 

        iterator = self.head
        previous_node = None

        while iterator is not None:
            historic = iterator.next # storing the historic forward
            iterator.next = previous_node # flipping the pointer

            previous_node = iterator # looping
            iterator = historic # looping
        self.head = previous_node

if __name__ == '__main__':
    print(colored('---------------- SINGLE LINKED LIST -----------------', 'red'))
    print(colored('------------------- LIST CREATION -------------------', 'red'))
    linked_list = SinglyLinkedList()
    linked_list.create(1)
    
    print(colored('------------------- LIST INSERTION ------------------', 'red'))    
    linked_list.insert(0, 'first')
    linked_list.insert(3, 'last')
    linked_list.insert(4, 4)
    linked_list.insert(2, 'middle')
    linked_list.print()

    print(colored('------------------- LIST TRAVERSAL ------------------', 'red'))
    linked_list.traversal()    

    print(colored('-------------------- LIST SEARCH --------------------', 'red'))
    print(linked_list.search(3))

    print(colored('---------------- DELETION OF A NODE -----------------', 'red'))
    linked_list.print()
    linked_list.delete_node('last')
    linked_list.delete_node('first')
    linked_list.print()
    linked_list.delete_node('middle')
    linked_list.print()
    linked_list.delete_node(2)
    linked_list.print()

    print(colored('------------------- LIST DELETION -------------------', 'red'))
    linked_list.delete()
    linked_list.print()

    print(colored('--------------- ALTERNATIVE APPROACH ----------------', 'red'))
    nodes = []
    for i in range(1, 11):
        nodes.append(Node(i))

    linked_list = LinkedList()

    for i,j in enumerate(nodes):
        linked_list.append(nodes[i].value)
    print(colored('---------------- SINGLE LINKED LIST -----------------', 'red'))
    linked_list.print()
    linked_list.find_element(2)

    new_node_A = Node(0)
    new_node_B = Node(99)

    linked_list.append_by_position(new_node_A, 0)
    linked_list.print()

    linked_list.append_by_position(new_node_B, 12)
    linked_list.print()

    linked_list.reverse_linked_list()
    linked_list.print()