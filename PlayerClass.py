import random

playerColors = ["red", "green", "blue", "orange", "yellow", "purple", "black", 
                "white", "pink", "brown"]

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

allPlayers = []
for i in range(10):
    player = Player(f"{i+1}")
    allPlayers.append(player)
    
print(allPlayers)

