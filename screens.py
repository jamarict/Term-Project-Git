from cmu_112_graphics import *
from ButtonClass import *
             
def appStarted(app):
    #Title Screen images
    app.imageTitleScreen = app.loadImage("images/openBackground.jpeg")
    titleScale = 1200/433 
    app.titleScreen = app.scaleImage(app.imageTitleScreen, titleScale)
    app.mode = "titleScreenMode"

    #button Info
    app.yPos = app.height*(11/14)
    app.dims = 50
    app.button1 = CircleButton(app.width/2, app.yPos, app.dims, "Switch to Main", backToMain)
    app.button2 = RectangleButton(app.width/2, app.yPos, app.dims, app.dims, "Switch to Title", goToTitle)


def redrawAll(app, canvas):
    app.button2.redraw(app, canvas)
     
def mousePressed(app, event):
    app.button2.buttonPressed(app, event)
    
def titleScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width/6, app.height*(3/12), app.width*(10/12), app.height*(4/12), fill = "sienna4")
    canvas.create_text(app.width/2, app.height*(7/24), text = "Collect & Conquer: 112", font = "FixedSys 35  italic", fill = "orange red")
    app.button1.redraw(app, canvas)

def titleScreenMode_mousePressed(app, event):
    app.button1.buttonPressed(app, event)

runApp(width =1100, height = 700)