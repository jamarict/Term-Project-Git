from BoardAlgorithm import *
from UnitClass import *
################################################################################

class GameObject(object):
    def __init__(self, app, playerNum, mapSize):
        # Initializes board, players, first player turn, and adds all necessary units & capitals
        self.playerList = [Player(i) for i in range(playerNum)]
        self.currentPlayerNum = 0
        self.currentPlayer = self.playerList[self.currentPlayerNum]
        self.currentPlayer.myTurn = True
        self.map, capitals = makeBoard(app, playerNum, mapSize)
        self.unitsOnBoard = dict()
        for i in range(len(self.playerList)):
            player = self.playerList[i]
            capital = capitals[i]
            capitalImage1 = app.loadImage("images/CapitalTile.png")
            capitalImage2 = app.scaleImage(capitalImage1, 1/(app.mapSize*493/700))
            capital.image = capitalImage2
            player.addCity(app, self, capital)
            player.addUnit(self, capital)
        for item in self.currentPlayer.currentUnits:
            item.canAct = True
            item.outline = "white"
            item.canMove = True
        self.currentPlayer.firstTurn = False
        
    def __repr__(self):
        return f"{type(self)}"
    
    def changeTurn(self, app): #changes player turns
        app.targetTile = None
        self.currentPlayer.myTurn = False
        for unit in self.currentPlayer.currentUnits:
            unit.canAct = False
            unit.outline = "black"
            unit.canMove = False
        for city in self.currentPlayer.currentCities:
            city.canMakeUnits = False
        self.currentPlayerNum = (self.currentPlayerNum + 1) % len(self.playerList)
        self.currentPlayer = self.playerList[self.currentPlayerNum]
        self.currentPlayer.myTurn = True
        for unit in self.currentPlayer.currentUnits:
            unit.canAct = True
            unit.outline = "white"
            unit.canMove = True
        for city in self.currentPlayer.currentCities:
            city.canMakeUnits = True
            if self.currentPlayer.firstTurn == False:
                self.currentPlayer.currency += city.starsPerTurn
        self.currentPlayer.firstTurn = False

    def getTile(self, x, y): # Gets tile at associated x,y coordinates
        if (x, y) not in self.map:
            return None
        else:
            return self.map[(x, y)]
    
    def getUnit(self, x, y): #Gets unit from unit dictionary, using x,y coordinates
        if (x, y) not in self.unitsOnBoard:
            return None
        else:
            return self.unitsOnBoard[(x,y)]


class vsCPU(GameObject):
    def __init__(self, app, playerNum, mapSize):
        playerNum += 1
        super().__init__(app, playerNum, mapSize)

class multiplayer(GameObject):
    def __init__(self, app, playerNum, mapSize):
        super().__init__(app, playerNum, mapSize)

class Player(object): # Player objects that represent those playing
    playerColors = ["red", "blue", "yellow", "white", "purple", "orange" ]
    def __init__(self, name):
        self.name = f"Player {name}"
        self.color = self.playerColors[name]
        # Cities and units are kept track of
        self.currentCities = []
        self.currentUnits = []
        self.myTurn = False
        self.currency = 5
        self.firstTurn = True

    def addCity(self, app, game, city): # Adds city to map and player's cities
        if isinstance(city, City):
            city.color = self.color
            for player in game.playerList:
                    if city in player.currentCities:
                        player.currentCities.remove(city)
            city.name = city.name + f" {len(self.currentCities) + 1}"
            self.currentCities.append(city)
        else:
            newCity = City(city.x, city.y)
            newCity.color = self.color
            newCity.name = newCity.name + f" {len(self.currentCities) + 1}"
            cityImage1 = app.loadImage("images/CityTile.png")
            cityImage2 = app.scaleImage(cityImage1, 1/(app.mapSize*459/700))
            newCity.image = cityImage2
            self.currentCities.append(newCity)
            game.map[(city.x, city.y)] = newCity
            
    def __repr__(self):
        return self.name
    
    def addUnit(self, game, city): #Add's unit to unit dictionary
        newUnit = Unit(city.x, city.y)
        newUnit.color = city.color
        self.currentUnits.append(newUnit)
        game.unitsOnBoard[(city.x, city.y)] = newUnit
    

