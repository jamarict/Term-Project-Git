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
        self.color = "red"
        self.canMove = True
        self.canAttack = True
        self.canAct = True

    def __repr__(self):
        return f"Warrior({self.x, self.y}"
        

    def redraw (self, app, canvas, x0, y0, x1, y1):
        r = 5
        canvas.create_oval(x0+r, y0+r, x1-r, y1-r, fill = self.color)

    def moveUnit(self, newX, newY):
        if self.canMove == True:
            if ((newX > self.x + self.movement) or (newX < self.x - self.movement) 
                or (newY > self.y + self.movement) or (newY < self.y - self.movement)):
                    pass
            else:
                self.x = newX
                self.y = newY
                self.canMove = False
