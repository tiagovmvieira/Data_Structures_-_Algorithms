import random

def bubble_sort(nums: list)-> list:
    nums = list(nums)
    
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

def insertion_sort(nums: list)-> list:
    nums = list(nums)

    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1

        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j + 1, cur)
    
    return nums

def merge(nums1: list, nums2: list):
    # List to store the results
    merged = []

    # Indices for iteration
    i, j = 0, 0

    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):
        # Include the smaller element in the result and move to the next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    return merged + nums1_tail + nums2_tail

def merge_sort(nums: list)-> list:
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # Get the midpoint
    mid = len(nums) // 2
    
    # Split
    left = nums[:mid]
    right = nums[mid:]

    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results
    sorted_nums = merge(left_sorted, right_sorted)
    
    return sorted_nums

if __name__ == '__main__':

    ## Initial test case
    # List of numbers in random order
    test_case = {
        'input': {
            'nums': [4, 2, 6, 3, 4, 6, 2, 1]
        },
        'output': [1, 2, 2, 3, 4, 4, 6, 6]
    }
    ## Different edge cases
    tests = []
    tests.append(test_case)

    # list of numbers in random order
    tests.append({
        'input': {
            'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
        },
        'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
    })

    # list that is already sorted
    tests.append({
        'input': {
            'nums': [3, 5, 6, 8, 9, 10, 99]
        },
        'output': [3, 5, 6, 8, 9, 10, 99]
    })

    # list that is sorted in descending order
    tests.append({
        'input': {
            'nums': [99, 10, 9, 8, 6, 5, 3]
        },
        'output': [3, 5, 6, 8, 9, 10, 99]
    })

    # list that contains repeating elements
    tests.append({
        'input': {
            'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
        },
        'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
    })

    # an empty list
    tests.append({
        'input': {
            'nums': []
        },
        'output': []
    })
    
    # a list containing just one element
    tests.append({
        'input': {
            'nums': [4]
        },
        'output': [4]
    })

    # a list containing one element repeated many times
    tests.append({
        'input': {
            'nums': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        },
        'output': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    })

    # a really long list
    in_list = list(range(10000))
    out_list = list(range(10000))
    random.shuffle(in_list)

    tests.append({
        'input': {
            'nums': in_list
        },
        'output': out_list
    })

    print('---------------------- TEST CASES ----------------------')
    print(*tests, sep = '\n')
    print('--------------------------------------------------------')
    print('\n')

    print('---------------------- BUBBLE SORT ----------------------')
    for i, j in enumerate(tests):
        print(f'TEST CASE {i}')
        print(j)
        print(bubble_sort(**tests[i]['input']) == tests[i]['output'])
        print('\n')
    print('--------------------------------------------------------')

    print('---------------------- INSERTION SORT ----------------------')
    for i, j in enumerate(tests):
        print(f'TEST CASE {i}')
        print(j)
        print(insertion_sort(**tests[i]['input']) == tests[i]['output'])
        print('\n')
    print('------------------------------------------------------------')

    print('---------------------- MERGE SORT ----------------------')
    for i, j in enumerate(tests):
        print(f'TEST CASE {i}')
        print(j)
        print(merge_sort(**tests[i]['input']) == tests[i]['output'])
        print('\n')
    print('------------------------------------------------------------')




    