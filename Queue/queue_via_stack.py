from termcolor import colored
from typing import Union

# Implement a queue using two stacks

class Stack():
    def __init__(self):
        self.list = []

    def __len__(self)-> int:
        return len(self.list)

    def is_empty(self)-> bool:
        if len(self.list) == 0:
            return True
        return False

    def push(self, value: float)-> str:
        self.list.append(value)
        return 'The element has been successfully inserted'

    def pop(self)-> Union[str, int]:
        if self.is_empty():
            return 'There is not any element in the Queue'
        return self.list.pop()
    
class QueueViaStack():
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def __str__(self)-> str:
        values = [str(val) for val in self.input_stack.list] if self.input_stack.list else None
        if values:
            return ' '.join(values)
        else:
            return str(values)

    def enqueue(self, value: float):
        self.input_stack.push(value)

    def dequeue(self)-> Union[str, int]:
        while self.input_stack.__len__() > 0:
            self.output_stack.push(self.input_stack.pop())
        
        result = self.output_stack.pop()

        while self.output_stack.__len__() > 0:
            self.input_stack.push(self.output_stack.pop())

        return result

if __name__ == '__main__':
    print(colored('------------------ QUEUE VIA STACK ------------------', 'red'))
    custom_queue = QueueViaStack()
    
    print(colored('---------------------- ENQUEUE ----------------------', 'red'))
    custom_queue.enqueue(1)
    custom_queue.enqueue(2)
    custom_queue.enqueue(3)

    print(colored('-------------------- QUEUE CHECK --------------------', 'red'))
    print(custom_queue)

    print(colored('---------------------- DEQUEUE ----------------------', 'red'))
    print(custom_queue.dequeue())

    print(colored('---------------------- ENQUEUE ----------------------', 'red'))
    custom_queue.enqueue(4)

    print(colored('---------------------- DEQUEUE ----------------------', 'red'))
    print(custom_queue.dequeue())