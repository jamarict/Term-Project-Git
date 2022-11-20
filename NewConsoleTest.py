from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *
from PlayerClass import *
import time
from boardAlgorithm import *

#Creates a viable map with boardAlgorithm. Requires number of player inpute and board size
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
    elif boardInput == "super":
        boardSize = 30
    
    finalBoard, capitals = makeBoard(numOfPlayers, boardSize)
    for i in range(numOfPlayers):
        playersList[i].addCity(capitals[i])
        playersList[i].addUnit(capitals[i])
    playersList[0].myTurn = True
    return finalBoard, playersList

def changeTurns(currentPlayer, players):
    players[currentPlayer].myTurn = False
    currentPlayer = (currentPlayer + 1) % len(players)
    players[currentPlayer].myTurn = True
    return currentPlayer

def printPlayerStatus(players):
    for player in players:
        print(player)
        print(player.myTurn)
        print(player.currentUnits)
        print(player.currentCities)




board, players = createViableBoard(3, "small")
print2dList(board)
currentPlayer = 0
printPlayerStatus(players)
input("continue")
print("------------------------------")
print(f"{players[currentPlayer]}")
print(players[currentPlayer].curentUnits[0])
players[currentPlayer].currentUnits[0].moveUnit(4,4)
print(players[currentPlayer].currentUnits[0].canMove)
print("------------------------------")
print(players[currentPlayer].currentUnits[0])
players[currentPlayer].currentUnits[0].moveUnit(7,7)
print(players[currentPlayer].currentUnits[0].canMove)










    














    








    
