from Screen import *
from GameClass import *
import time
################################################################################

def appStarted(app):
    #Image Info
    app.imageTitleScreen = app.loadImage("images/openBackground.jpeg")
    titleScale = app.width/app.imageTitleScreen.size[0] 
    app.titleScreen = app.scaleImage(app.imageTitleScreen, titleScale)
    app.gameOverImage = app.loadImage("images/FinalImage.jpg")
    
    #Positioning Info
    app.cx = app.width/2
    app.cy = app.height/2
    app.margin = (app.width - app.height)/2

    makeInitialButtons(app)
    
    #Initial Game Information
    app.mode = "titleScreenMode"
    app.playerNum = 0
    app.mapSize = 0
    app.mapText = "No"
    app.suggestionText = ""
    app.game = None
    app.buttonHub = []
    app.tile = None
    app.clickedUnit = None
    app.targetTile = None
    app.unit = None
    app.tip = ""
    app.displayTip = False


################################################################################   
#Screen Redraws and mousePressed

#Title Screen  
def titleScreenMode_redrawAll(app, canvas):
    drawTitle(app, canvas)
    app.buttonPlayGame.redraw(app, canvas)
    app.buttonHelp.redraw(app, canvas)
    app.buttonSetting.redraw(app, canvas)

def titleScreenMode_mousePressed(app, event):
    app.buttonPlayGame.buttonPressed(app, event)
    app.buttonHelp.buttonPressed(app, event)
    app.buttonSetting.buttonPressed(app, event)

################################################################################

# Help Screen   
def helpScreenMode_redrawAll(app, canvas):
    drawHelpScreen(app, canvas)
    app.buttonTitle.redraw(app, canvas)

def helpScreenMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)

################################################################################

# Settings Screen 
def settingsScreenMode_redrawAll(app, canvas):
    drawSettingsScreen(app, canvas)
    app.buttonTitle.redraw(app, canvas)

def settingsScreenMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)

################################################################################

# Game Setup Screen
def setupMode_redrawAll(app, canvas):
    drawSetupScreen(app, canvas)
    app.buttonTitle.redraw(app, canvas)
    for button in app.setupButtons:
        button.redraw(app, canvas) 
    app.buttonStartGame.redraw(app, canvas)
  
def setupMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)
    for button in app.setupButtons:
        button.buttonPressed(app, event)
    app.buttonStartGame.buttonPressed(app, event)

################################################################################

# In-Game Screen
def inPlayScreenMode_redrawAll(app, canvas):
    drawInPlayScreen(app, canvas)
    app.buttonEndTurn.redraw(app, canvas)
    drawBoard(app, canvas)
    drawUnits(app, canvas)
    for button in app.buttonHub:
        button.redraw(app, canvas)
    if app.displayTip:
        displayTip(app, canvas)

def inPlayScreenMode_mousePressed(app, event):
    if app.buttonEndTurn.buttonPressed(app, event): # End turn takes priority
        app.buttonHub = []
        return
    if app.buttonHub != []: # Check relevant buttons on screen
        if checkButtons(app, event) == True:
            return
    # Get Unit and Tile from click
    (row, col) = checkClick(app, event.x, event.y)
    app.tile = (app.game.getTile(row, col))
    app.unit = (app.game.getUnit(row, col))
    showCity(app)
    # If no tile is clicked on, show no buttons. Otherwise, show relevant
    # buttons for specific tile
    if app.tile == None:
        app.buttonHub = []
    else:
        app.buttonHub = makeButtonHub(app)   

# Sleep From
# https://www.bitdegree.org/learn/python-time
def inPlayScreenMode_timerFired(app):
    app.timerDelay = 1000
    checkPlayers(app)
    checkGameOver(app)
    if app.displayTip == True:
        time.sleep(1)
        app.displayTip = False

################################################################################

#Unit Movement Screen
def unitMoveMode_redrawAll(app, canvas):
    drawInPlayScreen(app, canvas)
    app.buttonEndTurn.redraw(app, canvas)
    drawBoard(app, canvas)
    drawUnits(app, canvas)

def unitMoveMode_mousePressed(app, event):
    (row, col) = checkClick(app, event.x, event.y)
    app.tile = (app.game.getTile(row, col))
    player = app.clickedUnit
    moveUnit(app, player, row, col)

################################################################################

# Unit Attack Screen
def unitAttackMode_redrawAll(app, canvas):
    drawInPlayScreen(app, canvas)
    app.buttonEndTurn.redraw(app, canvas)
    drawBoard(app, canvas)
    drawUnits(app, canvas)

def unitAttackMode_mousePressed(app, event):
    (row, col) = checkClick(app, event.x, event.y)
    playerUnit = app.clickedUnit
    enemyUnit = app.game.getUnit(row, col)
    runCombat(app, playerUnit, enemyUnit)

################################################################################

# Unit Creation Screen
def createUnitsMode_redrawAll(app, canvas):
    drawInPlayScreen(app, canvas)
    app.buttonEndTurn.redraw(app, canvas)
    drawBoard(app, canvas)
    drawUnits(app, canvas)
    for button in app.buttonHub:
        button.redraw(app, canvas)

def createUnitsMode_mousePressed(app, event):
    for button in app.buttonHub:
        button.buttonPressed(app, event)
    app.buttonHub = []
    app.mode = "inPlayScreenMode"

################################################################################

#Game Over Screen
def GameOverMode_redrawAll(app, canvas):
    drawGameOver(app, canvas)
    app.gameOverButton.redraw(app, canvas)
    
def GameOverMode_mousePressed(app, event):
    app.gameOverButton.buttonPressed(app, event)
    
runApp(width = 1500, height = 700)
    