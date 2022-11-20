from PlayerClass import*
from TilesClass import*
import random

def maxItemLength(a):
    maxLen = 0
    for row in range(len(a)):
        for col in range(len(a[row])):
            maxLen = max(maxLen, len(repr(a[row][col])))
    return maxLen

def print2dList(a):
    if a == []:
        print([])
        return
    print()
    rows, cols = len(a), len(a[0])
    maxCols = max([len(row) for row in a])
    fieldWidth = max(maxItemLength(a), len(f'col={maxCols-1}'))
    rowLabelSize = 5 + len(str(rows-1))
    rowPrefix = ' '*rowLabelSize+' '
    rowSeparator = rowPrefix + '|' + ('-'*(fieldWidth+3) + '|')*maxCols
    print(rowPrefix, end='  ')
    # Prints the column labels centered
    for col in range(maxCols):
        print(f'col={col}'.center(fieldWidth+2), end='  ')
    print('\n' + rowSeparator)
    for row in range(rows):
        # Prints the row labels
        print(f'row={row}'.center(rowLabelSize), end=' | ')
        # Prints each item of the row flushed-right but the same width
        for col in range(len(a[row])):
            print(repr(a[row][col]).center(fieldWidth+1), end=' | ')
        # Prints out missing cells in each column in case the list is ragged
        missingCellChar = chr(10006)
        for col in range(len(a[row]), maxCols):
            print(missingCellChar*(fieldWidth+1), end=' | ')
        print('\n' + rowSeparator)
    print()



def makeBoard(numOfPlayers, size):
    newBoard = None
    while newBoard == None:
        oldBoard = [[None for i in range(size)] for j in range(size)]
        possibleMoves = set()
        currentCapitals = set()
        for i in range(1,size-1):
            for j in range(1,size-1):
                possibleMoves.add((i,j))
        newBoard = makeCapitalsHelper(numOfPlayers, possibleMoves, oldBoard, currentCapitals)
    board = newBoard[0]
    capitals = newBoard[1]
    for i in range(size):
        for j in range(size):
            if isinstance(board[i][j], Capital):
                continue
            else:
                newTile = tileSelector(i, j)
                board[i][j] = newTile
    return board, capitals

def makeCapitalsHelper(numOfPlayers, possibleMoves, oldBoard, currentCapitals):
    if numOfPlayers == 0:
        return oldBoard, currentCapitals
    else:
        for i in range(len(possibleMoves)):
            currentCapital = random.choice(list(possibleMoves))
            if isLegalMove(currentCapital, currentCapitals):
                x = Capital(currentCapital[0], currentCapital[1])
                oldBoard[currentCapital[0]][currentCapital[1]] = x
                possibleMoves.remove(currentCapital)
                currentCapitals.add(x)
                result = makeCapitalsHelper(numOfPlayers-1, possibleMoves, oldBoard, currentCapitals)
                if result != None:
                    return result
        return None

def isLegalMove(currentCapital, currentCapitals):
    if len(currentCapitals) < 1:
        return True
    capX, capY = currentCapital[0], currentCapital[1]
    for item in currentCapitals:
        if int(((item.x - capX)**2 + (item.y-capY)**2)**0.5) <= 4:
            return False
    return True

def tileSelector(x, y):
    tile = random.random()
    if (0 <= tile < .20):
        return Mountain(x, y)
    elif (.20 <= tile < .54):
        return Forest(x, y)
    else:
        return Field(x, y)