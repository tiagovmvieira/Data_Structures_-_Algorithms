from typing import Union

def longest_common_subsequence_recursive(seq1: Union[str, list], seq2: Union[str, list])-> int:
    pass

if __name__ == '__main__':
    
    ## Initial Case
    # General Case with a string
    test_case = {
        'input': {
            'seq1': 'serendipitous', 
            'seq2': 'precipitation'
        },
        'output': 7
    }
    ## Different edge cases
    tests = []
    tests.append(test_case)

    # General case with a list
    tests.append({
        'input': {
            'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
            'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
        },
        'output': 5
    })

    # No common subsequence
    tests.append({
        'input': {
            'seq1': 'longest',
            'seq2': 'stone'
        },
        'output': 3
    })

    # One iis a subsequence of the other
    tests.append({
        'input': {
            'seq1': 'dense',
            'seq2': 'condensed'
        },
        'output': 5
    })

    # One sequence is empty
    tests.append({
        'input': {
            'seq1': '',
            'seq2': 'opkpoiklklj'
        },
        'output': 0
    })

    # Both sequences are empty
    tests.append({
        'input': {
            'seq1': '',
            'seq2': ''
        },
        'output': 0
    })

    # Multiple subsequences with same length
    tests.append({
        'input': {
            'seq1': 'abcdef',
            'seq2': 'badcfe'
        },
        'output': 3
    })

    print('---------------------- TEST CASES ----------------------')
    print(*tests, sep = '\n')
    print('--------------------------------------------------------')
    print('\n')
    
    for i, j in enumerate(tests):
        print('TEST CASE')
        print(j)
        longest_common_subsequence_recursive(**tests[i]['input'])
        