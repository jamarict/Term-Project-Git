import random
from UnitClass import *

# Information is stored about the player, like what cities & units they have,
# stars (currency), if it's their turn, their color, etc...
class Player(object):
    playerList = []

    def __init__(self, name):
        self.name = name
        self.currentUnits = []
        self.currentCities = []
        self.stars = 5
        self.starsPerTurn = 0
        self.myTurn = False
        self.color = "pink"

    def __repr__(self):
        return f"{self.name} + {self.color}"

    # Adds designated city to currentCities
    def addCity(self, city):
        self.currentCities.append(city)

    # takes a city Tile and adds a a new unit onto that tile
    def addUnit(self, city):
        newUnit = Unit(city.x, city.y)
        self.currentUnits.append(newUnit)