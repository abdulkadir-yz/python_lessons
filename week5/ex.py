board = ["", "", "", "", "", "", "", "", ""]

def print_board():
    """Print the current state of the board."""
    print("\n")
    print(f" {board[0] or ' '} | {board[1] or ' '} | {board[2] or ' '} ")
    print("---+---+---")
    print(f" {board[3] or ' '} | {board[4] or ' '} | {board[5] or ' '} ")
    print("---+---+---")
    print(f" {board[6] or ' '} | {board[7] or ' '} | {board[8] or ' '} ")
    
    print("\n")

win_lines = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
  [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
  [0, 4, 8], [2, 4, 6]              # Diagonal
]