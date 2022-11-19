from PlayerClass import *
from UnitClass import *
################################################################################

# Tiles make up the map of the game. No matter what kind of Tile, grid position
# and unit status on tile should be stored
class Tile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #Initialize every Tile as not having a unit on them
        self.unitOnTile = False
        self.containsRuin = False

    def __repr__(self):
        return f"{self.name}"
# Field Tiles contain specific resources & can have certain buildings built
# on them
class Field(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "pale green"
        self.name = "Field"

# Mountain Tiles hold fewer resources & should make certain player movements
# harder    
class Mountain(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "grey"
        self.name = "Mountain"

# Forest Tiles hold their spcific resources and can be altered depending on
# player upgrades
class Forest(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "forest green"
        self.name = "Forest"

# Villages can be considered "pre-cities". They do not belong to a specific
# and can be conquered. Once conquered, they become cities.
class Village(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.containsRuin = False
        self.color = "burlywood"
        self.name = "Village"
        
# Cities are owned by player. Cities have specific levels, give players stars,
# and level up. They can not contain ruins under any circumstance
class City(Tile):
    def __init__(self, x, y, player):
        super().__init__(x, y)
        player.currentCities.append(self)
        self.player = player
        self.namePlayer = player.name
        self.level = 1
        self.popToNextLevel = 2
        self.starsPerTurn = 1
        self.color = player.color
        self.containsRuin = False
        self.name = "City"
        self.canMakeUnits = True

    def __repr__(self):
        return f"{self.namePlayer}'s {self.name}"


    def spawnUnit(self):
        newUnit = Unit(self.x, self.y)
        self.player.currentUnits.append(newUnit)
        


# Capitals are a special kind of city. Like the "home-base", each player starts
# one capital per game and can not build any new ones. They give 2 stars/turn
class Capital(City):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)
        self.starsPerTurn = 2
        self.name = "Capital"


def getTile(board, xPos, yPos):
    if (xPos, yPos) == (-1, -1):
        return "Please Click on Board"
    tilePiece = board[xPos][yPos]
    return tilePiece
