from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *
from tempBoard import tempBoard

def getCellBounds(app, x, y):
    margin = 100
    gridHeight = app.height - (2 * margin)
    cellHeight = gridHeight / len(tempBoard)
    x0 = margin + x * cellHeight
    y0 = margin + y * cellHeight
    x1 = margin + (x + 1) * cellHeight
    y1 = margin + (y + 1) * cellHeight
    return x0, y0, x1, y1

def drawCell(app, canvas, x, y, tile):
    x0, y0, x1, y1 = getCellBounds(app, x, y)
    canvas.create_rectangle(x0, y0, x1, y1, fill = tile.color)


def drawBoard(app, canvas):
    for row in range(len(tempBoard)):
        for col in range(len(tempBoard[0])):
            drawCell(app, canvas, row, col, tempBoard[row][col])


def redrawAll(app, canvas):
    canvas.create_rectangle(0,0, app.width, app.height, fill = "lightblue")
    drawBoard(app, canvas)



runApp(width=1100, height=700)