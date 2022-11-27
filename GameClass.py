from BoardAlgorithm import *


class GameObject(object):
    def __init__(self, playerNum, mapSize):
        self.playerList = [Player(i) for i in range(playerNum)]
        self.currentPlayerNum = 0
        self.playerList[self.currentPlayerNum].myTurn = True
        self.map, capitals = makeBoard(playerNum, mapSize)
        for i in range(len(self.playerList)):
            self.playerList[i].addCity(capitals[i])
        
    def __repr__(self):
        return f"{type(self)}"
    
    def changeTurn(self):
        self.currenPlayer[self.currentPlayerNum].myTurn = False
        self.currentPlayerNum = (self.currentPlayerNum + 1) % len(self.playerList)
        self.currentPlayer = self.playerList[self.currentPlayerNum].myTurn = True


class vsCPU(GameObject):
    def __init__(self, playerNum, mapSize):
        playerNum += 1
        super().__init__(playerNum, mapSize)

class multiplayer(GameObject):
    def __init__(self, playerNum, mapSize):
        super().__init__(playerNum, mapSize)

class Player(object):
    playerColors = ["red", "blue", "yellow", "black", "purple", "orange" ]
    def __init__(self, name):
        self.name = f"Player {name}"
        self.color = self.playerColors[name]
        self.currentCities = []
        self.myTurn = False

    def addCity(self, city):
        city.color = self.color
        self.currentCities.append(city)

    def __repr__(self):
        return self.name
