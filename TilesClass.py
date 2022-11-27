import random
################################################################################

# Tiles make up the map of the game. No matter what kind of Tile, grid position
# and unit status on tile should be stored
class Tile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.resource = None
        #Initialize every Tile as not having a unit on them

    def __repr__(self):
        return f"{self.name}"
    
    def redraw(self, app, canvas):
        pass


# Field Tiles contain specific resources & can have certain buildings built
# on them
class Field(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "pale green"
        self.name = "Field"
        self.resource = self.spawnResources()

    def spawnResources(self):
        num = random.random()
        if (0 <= num < 0.28):
            self.name = self.name + " fruit"
            return "fruit"
        elif (0.28 <= num < 0.56):
            self.name = self.name + " crop"
            return "crop"
        else:
            return None
            

    

# Mountain Tiles hold fewer resources & should make certain player movements
# harder
class Mountain(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "grey"
        self.name = "Mountain"
        self.resource = self.spawnResources()
    
    def spawnResources(self):
        num = random.random()
        if (0 <= num < 0.50):
            self.name = self.name + " metal"
            return "metal"
        else:
            return None

# Forest Tiles hold their spcific resources and can be altered depending on
# player upgrades
class Forest(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "forest green"
        self.name = "Forest"
        self.resource = self.spawnResources()

    def spawnResources(self):    
        num = random.random()
        if (0 <= num < 0.33):
            self.name = self.name + " animal"
            return "animal"
        else:
            return None

# Villages can be considered "pre-cities". They do not belong to a specific player
# and can be conquered. Once conquered, they become cities.
class Village(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.color = "burlywood"
        self.name = "Village"
        
# Cities are owned by player. Cities have specific levels, give players stars,
# and level up.
class City(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.level = 1
        self.popToNextLevel = 2
        self.starsPerTurn = 1
        self.name = "City"
        self.canMakeUnits = True


    def __repr__(self):
        return f"{self.name}"


# Capitals are a special kind of city. Like the "home-base", each player starts with
# one capital per game and can not build any new ones. They give 2 stars/turn
class Capital(City):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.starsPerTurn = 2
        self.name = "Capital"
        self.color = "yellow"
