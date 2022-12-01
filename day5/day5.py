from collections import defaultdict


def read_input(filename):
    def _parse_line(line):
        start, _, end = line.strip("\n").split()
        return tuple(int(c) for c in start.split(",")), tuple(int(c) for c in end.split(",")) 

    with open(filename) as f:
        return [_parse_line(line) for line in f.readlines()]


def get_points(start, end):
    x1, y1 = start
    x2, y2 = end
    slope_x = x2 - x1
    slope_y = y2 - y1

    if slope_x == 0:
        slope_y = slope_y // abs(slope_y)
    elif slope_y == 0:
        slope_x = slope_x // abs(slope_x)
    else:
        slope_x = slope_x // abs(slope_x)
        slope_y = slope_y // abs(slope_y)
    
    points = [(x1, y1)]
    while (x1 != x2) or (y1 != y2):
        x1 += slope_x
        y1 += slope_y
        points.append((x1, y1))

    return points


def problem1(lines):
    points_seen = defaultdict(int)
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            points = get_points(line[0], line[1])
            for point in points:
                points_seen[point] += 1

    return sum(val >= 2 for val in points_seen.values())


def problem2(lines):
    points_seen = defaultdict(int)
    for line in lines:
        points = get_points(line[0], line[1])
        for point in points:
            points_seen[point] += 1

    return sum(val >= 2 for val in points_seen.values())


print(f"Problem 1: {problem1(read_input('input.txt'))}")
print(f"Problem 2: {problem2(read_input('input.txt'))}")
            
