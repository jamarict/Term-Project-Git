################################################################################


# Tiles make up the map of the game. No matter what kind of Tile, grid position
# and unit status on tile should be stored
class Tile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #Initialize every Tile as not having a unit on them
        self.unitOnTile = False

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
    field1 = Field(3,4)
    assert(field1.x == 3)
    assert(field1.y == 4)
    assert(field1.unitOnTile == False)
    assert(field1.color == "lightGreen")
    print("Passed")

testMountainClass()

def testFieldClass():
    print("Testing Tile Class...", end="\n")
    field1 = Field(3,4)
    assert(field1.x == 3)
    assert(field1.y == 4)
    assert(field1.unitOnTile == False)
    assert(field1.color == "lightGreen")
    print("Passed")

testFieldClass()