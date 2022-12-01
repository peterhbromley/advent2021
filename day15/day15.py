from heapq import heappush, heappop
import sys


def read_input(filename):
    with open(filename) as f:
        return [
            [int(x) for x in list(line.strip())]
            for line in f.readlines()
        ]


def _estimate(r, c, nrows, ncols):
    return ((nrows - 1) - r) + ((ncols - 1) - c)


def _neighbors(r, c, nrows, ncols):
    def _valid(nr, nc):
        return nr < nrows and nc < ncols and nr > -1 and nc > -1

    candidates = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    return [(row, col) for row, col in candidates if _valid(row, col)]


def astar(grid):
    nrows = len(grid)
    ncols = len(grid[0])

    visited = [
        [False for _ in range(ncols)]
        for _ in range(nrows)
    ]
    left = [
        [_estimate(r, c, nrows, ncols) for c in range(ncols)]
        for r in range(nrows)
    ]
    to = [
        [sys.maxsize for _ in range(ncols)]
        for _ in range(nrows)
    ]
    to[0][0] = 0

    to_process = []
    length, (row, col)= (0, (0, 0))
    heappush(to_process, (length, (row, col)))
    while (row, col) != (nrows - 1, ncols - 1):
        _, (row, col) = heappop(to_process)
        if not visited[row][col]:
            visited[row][col] = True

            for nr, nc in _neighbors(row, col, nrows, ncols):
                if not visited[nr][nc]:
                    curr_dist = to[nr][nc]
                    new_dist = to[row][col] + grid[nr][nc]
                    if new_dist < curr_dist:
                        to[nr][nc] = new_dist

                    heappush(to_process, (to[nr][nc] + left[nr][nc], (nr, nc)))
                
    return to[nrows - 1][ncols - 1]


def full_grid(grid):
    def _increment(val, n):
        if val + n > 9:
            return ((val + n) % 10) + 1
        return val + n

    def _new_grid(old_grid, n):
        return [
            [_increment(old_grid[r][c], n) for c in range(len(old_grid[0]))]
            for r in range(len(old_grid))
        ]

    final_grid = [x.copy() for x in grid]
    for i in range(1, 5):
        final_grid += _new_grid(grid, i)

    tall_grid = [x.copy() for x in final_grid]
    for j in range(1, 5):
        new = _new_grid(tall_grid, j)
        for i in range(len(new)):
            final_grid[i] += new[i] 

    return final_grid
        

grid = read_input("input.txt")
shortest = astar(grid)
print(f"Problem 1: {shortest}")

final_grid = full_grid(grid)
shortest = astar(final_grid)
print(f"Problem 2: {shortest}")

