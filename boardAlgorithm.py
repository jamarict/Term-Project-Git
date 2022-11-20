from PlayerClass import*
from TilesClass import*
import random
################################################################################

# Helper functions to print 2d List
# from https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#printing
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

################################################################################
#Board Generation

# main function that repeatedly tries to make a valid board
# A valid board is a board where none of the capitals have overlapping 3x3 regions
def makeBoard(numOfPlayers, size):
    newBoard = None
    while newBoard == None:
        oldBoard = [[None for i in range(size)] for j in range(size)]
        possibleMoves = list()
        currentCapitals = list()
        # Shrink range by 1 so no capitals spawn on outer edge of map
        for i in range(1,size-1):
            for j in range(1,size-1):
                possibleMoves.append((i,j))
        # Backtracking Helper that adds capitals to board. Returns board and capital locations
        newBoard = makeCapitalsHelper(numOfPlayers, possibleMoves, oldBoard, currentCapitals)
    board = newBoard[0]
    capitals = newBoard[1]
    # Create new Tile if current Tile is not a capital
    for i in range(size):
        for j in range(size):
            if isinstance(board[i][j], Capital):
                continue
            else:
                newTile = tileSelector(i, j)
                board[i][j] = newTile
    return board, capitals

# recursive function that puts capitals in random positions
def makeCapitalsHelper(numOfPlayers, possibleMoves, oldBoard, currentCapitals):
    # Base case when there's no more players to account for
    if numOfPlayers == 0:
        return oldBoard, currentCapitals
    else:
        # Check through possible moves
        for i in range(len(possibleMoves)):
            # Instead of systemically going theough each row & col, choose a random one
            currentCapital = random.choice(possibleMoves)
            # legality check
            if isLegalMove(currentCapital, currentCapitals):
                #Create Capital Tile, put it on the board, then remove it as a possible move
                capitalTile = Capital(currentCapital[0], currentCapital[1])
                oldBoard[currentCapital[0]][currentCapital[1]] = capitalTile
                possibleMoves.remove(currentCapital)
                currentCapitals.append(capitalTile)
                # Recursion
                result = makeCapitalsHelper(numOfPlayers-1, possibleMoves, oldBoard, currentCapitals)
                if result != None:
                    return result
        return None

# Legality check that uses pythagorean theorem to estimate the distance between capitals
# Distance must be above 4 to be considered legal.
def isLegalMove(currentCapital, currentCapitals):
    if len(currentCapitals) < 1:
        return True
    capX, capY = currentCapital[0], currentCapital[1]
    for item in currentCapitals: #Check each capital
        if int(((item.x - capX)**2 + (item.y-capY)**2)**0.5) <= 4:
            return False
    return True



# Random number generation to determine Tile Type
# Website to determine bounds:
# https://polytopia.fandom.com/wiki/Map_Generation
def tileSelector(x, y):
    tile = random.random()
    if (0 <= tile < .20):
        return Mountain(x, y)
    elif (.20 <= tile < .54):
        return Forest(x, y)
    else:
        return Field(x, y)
