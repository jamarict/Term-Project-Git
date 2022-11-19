import random

playerColors = ["navy", "yellow", "salmon", "red", "deep pink", "dark violet", "chocolate", 
                "maroon", "orchid", "slateblue"]

class Player(object):
    def __init__(self, name):
        self.name = name
        self.currentUnits = []
        self.currentCities = []
        self.stars = 5
        self.starsPerTurn = 0
        self.myTurn = True
        index = random.randint(0, len(playerColors)-1)
        self.color = playerColors.pop(index)

    def __repr__(self):
        return f"{self.name} + {self.color}"
