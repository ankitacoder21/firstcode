def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Create a 3x3 empty board
board = [[" " for _ in range(3)] for _ in range(3)]

# Example moves (X and O)
board[0][0] = "X"
board[1][1] = "O"
board[2][2] = "X"

# Print the board
print_board(board)
