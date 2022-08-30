from typing import Optional
from termcolor import colored

"""
Quizz

Cracking the Code Interview
10.1

Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
Write a method to merge B into A in sorted order.
"""

def create_array(lower_limit: int, upper_limit: int, len_array_b: Optional[int] = False)-> list:
    array = [value for value in range(lower_limit, upper_limit + 1)]

    if len_array_b:
        for i in range(len_array_b):
            array.append(None)
    
    return array

def sorted_merge(array_a: list, array_b: list)-> list:
    sorted_list = [None] * len(array_a)

    i = 0
    j = 0
    k = 0
    while i < len(array_a) and j < len(array_b):
        if array_a[i] is not None:
            if array_a[i] < array_b[j]:
                sorted_list[k] = array_a[i]
                i += 1
            else:
                sorted_list[k] = array_b[j]
                j += 1
        else:
            sorted_list[k] = array_b[j]
            j += 1
        k += 1

    while k < len(array_a):
        sorted_list[k] = array_a[i]
        i += 1
        k += 1

    return sorted_list


if __name__ == '__main__':
    print(colored('------------------- SORTED MERGE -----------------', 'red'))

    array_a = create_array(1, 5, 3)
    array_b = create_array(0, 2)

    print('array_a', array_a)
    print('array_b', array_b)
    
    sorted_list = sorted_merge(array_a, array_b)
    print(sorted_list)