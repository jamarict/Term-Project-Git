from cmu_112_graphics import *
from ButtonClass import *
from Screen import *
import time
################################################################################

def appStarted(app):
    #Image Info
    app.imageTitleScreen = app.loadImage("images/openBackground.jpeg")
    titleScale = 1600/433 
    app.titleScreen = app.scaleImage(app.imageTitleScreen, titleScale)
    app.imageOver = app.loadImage("images/FinalImage.jpg")
    scale = 7/8
    app.gameOverImage = app.scaleImage(app.imageOver, scale)
    app.mode = "titleScreenMode"
    app.margin = (app.width - app.height)/2

    #Positioning Info
    app.cx = app.width/2
    app.cy = app.height/2
    app.xScalar = (0.25, 0.5, 0.75, 1/11, 1/6, 10/12, 1/10, 9/10)
    app.yScalar = (11/14, 1/11, 2/15, 1/7, 3/5, 1/28, 5/24, 3/8, 7/24, 
                   1/10, 9/10, 3/20, 9/40, 19/40, 11/15, 12/15, 13/15)
    app.bigButtonDimensions = 70
    app.numButtonDimensions = 40
    app.endTurnDimensions = 50
    
    #Initial Buttons
    app.buttonPlayGame = CircleButton(app.width * app.xScalar[0], 
                                      app.height * app.yScalar[0], 
                                      app.bigButtonDimensions, "Play\nGame", 
                                      goToSetup, "red4")
    
    app.buttonHelp = CircleButton(app.width * app.xScalar[1], 
                                  app.height * app.yScalar[0], 
                                  app.bigButtonDimensions, "Help", 
                                  goToHelp, "Gold3")
    
    app.buttonSetting = CircleButton(app.width * app.xScalar[2], 
                                     app.height * app.yScalar[0], 
                                     app.bigButtonDimensions, "Settings", 
                                     goToSettings, "midnightblue")
    
    app.buttonTitle = CircleButton(app.width * app.xScalar[0], 
                                   app.height * app.yScalar[0], 
                                   app.bigButtonDimensions, "Back to\n Title", 
                                   goToTitle, "Black")

    app.buttonStartGame = CircleButton(app.width * app.xScalar[2], 
                                      app.height * app.yScalar[0], 
                                      app.bigButtonDimensions, 
                                      " Start \n Game", startGame, "green4")
    app.buttonEndTurn = CircleButton(app.width * 4/30, app.height * 23/30, app.endTurnDimensions, "End\nTurn", endTurn, "white")
    app.gameOverButton = RectangleButton(app.cx, app.height*7/8, 125, 50, "Back to Title", goToTitle, "White")


    
    #Set List-Based Buttons
    app.setupButtons = []
    for col in range(1,3):
        for row in range(1,4): # Player Number
            num = row + 3 * (col-1)
            app.setupButtons.append(ParameterCircButton(app.width * app.xScalar[0] * row, 
                                                        app.height * app.yScalar[2] * col + (app.height * app.yScalar[3]), 
                                                        app.numButtonDimensions, 
                                                        f"{num}", setParameter,
                                                        num, "red4"))
    for row in range(1,4): # Map Size
        app.setupButtons.append(ParameterRectButton(app.width * app.xScalar[0] * row, 
                                                    app.height * app.yScalar[4], 
                                                    app.width * app.xScalar
                                            [3], app.height * app.yScalar[5], 
                                                    f"{row}", setMapSize, row, "red4"))
    

    #Initial Game Information
    app.playerNum = 0
    app.mapSize = 0
    app.mapText = "No"
    app.suggestionText = ""
    app.tile = None
    app.buttonHub = []
    app.targetTile = None
    app.unit = None
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

    
# Help Screen   
def helpScreenMode_redrawAll(app, canvas):
    drawHelpScreen(app, canvas)
    app.buttonTitle.redraw(app, canvas)

def helpScreenMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)

    
# Settings Screen 
def settingsScreenMode_redrawAll(app, canvas):
    drawSettingsScreen(app, canvas)
    app.buttonTitle.redraw(app, canvas)

def settingsScreenMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)


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

# In-Game Screen
def inPlayScreenMode_redrawAll(app, canvas):
    drawInPlayScreen(app, canvas)
    app.buttonEndTurn.redraw(app, canvas)
    drawBoard(app, canvas)
    drawUnits(app, canvas)
    for button in app.buttonHub:
        button.redraw(app, canvas)
    displayTip(app, canvas)

def inPlayScreenMode_mousePressed(app, event):
    if app.buttonEndTurn.buttonPressed(app, event):
        app.buttonHub = []
        return
    if app.buttonHub != []:
        for button in app.buttonHub:
            if button.buttonPressed(app, event):
                return
    (row, col) = checkClick(app, event.x, event.y)
    app.tile = (app.game.getTile(row, col))
    if (row, col) in app.game.unitsOnBoard:
        app.unit = app.game.unitsOnBoard[(row, col)]
    else:
        app.unit = None
    if isinstance(app.tile, City):
        if app.tile in app.game.currentPlayer.currentCities:
            app.targetTile = app.tile
    if app.tile == None:
        app.buttonHub = []
    else:
        app.buttonHub = makeButtonHub(app)   

def inPlayScreenMode_timerFired(app):
    for player in app.game.playerList:
        if player.currentCities == []:
            app.game.playerList.remove(player)
    if len(app.game.playerList) == 1:
        app.mode = "GameOverMode"
    if app.displayTip == True:
        time.sleep(1.5)
        app.displayTip = False

def inPlayScreenMode_keyPressed(app, event):
    if event.key == "r":
        app.mode = "GameOverMode"

def unitMoveMode_redrawAll(app, canvas):
    drawInPlayScreen(app, canvas)
    app.buttonEndTurn.redraw(app, canvas)
    drawBoard(app, canvas)
    drawUnits(app, canvas)


def unitMoveMode_mousePressed(app, event):
    (row, col) = checkClick(app, event.x, event.y)
    app.tile = (app.game.getTile(row, col))
    if row == app.clickedUnit.x and col == app.clickedUnit.y:
        app.mode = "inPlayScreenMode"
        app.tip = "Invalid Move"
        app.displayTip = True
    elif (row,col) in app.game.unitsOnBoard:
        app.mode = "inPlayScreenMode"
        app.tip = "Space Occupied"
        app.displayTip = True
    elif (abs(app.clickedUnit.x - row) <= app.clickedUnit.movement and 
        abs(app.clickedUnit.y - col) <= app.clickedUnit.movement):
        del app.game.unitsOnBoard[(app.clickedUnit.x, app.clickedUnit.y)]
        app.clickedUnit.x = row
        app.clickedUnit.y = col
        app.game.unitsOnBoard[(row, col)] = app.clickedUnit
        app.clickedUnit.canMove = False
        app.clickedUnit.outline = "gray"
        app.mode = "inPlayScreenMode"
    else:
        app.mode = "inPlayScreenMode"
        app.tip = "Invalid Move"
        app.displayTip = True

def unitAttackMode_redrawAll(app, canvas):
    drawInPlayScreen(app, canvas)
    app.buttonEndTurn.redraw(app, canvas)
    drawBoard(app, canvas)
    drawUnits(app, canvas)

def unitAttackMode_mousePressed(app, event):
    (row, col) = checkClick(app, event.x, event.y)
    if (row, col) in app.game.unitsOnBoard and app.game.unitsOnBoard[(row, col)] not in app.game.currentPlayer.currentUnits:
        if (abs(app.clickedUnit.x - row) <= app.clickedUnit.range and
            abs(app.clickedUnit.y - col) <= app.clickedUnit.range):
            calculateDamage(app, app.clickedUnit, app.game.unitsOnBoard[(row, col)])
            app.mode = "inPlayScreenMode"
        else:
            app.tip = "Not In Range"
            app.displayTip = True
            app.mode = "inPlayScreenMode"
    else:
        app.tip = "Invalid Attack"
        app.displayTip = True
        app.mode = "inPlayScreenMode"

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

def GameOverMode_redrawAll(app, canvas):
    drawGameOver(app, canvas)
    if app.gameOverButton.redraw(app, canvas):
        appStarted(app)

def GameOverMode_mousePressed(app, event):
    app.gameOverButton.buttonPressed(app, event)
    



runApp(width = 1500, height = 700)
    