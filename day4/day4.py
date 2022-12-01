def read_input(filename):
    with open(filename) as f:
        numbers = [int(num) for num in f.readline().strip().split(",")]
        boards = []
        for line in f.readlines():
            if line == "\n":
                boards.append([])
            else:
                boards[-1].append(
                    [int(num) for num in line.strip("\n").split()]
                )

    if boards[-1] == []:
        return numbers, boards[:-1]
    else:
        return numbers, boards


def board_iter(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            yield i, j


def mark_board(board, marks, num):
    for i, j in board_iter(board):
        if board[i][j] == num:
            marks[i][j] = True
            return marks
    return marks


def check_win(marks):
    if any(all(row) for row in marks):
        return True
    elif any(
        all(row[i] for row in marks) for i in range(len(marks[0]))
    ):
        return True
    else:
        return False


def final_score(board, marks, final_num):
    unmarked_sum = sum(
        board[i][j]
        for i, j in board_iter(board)
        if not marks[i][j]
    )
    return unmarked_sum * final_num


def run(boards, numbers):
    n_boards = len(boards)
    rows = len(boards[0])
    cols = len(boards[0][0])

    all_marks = [
        [
            [
                False for _ in range(cols)
            ]
            for _ in range(rows)
        ]
        for _ in range(n_boards)
    ]
    
    has_won = [False for _ in range(n_boards)]
    first_win = -1
    for num in numbers:
        for i in range(len(boards)):
            all_marks[i] = mark_board(boards[i], all_marks[i], num)
            if check_win(all_marks[i]):
                if first_win == -1:
                    first_win = final_score(boards[i], all_marks[i], num)
                has_won[i] = True
                if all(has_won):
                    last_win = final_score(boards[i], all_marks[i], num)
                    return first_win, last_win
    assert False

numbers, boards = read_input("input.txt")
first_win, last_win = run(boards, numbers) 
print(f"Problem 1: {first_win}")
print(f"Problem 2: {last_win}")

