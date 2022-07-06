from termcolor import colored

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self)-> str:
        values = [str(val) for val in self.items]
        return ''.join(values)

    def is_empty(self)-> bool:
        if len(self.items) == 0:
            return True
        return False

    def enqueue(self, value: float)-> bool:
        self.items.append(value)
        return 'The element is inserted at the end of Queue'

    def dequeue(self)-> int:
        if self.is_empty():
            return 'There is not any element in the Queue'
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            return 'There is not any element in the Queue'
        return self.items[0]

    def delete(self):
        self.items = None

if __name__ == '__main__':
    print(colored('---------------------- QUEUE ----------------------', 'red'))
    print(colored('---------------------- LIMITLESS QUEUE LIST IMPLEMENTATION ----------------------', 'red'))
    custom_queue = Queue()

    print(colored('---------------------- CHECK IF STACK IS EMPTY ----------------------', 'red'))
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
    print('\n')