import random
import math
from termcolor import colored

def create_unsorted_list(lower_limit: float, upper_limit: float, duplicate_value: bool)-> list:
    sorted_list = [value for value in range(lower_limit, upper_limit + 1)]
    sorted_list.append(sorted_list[len(sorted_list)// 2]) if duplicate_value else None
    unsorted_list = random.sample(sorted_list, len(sorted_list))
    
    return unsorted_list

def bubble_sort(unsorted_list: list)-> list:
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    sorted_list = unsorted_list

    return sorted_list

def bucket_sort(unsorted_list: list)-> list:
    number_of_buckets = round(math.sqrt(len(unsorted_list)))
    max_value = max(unsorted_list)

    bucket = []

    for i in range(number_of_buckets):
        bucket.append([])

    for i in range(len(unsorted_list)):
        appropriate_bucket =  math.ceil(unsorted_list[i] * number_of_buckets / max_value)
        bucket[appropriate_bucket - 1].append(unsorted_list[i])

    for i in range(number_of_buckets):
        bucket[i] = bubble_sort(bucket[i])

    sorted_list = sum(bucket, [])

    return sorted_list


if __name__ == '__main__':
    print(colored('----------------- SORT ALGORITHMS ----------------', 'red'))
    print(colored('------------- UNSORTED LIST CREATION -------------', 'red'))
    unsorted_list = create_unsorted_list(1, 10, False)
    print('Unsorted list:', unsorted_list)

    print(colored('------------------- BUCKET SORT ------------------', 'red'))
    sorted_list = bucket_sort(unsorted_list)
    print('Sorted list:', sorted_list)

