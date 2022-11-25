from cmu_112_graphics import *
from ButtonClass import *


def drawTitle(app, canvas):
    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width/6, app.height*(5/24), app.width*(10/12), app.height*(9/24), fill = "sienna4")
    canvas.create_text(app.cx, app.height*(7/24), text = "Collect & Conquer:112", font = "FixedSys 40 bold italic", fill ="peachpuff")

def drawHelpScreen(app, canvas):
    textColor = "Gold3"
    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width*(1/10), app.height*(1/10), app.width*(9/10), app.height*(9/10), fill = "sienna4")
    canvas.create_text(app.cx, app.height*(3/20), text = "How To Play", font = "FixedSys 40 bold", fill = textColor)
    canvas.create_text(app.cx, app.height*(9/40), text = "Welcome to Collect & Conquer:112", font = "FixedSys 20 bold", fill = textColor)
    canvas.create_text(app.cx, app.height*(19/40), text = helpText, font = "FixedSys 15 bold", fill = textColor)

helpText = """In this game, you'll work to become the dominate civilization in the land.
After designating the number of players, a random map with capitals will
be generated. Each player starts with their specified capital and one basic
unit to move around with. Each player starts with 5 stars, which acts as 
currency to do in-game actions. 

With stars, you can do the following:
*Create new and specialized units to aid in combat
*Collect resources surrounding your cities

The interface is entirely mouse-based. To move units, click on your unit, 
then click on a viable location in their range. To attack units, click on your
unit, then click on an enemy unit within attack range. To collect resources,
click on a surrounding city tile with resources, then click the "Collect 
Resource" confirmation button
"""

def drawSettingsScreen(app, canvas):
    textColor = "midnightblue"
    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width*(1/10), app.height*(1/10), app.width*(9/10), app.height*(9/10), fill = "sienna4")
    canvas.create_text(app.cx,app.height*(3/20), text = "Settings", font = "FixedSys 40 bold", fill = textColor)
    canvas.create_text(app.cx,app.cy, text = "Feature Coming Soon!", font = "FixedSys 40 bold", fill = textColor)

def drawSetupScreen(app, canvas):
    textColor = "red4"
    canvas.create_image(app.cx, app.cy, image = ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width*(1/10), app.height*(1/10), app.width*(9/10), app.height*(9/10), fill = "sienna4")
    canvas.create_text(app.cx,app.height*(3/20), text = "Game Set-Up", font = "FixedSys 40 bold", fill = textColor)


