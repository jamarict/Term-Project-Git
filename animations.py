from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *
from PlayerClass import *
from NewConsoleTest import *
from screens import *

# Initialize player colors, current players, and margins
# Colors from http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
def appStarted(app):
    app.board, app.players = createViableBoard(5, "small")
    app.colors = ["navy", "yellow", "salmon", "red", "deep pink", "dark violet", "chocolate", 
                "maroon", "orchid", "slateblue"]
    for player in app.players:
        index = random.randint(0,len(app.colors)-1)
        player.color = app.colors.pop(index)
        player.currentCities[0].color = player.color
    currentPlayer = 0
    app.margin = 50
    app.addSpace = (app.width - app.height)/2
    app.unitsOnBoard = {}
    app.selection = (-1, -1)

# returns cell coordinates for drawing grid and units
# From https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
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

# returns row and col number based on mousepress coordinates
# From https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
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
# reutns True/False depending on if a point is on a grid
def pointInGrid(app, x, y):
    return ((app.margin + app.addSpace <= x <= app.width - (app.margin + app.addSpace))
            and (app.margin <= y <= app.height - app.margin))


# draws cell based on row, col, and tile color
def drawCell(app, canvas, x, y, tile):
    x0, y0, x1, y1 = getCellBounds(app, x, y)
    canvas.create_rectangle(x0, y0, x1, y1, fill = tile.color)
    canvas.create_text((x0+x1)/2,(y0+y1)/2, text = f"({tile.x},{tile.y})")

# Loops through board to draw board
def drawBoard(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            drawCell(app, canvas, row, col, app.board[col][row])

# draws units based on current units for each player
def drawAllUnits(app, canvas):
    for player in app.players:
        for unit in player.currentUnits:
            x0, y0, x1, y1 = getCellBounds(app, unit.y, unit.x)
            unit.redraw(app, canvas, x0, y0, x1, y1)

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lightblue")
    drawBoard(app, canvas)
    drawAllUnits(app, canvas)


def mousePressed(app, event):
    (row, col) = getCell(app, event.x, event.y) 
    currentTile = getTile(app.board,row, col) 

def keyPressed(app, event):
    if event.key == "r":
        app.board, app.players = createViableBoard(5, "small")
    elif event.key == "b":
        app.mode = "titleScreenMode"

def playGame():
    runApp(width=1100, height=700)

playGame()


 