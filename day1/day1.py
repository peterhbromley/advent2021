import sys 


def read_input(input_file):
    with open(input_file) as f:
        return [int(line.strip()) for line in f.readlines()]
    

def num_increasing(depths):
    return sum(depths[i] > depths[i-1] for i in range(1, len(depths)))


def problem1(input_file):
    return num_increasing(read_input(input_file)) 


def problem2(input_file):
    depths = read_input(input_file)
    depth_sums = [sum(window) for window in zip(depths, depths[1:], depths[2:])]
    return num_increasing(depth_sums)


input_file = "input.txt"
print(f"Problem 1: {problem1(input_file)}")
print(f"Problem 2: {problem2(input_file)}")

