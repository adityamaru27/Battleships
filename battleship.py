from random import randint
import random

board = []

def print_board(board):
    for row in board:
        print ( (" ".join(row)))


print ('Welcome to Battleship Arena!')
print()
print ('Please choose one of the following options: ')
print ('Press 1 for a one player game!')
##print ('Press 2 for a two player game!')
numberofplayers = int(input('Number of players: '))

while numberofplayers != 1 and numberofplayers != 2:
    print ('Oops! Invalid input, please try again...')
    print()
    numberofplayers = int(input('Number of players: '))
else:
    levels = {1 : 'Beginner', 2 : 'Difficult'}
    grid_size = int(input('Please choose increasing diffciulty level 1 or 2: '))
    while grid_size != 1 and grid_size != 2:
           grid_size = int(input('Please choose increasing diffciulty level 1 or 2: '))
    else:
        print ('You have chosen: ', levels[grid_size])
        if grid_size == 1:
            for number in range(0,5):
                board.append(['0'] * 5)
        elif grid_size == 2:
            for number in range(0, 6):
                board.append(['0'] * 6)
    print_board(board)

if grid_size == 1:
        ship1_col = randint(0, 4)
        ship1_row = randint(0, 4)
        ship2_col = randint(0, 4)
        ship2_row = randint(0, 4)
        number_enemies = 2
        print ('Number of enemies: ' + str(number_enemies))
        while ship1_col == ship2_col and ship1_row == ship2_row:
            ship1_col = randint(0, 4)
            ship1_row = randint(0, 4)
            ship2_col = randint(0, 4)
            ship2_row = randint(0, 4)
        else:
            for x in range(1,11):
                turn = x
                print ()
                print ('Turn ' + str(turn) + ' out of 10')
                guess_row = int(input('Please guess row: '))    #add a condition for if the user enters a non number input as col and row
                guess_col = int(input('Please guess col: '))
                if (guess_row == ship1_row and guess_col == ship1_col) or (guess_row == ship2_row and guess_col == ship2_col):
                    if board[guess_row][guess_col] == 'H':
                        print()
                        print ('Youv\'ve already sunk that ship try again')
                    else:
                        number_enemies =  number_enemies - 1
                        board[guess_row][guess_col] = 'H'
                        print ()
                        print ('Boom! You\'ve sunk a ship')
                        print ('Number of enemies: ' + str(number_enemies))
                        if number_enemies == 0:
                            print ("Congratulations! You won!")
                            break
                else:
                    if turn == 10:
                        print ('You have used too many turns, the enemy wins!')
                        break
                    elif (guess_row > 4 or guess_row < 0) or (guess_col > 4 or guess_row < 0):
                        print ('This is not even in the ocean!')
                    elif guess_row == ship1_row or guess_row == ship2_row:
                        print()
                        print ('You got the row correct, try again!')
                        board[guess_row][guess_col] = 'X'
                    elif guess_col == ship1_col or guess_col == ship2_col:
                        print()
                        print ('You got the column correct, try again!')
                        board[guess_row][guess_col] = 'X'
                    elif board[guess_row][guess_col] == 'X' or board[guess_row][guess_col] == 'H':
                        print()
                        print ('Youv\'ve already guessed that try again')
                    else:
                        print ('You missed!')
                        board[guess_row][guess_col] = 'X'
                print()
                print()
                print_board(board)
if grid_size == 2:
    ship1_col = randint(0, 5)
    ship1_row = randint(0, 5)
    ship2_col = randint(0, 5)
    ship2_row = randint(0, 5)
    ship3_row = randint(0, 5)
    ship3_col = randint(0, 5)
    number_enemies = 3
    print ('Number of enemies: ' + str(number_enemies))
    while (ship1_col == ship2_col and ship1_row == ship2_row) or \
          (ship2_col == ship3_col and ship2_row == ship3_row) or \
          (ship1_col == ship3_col and ship1_row == ship3_row):
           ship1_col = randint(0, 5)
           ship1_row = randint(0, 5)
           ship2_col = randint(0, 5)
           ship2_row = randint(0, 5)
           ship3_row = randint(0, 5)
           ship3_col = randint(0, 5)
    else:
        for x in range(1,13):
                turn = x
                print ()
                print ('Turn ' + str(turn) + ' out of 12')
                guess_row = int(input('Please guess row: '))    #add a condition for if the user enters a non number input as col and row
                guess_col = int(input('Please guess col: '))
                if (guess_row == ship1_row and guess_col == ship1_col) or \
                   (guess_row == ship2_row and guess_col == ship2_col) or \
                   (guess_row == ship3_row and guess_col == ship3_col):
                    if board[guess_row][guess_col] == 'H':
                        print()
                        print ('Youv\'ve already sunk that ship try again')
                    else:
                        number_enemies =  number_enemies - 1
                        board[guess_row][guess_col] = 'H'
                        print ()
                        print ('Boom! You\'ve sunk a ship')
                        print ('Number of enemies: ' + str(number_enemies))
                        if number_enemies == 0:
                            print ("Congratulations! You won!")
                            break
                else:
                    if turn == 12:
                        print ('You have used too many turns, the enemy wins!')
                        break
                    elif (guess_row == ship1_row or guess_row == ship2_row or guess_row == ship3_row) and \
                         (guess_col == ship1_col or guess_col == ship2_col or guess_col == ship3_col):
                        print()
                        print ('You got the row correct and the column correct but not of the same ship! You\'re closing in!')
                    elif guess_row == ship1_row or guess_row == ship2_row or guess_row == ship3_row:
                        print()
                        print ('You got the row correct, try again!')
                        board[guess_row][guess_col] = 'X'
                    elif guess_col == ship1_col or guess_col == ship2_col or guess_col == ship3_col:
                        print()
                        print ('You got the column correct, try again!')
                        board[guess_row][guess_col] = 'X'
                    elif (guess_row > 7 or guess_row < 0) or (guess_col > 7 or guess_row < 0):
                        print ('This is not even in the ocean!')
                    elif board[guess_row][guess_col] == 'X' or board[guess_row][guess_col] == 'H':
                        print()
                        print ('Youv\'ve already guessed that try again')
                    else:
                        print ('You missed!')
                        board[guess_row][guess_col] = 'X'
                print()
                print()
                print_board(board)
