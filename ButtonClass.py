from GameClass import *

# Button Classes to handle mouse interactions
class Button(object):
    def __init__(self, x, y, text, function, color):
        self.x = x
        self.y = y
        self.text = text
        self.f = function
        self.color = color


    def redraw(self, app, canvas): # Draw Button Text
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
            
    # Calls function asssigned to button
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
# Buttons Specific for Setting Game

class ParameterCircButton(CircleButton):
    def __init__(self, x, y, r, text, function, number, color):
        super().__init__(x, y, r, text, function, color)
        self.numSet = number

    def functionCall(self, app):
        self.f(app, self.numSet)

class ParameterRectButton(RectangleButton):
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
# Button Functions

def goToSetup(app): # Reset going to Setup Screen
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

def setParameter(app, number): #Sets player number
    app.playerNum = number

def setMapSize(app, number, text): #Sets map size and display text
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
    # Make single-player game w/CPU
    if app.playerNum == 1: 
        app.game = vsCPU(app)
    else: # Make local multiplayer game
        app.game = multiplayer(app)
    app.mode = "inPlayScreenMode"

def endTurn(app): #Transition to next player
    if app.mode != "inPlayScreenMode":
        app.mode = "inPlayScreenMode"
    app.game.changeTurn(app)

def moveUnit(app):
    app.mode = "unitMoveMode"
    app.buttonHub = []

def attackUnit(app):
    app.mode = "unitAttackMode"
    app.buttonHub = []

def createUnit(app): # Sets up Screen to make units
    app.mode = "createUnitsMode"
    app.buttonHub = makeUnitsHub(app)

def captureCity(app): # Adds city to player's city list and deactivates unit
    app.game.currentPlayer.addCity(app, app.game, app.tile)
    app.clickedUnit.outline = "black"
    app.clickedUnit.canAct = False
    app.clickedUnit.canMove = False
    app.buttonHub = []

# Harvest resource on specific tile and adds to the city's level
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
        showTip(app, "Not Enough Stars")
    app.buttonHub = []


# Creates a house on the specific tile and adds to the city's level
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
        showTip(app, "Not Enough Stars")
    app.buttonHub = []

################################################################################

def makeInitialButtons(app):
    bigDimensions = 70
    endDimensions = 50

    playGameX = app.width * 1/4
    playGameY = app.height * 11/14
    app.buttonPlayGame = CircleButton(playGameX, playGameY, bigDimensions,
                                                "Play\nGame", goToSetup, "red4")

    helpX = app.width * 1/2
    helpY = app.height * 11/14
    app.buttonHelp = CircleButton(helpX, helpY, bigDimensions, "Help", goToHelp,
                                                                        "Gold3")

    settingX = app.width * 3/4
    settingY = app.height * 11/14
    app.buttonSetting = CircleButton(settingX, settingY, bigDimensions, 
                                       "Settings", goToSettings, "midnightblue")

    titleX = app.width * 1/4
    titleY = app.height * 11/14
    app.buttonTitle = CircleButton(titleX, titleY, bigDimensions,
                                          "Back to\n Title", goToTitle, "black")

    startX = app.width * 3/4
    startY = app.height * 11/14
    app.buttonStartGame = CircleButton(startX, startY, bigDimensions, 
                                           " Start\n Game", startGame, "green4")

    endX = app.width * 4/30
    endY = app.height * 23/30
    app.buttonEndTurn = CircleButton(endX, endY, endDimensions, "End\nTurn",
                                                               endTurn, "white")

    gameOverY = app.height * 7/8
    gameOverWidth = 125
    gameOverHeight = 50
    app.gameOverButton = RectangleButton(app.cx, gameOverY, gameOverWidth, 
                            gameOverHeight, "Back To Title", goToTitle, "white")
    
    numDimensions = 40
    buttonRows = 3
    buttonCols = 2
    makeNumberButtons(app, numDimensions, buttonRows, buttonCols)

    sizeWidth = 1/11
    sizeHeight = 1/28
    makeSizeButtons(app, buttonRows, sizeWidth, sizeHeight)

def makeNumberButtons(app, dim, rows, cols):
    rowRef = app.width * 1/4
    colRef1 = app.height * 2/15
    colRef2 = app.height * 1/7
    app.setupButtons = []
    for col in range(1, cols + 1):
        for row in range(1, rows+ 1):
            num = row + 3 * (col - 1)
            button = ParameterCircButton(rowRef * row, colRef1 * col + colRef2,
                                    dim, f"{num}", setParameter, num, "red4")
            app.setupButtons.append(button)

def makeSizeButtons(app, rows, width, height):
    posX = app.width * 1/4
    posY = app.height * 3/5
    for row in range(1, rows + 1):
        button = ParameterRectButton(posX * row, posY, app.width * width, 
                         app.height * height, f"{row}", setMapSize, row, "red4")
        app.setupButtons.append(button)


################################################################################

def makeButtonHub(app):
    buttonDims = 80
    buttonList = []
    x = app.tile.x
    y = app.tile.y
    unit = app.game.getUnit(x, y)

    posX1 = app.width * 16/20
    posY1 = app.height * 3/20
    posX2 = app.width * 37/40
    posY2 = app.height * 10/20
    posY3 = app.height * 17/20

    if unit != None and unit in app.game.currentPlayer.currentUnits:
        app.clickedUnit = unit
        if unit.canAct == False:
            pass
        else:
            if unit.canMove == True:
                moveUnitButton = CircleButton(posX1, posY1, buttonDims, 
                                                "Move\nUnit", moveUnit, "black")
                buttonList.append(moveUnitButton)
            attackUnitButton = CircleButton(posX2, posY1, buttonDims, 
                                           "Attack\n Unit", attackUnit, "black")
            buttonList.append(attackUnitButton)
            if (((isinstance(app.tile,City)) and (app.tile not in app.game.currentPlayer.currentCities)) 
                or isinstance(app.tile, Village)):
                captureCityButton = CircleButton(posX1, posY2, buttonDims, 
                                         "Capture\n City", captureCity, "black")
                buttonList.append(captureCityButton)
    if isinstance(app.tile, City):
        if (x,y) in app.game.unitsOnBoard:
            pass
        elif app.tile not in app.game.currentPlayer.currentCities:
            pass
        else:
            createUnitButton = CircleButton(posX2, posY2, buttonDims, 
                                           "Create\n Unit", createUnit, "black")
            buttonList.append(createUnitButton)
    value, tile = cityCheck(app)
    if value == True:
        app.targetTile = tile
        if tile.resource != None:
            harvestResourceButton = CircleButton(posX1, posY3, buttonDims, 
                          "Harvest\nResource\n  1⭐", harvestResource, "black")
            buttonList.append(harvestResourceButton)
        if isinstance(app.tile, Field):
            if app.tile.hasHouse == False:
                createHouseButton = CircleButton(posX2, posY3, buttonDims, 
                                   "Create\nHouse\n 2⭐", createHouse, "black")
                buttonList.append(createHouseButton)
    else:
        app.targetTile = None
    return buttonList


def cityCheck(app):
    x = app.tile.x
    y = app.tile.y
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            newX = x + dx
            newY = y + dy
            if newX < 0 or newX >= app.mapSize or newY < 0 or newY >= app.mapSize:
                continue
            targetTile = app.game.map[(newX, newY)]
            if isinstance(targetTile, City):
                if targetTile in app.game.currentPlayer.currentCities:
                    return True, targetTile
    return False, None

################################################################################

# Makes the pressable button hub for selecting a new unit
def makeUnitsHub(app):
    buttonList = []
    width = 90
    height = 150
    leftX = app.width*64/80
    upperY = app.height*5/20
    rightX = app.width*74/80
    lowerY = app.height*15/20
    
    warrior = Unit(-1,-1)
    createWarriorButton = RectangleButton(leftX, upperY, width, height, 
                       makeUnitText(warrior, "Warrior"), createWarrior, "black")
    buttonList.append(createWarriorButton)
    
    archer = Archer(-1, -1)
    createArcherButton = RectangleButton(rightX, upperY, width, height , 
                          makeUnitText(archer, "Archer"), createArcher, "black")
    buttonList.append(createArcherButton)
    
    rider = Rider(-1,-1)
    createRiderButton = RectangleButton(leftX, lowerY, width, height, 
                             makeUnitText(rider, "Rider"), createRider, "black")
    buttonList.append(createRiderButton)
    
    defender = Defender(-1,-1)
    createDefenderButton = RectangleButton(rightX, lowerY, width, height, 
                    makeUnitText(defender, "Defender"), createDefender, "black")
    buttonList.append(createDefenderButton)
    return buttonList

#Functions to create and place specific units
def createWarrior(app):
    if app.game.currentPlayer.currency >= Unit(-1,-1).cost:
        app.game.currentPlayer.currency -= Unit(-1,-1).cost
        player = app.game.currentPlayer
        city = app.tile
        newWarrior = Unit(city.x, city.y)
        changeUnit(player, app.game, city, newWarrior)
        city.canMakeUnits = False
    else:
        showTip(app, "Not Enough Stars")

def createArcher(app):
    if app.game.currentPlayer.currency >= Archer(-1,-1).cost:
        app.game.currentPlayer.currency -= Archer(-1,-1).cost
        player = app.game.currentPlayer
        city = app.tile
        newArcher = Archer(city.x, city.y)
        changeUnit(player, app.game, city, newArcher)
        city.canMakeUnits = False
    else:
        showTip(app, "Not Enough Stars")

    
def createRider(app):
    if app.game.currentPlayer.currency >= Rider(-1,-1).cost:
        app.game.currentPlayer.currency -= Rider(-1,-1).cost
        player = app.game.currentPlayer
        city = app.tile
        newRider = Rider(city.x, city.y)
        changeUnit(player, app.game, city, newRider)
        city.canMakeUnits = False
    else:
        showTip(app, "Not Enough Stars")


def createDefender(app):
    if app.game.currentPlayer.currency >= Defender(-1,-1).cost:
        app.game.currentPlayer.currency -= Defender(-1,-1).cost
        player = app.game.currentPlayer
        city = app.tile
        newDefender = Defender(city.x, city.y)
        changeUnit(player, app.game, city, newDefender)
        city.canMakeUnits = False
    else:
        showTip(app, "Not Enough Stars")

# Generates display text based off of unit
def makeUnitText(unit, name):
    return f"""Create
{name}

Cost:{unit.cost}⭐
Health:{unit.health}
Movement:{unit.movement}
Range:{unit.range}
Attack:{unit.attack}
Defense:{unit.defense}"""


