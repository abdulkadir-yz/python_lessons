# Set up variables

# To avoid the board from moving its border lines when printed, we can store spaces in the below list.
# So, we are basically replacing the space with an "X" or an "O".
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
current_player = "X"
turn_counts = 0
game_active = True

# Winning combinations
win_lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],  # Horizontal
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],  # Vertical
    [0, 4, 8],
    [2, 4, 6],  # Diagonal
]


def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


while game_active:
    print_board()

    valid_move = False
    # Validate the input (deal with edge cases)
    while not valid_move:
        move = input(f"Player {current_player}, Please enter a spot from 0-8: ")

        if move.isdigit():
            move = int(move)

            if 0 <= move <= 8:
                if board[move] == " ":
                    valid_move = True
                else:
                    print("Spot is already taken")
            else:
                print("Please enter a number within 0 and 8")
        else:
            print("Please enter only numbers")

    board[move] = current_player
    turn_counts += 1

    # Check if someone won the game
    for line in win_lines:

        pos1, pos2, pos3 = line[0], line[1], line[2]

        if board[pos1] == board[pos2] == board[pos3] and board[pos1] != " ":
            print_board()
            print(f"player {current_player} has WON!")
            game_active = False
            break

    # Check for ties
    if game_active == True and turn_counts == 9:
        print_board()
        print("It is a tie!")
        game_active = False

    # swapping the player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"