def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''

    while marker != "X" and marker != "O":
        marker = input('Player 1 : Choose X or O ').upper()

    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    # Return True if 3 markers in a row is the same.

    # Win -
    return (
        # Win -
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        # Win |
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        # Win /
        (board[1] == board[5] == board[9] == mark) or
        # Win \
        (board[7] == board[5] == board[3] == mark)
        )
