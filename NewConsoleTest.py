from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *
from PlayerClass import *
import time
from boardAlgorithm import *

def createViableBoard(numOfPlayers, boardInput):
    playersList = []
    for i in range(numOfPlayers):
        newPlayer = Player(f"Player {i}")
        playersList.append(newPlayer)

    if boardInput == "small":
        boardSize = 11
    elif boardInput == "medium":
        boardSize = 15 
    elif boardInput == "large":
        boardSize = 19
    
    finalBoard, capitals = makeBoard(numOfPlayers, boardSize)
    print2dList(finalBoard)
    print(capitals)
    return finalBoard


board = createViableBoard(5, "small")

    
