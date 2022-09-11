import random

class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class GenericLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self)-> str:
        node_values = [str(node.value) for node in self]
        return ' -> '.join(node_values)

    def __len__(self)-> int:
        result = 0
        iterator = self.head

        while iterator is not None:
            result += 1
            iterator = iterator.next
        return result

    def insert(self, value: int):
        node = Node(value)
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return self.tail
    
    def generate(self, number_elements: int, min_value: int, max_value: int)-> str:
        # reset previous instances
        self.head = None
        self.tail = None

        for i in range(number_elements):
            self.insert(random.randint(min_value, max_value))

        return self