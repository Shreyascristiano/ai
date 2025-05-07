def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_board(board, n):
    for i in range(n):
        row = ['#' for _ in range(n)]
        row[board[i]] = 'Q'
        print(" ".join(row))
    print()

def solve_backtracking(board, row, n):
    if row == n:
        print("Backtracking Solution:")
        print_board(board, n)
        return True  # Found a solution

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_backtracking(board, row + 1, n):
                return True  # Comment this line to find all solutions
    return False

# Run backtracking for 4 queens
n = 4
board = [-1] * n
solve_backtracking(board, 0, n)
