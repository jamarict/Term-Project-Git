from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *
from PlayerClass import *

numOfPlayers = int(input("how many players are playing: "))
playersList = []
for i in range(numOfPlayers):
    newPlayer = Player(f"Player {i}")
    playersList.append(newPlayer)
print(playersList)

boardInput = input("what board Size would you like: ")
if boardInput == "small":
    boardSize = 11
elif boardInput == "medium":
    boardSize = 15
elif boardInput == "large":
    boardSize = 19

