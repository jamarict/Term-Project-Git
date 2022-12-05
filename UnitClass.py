###############################################################################
# Units are movable warriors that the player controls. There is a generic unit
# that has the following stats. Special units have specific stats and abilities
# Stats obtained from:
# https://polytopia.fandom.com/wiki/List_of_Units
class Unit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.outline = "black"
        self.canAct = False
        self.canMove = False
        self.cost = 3
        self.movement = 1
        self.range = 1
        self.attack = 2
        self.defense = 2
        self.health = 10
        self.maxHealth = 10
        self.name = "W"
        self.title = "Warrior"

    def __repr__(self):
        return self.name
    
    #units redraw themselves based on getCellBounds outputs
    def redraw (self, app, canvas, x0, y0, x1, y1):
        r = 5
        canvas.create_oval(x0+r, y0+r, x1-r, y1-r, fill = self.color, width = 3, outline = self.outline)
        canvas.create_text((x0+x1)/2, (y0+y1)/2, text = self.name)

class Archer(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cost = 4
        self.range = 2
        self.defense = 1
        self.name = "A"
        self.title = "Archer"


class Rider(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cost = 4
        self.movement = 2
        self.defense = 1
        self.name = "R"
        self.title = "Rider"


class Defender(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cost = 4
        self.attack = 1
        self.defense = 3
        self.health = 15
        self.maxHealth = 15
        self.name = "D"
        self.title = "Defender"



