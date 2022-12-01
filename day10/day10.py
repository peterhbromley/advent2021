def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


SYNTAX_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
AUTOCOMPLETE_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
PAIRS = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}


def first_illegal(line):
    stack = []
    for char in line:
        if char in PAIRS.keys():
            stack.append(char)
        else:
            last_open = stack.pop()
            if char != PAIRS[last_open]:
                return char
    return stack 

lines = read_input("input.txt")
score = 0
for line in lines:
    illegal = first_illegal(line)
    if isinstance(illegal, str): 
        score += SYNTAX_SCORE[illegal]

print(f"Problem 1: {score}")


def autocomplete(line):
    stack = first_illegal(line)
    if isinstance(stack, list):
        score = 0
        while stack:
            last_open = stack.pop()
            score *= 5
            score += AUTOCOMPLETE_SCORE[PAIRS[last_open]]
        return score
    return None


scores = []
for line in lines:
    auto = autocomplete(line)
    if auto:
        scores.append(auto)

scores = sorted(scores)
winner = len(scores) // 2

print(f"Problem 2: {scores[winner]}")
