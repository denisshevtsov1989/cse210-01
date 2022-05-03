"""
Denis Shevtsov
CSE210-01
Tic-Tac-Toe
"""

import random


def drawBoard(board):
    # This function draws a game board with completed moves

    # "Board" comes from 10 lines that draw the board in character graphics
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def inputPlayerLetter():
    # Allows the player to select the symbol they want to play
    # Returns a list with the player's letter as the first element and the computer's letter as the second element
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('What character will you play? (X or O)')
        letter = input().upper()

    # The first element of the returned list must always be the character of the player.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # It is randomly determined who will go first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # This function returns True if the player wants to play again. Otherwise False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # The function takes into account the position on the board and the current move of the player. Returns True if the player won
    # We use bo instead of board and le instead of fully qualified variable names
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
 # Make a copy of the game board and return it
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def isSpaceFree(board, move):
    # Returns True if the move is possible
    return board[move] == ' '


def getPlayerMove(board):
   # Allows the player to make a move
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Your turn (1-9):')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Returns a random move from the given list of possible moves
    # Returns None if there are no moves
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Gets a copy of the contents of the board and the letter that the computer moves.
    # Based on this, it determines where to move and returns the move.
    if computerLetter == 'Х':
        playerLetter = 'О'
    else:
        playerLetter = 'Х'

    # This is where the Tic-Tac-Toe AI algorithm starts
    # The first step is to determine the possibility of winning on the next turn
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

   # Check if the player can win on the next turn to block him
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to occupy one of the corners if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Occupy the center if it is free
    if isSpaceFree(board, 5):
        return 5

    # Occupy one of the side cells
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if all cells on the board have been occupied. Otherwise return False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Lets play "Tic-tac-toe"!')

while True:
   # Reset the state of the game board
    theBoard = [' ']*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('Will walk firs '+turn + '\n')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Congratulations!!! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Draw. Play better next time')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer won! You played...')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Draw. Play better next time')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
###
################################