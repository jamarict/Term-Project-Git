from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *
from tempBoard import *

def appStarted(app):
    unit1 = Unit(5,3)
    unit2 = Unit(9,10)
    app.unitsOnBoard = [unit1, unit2]


def getCellBounds(app, x, y):
    margin = 100
    gridHeight = app.height - (2 * margin)
    cellHeight = gridHeight / len(tempBoard[0])
    x0 = margin + x * cellHeight
    x1 = margin + (x + 1) * cellHeight
    y0 = margin + y * cellHeight
    y1 = margin + (y + 1) * cellHeight
    return x0, y0, x1, y1
    
def drawCell(app, canvas, x, y, tile):
    x0, y0, x1, y1 = getCellBounds(app, x, y)
    canvas.create_rectangle(x0, y0, x1, y1, fill = tile.color)
    canvas.create_text((x0+x1)/2,(y0+y1)/2, text = f"({tile.x},{tile.y})")

def drawBoard(app, canvas):
    for row in range(len(tempBoard)):
        for col in range(len(tempBoard[0])):
            drawCell(app, canvas, row, col, tempBoard[col][row])

def drawUnit(app, canvas, item):
    x0, y0, x1, y1 = getCellBounds(app, item.y, item.x)
    r = 5
    canvas.create_oval(x0+r, y0+r,x1-r, y1-r, fill = item.color)

def drawAllUnits(app, canvas):
    for item in app.unitsOnBoard:
        drawUnit(app, canvas, item)

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lightblue")
    drawBoard(app, canvas)
    drawAllUnits(app, canvas)

runApp(width=1100, height=700)
