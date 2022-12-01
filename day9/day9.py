def read_input(filename):
    with open(filename) as f:
        return [
            [int(x) for x in list(line.strip())]
            for line in f.readlines()
        ]


def _adjacent(board, i, j):
    vals = []
    coords = []
    for ci, cj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if ci >= 0 and cj >= 0:
            try:
                vals.append(board[ci][cj])
                coords.append((ci, cj))
            except IndexError:
                continue
    return vals, coords


def find_minimums(board):
    height = len(board)
    width = len(board[0])
    mins = []
    min_coords = []
    for i in range(height):
        for j in range(width):
            point = board[i][j]
            adjacent, _ = _adjacent(board, i, j)
            if point < min(adjacent):
                mins.append(point)
                min_coords.append((i, j))

    return mins, min_coords


board = read_input("input.txt")
mins, min_coords = find_minimums(board)
risk_levels = [m + 1 for m in mins]
print(f"Problem 1: {sum(risk_levels)}")
            

def find_basin_size(board, low_point):
    seen = []
    queue = [low_point]

    while queue:
        current_i, current_j = queue.pop(0)
        seen.append((current_i, current_j))
        adj, adj_coords = _adjacent(board, current_i, current_j)
        for adj_val, adj_coord in zip(adj, adj_coords):
            if adj_coord not in seen and adj_coord not in queue and adj_val != 9:
                queue.append(adj_coord)

    return len(seen)


sizes = [find_basin_size(board, min_coord) for min_coord in min_coords]
top_3 = sorted(sizes, reverse=True)[:3]
print(f"Problem 2: {top_3[0] * top_3[1] * top_3[2]}")
