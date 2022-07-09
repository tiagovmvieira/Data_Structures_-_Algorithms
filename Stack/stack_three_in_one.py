from typing import Union

# Use a single list to implement three stacks

class MultiStack:
    def __init__(self, stack_size: int):
        self.number_of_stacks = 3
        self.custom_list = [0] * (stack_size * self.number_of_stacks)
        self.size_of_stacks = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def is_full(self, stack_number: int)-> bool:
        if self.size_of_stacks[stack_number] == self.stack_size:
            return True
        return False

    def is_empty(self, stack_number: int)-> bool:
        if self.size_of_stacks[stack_number] == 0:
            return True
        return False
    
    def index_of_top(self, stack_number: int)-> float:
        offset = stack_number * self.stack_size
        return offset + self.size_of_stacks[stack_number] - 1

    def push(self, value: float, stack_number: int)-> str:
        if self.is_full(stack_number):
            return 'The selected Stack is already full'
        self.size_of_stacks[stack_number] += 1
        self.custom_list[self.index_of_top(stack_number)] = value
        return 'The element has been successfully inserted on the selected stacks'

    def pop(self, stack_number: int)-> Union[str, float]:
        if self.is_empty(stack_number):
            return 'There is not any element in the selected Stack'
        value = self.custom_list[self.index_of_top(stack_number)]
        self.custom_list[self.index_of_top(stack_number)] = 0 #initial shape
        self.size_of_stacks[stack_number] -= 1
        return value

    def peek(self, stack_number: int)-> Union[str, float]:
        if self.is_empty(stack_number):
            return 'There is not any element in the selected Stack'
        return self.custom_list[self.index_of_top(stack_number)]


if __name__ == '__main__':
    print('---------------------- STACK THREE IN ONE ----------------------')
    custom_stack = MultiStack(6)

    print('---------------------- CHECK IF A SELECTED STACK IS EMPTY ----------------------')
    print(custom_stack.is_empty(1))

    print('---------------------- CHECK IF A SELECTED STACK IS FULL ----------------------')
    print(custom_stack.is_full(0))

    print('---------------------- PUSH INTO A SELECTED STACK ----------------------')
    custom_stack.push(1, 0)
    custom_stack.push(2, 0)
    custom_stack.push(3, 2)
    print('---------------------- POP FROM A SELECTED STACK ----------------------')
    print(custom_stack.pop(0))

    print('---------------------- PEEK FROM A SELECTED STACK ----------------------')
    print(custom_stack.peek(2))