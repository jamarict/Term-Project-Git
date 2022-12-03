import random
from cmu_112_graphics import *
################################################################################

# All tile information from:
# https://polytopia.fandom.com/wiki/Terrain 

# Tiles make up the map of the game. No matter what kind of Tile, grid position
# and unit status on tile should be stored
class Tile(object):
    size = None
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.resource = None
        
        #Initialize every Tile as not having a unit on them

    def __repr__(self):
        return f"{self.name}"
    
    def redraw(self, app, canvas, x0, y0, x1, y1):
        canvas.create_rectangle(x0, y0, x1, y1, width = 1, fill = None, outline = "black")
        if self.resource != None:
            canvas.create_oval(x0+20, y0+20, x1-20, y1-20, fill = "gold")


# Field Tiles contain specific resources & can have certain buildings built
# on them
class Field(Tile):
    image = None

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "pale green"
        self.name = "Field"
        self.resource = self.spawnResources()
        self.hasHouse = False



    def redraw(self, app, canvas, x0, y0, x1, y1):
        canvas.create_image((x0+x1)/2, (y0+y1)/2, image = ImageTk.PhotoImage(self.image))
        super().redraw(app, canvas, x0, y0, x1, y1)
        if self.hasHouse == True:
            canvas.create_rectangle(x0+20, y0+20,x1-20,y1-20, fill = "black")

    # Self-contained functions to determin resource, different for each Tile
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

    def redraw(self, app, canvas, x0, y0, x1, y1):
        canvas.create_image((x0+x1)/2, (y0+y1)/2, image = ImageTk.PhotoImage(self.image))
        super().redraw(app, canvas, x0, y0, x1, y1)
        
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
    image = None
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "forest green"
        self.name = "Forest"
        self.resource = self.spawnResources()

    def redraw(self, app, canvas, x0, y0, x1, y1):
        canvas.create_image((x0+x1)/2, (y0+y1)/2, image = ImageTk.PhotoImage(self.image))
        super().redraw(app, canvas, x0, y0, x1, y1)
        

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
    image = None
    def __init__(self, x, y):
        super().__init__(x,y)
        self.color = "burlywood"
        self.name = "Village"

    def redraw(self, app, canvas, x0, y0, x1, y1):
        canvas.create_image((x0+x1)/2, (y0+y1)/2, image = ImageTk.PhotoImage(self.image))
        super().redraw(app, canvas, x0, y0, x1, y1)
        
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


# Capitals are a special kind of city. Like the "home-base", each player starts with
# one capital per game and can not build any new ones. They give 2 stars/turn
class Capital(City):
    image = None
    def __init__(self, x, y):
        super().__init__(x, y)
        self.starsPerTurn = 2
        self.name = "Capital"
        self.color = "yellow"

    def redraw(self, app, canvas, x0, y0, x1, y1):
        canvas.create_image((x0+x1)/2, (y0+y1)/2, image = ImageTk.PhotoImage(self.image))
        canvas.create_rectangle(x0, y0, x1, y1, width = 3, fill = None, outline = self.color)
        if self.resource != None:
            canvas.create_oval(x0+20, y0+20, x1-20, y1-20, fill = "gold")
        

