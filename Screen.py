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
    setupx0 = app.width * 1/10
    setupx1 = app.width * 9/10
    setupy0 = app.height * 1/10
    setupy1 = app.height * 9/10
    text1Y = app.height * 3/20
    text2Y = app.height * 11/15
    text3Y = app.height * 12/15
    text4Y = app.height * 13/15

    canvas.create_image(app.cx, app.cy, image = ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(setupx0, setupy0, setupx1, setupy1, fill = "sienna4")
    canvas.create_text(app.cx, text1Y, text = "Game Set-Up", 
                                    font = "FixedSys 40 bold", fill = textColor)
    canvas.create_text(app.cx,text2Y, text = f"{app.playerNum} Players Playing", 
                                         font = "FixedSys 18", fill = textColor)
    canvas.create_text(app.cx, text3Y, text = f"{app.mapText} Map Size Selected", 
                                         font = "FixedSys 18", fill = textColor)
    canvas.create_text(app.cx,text4Y, text = app.suggestionText, 
                                    font = "FixedSys 15 bold", fill = textColor)

def drawInPlayScreen(app, canvas):
    totalStarsPerTurn = 0
    for city in app.game.currentPlayer.currentCities:
        totalStarsPerTurn += city.starsPerTurn
    
    box1x0, box1x1 = app.width * 1/30, app.width * 7/30
    box1y0, box1y1 = app.height * 1/10, app.height * 9/10
    box2x0, box2x1 = app.width * 3/60, app.width * 13/60
    box2y0, box2y1 = app.height * 3/20, app.height * 17/20
    textcx = app.width * 4/30
    text1Y = app.height * 5/40
    text2Y = app.height * 7/40
    text3Y = app.height * 9/40
    text4Y = app.height * 45/160
    text5Y = app.height * 13/40
    textTitleY = app.height * 16/40
    textInfoY = app.height * 22/40


    canvas.create_image(app.cx, app.cy, image = ImageTk.PhotoImage(app.titleScreen))
    canvas.create_rectangle(box1x0, box1y0 , box1x1 , box1y1, fill = "sienna4")
    canvas.create_rectangle(box2x0, box2y0, box2x1, box2y1, fill = "bisque")

    canvas.create_text(textcx, text1Y, text = "Game Info", 
                               font = "FixedSys 30 bold", fill = "floral white")
    
    canvas.create_text(textcx, text2Y, text = "Current Player's Turn:", 
                                      font = "FixedSys 15 bold", fill = "black")
    
    canvas.create_text(textcx, text3Y, text = f"{app.game.currentPlayer}", 
                                            font = "FixedSys 20 bold", 
                                            fill = app.game.currentPlayer.color)
    
    canvas.create_text(textcx,text4Y, 
                        text = f"Currency:{app.game.currentPlayer.currency}⭐", 
                        font = "FixedSys 15 bold", fill = "gold2")
    
    canvas.create_text(textcx, text5Y, text = f"Stars Per Turn:{totalStarsPerTurn}", 
                                      font = "FixedSys 15 bold", fill = "black")
    
    if app.unit == app.targetTile == None:
        pass
    elif app.unit == None and app.targetTile != None: 
        canvas.create_text(textcx, textTitleY, 
                text = f"{app.targetTile}", font = "FixedSys 20 bold", 
                fill = app.targetTile.color)
        
        infoText = f"""* City Level: {app.targetTile.level}

* Resource Til
Level Up: {app.targetTile.popToNextLevel}

* Stars Per Turn: {app.targetTile.starsPerTurn}

* Can Make Units: {app.targetTile.canMakeUnits}"""
                
        canvas.create_text(textcx, textInfoY, text = infoText, 
                              font = "FixedSys 17", fill = "black")
    
    else:
        unitText = f"""*Position: {app.unit.x, app.unit.y}
*Health: {app.unit.health}
*Movement: {app.unit.movement}
*Range: {app.unit.range}
*Attack: {app.unit.attack}
*Defense: {app.unit.defense}
*Can Move: {app.unit.canMove}
*Can Act: {app.unit.canAct}"""
        
        canvas.create_text(textcx, textTitleY, text = f"{app.unit.color} {app.unit.title}", 
                               font = "FixedSys 20 bold", fill = app.unit.color)
        canvas.create_text(textcx, textInfoY, text = unitText, 
                                           font = "FixedSys 17", fill = "black")



def displayTip(app, canvas):
    popUpx0, popUpx1 = app.width * 6/20, app.width * 14/20
    popUpy0, popUpy1 = app.height * 8/20, app.height * 12/20
    canvas.create_rectangle(popUpx0, popUpy0, popUpx1, popUpy1, fill = "sienna4")
    canvas.create_text(app.cx, app.cy, text = f"{app.tip}", 
                                       font = "FixedSys 40 bold", fill = "gold")


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

# Retrieves row and col numbers based on mouse click, 
# from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCell(app, x, y): 
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
