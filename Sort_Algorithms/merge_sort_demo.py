import random
from termcolor import colored

def create_unsorted_list(lower_limit: float, upper_limit: float, duplicate_value: bool)-> list:
    sorted_list = [value for value in range(lower_limit, upper_limit + 1)]
    sorted_list.append(sorted_list[len(sorted_list)// 2]) if duplicate_value else None
    unsorted_list = random.sample(sorted_list, len(sorted_list))

    return unsorted_list

def merge(unsorted_list: list, left_index: int, middle_index: int, right_index: int)-> list:
    n1 = middle_index - left_index + 1
    n2 = right_index - middle_index

    L = [None] * n1
    R = [None] * n2

    #allocating the values of the array into the sub-arrays
    for i in range(0, n1):
        L[i] = unsorted_list[left_index + i]
    for j in range(0, n2):
        R[j] = unsorted_list[middle_index + 1 + j]

    i = 0
    j = 0
    k = left_index
    
    #combining the sub-arrays in a sorted order list
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            unsorted_list[k] = L[i]
            i += 1
        else:
            unsorted_list[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        unsorted_list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        unsorted_list[k] = R[j]
        j += 1
        k += 1

    return unsorted_list

def merge_sort(unsorted_list: list, left_index: int, right_index: int)-> list:
    if left_index < right_index:
        middle_index = (left_index + (right_index - 1)) // 2
        merge_sort(unsorted_list, left_index, middle_index) #1st sub-array
        merge_sort(unsorted_list, middle_index + 1, right_index) #2nd sub-array
        merge(unsorted_list, left_index, middle_index, right_index) #merging the sub-arrays 

    return unsorted_list


if __name__ == '__main__':
    print(colored('----------------- SORT ALGORITHMS ----------------', 'red'))
    print(colored('------------- UNSORTED LIST CREATION -------------', 'red'))
    unsorted_list = create_unsorted_list(1, 11, False)
    print('Unsorted list:', unsorted_list)

    print(colored('------------------- MERGE SORT -------------------', 'red'))
    sorted_list = merge_sort(unsorted_list, 0, len(unsorted_list) - 1)
    print('Sorted list:', sorted_list)