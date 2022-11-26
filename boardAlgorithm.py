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

def print2dDict(a):
    bestRow = -1
    bestCol = -1
    for key in a:
        if key[0] > bestRow:
            bestRow = key[0]
        if key[1] > bestCol:
            bestCol = key[1]
    rows, cols = bestRow + 1, bestCol + 1
    print(rows, cols)

################################################################################
#Board Generation



    # # Create new Tile if current Tile is not a capital
    # for i in range(size):
    #     for j in range(size):
    #         if isinstance(board[i][j], Capital):
    #             continue
    #         else:
    #             newTile = tileSelector(i, j)
    #             board[i][j] = newTile
    # return board, capitals

# main function that repeatedly tries to make a valid board
# A valid board is a board where none of the capitals have overlapping 3x3 regions
def makeBoard(playerNum, mapSize):
    newBoard = None
    while newBoard == None:
        oldBoard = dict() #Store Map as a dictionary with coordinate keys
        possibleMoves = list()
        currentCities = list()
        # Shrink range by 1 so no capitals spawn on outer edge of map
        for row in range(1, mapSize - 1):
            for col in range(1, mapSize -1):
                possibleMoves.append((row, col))
        # Set Total Possible Cities Based on Map Size
        if mapSize == 11:
            totalCities = 5
        elif mapSize == 15:
            totalCities = 9
        elif mapSize == 19:
            totalCities = 13
        # Backtracking Helper that adds capitals to board. Returns board and capital locations
        newBoard = makeCapitalsHelper(playerNum, totalCities, possibleMoves, 
                                      oldBoard, currentCities)
    board = newBoard[0]
    capitals = newBoard[1]
    for row in range(mapSize):
        for col in range(mapSize):
            key = (row, col)
            if key in board:
                continue
            else:
                newTile = tileSelector(row, col)
                board[key] = newTile
    return board, capitals

# recursive function that puts capitals and villages in random positions
def makeCapitalsHelper(playerNum, totalCities, possibleMoves, oldBoard, currentCities):
    # Base case when there's no more cities
    if totalCities == 0:
        return oldBoard, currentCities
    else:
        # Check through possible moves
        for i in range(len(possibleMoves)):
            currentLocation = random.choice(possibleMoves)
            currentLocationX, currentLocationY = currentLocation[0], currentLocation[1]
            # Legality Check
            if isLegalMove(currentLocationX, currentLocationY, currentCities):
                if playerNum > 0:
                    #Create Capital Tile for unaccounted Players
                    currentTile = Capital(currentLocationX, currentLocationY)
                else:
                    #Create Empty Village Tile once all players have a capital
                    currentTile = Village(currentLocationX, currentLocationY)
                #Update Board and Remove Move
                oldBoard[(currentLocationX, currentLocationY)] = currentTile
                possibleMoves.remove(currentLocation)
                currentCities.append(currentTile)
                # Recursion
                result = makeCapitalsHelper(playerNum - 1, totalCities - 1, 
                                            possibleMoves, oldBoard, currentCities)
                if result != None:
                    return result
        return None

# Legality check that uses pythagorean theorem to estimate the distance between cities
# Distance must be above 4 to be considered legal.
def isLegalMove(cx, cy, currentCities):
    if len(currentCities) < 1:
        return True
    for item in currentCities: #Check each capital/village
        if int(((item.x - cx)**2 + (item.y-cy)**2)**0.5) <= 4:
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