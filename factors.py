"""
Enumerate the ways a number between 1 and 45 can be represented as
a sum of unique digits between 1 and 9 inclusive.
"""
from itertools import combinations

max_word = 9
digits = list(range(1, max_word + 1))
max_sum = sum(digits)

def get_combos(desired_sum, length_of_word):
    
    """ Return a list of tuples, where each tuple contains `length_of_word`
        unique digits from `digits` that sum to `desired_sum`.

        `desired_sum`:    1 <= desired_sum <= max_sum
        `length_of_word`: 1 <= length_of_word <= max_word
        
        The tuples are sorted internally in increasing order and appear
        in the list in lexicographic order.
    """

    combos = []
    combs = combinations(digits,length_of_word)
    for c in combs:
        if sum(c) == desired_sum:
            combos.append(c)
    return combos

def list_all():
    for desired_sum in range(3, max_sum + 1):
        print(desired_sum)
        for length_of_word in range(2, max_word + 1):
            combos = get_combos(desired_sum, length_of_word)
            if combos and len(combos) < 5:
                print('  ', length_of_word, combos)
            else:
                if len(combos) >= 5:
                    print('  ', length_of_word, 'Too many to list')
            

if __name__ == '__main__':
    """    
    print('\nExpect:\n[(7, 8, 9)]\n')
    print('Result:\n', get_combos(24, 3), sep='')

    print('\nExpect:\n[(4, 7, 8, 9), (5, 6, 8, 9)]\n')
    print('Result:\n', get_combos(28, 4), sep='')

    print('\nExpect:\n[]\n')
    print('Result:\n', get_combos(45, 4), sep='')
    """

    list_all()

