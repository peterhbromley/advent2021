from collections import defaultdict


def read_input(filename):
    with open(filename) as f:
        start = ""
        mapping = {}
        for line in f.readlines():
            if line.strip() and "->" not in line:
                start = line.strip()
            elif line.strip():
                pair, _, insert = line.strip().split()
                mapping[pair] = [pair[0] + insert, insert + pair[1]]

        return start, mapping 


def _str_to_dict(string):
    pair_counts = defaultdict(int)
    total_counts = defaultdict(int)
    for c1, c2 in zip(string, string[1:]):
        pair_counts[c1 + c2] += 1
        total_counts[c1] += 1
    total_counts[string[-1]] += 1

    return pair_counts, total_counts


def insert(current, mapping, total_counts):
    new_pair_counts = defaultdict(int)
    for pair, count in current.items():
        np1, np2 = mapping[pair]
        new_pair_counts[np1] += count
        new_pair_counts[np2] += count

        new_char = np1[-1]
        total_counts[new_char] += count

    return new_pair_counts, total_counts


string, mapping = read_input("input.txt")
pair_counts, total_counts = _str_to_dict(string)
for _ in range(10):
    pair_counts, total_counts = insert(pair_counts, mapping, total_counts)

print(f"Problem 1: {max(total_counts.values()) - min(total_counts.values())}")

string, mapping = read_input("input.txt")
pair_counts, total_counts = _str_to_dict(string)
for _ in range(40):
    pair_counts, total_counts = insert(pair_counts, mapping, total_counts)

print(f"Problem 2: {max(total_counts.values()) - min(total_counts.values())}")
