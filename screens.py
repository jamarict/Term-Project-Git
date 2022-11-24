from cmu_112_graphics import *

def titleScreenMode_redrawAll(app, canvas):
    app.image = app.loadImage("openBackground.jpeg")
    canvas.create_text(app.width/2, app.height/2, text = "Hello World")

def appStarted(app):
    app.mode = "titleScreenMode"

runApp(width =1100, height = 700)