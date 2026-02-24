# Tic-Tac-Toe Game in Python
# A two-player terminal game

# ── The Board ──────────────────────────────────────────────

# We create a list with 9 empty strings, one for each cell of the 3x3 board.
# Index mapping to positions:
#   1 | 2 | 3
#   ---------
#   4 | 5 | 6
#   ---------
#   7 | 8 | 9
# Why a list? Because lists are mutable — we can update individual cells later
# with board[spot] = "X". If we used a tuple, we couldn't modify it after creation.
# Why empty strings ""? An empty string is "falsy" in Python, which lets us
# use the `or` trick (see print_board) and also check `board[spot] != ""`
# to know if a cell is already taken.
board = ["", "", "", "", "", "", "", "", ""]


def print_board():
    """Print the current state of the board."""
    # Print a blank line before the board for visual spacing in the terminal.
    print("\n")
    # f-string: lets us embed expressions inside {} directly in the string.
    # `board[0] or ' '` — this is the key trick:
    #   - If board[0] has a value like "X" or "O" (truthy), it is printed.
    #   - If board[0] is "" (falsy / empty string), Python's `or` returns the
    #     right side: a single space ' '. This keeps the grid aligned even when
    #     no move has been made in that cell.
    # Why not just print board[0]? Because printing "" would collapse the
    # spacing and the board would look broken/unaligned.
    print(f" {board[0] or ' '} | {board[1] or ' '} | {board[2] or ' '} ")
    # Separator line between rows to visually form the grid.
    print("---+---+---")
    # Second row (indices 3, 4, 5) — same logic as above.
    print(f" {board[3] or ' '} | {board[4] or ' '} | {board[5] or ' '} ")
    print("---+---+---")
    # Third row (indices 6, 7, 8) — same logic as above.
    print(f" {board[6] or ' '} | {board[7] or ' '} | {board[8] or ' '} ")
    # Print a blank line after the board for spacing.
    print("\n")


# ── Win Detection ──────────────────────────────────────────

# This is a list of all possible winning combinations (lines of three).
# Each inner list contains three indices that form a straight line on the board.
# Why define this as a constant outside the function? Because these combinations
# never change — defining them once avoids recalculating them on every call.
# If we didn't have this, we would need complex if/elif logic to check every
# possible win, which would be longer, harder to read, and error-prone.
win_lines = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal (top, middle, bottom rows)
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical   (left, center, right cols)
    [0, 4, 8], [2, 4, 6],             # Diagonal   (top-left→bottom-right, top-right→bottom-left)
]


def check_winner():
    """Return 'X', 'O', or None."""
    # We loop through every winning line.
    # `for a, b, c in win_lines` — this is called "unpacking". Each inner list
    # has exactly 3 elements, so Python assigns them to a, b, c automatically.
    # Why unpacking? It makes the code cleaner than writing win_lines[i][0], etc.
    for a, b, c in win_lines:
        # Check two conditions:
        #   1) board[a] == board[b] == board[c] — all three cells have the same value.
        #      Python allows chained comparison like this; it's equivalent to
        #      (board[a] == board[b]) and (board[b] == board[c]).
        #   2) board[a] != "" — the cells are not empty. Without this check,
        #      three empty cells ("" == "" == "") would falsely count as a win.
        if board[a] == board[b] == board[c] and board[a] != "":
            # Return the winning symbol ("X" or "O").
            # Why return instead of print? Because the caller (play()) decides
            # what to do with the result — printing, breaking, etc. This keeps
            # the function focused on one job (detecting the winner).
            return board[a]
    # If no winning line was found after checking all 8 combinations, return None.
    # None means "no winner yet". The caller can check `if winner:` because
    # None is falsy in Python.
    return None


# ── Game Loop ──────────────────────────────────────────────
def play():
    # "X" always goes first — this is the standard convention in Tic-Tac-Toe.
    # We store the current player as a string so we can directly place it on the board.
    current_player = "X"

    # `turns` counts the total number of successful moves made.
    # Why do we need this? To detect a tie. A 3x3 board has 9 cells, so if
    # turns reaches 9 and nobody has won, the game is a draw.
    # If we didn't track this, the game would loop forever after all cells are filled
    # because the while True loop has no other way to know the board is full.
    turns = 0

    # Print the welcome messages and show the initial (empty) board so the
    # players can see the grid layout before making their first move.
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns entering a spot number (1-9).")
    print_board()

    # `while True` creates an infinite loop. The game keeps running until
    # someone wins or it's a tie, at which point we use `break` to exit.
    # Why not `while turns < 9`? Because we also need to break on a win,
    # and using `while True` with explicit `break` statements makes the
    # exit conditions clearer and easier to manage.
    while True:
        # --- ask for input & validate ---

        # `input()` pauses the program and waits for the user to type something
        # and press Enter. It always returns a string (e.g., "3", "abc", "").
        # The f-string in the prompt shows whose turn it is.
        raw = input(f"Player {current_player}, pick a spot (1-9): ")

        # non-integer guard
        # `try/except` is Python's error-handling mechanism.
        # `int(raw)` tries to convert the user's input string to an integer.
        # If the input is not a valid number (e.g., "abc", "", "2.5"), Python
        # raises a ValueError exception. Without try/except, this would crash
        # the entire program. The except block catches that error gracefully.
        try:
            spot = int(raw)
        except ValueError:
            # Inform the user and `continue` — this jumps back to the top of
            # the while loop, skipping everything below and asking for input again.
            # Why `continue` instead of `else`? Because there are multiple
            # validation checks below. Using `continue` for each invalid case
            # keeps the code flat and readable instead of deeply nested if/else.
            print("❌ Invalid input! Please enter a number between 1 and 9.")
            continue

        # range guard
        # Even though the input is a valid integer, it might be outside 1-9.
        # Our board list has indices 0 through 8. Accessing out-of-range indices
        # would either crash (IndexError) or give unexpected behavior (negative
        # indices wrap around in Python, so board[-1] == board[8]).
        if spot < 1 or spot > 9:
            print("❌ Out of range! Please enter a number between 1 and 9.")
            continue

        # already-taken guard
        # If the cell is not empty (i.e., it already has "X" or "O"), the player
        # must choose a different cell. Without this check, a player could
        # overwrite the opponent's move, which would break the game.
        # Convert from 1-based (user-facing) to 0-based (internal index).
        spot -= 1

        if board[spot] != "":
            print("❌ Spot already taken! Pick another one.")
            continue

        # --- place the token ---
        # If we reach this point, all three validations passed: the input is
        # a valid integer, within range, and the cell is empty.
        # We place the current player's symbol on the board.
        board[spot] = current_player
        # Increment the turn counter. This is done AFTER placing the move so
        # invalid attempts don't count as turns.
        turns += 1
        # Show the updated board so both players can see the new state.
        print_board()

        # --- check for a win ---
        # Call check_winner() to see if the move we just made created a
        # winning line. We check AFTER every move because a win can only
        # happen as a result of the most recent move.
        winner = check_winner()
        if winner:
            # `winner` is truthy ("X" or "O"), so we announce the winner and
            # `break` out of the while True loop, ending the game.
            print(f"🎉 Player {winner} wins! Congratulations!")
            break

        # --- check for a tie ---
        # If 9 turns have been made and no winner was found (we already
        # checked above), every cell is filled — it's a draw.
        # Why check this AFTER the win check? Because the 9th move could be
        # the winning move. If we checked for a tie first, we'd incorrectly
        # declare a tie instead of a win on the final move.
        if turns == 9:
            print("🤝 It's a tie!")
            break 

        # --- swap turns ---
        # Switch to the other player. If it was "X"'s turn, it becomes "O"'s
        # turn, and vice versa.
        # Why an if/else instead of something fancier? It's simple and clear.
        # An alternative would be a ternary:
        #   current_player = "O" if current_player == "X" else "X"
        # Both approaches do the same thing; this version is more readable
        # for beginners.
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# ── Entry Point ────────────────────────────────────────────

# `__name__` is a special built-in variable in Python.
# When you run this file directly (e.g., `python tic_tac_toe.py`), Python sets
# __name__ to "__main__". So the condition is True and play() is called.
# But if another file imports this module (e.g., `import tic_tac_toe`), then
# __name__ is set to "tic_tac_toe" (the module name), NOT "__main__".
# In that case, play() would NOT be called automatically.
# Why is this useful? It lets you reuse functions like check_winner() or
# print_board() in other files (e.g., for testing) without the game starting
# automatically on import. Without this guard, importing the module would
# immediately launch the interactive game, which is almost never what you want.
if __name__ == "__main__":
    play()
