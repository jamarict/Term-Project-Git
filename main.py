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
    app.dims = 70
    app.buttonPlayGame = CircleButton(app.width/4, app.yPos, app.dims, "Play\nGame", backToMain, "red4")
    app.buttonHelp = CircleButton(app.width*(2/4), app.yPos, app.dims, "Help", goToHelp, "Gold3")
    app.buttonSetting = CircleButton(app.width*(3/4), app.yPos, app.dims, "Settings", goToSettings, "midnightblue")
    app.buttonTitle = CircleButton(app.width*(2/4), app.yPos, app.dims, "Back to\n Title", goToTitle, "Black")


    
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

def setupMode_mousePressed(app, event):
    app.buttonTitle.buttonPressed(app, event)

    
runApp(width =1100, height = 700)