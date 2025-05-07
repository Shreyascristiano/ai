def print_board(board, n):
    for i in range(n):
        row = ['#' for _ in range(n)]
        row[board[i]] = 'Q'
        print(" ".join(row))
    print()

def solve_branch_and_bound(row, n, board, cols, diag1, diag2):
    if row == n:
        print("Branch and Bound Solution:")
        print_board(board, n)
        return True  # Found a solution

    for col in range(n):
        if not cols[col] and not diag1[row - col] and not diag2[row + col]:
            board[row] = col
            cols[col] = diag1[row - col] = diag2[row + col] = True

            if solve_branch_and_bound(row + 1, n, board, cols, diag1, diag2):
                return True

            # Backtrack
            cols[col] = diag1[row - col] = diag2[row + col] = False
    return False

# Run branch and bound for 4 queens
n = 4
board = [-1] * n
cols = [False] * n
diag1 = {}  # row - col
diag2 = {}  # row + col

# Initialize all diagonals
for i in range(-n, n): diag1[i] = False
for i in range(2 * n): diag2[i] = False

solve_branch_and_bound(0, n, board, cols, diag1, diag2)
