import random
from termcolor import colored

def create_unsorted_list(lower_limit: float, upper_limit: float, duplicate_value: bool)-> list:
    sorted_list = [value for value in range(lower_limit, upper_limit + 1)]
    sorted_list.append(sorted_list[len(sorted_list)// 2]) if duplicate_value else None
    unsorted_list = random.sample(sorted_list, len(sorted_list))
    
    return unsorted_list

def selection_sort(unsorted_list: list)-> list:
    sorted_list = []
    while unsorted_list:
        min_element = min(unsorted_list)
        unsorted_list[0], unsorted_list[unsorted_list.index(min_element)] = unsorted_list[unsorted_list.index(min_element)], unsorted_list[0]
        sorted_list.append(min_element)
        unsorted_list.pop(unsorted_list.index(min_element))
    
    return sorted_list

if __name__ == '__main__':
    print(colored('----------------- SORT ALGORITHMS ----------------', 'red'))
    print(colored('------------- UNSORTED LIST CREATION -------------', 'red'))
    unsorted_list = create_unsorted_list(1, 10, True)
    print('Unsorted list:', unsorted_list)

    print(colored('----------------- SELECTION SORT -----------------', 'red'))
    sorted_list = selection_sort(unsorted_list)
    print('Sorted list:', sorted_list)