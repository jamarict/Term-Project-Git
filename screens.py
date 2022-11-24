from cmu_112_graphics import *
from ButtonClass import *
        
            

def appStarted(app):
    #Title Screen images
    app.imageTitleScreen = app.loadImage("images/openBackground.jpeg")
    titleScale = 1200/433 
    app.titleScreen = app.scaleImage(app.imageTitleScreen, titleScale)
    app.yPos = app.height*(11/14)
    app.dims = 50
    app.button1 = CircleButton(app.width/2, app.yPos, app.dims, "Switch to Main", backToMain)
    app.button2 = RectangleButton(app.width/2, app.yPos, app.dims, app.dims, "Switch to Title", goToTitle)
    app.mode = "titleScreenMode"


def redrawAll(app, canvas):
    app.button2.redraw(app, canvas)
     

def mousePressed(app, event):
    app.button2.buttonPressed(app, event)
    

def titleScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width/4, app.height*(1/6), app.width*3/4, app.height*(5/12), fill = "sienna4")
    app.button1.redraw(app, canvas)

def titleScreenMode_mousePressed(app, event):
    app.button1.buttonPressed(app, event)

runApp(width =1100, height = 700)