from cmu_112_graphics import *
from ButtonClass import *


def drawTitle(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width/6, app.height*(5/24), app.width*(10/12), app.height*(9/24), fill = "sienna4")
    canvas.create_text(app.width/2, app.height*(7/24), text = "Collect & Conquer:112", font = "FixedSys 35 bold italic", fill ="peachpuff")

def drawHelpScreen(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width*(1/10), app.height*(1/10), app.width*(9/10), app.height*(9/10), fill = "sienna4")




       
def appStarted(app):
    #Title Screen images
    app.imageTitleScreen = app.loadImage("images/openBackground.jpeg")
    titleScale = 1200/433 
    app.titleScreen = app.scaleImage(app.imageTitleScreen, titleScale)
    app.mode = "titleScreenMode"


    #button Info
    app.yPos = app.height*(11/14)
    app.dims = 70
    app.buttonPlayGame = CircleButton(app.width/4, app.yPos, app.dims, "Play\nGame", backToMain)
    app.buttonHelp = CircleButton(app.width*(2/4), app.yPos, app.dims, "Help", goToHelp)
    app.buttonSetting = CircleButton(app.width*(3/4), app.yPos, app.dims, "Settings", goToSettings)
    app.buttonTitle = CircleButton(app.width*(2/4), app.yPos, app.dims, "Back to\n Title", goToTitle)


    
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
runApp(width =1100, height = 700)