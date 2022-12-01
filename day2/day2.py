def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [(line.split()[0], int(line.split()[1])) for line in lines]


def problem1(commands):
    h, v = 0, 0
    for direction, length in commands:
        if direction == "forward":
            h += length
        elif direction == "down":
            v += length
        elif direction == "up":
            v -= length

    return h * v


def problem2(commands):
    h, v, aim = 0, 0, 0
    for direction, length in commands:
        if direction == "forward":
            h += length
            v += length * aim
        elif direction == "down":
            aim += length
        elif direction == "up":
            aim -= length

    return h * v


print(problem1(read_input("input.txt")))
print(problem2(read_input("input.txt")))

