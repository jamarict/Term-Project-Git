import random
from UnitClass import *


class Player(object):
    playerColors = ["navy", "yellow", "salmon", "red", "deep pink", "dark violet", "chocolate", 
                "maroon", "orchid", "slateblue"]

    playerList = []

    def __init__(self, name):
        self.name = name
        self.currentUnits = []
        self.currentCities = []
        self.stars = 5
        self.starsPerTurn = 0
        self.myTurn = True
        color = None
        while color == None:
            color = random.choice(self.playerColors)
            for item in self.playerList:
                if item.color == color:
                    color = None
        self.color = color

    def __repr__(self):
        return f"{self.name} + {self.color}"

    def addUnit(self, x, y):
        newUnit = Unit(x, y)
        self.currentUnits.append(newUnit)

