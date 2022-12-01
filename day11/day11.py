def read_input(filename):
    with open(filename) as f:
        return [
            [int(x) for x in list(line.strip())]
            for line in f.readlines()
        ]


def _valid(board, coord):
    i, j = coord
    return i >= 0 and j >= 0 and i < len(board) and j < len(board[0])


def _neighbors(board, coord):
    i, j = coord
    neighbors = [(i+1, j), (i+1, j+1), (i+1, j-1), (i, j+1), (i, j-1), (i-1, j+1), (i-1, j), (i-1, j-1)]
    return [n for n in neighbors if _valid(board, n)]


def run_flashes(board):
    need_to_flash = [
        (i, j) for i in range(len(board)) for j in range(len(board[0]))
        if board[i][j] > 9
    ]
    while need_to_flash:
        current = need_to_flash.pop()
        neighbors = _neighbors(board, current)
        for ni, nj in neighbors:
            if board[ni][nj] < 10:
                board[ni][nj] += 1

                if board[ni][nj] > 9:
                    need_to_flash.append((ni, nj))

    to_reset = [
        (i, j) for i in range(len(board)) for j in range(len(board[0]))
        if board[i][j] > 9
    ]
    total_flashes = len(to_reset)

    for ri, rj in to_reset:
        board[ri][rj] = 0

    return total_flashes


def run(board):
    total_flashes = 0
    for _ in range(100):
        board = [[x + 1 for x in row] for row in board]
        total_flashes += run_flashes(board)

    return total_flashes


def run_for_sync_step(board):
    iters = 0
    while True:
        board = [[x + 1 for x in row] for row in board]
        total_flashes = run_flashes(board)
        iters += 1

        if total_flashes == len(board) * len(board[0]):
            return iters


board = read_input('input.txt')
total_flashes = run(board)

print(f"Problem 1: {total_flashes}")

board = read_input('input.txt')
sync_iter = run_for_sync_step(board)
print(f"Problem 2: {sync_iter}")

