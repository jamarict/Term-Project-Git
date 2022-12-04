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
        self.movement = 1

    def __repr__(self):
        return f"Warrior({self.x, self.y}"
    

    #units redraw themselves based on getCellBounds outputs
    def redraw (self, app, canvas, x0, y0, x1, y1):
        r = 10
        canvas.create_oval(x0 + r, y0 + r, x1 -r, y1 - r, fill = self.color, width = 3, outline = self.outline)
