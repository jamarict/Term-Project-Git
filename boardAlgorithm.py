from TilesClass import*
import random
################################################################################
#Board Generation

# main function that repeatedly tries to make a valid board
# A valid board is a board where none of the capitals have overlapping 3x3 regions
def makeBoard(app, playerNum, mapSize):
    newBoard = None
    while newBoard == None:
        oldBoard = dict() #Store Map as a dictionary with coordinate keys
        possibleMoves = list()
        currentCities = list()
        # Shrink range by 1 so no capitals spawn on outer edge of map
        for row in range(1, mapSize - 1):
            for col in range(1, mapSize -1):
                possibleMoves.append((row, col))
        # Set Total Possible Cities Based on Map Size
        if mapSize == 11:
            totalCities = 5
        elif mapSize == 15:
            totalCities = 9
        elif mapSize == 19:
            totalCities = 13
        # Backtracking Helper that adds capitals to board. Returns board and capital locations
        newBoard = makeCapitalsHelper(app, playerNum, totalCities, possibleMoves, 
                                      oldBoard, currentCities)
    board = newBoard[0]
    capitals = newBoard[1]
    for row in range(mapSize):
        for col in range(mapSize):
            key = (row, col)
            if key in board:
                continue
            else:
                newTile = tileSelector(app, row, col)
                board[key] = newTile
    return board, capitals

# recursive function that puts capitals and villages in random positions
def makeCapitalsHelper(app, playerNum, totalCities, possibleMoves, oldBoard, currentCities):
    # Base case when there's no more cities
    if totalCities == 0:
        return oldBoard, currentCities
    else:
        # Check through possible moves
        for i in range(len(possibleMoves)):
            currentLocation = random.choice(possibleMoves)
            currentLocationX, currentLocationY = currentLocation[0], currentLocation[1]
            # Legality Check
            if isLegalMove(currentLocationX, currentLocationY, currentCities):
                if playerNum > 0:
                    #Create Capital Tile for unaccounted Players
                    currentTile = Capital(currentLocationX, currentLocationY)
                    
                else:
                    #Create Empty Village Tile once all players have a capital
                    currentTile = Village(currentLocationX, currentLocationY)
                    currentTileImage1 = app.loadImage("images/VillageTile.png")
                    currentTileImage2 = app.scaleImage(currentTileImage1, 1/(app.mapSize * 265/700))
                    currentTile.image = currentTileImage2
                #Update Board and Remove Move
                oldBoard[(currentLocationX, currentLocationY)] = currentTile
                possibleMoves.remove(currentLocation)
                currentCities.append(currentTile)
                # Recursion
                result = makeCapitalsHelper(app, playerNum - 1, totalCities - 1, 
                                            possibleMoves, oldBoard, currentCities)
                if result != None:
                    return result
        return None

# Legality check that uses pythagorean theorem to estimate the distance between cities
# Distance must be above 4 to be considered legal.
def isLegalMove(cx, cy, currentCities):
    if len(currentCities) < 1:
        return True
    for item in currentCities: #Check each capital/village
        if int(((item.x - cx)**2 + (item.y-cy)**2)**0.5) <= 4:
            return False
    return True

# Random number generation to determine Tile Type
# Website to determine bounds:
# https://polytopia.fandom.com/wiki/Map_Generation
def tileSelector(app, x, y):
    tile = random.random()
    if (0 <= tile < .20):
        tile = Mountain(x,y)
        tileImage1 = app.loadImage("images/MountainTile.png")
        tileImage2 = app.scaleImage(tileImage1, 1/(app.mapSize * 470/700))
        tile.image = tileImage2
        return tile
    elif (.20 <= tile < .54):
        tile = Forest(x,y)
        tileImage1 = app.loadImage("images/ForestTile.png")
        tileImage2 = app.scaleImage(tileImage1, 1/(app.mapSize*467/700))
        tile.image = tileImage2
        return tile
    else:
        tile = Field(x,y)
        tileImage1 = app.loadImage("images/FieldTile.png")
        tileImage2 = app.scaleImage(tileImage1, 1/(app.mapSize*310/700) )
        tile.image = tileImage2
        return tile
    