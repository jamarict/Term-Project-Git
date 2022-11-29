from cmu_112_graphics import *
from ButtonClass import *
from Screen import *
################################################################################

def appStarted(app):
    #Image Info
    app.imageTitleScreen = app.loadImage("images/openBackground.jpeg")
    titleScale = 1600/433 
    app.titleScreen = app.scaleImage(app.imageTitleScreen, titleScale)
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
    drawBoard(app, canvas)
    drawUnits(app, canvas)
    for button in app.buttonHub:
        button.redraw(app, canvas)

def inPlayScreenMode_mousePressed(app, event):
    if app.buttonHub != []:
        for button in app.buttonHub:
            if button.buttonPressed(app, event):
                app.buttonHub = []
                return
    (row, col) = checkClick(app, event.x, event.y)
    app.tile = (app.game.getTile(row, col))
    if app.tile == None:
        app.buttonHub = []
    else:
        app.buttonHub = makeButtonHub(app)

def inPlayScreenMode_keyPressed(app, event):
    if event.key == "r":
        x = Unit(0,0)
        x.canAct = True
        app.game.currentPlayer.currentUnits.append(x)
        app.game.unitsOnBoard[(0,0)] = x
        y = Village(0,0)
        app.game.playerList[1].addCity(app.game, y)
        app.game.map[(0,0)] = y
    if event.key == "p":
        print(app.game.currentPlayer.currency)
        for city in app.game.currentPlayer.currentCities:
            print(city, city.level)
            print(city, city.popToNextLevel)
            print(city, city.starsPerTurn)
runApp(width = 1500, height = 700)
    