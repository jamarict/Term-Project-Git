from BoardAlgorithm import *


class GameObject(object):
    def __init__(self, playerNum, mapSize):
        self.playerList = [Player(i) for i in range(playerNum)]
        self.currentPlayerNum = 0
        self.currentPlayer = self.playerList[self.currentPlayerNum]
        self.currentPlayer.myTurn = True
        self.map, capitals = makeBoard(playerNum, mapSize)
        self.unitsOnBoard = dict()
        for i in range(len(self.playerList)):
            player = self.playerList[i]
            capital = capitals[i]
            player.addCity(capital)
            player.addUnit(self, capital)
        
    def __repr__(self):
        return f"{type(self)}"
    
    def changeTurn(self):
        self.currentPlayer.myTurn = False
        self.currentPlayerNum = (self.currentPlayerNum + 1) % len(self.playerList)
        self.currentPlayer = self.playerList[self.currentPlayerNum]
        self.currentPlayer.myTurn = True

    def getTile(self, x, y):
        if (x, y) not in self.map:
            return None
        else:
            return self.map[(x, y)]
    
    def getUnit(self, x, y):
        if (x, y) not in self.unitsOnBoard:
            return None
        else:
            return self.unitsOnBoard[(x,y)]


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
        self.currentUnits = []
        self.myTurn = False

    def addCity(self, city):
        city.color = self.color
        self.currentCities.append(city)

    def __repr__(self):
        return self.name
    
    def addUnit(self, game, city):
        newUnit = Unit(city.x, city.y)
        newUnit.color = city.color
        self.currentUnits.append(newUnit)
        game.unitsOnBoard[(city.x, city.y)] = newUnit
    

