# Units are movable warriors that the player controls. There is a generic unit
# that has the following stats. Special units have specific stats and abilities
class Unit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = 2
        self.health = 10     
        self.attack = 2
        self.defense = 2
        self.movement = 1
        self.range = 1
        self.color = "grey"
        self.canMove = True
        self.canAttack = True
        self.canAct = True
        

    def redraw (self, app, canvas, x0, y0, x1, y1):
        r = 5
        canvas.create_oval(x0+r, y0+r, x1-r, y1-r, fill = self.color)

        


    