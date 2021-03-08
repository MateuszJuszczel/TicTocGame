import random


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


def choose_first_player():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    # Return boolean if in board is empty space
    return board[position] == ' '


def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    # Board is full is we return True
    return True


def player_choice(board):

    position = 0

    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position (1-9): '))

    return position


def replay():

    input('Play again? Enter Yes or No ')

    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')

while True:

    #Play the game

    # Set everything up (Board, Whos First, Choose markers
    the_board = [' '] * 10

    player1_marker, player2_marker = player_input()

    turn = choose_first_player()
    print(turn + ' will go first')

    play_game = input('Ready to play? Yes or No? ')

    if play_game.lower()[0] == 'Yes':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            #Show the board
            display_board(the_board)
            #Chooose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board, player1_marker, position)

            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            #Check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print(' Tie game!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Show the board
            display_board(the_board)
            # Chooose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            # Check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print(' Tie game!')
                    break
                else:
                    turn = 'Player 1'

