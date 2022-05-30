import math

def count_rotations_linear(nums: list)-> int:
    assert isinstance(nums, list), 'Nums is not an instance of list'

    position = 0

    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position

        position += 1
    return -1


def count_rotations_binary(nums: list)-> int:
    lo, hi = 0, len(nums) - 1

    iteration_no = 1

    while lo <= hi:
        print('Iteration no:', iteration_no)
        mid_index = math.floor((lo + hi) / 2 )
        mid_value = nums[mid_index]

        print('lo:', lo, ', hi:', hi, ', mid_index:', mid_index, ', mid_value:', mid_value)

        if mid_index > 0 and nums[mid_index] < nums[mid_index - 1]:
            return mid_index
        elif nums[mid_index] > nums[mid_index - 1]:
            hi = mid_index - 1
        else:
            lo = mid_index + 1

        iteration_no += 1
    return -1
    
if __name__ == '__main__':

    ## Inital test_case
    test_case = {
        'input': {
           'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14],
        },
        'output': 3
    }    
    ## Different edge cases
    tests = []
    tests.append(test_case)

    # A list of size 8 rotated 5 times
    tests.append({
        'input': {
            'nums': [19, 25, 29, 32, 34, 3, 5, 6, 7, 9, 11, 14]
        },
        'output': 5
    }
    )

    # A list that wasn't rotated at all
    tests.append({
        'input': {
            'nums': [1, 2, 3, 4]
        },
        'output': -1
    })

    # A list that was rotated just once.
    tests.append({
        'input': {
            'nums': [5, 1, 2, 3, 4]
        },
        'output': 1
    })

    # A list that was rotated n-1 times, where n is the size of the list
    tests.append({
        'input': {
            'nums': [10, 11, 12, 13, 14, 15, 16, 17, 18, -15]
        },
        'output': 9
    })

    # A list that was rotated n times, where n is the size of the list
    tests.append({
        'input': {
            'nums': [0, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        },
        'output': 10
    })

    # An empty list
    tests.append({
        'input': {
            'nums': []
        },
        'output': -1
    })

    # A list contaiing just one element
    tests.append({
        'input': {
            'nums': [1]
        },
        'output': -1
    })

    print('---------------------- TEST CASES ----------------------')
    print(*tests, sep = '\n')
    print('--------------------------------------------------------')
    print('\n')

    print('---------------------- COUNT ROATITIONS BRUTE FORCE ----------------------')
    for i, j in enumerate(tests):
        print('TEST CASE')
        print(j)
        print(count_rotations_linear(**tests[i]['input']) == tests[i]['output'])
        print('\n')
    print('--------------------------------------------------------')

    print('---------------------- COUNT ROTATIONS BINARY SEARCH ----------------------')
    for i, j in enumerate(tests):
        print('TEST CASE')
        print(j)
        print(count_rotations_binary(**tests[i]['input']) == tests[i]['output'])
        print('\n')
    print('--------------------------------------------------------')