from GameClass import *

# Button Classes to handle mouse interactions
class Button(object):
    def __init__(self, x, y, text, function, color):
        self.x = x
        self.y = y
        self.text = text
        self.f = function
        self.color = color


    def redraw(self, app, canvas): # Button share text drawing
        canvas.create_text(self.x, self.y, text = f"{self.text}", 
                           font = "FixedSys 20", fill = self.color)

###############################################################################

class CircleButton(Button):
    def __init__(self, x, y, r, text, function, color):
        super().__init__(x, y, text, function, color)
        self.r = r
    
    def buttonPressed(self, app, event): # Pythagorean Distance Mouse Detection
        d = ((self.x - event.x) ** 2 + (self.y - event.y) ** 2)**0.5
        if d <= self.r:
            self.functionCall(app)
            return True
            
    def functionCall(self, app):
        self.f(app)

    def redraw(self, app, canvas):
        x0, y0 = self.x - self.r, self.y - self.r
        x1, y1 = self.x + self.r, self.y + self.r
        canvas.create_oval(x0, y0, x1, y1, fill = "sienna3")
        super().redraw(app, canvas)

        
class RectangleButton(Button):
    def __init__(self, x, y, width, height, text, function, color):
        super().__init__(x, y, text, function, color)
        self.leftBound = self.x - width
        self.rightBound = self.x + width
        self.upperBound = self.y - height
        self.lowerBound = self.y + height

    
    def buttonPressed(self, app, event): # Rect Bounded Mouse Detection
        if ((self.leftBound <= event.x <= self.rightBound) and 
        (self.upperBound <= event.y <= self.lowerBound)):
            self.functionCall(app)
    
    def functionCall(self, app):
        self.f(app)
    
    def redraw(self, app, canvas):
        canvas.create_rectangle(self.leftBound, self.upperBound, 
                                self.rightBound, self.lowerBound, 
                                fill = "sienna3")
        super().redraw(app, canvas)

################################################################################

class ParameterCircButton(CircleButton):
    def __init__(self, x, y, r, text, function, number, color):
        super().__init__(x, y, r, text, function, color)
        self.numSet = number

    def functionCall(self, app):
        self.f(app, self.numSet)

class ParameterRectButton(RectangleButton): # Converting to Map Metrics
    def __init__(self, x, y, width, height, text, function, number, color):
        super().__init__(x, y, width, height, text, function, color)
        self.numSet = number
        if number == 1:
            self.text = "Small"
            self.numSet = 11
        elif number == 2:
            self.text = "Medium"
            self.numSet = 15
        elif number == 3:
            self.text = "Large"
            self.numSet = 19


    def functionCall(self, app):
        self.f(app, self.numSet, self.text)

################################################################################

#Button Functions

def goToSetup(app): # Reset going back to Title
    app.playerNum = 0
    app.mapSize = 0
    app.mapText = "No"
    app.suggestionText = ""
    app.mode = "setupMode"

def goToTitle(app):
    app.mode = "titleScreenMode" 

def goToHelp(app):
    app.mode = "helpScreenMode"

def goToSettings(app):
    app.mode = "settingsScreenMode"

def setParameter(app, number):
    app.playerNum = number

def setMapSize(app, number, text):
    app.mapText = text
    app.mapSize = number

def startGame(app): # Check Pre-Game Conditions
    if app.mapSize == 0:
        if app.playerNum == 0:
            app.suggestionText = "Select Players and Map Size"
            return
        else:
            app.suggestionText = "Select a Map Size"
            return
    elif app.mapSize == 11:
        if app.playerNum == 0:
            app.suggestionText = "Select Players"
            return
        elif app.playerNum >= 3:
            app.suggestionText = "Select Less Players or Bigger Map"
            return
    elif app.mapSize == 15:
        if app.playerNum == 0:
            app.suggestionText = "Select Players"
            return
        elif app.playerNum >= 5:
            app.suggestionText = "Select Less Players or Bigger Map"
            return
    elif app.mapSize == 19:
        if app.playerNum == 0:
            app.suggestionText = "Select Players"
            return
    if app.playerNum == 1: # Make single-player game w/CPU
        app.game = vsCPU(app, 1, app.mapSize)
    else: # Make local multiplayer game
        app.game = multiplayer(app, app.playerNum, app.mapSize)
    app.mode = "inPlayScreenMode"

def endTurn(app):
    if app.mode != "inPlayScreenMode":
        app.mode = "inPlayScreenMode"
    app.game.changeTurn(app)

def moveUnit(app):
    app.mode = "unitMoveMode"
    app.buttonHub = []

def attackUnit(app):
    app.mode = "unitAttackMode"
    app.buttonHub = []

def createUnit(app):
    app.mode = "createUnitsMode"
    app.buttonHub = makeUnitsHub(app)


def captureCity(app):
    app.game.currentPlayer.addCity(app, app.game, app.tile)
    app.clickedUnit.outline = "black"
    app.clickedUnit.canAct = False
    app.clickedUnit.canMove = False
    app.buttonHub = []

def harvestResource(app):
    if app.game.currentPlayer.currency >= 1:
        app.game.currentPlayer.currency -= 1
        app.tile.resource = None
        app.targetTile.popToNextLevel -= 1
        if app.targetTile.popToNextLevel == 0:
            app.targetTile.level += 1
            app.targetTile.starsPerTurn += 1
            app.targetTile.popToNextLevel = app.targetTile.level + 1
    else:
        app.tip = "Not Enough Stars"
        app.displayTip = True
    app.buttonHub = []

def createHouse(app):
    if app.game.currentPlayer.currency >= 2 and app.tile.hasHouse == False:
        app.game.currentPlayer.currency -= 2
        app.tile.hasHouse = True
        app.targetTile.popToNextLevel -= 2
        if app.targetTile.popToNextLevel <= 0:
            extra = 0 - app.targetTile.popToNextLevel
            app.targetTile.level += 1
            app.targetTile.starsPerTurn += 1
            app.targetTile.popToNextLevel = app.targetTile.level + 1 - extra
    else:
        app.tip = "Not Enough Stars"
        app.displayTip = True
    app.buttonHub = []


def makeUnitsHub(app):
    buttonList = []
    warrior = Unit(-1,-1)
    createWarriorButton = RectangleButton(app.width*64/80, app.height*5/20, 90, 150 , f"""Create\nWarrior\n\nCost:{warrior.cost}⭐
Health:{warrior.health}\nMovement:{warrior.movement}\nRange:{warrior.range}\nAttack:{warrior.attack}\nDefense:{warrior.defense}""", createWarrior, "black")
    buttonList.append(createWarriorButton)
    archer = Archer(-1, -1)
    createArcherButton = RectangleButton(app.width*74/80, app.height*5/20, 90, 150 , f"""Create\nArcher\n\nCost:{archer.cost}⭐
Health:{archer.health}\nMovement:{archer.movement}\nRange:{archer.range}\nAttack:{archer.attack}\nDefense:{archer.defense}""", createArcher, "black")
    buttonList.append(createArcherButton)
    rider = Rider(-1,-1)
    createRiderButton = RectangleButton(app.width*64/80, app.height*15/20, 90, 150 , f"""Create\nRider\n\nCost:{rider.cost}⭐
Health:{rider.health}\nMovement:{rider.movement}\nRange:{rider.range}\nAttack:{rider.attack}\nDefense:{rider.defense}""", createRider, "black")
    buttonList.append(createRiderButton)
    defender = Defender(-1,-1)
    createDefenderButton = RectangleButton(app.width*74/80, app.height*15/20, 90, 150 , f"""Create\nDefender\n\nCost:{defender.cost}⭐
Health:{defender.health}\nMovement:{defender.movement}\nRange:{defender.range}\nAttack:{defender.attack}\nDefense:{defender.defense}""", createDefender, "black")
    buttonList.append(createDefenderButton)
    return buttonList
    

def createWarrior(app):
    if app.game.currentPlayer.currency >= Unit(-1,-1).cost:
        app.game.currentPlayer.currency -= Unit(-1,-1).cost
        city = app.tile
        newWarrior = Unit(city.x, city.y)
        newWarrior.color = city.color
        app.game.currentPlayer.currentUnits.append(newWarrior)
        app.game.unitsOnBoard[(city.x, city.y)] = newWarrior
        city.canMakeUnits = False
    else:
        app.tip = "Not Enough Stars"
        app.displayTip = True

def createArcher(app):
    if app.game.currentPlayer.currency >= Archer(-1,-1).cost:
        app.game.currentPlayer.currency -= Archer(-1,-1).cost
        city = app.tile
        newWarrior = Archer(city.x, city.y)
        newWarrior.color = city.color
        app.game.currentPlayer.currentUnits.append(newWarrior)
        app.game.unitsOnBoard[(city.x, city.y)] = newWarrior
        city.canMakeUnits = False
    else:
        app.tip = "Not Enough Stars"
        app.displayTip = True

    
def createRider(app):
    if app.game.currentPlayer.currency >= Rider(-1,-1).cost:
        app.game.currentPlayer.currency -= Rider(-1,-1).cost
        city = app.tile
        newWarrior = Rider(city.x, city.y)
        newWarrior.color = city.color
        app.game.currentPlayer.currentUnits.append(newWarrior)
        app.game.unitsOnBoard[(city.x, city.y)] = newWarrior
        city.canMakeUnits = False
    else:
        app.tip = "Not Enough Stars"
        app.displayTip = True


def createDefender(app):
    if app.game.currentPlayer.currency >= Defender(-1,-1).cost:
        app.game.currentPlayer.currency -= Defender(-1,-1).cost
        city = app.tile
        newWarrior = Defender(city.x, city.y)
        newWarrior.color = city.color
        app.game.currentPlayer.currentUnits.append(newWarrior)
        app.game.unitsOnBoard[(city.x, city.y)] = newWarrior
        city.canMakeUnits = False
    else:
        app.tip = "Not Enough Stars"
        app.displayTip = True
