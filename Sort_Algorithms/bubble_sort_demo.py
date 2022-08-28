import random
from termcolor import colored

def create_unordered_list(lower_limit: float, upper_limit: float, duplicate_value: bool)-> list:
    sorted_list = [value for value in range(lower_limit, upper_limit + 1)]
    sorted_list.append(sorted_list[len(sorted_list)// 2]) if duplicate_value else None
    unsorted_list = random.sample(sorted_list, len(sorted_list))
    
    return unsorted_list

def bubble_sort(unsorted_list: list):
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    sorted_list = unsorted_list
    
    return sorted_list

if __name__ == '__main__':
    print(colored('----------------- SORT ALGORITHMS ----------------', 'red'))
    print(colored('------------- UNSORTED LIST CREATION -------------', 'red'))
    unsorted_list = create_unordered_list(1, 10, True)
    print('Unsorted list:', unsorted_list)

    print(colored('------------------- BUBBLE SORT ------------------', 'red'))
    sorted_list = bubble_sort(unsorted_list)
    print('Sorted list:', sorted_list)

