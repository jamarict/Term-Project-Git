import random
from UnitClass import *


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

    def addCity(self, city):
        self.currentCities.append(city)

    def addUnit(self, city):
        newUnit = Unit(city.x, city.y)
        self.currentUnits.append(newUnit)


