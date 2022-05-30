import math

from typing import List

def binary_search(lo: int, hi: int, condition: str)-> int:
    iteration_no = 1
    while lo <= hi:
        print('Iteration no:', iteration_no)
        print('lo:', lo, 'hi:', hi)
        mid_index = math.floor((lo + hi) / 2 )
        print('mid_index:', mid_index)
        result = condition(mid_index, lo, hi)

        if result == 'found':
            return mid_index
        elif result == 'left':
            hi = mid_index - 1
        else:
            lo = mid_index + 1
        iteration_no += 1
    return -1

def locate_first_position(cards: list, query: int)-> int:
    print('Locating first position...')
    def condition(mid_index: int, lo: int, hi: int)-> str:
        print('Current set of cards:', cards[lo:hi + 1])
        if cards[mid_index] == query:
            if mid_index > 0 and cards[mid_index - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid_index] < query:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(cards) - 1, condition)

def locate_last_position(cards: list, query: int)-> int:
    print('Locating last position...')
    def condition(mid_index: int, lo: int, hi: int)-> str:
        print('Current set of cards:', cards[lo:hi + 1])
        print('cards mid index', cards[mid_index])
        if cards[mid_index] == query:
            if mid_index < len(cards) - 1 and cards[mid_index + 1] == query:
                return 'right'
            else:
                return 'found'
        elif cards[mid_index] < query:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(cards) - 1, condition)

def first_last_position(cards: int, query: int)-> List:
    return [locate_first_position(cards, query), locate_last_position(cards, query)]


if __name__ == '__main__':
    
    ## Inital test_case
    test_case = {
        'input': {
           'cards': [0, 1, 3, 4, 7, 10, 11, 13],
           'query': 7 
        },
        'output': [4, 4]
    }
    ## Different edge cases
    tests = []
    tests.append(test_case)
    
    # query occurs in the middle
    tests.append({
        'input': {
            'cards': [0, 1, 3, 4, 7, 10, 11, 13],
            'query': 4
        },
        'output': [3, 3]
    })

    # query occurs in the first element
    tests.append({
        'input': {
            'cards': [-1, 1, 2, 4],
            'query': -1
        },
        'output': [0, 0]
    })

    # query occurs in the last element
    tests.append({
        'input': {
            'cards': [-127, -9, -1, 3],
            'query': 3
        },
        'output': [3, 3]
    })

    # cards contains just one element, query
    tests.append({
        'input': {
            'cards': [6],
            'query': 6
        },
        'output': [0, 0]
    })

    # cards does not contain query
    tests.append({
        'input': {
            'cards': [-9, 2, 5, 7, 9],
            'query': 4
        },
        'output': [-1, -1]
    })

    # cards is empty
    tests.append({
        'input': {
            'cards': [],
            'query': 7,
        },
        'output': [-1, -1]
    })
    
    # numbers can repeat in cards
    tests.append({
        'input': {
            'cards': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8],
            'query': 3
        },
        'output': [6, 6]
    })

    # query occurs multiples times
    tests.append({
        'input': {
            'cards': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8],
            'query': 6
        },
        'output': [7, 11]
    })

    print('---------------------- TEST CASES ----------------------')
    print(*tests, sep = '\n')
    print('--------------------------------------------------------')
    print('\n')

    print('---------------------- LOCATE CARD POSITIONS BINARY SEARCH ----------------------')
    for i, j in enumerate(tests):
        print('TEST CASE')
        print(j)
        print(first_last_position(**tests[i]['input']) == tests[i]['output'])
        print('\n')
    print('--------------------------------------------------------')