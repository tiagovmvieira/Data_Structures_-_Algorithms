import math

def binary_search(lo: int, hi: int, condition: str)-> int:
    while lo <= hi:
        mid_index = math.floor((lo + hi) / 2 )
        result = condition(mid_index)

        if result == 'found':
            return mid_index
        elif result == 'left':
            hi = mid_index - 1
        else:
            lo = mid_index + 1
    return -1

def locate_card(cards: list, query: int)-> int:
    # integration tests
    assert isinstance(cards, list), 'cards is not an instance of list'
    assert isinstance(query, int), 'query is not an instance of a query'
    
    if (any(elem is None for elem in cards)):
        return -1

    def condition(mid_index: int):
        if cards[mid_index] == query:
            if mid_index > 0 and cards[mid_index - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid_index] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)

test_case = {
    'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 6
        },
        'output': 2
    }

print(locate_card(**test_case['input']) == test_case['output'])
