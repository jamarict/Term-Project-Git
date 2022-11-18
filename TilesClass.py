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

# Field Tiles contain specific resources & can have certain buildings built
# on them
class Field(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "lightGreen"

# Mountain Tiles hold fewer resources & should make certain player movements
# harder    
class Mountain(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "brown"

# Forest Tiles hold their spcific resources and can be altered depending on
# player upgrades
class Forest(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "darkGreen"

# Villages can be considered "pre-cities". They do not belong to a specific
# and can be conquered. Once conquered, they become cities.
class Village(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.containsRuin = False
        
# Cities are owned by player. Cities have specific levels, give players stars,
# and level up. They can not contain ruins under any circumstance
class City(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.level = 1
        self.popToNextLevel = 2
        self.starsPerTurn = 1
        self.color = "red"
        self.containsRuin = False

# Capitals are a special kind of city. Like the "home-base", each player starts
# one capital per game and can not build any new ones. They give 2 stars/turn
class Capital(City):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.starsPerTurn = 2
        self.color = "yellow"





def testTileClass():
    print("Testing Tile Class...", end="\n")
    tile1 = Tile(3,4)
    assert(tile1.x == 3)
    assert(tile1.y == 4)
    assert(tile1.unitOnTile == False)
    print("Passed")

testTileClass()


def testFieldClass():
    print("Testing Tile Class...", end="\n")
    field1 = Field(7,5)
    assert(field1.x == 7)
    assert(field1.y == 5)
    assert(field1.unitOnTile == False)
    assert(field1.color == "lightGreen")
    print("Passed")

testFieldClass()

def testMountainClass():
    print("Testing Tile Class...", end="\n")
    mountain1 = Mountain(0,0)
    assert(mountain1.x == 0)
    assert(mountain1.y == 0)
    assert(mountain1.unitOnTile == False)
    assert(mountain1.color == "brown")
    print("Passed")

testMountainClass()

def testForestClass():
    print("Testing Tile Class...", end="\n")
    forest1 = Forest(10,11)
    assert(forest1.x == 10)
    assert(forest1.y == 11)
    assert(forest1.unitOnTile == False)
    assert(forest1.color == "darkGreen")
    print("Passed")

testForestClass()

def testCityClass():
    print("Testing City Class...", end="\n")
    city1 = City(9,9)
    assert(city1.x == 9)
    assert(city1.y == 9)
    assert(city1.level == 1)
    assert(city1.popToNextLevel == 2)
    assert(city1.starsPerTurn == 1)
    assert(city1.unitOnTile == False)
    assert(city1.containsRuin == False)
    assert(city1.color == "red")
    print("Passed")

testCityClass()

def testCapitalClass():
    print("Testing Capital Class...", end="\n")
    capital1 = Capital(3,3)
    assert(capital1.x == 3)
    assert(capital1.y == 3)
    assert(capital1.level == 1)
    assert(capital1.popToNextLevel == 2)
    assert(capital1.starsPerTurn == 2)
    assert(capital1.unitOnTile == False)
    assert(capital1.color == "yellow")
    print("Passed")

testCityClass()