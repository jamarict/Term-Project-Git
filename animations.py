from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *
from PlayerClass import *
from NewConsoleTest import *


def appStarted(app):
    app.playerColors = ["navy", "yellow", "salmon", "red", "deep pink", "dark violet", "chocolate", 
                "maroon", "orchid", "slateblue"]
    app.board = createViableBoard(5, "small")
    app.margin = 50
    app.addSpace = (app.width - app.height)/2
    app.unitsOnBoard = {}
    app.selection = (-1, -1)


def getCellBounds(app, x, y):
    margin = app.margin
    addSpace = app.addSpace
    gridHeight = app.height - (2 * margin)
    cellHeight = gridHeight / len(app.board[0])
    x0 = (margin + x * cellHeight)+addSpace
    x1 = (margin + (x + 1) * cellHeight)+addSpace
    y0 = margin + y * cellHeight
    y1 = margin + (y + 1) * cellHeight
    return x0, y0, x1, y1

def getCell(app, x, y):
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridHeight = app.height - 2*app.margin
    cellHeight = gridHeight / len(app.board)
    row = int((y-app.margin)/cellHeight)
    col = int((x-(app.margin+app.addSpace))/cellHeight) 
    if col == 11:
        col = 10
    return (row, col)


def pointInGrid(app, x, y):
    return ((app.margin + app.addSpace <= x <= app.width - (app.margin + app.addSpace))
            and (app.margin <= y <= app.height - app.margin))

def keyPressed(app, event):
    if event.key == "r":
        app.board = createViableBoard(5, "small")


def drawCell(app, canvas, x, y, tile):
    x0, y0, x1, y1 = getCellBounds(app, x, y)
    canvas.create_rectangle(x0, y0, x1, y1, fill = tile.color)
    canvas.create_text((x0+x1)/2,(y0+y1)/2, text = f"({tile.x},{tile.y})")

def drawBoard(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            drawCell(app, canvas, row, col, app.board[col][row])

# def drawAllUnits(app, canvas):
#     for item in player1.currentUnits:
#         x0, y0, x1, y1 = getCellBounds(app, item.y, item.x)
#         item.redraw(app, canvas, x0, y0, x1, y1)


def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lightblue")
    drawBoard(app, canvas)
    # drawAllUnits(app, canvas)

def mousePressed(app, event):
    (row, col) = getCell(app, event.x, event.y) 
    currentTile = getTile(app.board,row, col)    


def playGame():
    runApp(width=1100, height=700)

playGame()


