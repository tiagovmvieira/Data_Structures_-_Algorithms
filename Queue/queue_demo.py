from termcolor import colored
from typing import Union

class Queue:
    def __init__(self):
        self.list = []

    def __str__(self)-> str:
        values = [str(val) for val in self.list] if self.list else None
        if values:
            return ' '.join(values)
        else:
            return str(values)

    def is_empty(self)-> bool:
        if len(self.list) == 0:
            return True
        return False

    def enqueue(self, value: float)-> str:
        self.list.append(value)
        return 'The element is inserted at the end of Queue'

    def dequeue(self)-> float:
        if self.is_empty():
            return 'There is not any element in the Queue'
        return self.list.pop(0)
    
    def peek(self)-> float:
        if self.is_empty():
            return 'There is not any element in the Queue'
        return self.list[0]

    def delete(self):
        self.list = None

class CircularQueue:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.list = [None] * max_size
        self.start = -1
        self.top = -1

    def __str__(self)-> str:
        values = [str(val) for val in self.list]
        return ' '.join(values)

    def is_full(self)-> bool:
        if self.top + 1 == self.start: # close to each other
            return True
        elif self.start == 0 and self.top + 1 == self.max_size: # extrem
            return True
        return False
    
    def is_empty(self)-> bool:
        if self.top == -1:
            return True
        return False

    def enqueue(self, value: float)-> str:
        if self.is_full():
            return 'The Queue is already full'
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value
            return "The element is inserted at the end of Queue"

    def dequeue(self)-> Union[str, int]:
        if self.is_empty():
            return 'There is not any element in the Queue'
        else:
            first_element = self.list[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            return first_element

    def peek(self)-> Union[str, float]:
        if self.is_empty():
            return 'There is not any element in the Queue'
        else:
            return self.list[self.start]
    
    def delete(self):
        self.list = [None] * self.max_size
        self.start = -1
        self.top = -1
    
class Node:
    def __init__(self, val = None):
        self.value = val
        self.next = None

    def __str__(self)-> str:
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        iterator = self.head
        while iterator is not None:
            yield iterator
            iterator = iterator.next

class QueueLinkedList():
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self)-> str:
        if self.linked_list.head is None:
            return 'There is not any Queue to return'
        values = [str(val) for val in self.linked_list]
        return ' '.join(values)

    def is_empty(self)-> bool:
        if self.linked_list.head is None:
            return True
        return False
    
    def enqueue(self, value: float):
        node = Node(value)
        if self.is_empty():
            self.linked_list.head = node
            self.linked_list.tail = node
        else:
            self.linked_list.tail.next = node
            self.linked_list.tail = node

    def dequeue(self)-> Union[str, float]:
        if self.is_empty():
            return 'There is not any node on the Queue'
        temp_node = self.linked_list.head
        if temp_node.next is None:
            self.linked_list.head = None
            self.linked_list.tail = None
        else:
            self.linked_list.head = self.linked_list.head.next
        return temp_node
 
    def peek(self)-> Union[str, float]:
        if self.is_empty():
            return 'There is not any node on the Queue'
        return self.linked_list.head

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None

if __name__ == '__main__':
    print(colored('---------------------- QUEUE ----------------------', 'red'))
    print(colored('---------------------- LIMITLESS QUEUE LIST IMPLEMENTATION ----------------------', 'red'))
    custom_queue = Queue()

    print(colored('---------------------- CHECK IF QUEUE IS EMPTY ----------------------', 'red'))
    print(custom_queue.is_empty())
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- ENQUEUE ----------------------', 'red'))
    for i in range(11):
        custom_queue.enqueue(i)
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- DEQUEUE ----------------------', 'red'))
    print(custom_queue.dequeue())
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- PEEK THE FIRST ELEMENT FROM THE QUEUE  ----------------------', 'red'))
    print(custom_queue.peek())

    print(colored('---------------------- DELETE THE QUEUE ----------------------', 'red'))
    custom_queue.delete()
    print('Custom Queue: ', custom_queue)
    print('\n')

    print(colored('---------------------- LIMITED QUEUE LIST IMPLEMENTATION ----------------------', 'red'))
    custom_queue = CircularQueue(10)

    print(colored('---------------------- CHECK IF QUEUE IS EMPTY ----------------------', 'red'))
    print(custom_queue.is_empty())
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- ENQUEUE ----------------------', 'red'))
    for i in range(custom_queue.max_size):
        custom_queue.enqueue(i)
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- DEQUEUE ----------------------', 'red'))
    for i in range(custom_queue.max_size // 2):
        custom_queue.dequeue()
        print('Custom Queue: ', custom_queue)

    custom_queue.dequeue()
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- ENQUEUE ----------------------', 'red'))
    for i in range(custom_queue.max_size // 2):
        custom_queue.enqueue(i)
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- PEEK THE FIRST ELEMENT FROM THE QUEUE  ----------------------', 'red'))
    print(custom_queue.peek())

    print(colored('---------------------- DELETE THE QUEUE ----------------------', 'red'))
    custom_queue.delete()
    print('Custom Queue: ', custom_queue)
    print('\n')

    print(colored('---------------------- LIMITLESS QUEUE LINKED LIST IMPLEMENTATION ----------------------', 'red'))
    custom_queue = QueueLinkedList()

    print(colored('---------------------- CHECK IF QUEUE IS EMPTY ----------------------', 'red'))
    print(custom_queue.is_empty())
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- ENQUEUE ----------------------', 'red'))
    for i in range(11):
        custom_queue.enqueue(i)
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- DEQUEUE ----------------------', 'red'))
    print(custom_queue.dequeue())
    print('Custom Queue: ', custom_queue)

    print(colored('---------------------- PEEK THE FIRST ELEMENT FROM THE QUEUE  ----------------------', 'red'))
    print(custom_queue.peek())

    print(colored('---------------------- DELETE THE QUEUE ----------------------', 'red'))
    custom_queue.delete()
    print('Custom Queue: ', custom_queue)