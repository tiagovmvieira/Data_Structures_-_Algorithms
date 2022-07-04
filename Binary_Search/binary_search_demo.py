import math
from time import perf_counter


def locate_card_brute_force(cards: list, query: int)-> int:
    beginning = perf_counter()
    # integration tests
    assert isinstance(cards, list), 'cards is not an instance of list'
    assert isinstance(query, int), 'query is not an instance of a query'

    position = 0
    while position < len(cards):
        if cards[position] == query:
            end = perf_counter()
            return position
        position += 1
    return -1

def test_location(cards: list, query: int, mid_index: int)-> str:
    mid_value = cards[mid_index]
    print('mid_index:', mid_index, ', mid_value:', mid_value)
    if mid_value == query:
        if mid_index - 1 >= 0 and cards[mid_index - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_value <= query:
        return 'left'
    else: 
        return 'right'

def locate_card_binary_search(cards: list, query: int)-> int:
    # integration tests
    assert isinstance(cards, list), 'cards is not an instance of list'
    assert isinstance(query, int), 'query is not an instance of a query'
    
    if (any(elem is None for elem in cards)):
        return -1

    lo, hi = 0, len(cards) - 1
    iteration_no = 1
    while lo <= hi:
        print('Iterarion no:', iteration_no)
        print('lo:', lo, ', hi:', hi)
        mid_index = math.floor((lo + hi) / 2)

        print('Current set of cards:', cards[lo:hi + 1])
        result = test_location(cards, query, mid_index)

        if result == 'found':
            return mid_index
        elif result == 'left':
            hi = mid_index - 1
        elif result == 'right':
            lo = mid_index + 1

        iteration_no += 1
    return -1
        

if __name__ == '__main__':
    
    ## Inital test_case
    test_case = {
        'input': {
           'cards': [13, 11, 10, 7, 4, 3, 1, 0],
           'query': 7 
        },
        'output': 3
    }
    ## Different edge cases
    tests = []
    tests.append(test_case)
    
    # query occurs in the middle
    tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
    })

    # query occurs in the first element
    tests.append({
        'input': {
            'cards': [4, 2, 1, -1],
            'query': 4
        },
        'output': 0
    })

    # query occurs in the last element
    tests.append({
        'input': {
            'cards': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
    })

    # cards contains just one element, query
    tests.append({
        'input': {
            'cards': [6],
            'query': 6
        },
        'output': 0
    })

    # cards does not contain query
    tests.append({
        'input': {
            'cards': [9, 7, 5, 2, -9],
            'query': 4
        },
        'output': -1
    })

    # cards is empty
    tests.append({
        'input': {
            'cards': [],
            'query': 7
        },
        'output': -1
    })

    # cards contains a None entry
    tests.append({
        'input': {
            'cards': [None, 1, 2, 7],
            'query': 7
        },
        'output': -1
    })
    
    # numbers can repeat in cards
    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 7
    })

    # query occurs multiples times
    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 6
        },
        'output': 2
    })

    print('---------------------- TEST CASES ----------------------')
    print(*tests, sep = '\n')
    print('--------------------------------------------------------')
    print('\n')

    print('---------------------- LOCATE CARD BRUTE FORCE ----------------------')
    beginning = perf_counter()
    for i, j in enumerate(tests):
        print('TEST CASE')
        print(j)
        print(locate_card_brute_force(**tests[i]['input']) == tests[i]['output'])
        print('\n')
    end = perf_counter()
    print(f'TIME ESTIMATION {end - beginning}s')
    print('--------------------------------------------------------')

    print('---------------------- LOCATE CARD BINARY SEARCH ----------------------')
    
    for i, j in enumerate(tests):
        print(f'TEST CASE {i}')
        print(j)
        print(locate_card_binary_search(**tests[i]['input']) == tests[i]['output'])
        print('\n')
    print('--------------------------------------------------------')

    #print(locate_card(**tests[0]['input']) == tests[0]['output'])

