import random
from cmu_112_graphics import *
################################################################################
# Tiles make up the map of the game.

# Tile information from:
# https://polytopia.fandom.com/wiki/Terrain 
# https://polytopia.fandom.com/wiki/Map_Generation
################################################################################
# Generic Tile on which all tiles are built upon. Position determines place on
# board
class Tile(object):
    # ALl tiles are representative image

    def __init__(self, x, y):
        # Position stored as (x,y) coordinate
        self.x = x
        self.y = y
        self.image = None
        self.color = "black"


        # Tiles have the potential to contain resources
        self.resource = None

    def __repr__(self):
        return self.name
    
    #units redraw themselves based on getCellBounds outputs
    def redraw(self, app, canvas, x0, y0, x1, y1):
        canvas.create_image((x0+x1)/2, (y0+y1)/2, image = 
                                                 ImageTk.PhotoImage(self.image))
        canvas.create_rectangle(x0, y0, x1, y1, width = 1, fill = None, 
                                                              outline = self.color)
        if self.resource != None:
            canvas.create_oval(x0+20, y0+20, x1-20, y1-20, fill = "gold")


# Field Tiles contain resources and can have houses built on them
class Field(Tile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Field"
        self.resource = self.spawnResources()
        self.house = None

        # Fields do no have houses to start
        self.hasHouse = False

    def redraw(self, app, canvas, x0, y0, x1, y1):
        super().redraw(app, canvas, x0, y0, x1, y1)
        if self.hasHouse == True:
            canvas.create_image((x0+x1)/2, (y0+y1)/2, image = ImageTk.PhotoImage(self.house))

    # Self-contained function to determine resource, different for each Tile
    # Based on random number generation
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


# Mountain Tiles hold less resources than fields and forests
class Mountain(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Mountain"
        self.resource = self.spawnResources()
        
    def spawnResources(self):
        num = random.random()
        if (0 <= num < 0.33):
            self.name = self.name + " metal"
            return "metal"
        else:
            return None

# Forest Tiles hold less resources than fields
class Forest(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Forest"
        self.resource = self.spawnResources()

    def spawnResources(self):    
        num = random.random()
        if (0 <= num < 0.40):
            self.name = self.name + " animal"
            return "animal"
        else:
            return None

################################################################################

# Villages can be considered "pre-cities". They do not belong to a specific 
# player and can be conquered. Once conquered, they become cities.
class Village(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.name = "Village"
        self.color = "black"

        
# Cities are owned by player. Cities have specific levels, give players stars,
# and level up.
class City(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.level = 1
        
        # Pop to Next Level: How many resources you need to level up your city.
        # Resources are gained by harvesting resources or creating houses
        self.popToNextLevel = 2

        # Cities give stars per turn and add to the player's currency
        self.starsPerTurn = 1

        #Cities can make max 1 unit each turn.
        self.canMakeUnits = False

        self.name = "City"
        self.color = "pink"


    def redraw(self, app, canvas, x0, y0, x1, y1):
        super().redraw(app, canvas, x0, y0, x1, y1)
        #Cities have the player's color outlined to show ownership
        canvas.create_rectangle(x0, y0,x1, y1, width = 4, fill = None, 
                                                          outline = self.color)



# Capitals are like "home-base" cities. Each player starts with one capital per 
# game and can not build any new ones.
class Capital(City):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.starsPerTurn = 2
        self.name = "Capital"


