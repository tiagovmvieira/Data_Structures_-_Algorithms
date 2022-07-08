from typing import Union

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self)-> str:
        if self.list is None:
            return 'There is not any stack to return'
        values = self.list.reverse()
        values = [str(val) for val in self.list]
        return '\n'.join(values)

    def is_empty(self)-> bool:
        if len(self.list) == 0:
            return True
        return False

    def push(self, value: float)-> str:
        self.list.append(value)
        return 'The element has been successfully inserted'

    def pop(self)-> Union[str, int]:
        if self.is_empty():
            return 'There is not any element in the stack'
        return self.list.pop()

    def peek(self)-> Union[str, int]:
        if self.is_empty():
            return 'There is not any element in the stack'
        return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None

class StackWithLimit:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.list = []

    def __str__(self)-> str:
        if self.list is None:
            return 'There is not any stack to return'
        values = self.list.reverse()
        values = [str(val) for val in self.list]
        return '\n'.join(values)
    
    def is_empty(self)-> bool:
        if len(self.list) == 0:
            return True
        return False

    def is_full(self)-> bool:
        if len(self.list) == self.max_size:
            return True
        return False
    
    def push(self, value: float)-> str:
        if self.is_full():
            return 'The Stack is already full'
        self.list.append(value)
        return 'The element has been successfully inserted'

    def pop(self)-> Union[str, int]:
        if self.is_empty():
            return 'There is not any element in the stack'
        return self.list.pop()
    
    def peek(self)-> Union[str, int]:
        if self.is_empty():
            return 'There is not any element in the stack'
        return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None

class Node:
    def __init__(self, val = None):
        self.value = val
        self.next = None

    def __str__(self)-> str:
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        iterator = self.head
        while iterator is not None:
            yield iterator
            iterator = iterator.next

class StackLinkedList:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self)-> str:
        if self.linked_list.head is None:
            return 'There is not any stack to return'
        values = [str(val.value) for val in self.linked_list]
        return '\n'.join(values)

    def is_empty(self)-> bool:
        if self.linked_list.head is None:
            return True
        return False

    def push(self, val: float):
        node = Node(val)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self)-> Union[str, float]:
        if self.is_empty():
            return 'There is not any element on the Stack'
        node_value = self.linked_list.head.value
        self.linked_list.head = self.linked_list.head.next
        return node_value

    def peek(self)-> Union[str, float]:
        if self.is_empty():
            return 'There is not any element on the Stack'
        node_value = self.linked_list.head.value
        return node_value

    def delete(self):
        self.linked_list.head = None

if __name__ == '__main__':
    print('---------------------- STACK ----------------------')
    print('---------------------- LIMITLESS STACK LIST IMPLEMENTATION ----------------------')
    custom_stack = Stack()

    print('---------------------- CHECK IF STACK IS EMPTY ----------------------')
    print(custom_stack.is_empty())

    print('---------------------- PUSH INTO THE STACK --------------------------')
    for i in range(11):
        custom_stack.push(i)

    print(custom_stack)

    print('---------------------- POP FROM THE STACK --------------------------')
    custom_stack.pop()
    print(custom_stack)

    print('---------------------- PEEK THE FIRST ELEMENT FROM THE STACK --------------------------')
    print(custom_stack.peek())

    print('---------------------- DELETE THE STACK --------------------------')
    custom_stack.delete()
    print(custom_stack)
    print('\n')
    
    print('---------------------- LIMITLED STACK LIST IMPLEMENTATION ----------------------')
    custom_stack = StackWithLimit(4)

    print('---------------------- CHECK IF STACK IS EMPTY ----------------------')
    print(custom_stack.is_empty())

    print('---------------------- CHECK IF STACK IS FULL ----------------------')
    print(custom_stack.is_full())

    print('---------------------- PUSH INTO THE STACK --------------------------')
    for i in range(6):
        print(custom_stack.push(i))

    print(custom_stack)

    print('---------------------- POP FROM THE STACK --------------------------')
    custom_stack.pop()
    print(custom_stack)

    print('---------------------- PEEK THE FIRST ELEMENT FROM THE STACK --------------------------')
    print(custom_stack.peek())

    print('---------------------- DELETE THE STACK --------------------------')
    custom_stack.delete()
    print(custom_stack)
    print('\n')

    print('----------------------  LIMITLESS STACK LINKED LIST IMPLEMENTATION ----------------------')
    custom_stack = StackLinkedList()

    print('---------------------- CHECK IF STACK IS EMPTY ----------------------')
    print(custom_stack.is_empty())

    print('---------------------- PUSH INTO THE STACK --------------------------')
    for i in range(11):
        custom_stack.push(i)

    print(custom_stack)

    print('---------------------- POP FROM THE STACK --------------------------')
    custom_stack.pop()
    print(custom_stack)

    print('---------------------- PEEK THE FIRST ELEMENT FROM THE STACK --------------------------')
    print(custom_stack.peek())

    print('---------------------- DELETE THE STACK --------------------------')
    custom_stack.delete()
    print(custom_stack)