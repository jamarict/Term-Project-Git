from ButtonClass import *
from cmu_112_graphics import *
################################################################################

#In-Game Texts and Screens
def drawTitle(app, canvas):
    titlex0 = app.width * 1/6
    titlex1 = app.width  * 10/12
    titley0 = app.height * 5/24
    titley1 = app.height * 3/8
    textY = app.height * 7/24

    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(titlex0, titley0, titlex1, titley1,fill = "sienna4")
    canvas.create_text(app.cx, textY, text = "Collect & Conquer:112", 
                            font = "FixedSys 40 bold italic", fill ="peachpuff")

    
def drawHelpScreen(app, canvas):
    helpx0 = app.width * 1/10
    helpx1 = app.width * 9/10
    helpy0 = app.height * 1/10
    helpy1 = app.height * 9/10
    textColor = "Gold3"
    titleTextY = app.height * 3/20

    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(helpx0, helpy0, helpx1 ,helpy1, fill = "sienna4")
    canvas.create_text(app.cx, titleTextY, text = "How To Play", 
                                    font = "FixedSys 40 bold", fill = textColor)

def drawSettingsScreen(app, canvas):
    settingx0 = app.width * 1/10
    settingx1 = app.width * 9/10
    settingy0 = app.height * 1/10
    settingy1 = app.height * 9/10
    textColor = "midnightblue"
    titleTextY = app.height * 3/20

    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(settingx0, settingy0, settingx1, settingy1,
                                                               fill = "sienna4")
    canvas.create_text(app.cx, titleTextY, text = "Settings",
                                    font = "FixedSys 40 bold", fill = textColor)
    canvas.create_text(app.cx, app.cy, text = "Features Coming Soon!", 
                       font = "FixedSys 40 bold", fill = textColor)

def drawGameOver(app, canvas):
    box1x0, box1x1 = app.width * 1/4, app.width * 3/4
    box1y0, box1y1 = app.height * 1/4, app.height * 3/4
    box2x0, box2x1 = app.width * 9/32, app.width * 23/32
    box2y0, box2y1 = app.height * 9/32, app.height * 23/32
    text1Y = app.height * 11/32
    text2Y = app.height * 1/2
    text3Y = app.height * 21/32
    
    canvas.create_image(app.cx, app.cy, image = ImageTk.PhotoImage(app.gameOverImage))
    canvas.create_rectangle(box1x0, box1y0, box1x1, box1y1, fill = "sienna4")
    canvas.create_rectangle(box2x0, box2y0, box2x1, box2y1, fill = "bisque3")
    
    canvas.create_text(app.cx, text1Y, text = "Congratulations", fill = "gold", 
                                                      font = "FixedSys 60 bold")
    canvas.create_text(app.cx, text2Y, 
                        text = f"  {app.game.currentPlayer} Is\nThe Glorious Victor", 
                        fill = f"{app.game.currentPlayer.color}", 
                        font = "FixedSys 40 bold")
    canvas.create_text(app.cx, text3Y, text = f"Reign With Wisdom", 
                        fill = f"{app.game.currentPlayer.color}", 
                        font = "FixedSys 40 bold italic")

    

def drawSetupScreen(app, canvas): # Update Screen with user input to show pre-game conditions
    textColor = "red4"
    canvas.create_image(app.cx, app.cy, image = ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width * app.xScalar[6],
                            app.height * app.yScalar[9], app.width * app.xScalar[7], 
                            app.height * app.yScalar[10], fill = "sienna4")
    canvas.create_text(app.cx,app.height * app.yScalar[11], text = "Game Set-Up", 
                       font = "FixedSys 40 bold", fill = textColor)
    canvas.create_text(app.cx, app.height * app.yScalar[14], 
                       text = f"{app.playerNum} Players Playing", 
                       font = "FixedSys 18", fill = textColor)
    canvas.create_text(app.cx, app.height * app.yScalar[15], 
                       text = f"{app.mapText} Map Size Selected", 
                       font = "FixedSys 18", fill = textColor)
    canvas.create_text(app.cx, app.height * app.yScalar[16], 
                       text = app.suggestionText, font = "FixedSys 15 bold", 
                       fill = textColor)

def drawInPlayScreen(app, canvas):
    totalStarsPerTurn = 0
    for city in app.game.currentPlayer.currentCities:
        totalStarsPerTurn += city.starsPerTurn
    
    
    canvas.create_image(app.cx, app.cy, image = ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(app.width * 1/30, app.height * 1/10, app.width * 7/30, app.height * 9/10, fill = "sienna4")
    canvas.create_rectangle(app.width * 3/60, app.height * 3/20, app.width * 13/60, app.height * 17/20, fill = "bisque")
    canvas.create_text(app.width * 4/30, app.height * 5/40, text = "Game Info", font = "FixedSys 30 bold", fill = "floral white")
    canvas.create_text(app.width * 4/30, app.height * 7/40, text = "Current Player's Turn:", font = "FixedSys 15 bold", fill = "black")
    canvas.create_text(app.width * 4/30, app.height * 9/40, text = f"{app.game.currentPlayer}", font = "FixedSys 20 bold", fill = app.game.currentPlayer.color)
    canvas.create_text(app.width * 4/30, app.height * 45/160, text = f"Currency:{app.game.currentPlayer.currency}⭐", font = "FixedSys 15 bold", fill = "gold2")
    canvas.create_text(app.width * 4/30, app.height * 13/40, text = f"Stars Per Turn:{totalStarsPerTurn}", font = "FixedSys 15 bold", fill = "black")
    if app.unit == app.targetTile == None:
        pass
    elif app.unit == None and app.targetTile != None: 
        canvas.create_text(app.width * 4/30, app.height * 16/40, text = f"{app.targetTile}", font = "FixedSys 20 bold", fill = "black")
        infoText = f"""* City Level: {app.targetTile.level}\n\n* Resource Til\n  Level Up: {app.targetTile.popToNextLevel}
            \n* Stars Per Turn: {app.targetTile.starsPerTurn}\n\n* Can Make Units: {app.targetTile.canMakeUnits}"""
        canvas.create_text(app.width * 4/30, app.height * 22/40, text = infoText, font = "FixedSys 17", fill = "black")
    else:
        unitText = f"""*Position: {app.unit.x, app.unit.y}\n*Health: {app.unit.health}\n*Movement: {app.unit.movement}\n*Range: {app.unit.range}
*Attack: {app.unit.attack}\n*Defense: {app.unit.defense}\n*Can Move: {app.unit.canMove}\n*Can Act: {app.unit.canAct}"""
        canvas.create_text(app.width * 4/30, app.height * 16/40, text = f"{app.unit.color} {app.unit.title}", font = "FixedSys 20 bold", fill = app.unit.color)
        canvas.create_text(app.width * 4/30, app.height * 22/40, text = unitText, font = "FixedSys 17", fill = "black")


################################################################################

def drawBoard(app, canvas): # Draws game board, from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    for x in range(app.mapSize):
        for y in range(app.mapSize):
            drawCell(app, canvas, x, y, app.game.map[(y,x)])
            
def drawCell(app, canvas, x, y, tile): # Draws individual cell based on bounds, from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    x0, y0, x1, y1 = getCellBounds(app, x, y)
    tile.redraw(app, canvas, x0, y0, x1, y1)

def drawUnits(app, canvas):
    for item in app.game.unitsOnBoard:
        (y, x) = item
        drawUnit(app, canvas, x, y, app.game.unitsOnBoard[item])

def drawUnit(app, canvas, x, y, unit):
    x0, y0, x1, y1 = getCellBounds(app, x, y)
    unit.redraw(app, canvas, x0, y0, x1, y1)

def getCellBounds(app, x, y): # Finds cell bounds for drawing, from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    gridLength = app.height
    cellLength = gridLength / app.mapSize
    x0 = app.margin + (x * cellLength)
    y0 = y * cellLength
    x1 = app.margin + (x + 1) * cellLength
    y1 = (y + 1) * cellLength
    return x0, y0, x1, y1
    
def getCell(app, x, y): # Retrieves row and col numbers based on mouse click, from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridLength = app.height
    cellLength = gridLength / app.mapSize
    row = int(y / cellLength)
    col = int((x - app.margin) / cellLength) 
    if col == app.mapSize:
        col -= 1
    return (row, col)

def pointInGrid(app, x, y): # Returns true of mouse click is inside board, from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    return (app.margin <= x <= app.width - app.margin) and (0 <= y <= app.height)

def checkClick(app, mouseX, mouseY): # Verifies mouse click on screen
    (row, col) = getCell(app, mouseX, mouseY)
    return (row, col)

################################################################################

def makeButtonHub(app):
    buttonDims = 80
    buttonList = []
    x = app.tile.x
    y = app.tile.y
    if (x,y) in app.game.unitsOnBoard and app.game.unitsOnBoard[(x, y)] in app.game.currentPlayer.currentUnits:
        app.clickedUnit = app.game.unitsOnBoard[(x, y)]
        if app.clickedUnit.canAct == False:
            pass
        else:
            if app.clickedUnit.canMove == True:
                moveUnitButton = CircleButton(app.width * 16/20, app.height * 3/20, buttonDims, "Move\nUnit", moveUnit, "black")
                buttonList.append(moveUnitButton)
            attackUnitButton = CircleButton(app.width * 37/40, app.height * 3/20, buttonDims, "Attack\n Unit", attackUnit, "black")
            buttonList.append(attackUnitButton)
            if isinstance(app.tile, Village) or ((isinstance(app.tile,City)) and (app.tile not in app.game.currentPlayer.currentCities)):
                captureCityButton = CircleButton(app.width * 16/20, app.height * 10/20, buttonDims, "Capture\n City", captureCity, "black")
                buttonList.append(captureCityButton)
    if isinstance(app.tile, City):
        if (x,y) in app.game.unitsOnBoard:
            pass
        elif app.tile not in app.game.currentPlayer.currentCities:
            pass
        else:
            createUnitButton = CircleButton(app.width * 37/40, app.height * 10/20, buttonDims, "Create\n Unit", createUnit, "black")
            buttonList.append(createUnitButton)
    value, tile = cityCheck(app)
    if value == True:
        app.targetTile = tile
        if app.tile.resource != None:
            harvestResourceButton = CircleButton(app.width * 16/20, app.height * 17/20, buttonDims, "Harvest\nResource\n  1⭐", harvestResource, "black")
            buttonList.append(harvestResourceButton)
        if isinstance(app.tile, Field):
            if app.tile.hasHouse == False:
                createHouseButton = CircleButton(app.width * 37/40, app.height * 17/20, buttonDims, "Create\nHouse\n 2⭐", createHouse, "black")
                buttonList.append(createHouseButton)
    else:
        app.targetTile = None
    return buttonList


def cityCheck(app):
    x = app.tile.x
    y = app.tile.y
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            newX = x + dx
            newY = y + dy
            if newX < 0 or newX >= app.mapSize or newY < 0 or newY >= app.mapSize:
                continue
            targetTile = app.game.map[(newX, newY)]
            if isinstance(targetTile, City):
                if targetTile in app.game.currentPlayer.currentCities:
                    return True, targetTile
    return False, None



def displayTip(app, canvas):
    canvas.create_rectangle(app.width * 6/20, app.height * 8/20, app.width * 14/20, app.height * 12/20, fill = "sienna4")
    canvas.create_text(app.cx, app.cy, text = f"{app.tip}", font = "FixedSys 40 bold", fill = "gold")