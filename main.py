from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *

capital1 = Capital(0,0)
forest1 = Forest(0,1)
field1 = Field(1,0)
mountain1 = Mountain(1,1)
board = [[capital1, forest1],
         [field1, mountain1]]


def getCellBounds(app, x, y):
    margin = 500
    gridHeight = app.height - 2 * margin
    cellHeight = gridHeight / len(board[0])
    x0 = margin + x * cellHeight
    y0 = margin + y * cellHeight
    x1 = margin + (x + 1) * cellHeight
    y1 = margin + (y + 1) * cellHeight
    return x0, y0, x1, y1

def drawCell(app, canvas, x, y, tile):
    x0, y0, x1, y1 = getCellBounds(app, x, y)
    canvas.create_rectangle(x0, y0, x1, y1, fill = tile.color)


def drawBoard(app, canvas):
    for row in range(len(board)):
        for col in range(len(board[0])):
            drawCell(app, canvas, row, col, board[row][col])


def redrawAll(app, canvas):
    canvas.create_rectangle(0,0, app.width, app.height, fill = "lightblue")
    drawBoard(app, canvas)



runApp(width=1100, height=700)