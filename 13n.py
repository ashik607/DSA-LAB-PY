



def print_board(board):
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col, n):
    # check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # check if there is a queen in the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # check if there is a queen in the lower diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # if all checks pass, the position is safe
    return True

def solve_n_queens(board, col, n):
    # if all queens are placed, print the solution
    if col >= n:
        print_board(board)
        print()
        return True

    # check all rows in this column
    for row in range(n):
        if is_safe(board, row, col, n):
            # place the queen at this position
            board[row][col] = "Q"

            # move to the next column
            solve_n_queens(board, col + 1, n)

            # backtrack and remove the queen from this position
            board[row][col] = "-"

    # if no safe position is found, return False to backtrack
    return False

# main function
n = int(input("Enter the size of the board: "))
board = [["-" for x in range(n)] for y in range(n)]
solve_n_queens(board, 0, n)
