from cmu_112_graphics import *
from ButtonClass import *
from screens import *



def appStarted(app):
    #Title Screen images
    app.imageTitleScreen = app.loadImage("images/openBackground.jpeg")
    titleScale = 1200/433 
    app.titleScreen = app.scaleImage(app.imageTitleScreen, titleScale)
    app.mode = "titleScreenMode"


    #button Info
    app.cx = app.width/2
    app.cy = app.height/2
    app.yPos = app.height*(11/14)
    app.bigButtonDims = 70
    app.numButtonDims = 40
    app.buttonPlayGame = CircleButton(app.width/4, app.yPos, app.bigButtonDims, "Play\nGame", backToMain, "red4")
    app.buttonHelp = CircleButton(app.width*(2/4), app.yPos, app.bigButtonDims, "Help", goToHelp, "Gold3")
    app.buttonSetting = CircleButton(app.width*(3/4), app.yPos, app.bigButtonDims, "Settings", goToSettings, "midnightblue")
    app.buttonTitle = CircleButton(app.width*(1/4), app.yPos, app.bigButtonDims, "Back to\n Title", goToTitle, "Black")
    app.playerNum = "No Players Set"
    app.mapSize = "No Size Selected"
    app.setupButtons = []
    for col in range(1,3):
        for row in range(1,4):
            num = row + 3 * (col-1)
            app.setupButtons.append(ParameterCircButton(app.width*(3/12)*(row), app.height*(2/15)*(col)+100, app.numButtonDims, f"{num}", setParameter, num, "red4"))
    for row in range(1,4):
        app.setupButtons.append(ParameterRectButton(app.width*(3/12)*(row), app.height*(9/15), 100, 25, f"{row}", setMapSize, row, "red4"))

 
def titleScreenMode_redrawAll(app, canvas):
    drawTitle(app, canvas)
    app.buttonPlayGame.redraw(app, canvas)
    app.buttonHelp.redraw(app, canvas)
    app.buttonSetting.redraw(app, canvas)

def titleScreenMode_mousePressed(app, event):
    app.buttonPlayGame.buttonPressed(app, event)
    app.buttonHelp.buttonPressed(app, event)
    app.buttonSetting.buttonPressed(app, event)

    
def helpScreenMode_redrawAll(app, canvas):
    drawHelpScreen(app, canvas)
    app.buttonTitle.redraw(app, canvas)

def helpScreenMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)

def settingsScreenMode_redrawAll(app, canvas):
    drawSettingsScreen(app, canvas)
    app.buttonTitle.redraw(app, canvas)

def settingsScreenMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)

def setupMode_redrawAll(app, canvas):
    drawSetupScreen(app, canvas)
    app.buttonTitle.redraw(app, canvas)
    for button in app.setupButtons:
        button.redraw(app, canvas)
        print(button.numSet)

        
def setupMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)
    for button in app.setupButtons:
        button.buttonPressed(app, event)
    

    
runApp(width =1100, height = 700)