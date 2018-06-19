import random


# Build the board display
def display_board(board):

    print('\n'*10)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Player 1 chooses marker
def player_input():
    marker =''

    while not (marker == 'O' or marker == 'X'):
        marker = input("Player 1: Please pick a marker 'X' or 'O': ").upper()

    if marker == 'O':
        return('O', 'X')
    else:
        return('X', 'O')

# Place marker in a position
def place_marker(board, marker, position):
    board[position] = marker

# Check if marker won
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # bottom row
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # middle row
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # top row
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal 1
            (board[3] == mark and board[5] == mark and board[7] == mark) or  # diagonal 2
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # left column
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # middle column
            (board[3] == mark and board[6] == mark and board[9] == mark))   # right column


# Randomly pick starting player
def choose_first():
    player = (random.randint(1,2))
    if player == 1:
        return 'Player 1'
    elif player == 2:
        return 'Player 2'

# Check space availability
def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True

# Check if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
        return True


# Check if a player's position can be used
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        return position

# Replay the game
def replay():
    again = input("play again(Y/N)?: ").lower()
    if again == 'y':
        return True
    elif again == 'n':
        return False
    else:
        replay()



# Main Function
print('Welcome to Tic Tac Toe!')

while True:
    # reset board
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + ' starts first.')

    game_play = input("Are you ready to play?(y/n): ")
    if game_play.lower() == 'y':
        game_on = True
    else:
        game_on = False




    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print ('Congratulations! You won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ("The game is a draw!")
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print ('Congratulations! You won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ("The game is a draw!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break