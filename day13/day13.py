def read_input(filename):
    with open(filename) as f:
        grid = []
        instructions = []
        for line in f.readlines():
            line = line.strip()
            if len(line.split(",")) == 2:
                x, y = line.split(",")
                grid.append((int(x), int(y)))
            else:
                try:
                    l, r = line.split("=")
                except ValueError:
                    continue
                instructions.append((l[-1], int(r)))

        return grid, instructions


def fold(grid, instruction):
    axis, loc = instruction
    tuple_idx = 0 if axis == "x" else 1

    for i in range(len(grid)):
        val = grid[i][tuple_idx]
        if val > loc:
            diff = loc - val
            pt_list = list(grid[i])
            pt_list[tuple_idx] = loc + diff
            grid[i] = tuple(pt_list)


def perform_all_folds(grid, instructions):
    for inst in instructions:
        fold(grid, inst)
        grid = list(set(grid))

    return grid


def _print_grid(grid_obj):
    for row in grid_obj:
        for pt in row:
            print(pt, end="")
        print("")


def display_grid(grid):
    max_x = max(grid, key=lambda x: x[0])[0]
    max_y = max(grid, key=lambda x: x[1])[1]
    grid_obj = [
        ["." for _ in range(max_x + 1)]
        for _ in range(max_y + 1)
    ]
    for x, y in grid:
        grid_obj[y][x] = "#"

    _print_grid(grid_obj)


grid, instructions = read_input("input.txt")
fold(grid, instructions[0])
grid = list(set(grid))

print(f"Problem 1: {len(grid)}")

grid, instructions = read_input("input.txt")
grid = perform_all_folds(grid, instructions)
display_grid(grid)
