"""
Mapping:
    0000 
   5    1 
   5    1 
    6666
   4    2
   4    2
    3333

digit 1: letters must be in positions [1, 2]
digit 4: letters must be in positions [1, 2, 5, 6]
digit 7: letters must be in positions [0, 1, 2]
digit 8: letters must be in positions [0, 1, 2, 3, 4, 5, 6] (this gives us no info)

digit 2: letters must be in positions [0, 1, 3, 4, 6]
digit 3: letters must be in positions [0, 1, 2, 3, 6]
digit 5: letters must be in positions [0, 2, 3, 5, 6]
    all have 0, 3, 6
    only digit 2 has pos 4
    only digit 5 has pos 5

digit 0: letters must be in positions [0, 1, 2, 3, 4, 5]
digit 6: letters must be in positions [0, 2, 3, 4, 5, 6]
digit 9: letters must be in positions [0, 1, 2, 3, 5, 6]
    all have 0, 2, 3, 5
    
Letter mappings:
{
    a: {0, 1, 2, 3, 4, 5, 6},
    b: {0, 1, 2, 3, 4, 5, 6},
    ...
    g: {0, 1, 2, 3, 4, 5, 6},
}
    
"""
from collections import defaultdict


def read_input(filename):
    with open(filename) as f:
        left_sides, right_sides = [], []
        for line in f.readlines():
            left, right = line.strip("\n").split("|")
            left_sides.append(left.split())
            right_sides.append(right.split())

    return left_sides, right_sides


left, right = read_input("input.txt")
problem1 = sum(sum(len(val) in [2, 3, 4, 7] for val in line) for line in right)
print(f"Problem 1: {problem1}")

DIGIT0 = {0, 1, 2, 3, 4, 5}
DIGIT1 = {1, 2}
DIGIT2 = {0, 1, 3, 4, 6}
DIGIT3 = {0, 1, 2, 3, 6}
DIGIT4 = {1, 2, 5, 6}
DIGIT5 = {0, 2, 3, 5, 6}
DIGIT6 = {0, 2, 3, 4, 5, 6}
DIGIT7 = {0, 1, 2}
DIGIT8 = {0, 1, 2, 3, 4, 5, 6}
DIGIT9 = {0, 1, 2, 3, 5, 6}

def _set_to_str(pos):
    if pos == DIGIT0:
        return '0'
    elif pos == DIGIT1:
        return '1'
    elif pos == DIGIT2:
        return '2'
    elif pos == DIGIT3:
        return '3'
    elif pos == DIGIT4:
        return '4'
    elif pos == DIGIT5:
        return '5'
    elif pos == DIGIT6:
        return '6'
    elif pos == DIGIT7:
        return '7'
    elif pos == DIGIT8:
        return '8'
    elif pos == DIGIT9:
        return '9'
    else:
        assert False, "Bad position set"

def prune(mappings, positions, letters):
    assert len(positions) == len(letters)
    for letter in mappings.keys():
        if letter in letters:
            mappings[letter] &= positions 
        else:
            mappings[letter] = mappings[letter].difference(positions)


def infer_mapping(info):
    letter_to_pos = {
        letter: set(range(7)) for letter in list('abcdefg')
    }

    letters_5 = []
    letters_6 = []
    for letters in info:
        if len(letters) == 5:
            letters_5.append(letters)
        elif len(letters) == 6:
            letters_6.append(letters)
        elif len(letters) == 2:
            prune(letter_to_pos, DIGIT1, letters)
        elif len(letters) == 3:
            prune(letter_to_pos, DIGIT7, letters)
        elif len(letters) == 4:
            prune(letter_to_pos, DIGIT4, letters)
    
    letter_5_counts = defaultdict(int)
    for letter in ''.join(letters_5):
        letter_5_counts[letter] += 1

    prune(letter_to_pos, {0, 3, 6}, [l for l in letter_5_counts.keys() if letter_5_counts[l] == 3])
    prune(letter_to_pos, {1, 2}, [l for l in letter_5_counts.keys() if letter_5_counts[l] == 2])
    prune(letter_to_pos, {4, 5}, [l for l in letter_5_counts.keys() if letter_5_counts[l] == 1])

    letter_6_same = set.intersection(*[set(x) for x in letters_6])
    prune(letter_to_pos, {0, 2, 3, 5}, letter_6_same)
            
    return letter_to_pos 


def get_digits(mapping, output):
    digits = []
    for letters in output:
        pos = set()
        for letter in letters:
            pos |= mapping[letter]
        digits.append(_set_to_str(pos))

    return int(''.join(digits))


left, right = read_input("input.txt")
digits = []
for l, r in zip(left, right):
    mapping = infer_mapping(l)
    assert all([len(x) == 1 for x in mapping.values()])
    digits.append(get_digits(mapping, r))

print(f"Problem 2: {sum(digits)}")
