import random
# Simple 2 player TIC TAC TOE
# An inbuilt function Random has been imported for this project
# Functions used :
# 1. game_order 2. player1_input 3. player2_input 4. winner
# 5. winner_player1 6. winner_player2 7. who_starts_first


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def game_order():
    print('''
This is a game called TIC TAC TOE there is a basic instruction for this game 

Player1 will be 'X' and Player2 will be 'O'
    ''')
    global player1, player2
    player1 = input('Player1 Enter your name: ')
    player2 = input('Player2 Enter your name: ')
    y= input('To start the game press the space bar: ')
    if y==' ':
        print_board()
        who_starts_first()
    else:
        print('The input is invalid please try again')
        game_order()


# A list is taken to manage all the inputs do not use tuples as they cannot be updated
def print_board():
    print(board[0], '|', board[1], '|', board[2])
    print('---'*3)
    print(board[3], '|', board[4], '|', board[5])
    print('---'*3)
    print(board[6], '|', board[7], '|', board[8])


# A random variable value decides who plays first
def who_starts_first():
    print('\r\n This will be a automated decision made by the computer')
    z= random.randint(0,1)
    if z==0:
        print(f'\r\n {player1} gets the first chance')
        player1_input()
    else:
        print(f'\r\n {player2} gets the first chance')
        player2_input()


# The input function takes data from the user it is using the concept of recursion to avoid error
def player1_input():
    for i in range(1):
        try:
            p1 = int(input('\r\n Enter the position at which you want to place a cross [1-9]: '))
        except ValueError :
            print('\r\nInvalid Input')
            player1_input()
        if p1 < 10 and board[p1-1] == ' ' :
            board[p1-1] = 'X'
            print_board()
            winner()
            if x == True:
                   break
            print(f'\r\n {player2} will make its move next')
            player2_input()
            print_board()
            winner()
            if x == True:
                break
            print(f'\r\n {player2} will make its move next')
            player2_input()
        else:
            print('\r\n Invalid Input please try another input')
            player1_input()


def player2_input():
    for i in range(1):
        try:
            p2 = int(input('\r\n Enter the position at which you want to place the nought [1-9]: '))
        except ValueError:
            print('\r\nInvalid Input')
            player2_input()
        if p2 < 10 and board[p2-1] == ' ':
            board[p2-1] = 'O'
            print_board()
            winner()
            if x == True:
                break
            print(f'\r\n {player1} plays next')
            player1_input()
        else:
            print('\r\n Invalid Input please try another input')
            player2_input()



x = False


# The core logic of winning is based on simple logic the following combinations are the winning combinations
def winner():
    global x
    for i in range(1):
        if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == board[8] == 'X':
            winner_player1()
            x = True
        elif board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X':
            winner_player1()
            x = True
        elif board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
            winner_player1()
            x = True
        elif board[0] == board[1] == board[2] == 'O' or board[3] == board[4] == board[5] == 'O' or board[6] == board[7] == board[8] == 'O':
            winner_player2()
            x = True
        elif board[0] == board[3] == board[6] == 'O' or board[1] == board[4] == board[7] == 'O' or board[2] == board[5] == board[8] == 'O':
            winner_player2()
            x = True
        elif board[0] == board[4] == board[8] == 'O' or board[2] == board[4] == board[6] == 'O':
            winner_player2()
            x = True
    else:
        # If all the places of the list are occupied and none of the winning condition is satisfied the match ends in a draw
        if board.count('X') + board.count('O') == 9:
            print('\r\n This is a draw well played !!! Please try again to reach a conclusion')
            x = True


def winner_player1():
    print(f'''\r\n Congratulations {player1} you are the WINNER !!!  :') ''')
    print(f'''\r\n {player2} you lost :'( ''')


def winner_player2():
    print(f'''\r\n Congratulations {player2} you are the WINNER !!!   :') ''')
    print(f'''\r\n {player1} you lost :'( ''')


# Function Call
game_order()