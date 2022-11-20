from PlayerClass import*
from TilesClass import*
import random

def makeBoard(playerList, size):
    newBoard = None
    while newBoard == None:
        oldBoard = [[None for i in range(size)] for j in range(size)]
        possibleMoves = set()
        currentCapitals = set()
        for i in range(1,size-1):
            for j in range(1,size-1):
                possibleMoves.add((i,j))
        newBoard = makeCapitalsHelper(playerList, possibleMoves, oldBoard, currentCapitals)
    for i in range(size):
        for j in range(size):
            if isinstance(newBoard[i][j], Capital):
                continue
            else:
                newTile = tileSelector(i, j)
                newBoard[i][j] = newTile
    return newBoard

def makeCapitalsHelper(playerList, possibleMoves, oldBoard, currentCapitals):
    if playerList == []:
        return oldBoard
    else:
        for i in range(len(possibleMoves)):
            currentCapital = random.choice(list(possibleMoves))
            if isLegalMove(currentCapital, currentCapitals):
                oldBoard[currentCapital[0]][currentCapital[1]] = Capital([currentCapital[0]], [currentCapital[0]], playerList[0])
                possibleMoves.remove(currentCapital)
                currentCapitals.add(currentCapital)
                result = makeCapitalsHelper(playerList[1:], possibleMoves, oldBoard, currentCapitals)
                if result != None:
                    return result
        return None

def isLegalMove(currentCapital, currentCapitals):
    capX, capY = currentCapital[0], currentCapital[1]
    for item in currentCapitals:
        if abs((item[0] + item[1]) - (capX + capY)) <= 4:
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