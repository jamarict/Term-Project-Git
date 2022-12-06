from TilesClass import *
################################################################################
#Board Generation

# Main function that repeatedly tries to make a valid board, where none of the 
# capitals and villages have overlapping 3x3 regions
def makeBoard(app):
    newBoard = None
    while newBoard == None:
        oldBoard = dict() # Store Map as a dictionary with coordinate keys
        possibleMoves = list()
        currentCities = list()
        # Shrink range by 1 so no capitals spawn on outer edge of map
        for row in range(1, app.mapSize - 1):
            for col in range(1, app.mapSize -1):
                possibleMoves.append((row, col))
        # Set Total Possible Cities Based on Map Size
        if app.mapSize == 11:
            totalCities = 5
        elif app.mapSize == 15:
            totalCities = 9
        elif app.mapSize == 19:
            totalCities = 13
        # Backtracking Helper that adds capitals to board. Returns board and 
        # capital locations
        newBoard = makeCapitalsHelper(app, totalCities, possibleMoves, oldBoard, 
                                                                  currentCities)
    board = newBoard[0]
    capitals = newBoard[1]
    for row in range(app.mapSize):
        for col in range(app.mapSize):
            key = (row, col)
            if key in board: #Skip capitals and villages
                continue
            else:
                newTile = tileSelector(app, row, col)
                board[key] = newTile
    return board, capitals

# recursive function that puts capitals and villages in random positions
def makeCapitalsHelper(app, totalCities, possibleMoves, oldBoard, 
                                                                 currentCities):
    # Base case when there's no more cities to add
    if totalCities == 0:
        return oldBoard, currentCities
    else:
        # Check through possible moves
        for i in range(len(possibleMoves)):
            position = random.choice(possibleMoves)
            posX, posY = position[0], position[1]
            
            # Legality Check
            if isLegalMove(posX, posY, currentCities):
                if app.playerNum > 0:
                    #Create Capital Tile for unaccounted Players
                    currentTile = Capital(posX, posY)
                    createImage(app, currentTile)
                else:
                    currentTile = Village(posX, posY)
                    createImage(app, currentTile)

                #Update Board and Remove Move
                oldBoard[(posX, posY)] = currentTile
                possibleMoves.remove(position)
                currentCities.append(currentTile)
                
                # Recursion
                app.playerNum -= 1
                result = makeCapitalsHelper(app, totalCities - 1, possibleMoves, 
                                                        oldBoard, currentCities)
                if result != None:
                    return result
                app.playerNum += 1
        return None

################################################################################

# Legality check that uses pythagorean theorem to estimate the distance between cities
# Distance must be above 4 to be considered legal.
def isLegalMove(posX, posY, currentCities):
    if len(currentCities) < 1:
        return True
    for tile in currentCities: #Check each capital/village
        if int(((tile.x - posX)**2 + (tile.y-posY)**2)**0.5) <= 4:
            return False
    return True

# Random number generation to determine Tile Type
# Website to determine bounds:
# https://polytopia.fandom.com/wiki/Map_Generation
def tileSelector(app, x, y):
    num = random.random()
    if (0 <= num < .20):
        tile = Mountain(x,y)
        createImage(app, tile)
        return tile

    elif (.20 <= num < .54):
        tile = Forest(x,y)
        createImage(app, tile)
        return tile
    
    else:
        tile = Field(x,y)
        createImage(app, tile)
        return tile
    
# Creates images for all respective tiles. Set them to be proportional to their
# width and the app's height
# Map Images from:
# http://mercenarylight.synthasite.com/fire-emblem-sprites.php
def createImage(app, tile):
    if isinstance(tile, Capital):
        capitalImage1 = app.loadImage("images/CapitalTile.png")
        capitalImage2 = app.scaleImage(capitalImage1, 
                              1/(app.mapSize*capitalImage1.size[0]/app.height))
        tile.image = capitalImage2

    elif isinstance(tile, Village):
        villageImage1 = app.loadImage("images/VillageTile.png")
        villageImage2 = app.scaleImage(villageImage1, 
                               1/(app.mapSize*villageImage1.size[0]/app.height))
        tile.image = villageImage2

    elif isinstance(tile, Mountain):
        mountainImage1 = app.loadImage("images/MountainTile.png")
        mountainImage2 = app.scaleImage(mountainImage1, 
                              1/(app.mapSize*mountainImage1.size[0]/app.height))
        tile.image = mountainImage2
        
    elif isinstance(tile, Forest):
        forestImage1 = app.loadImage("images/ForestTile.png")
        forestImage2 = app.scaleImage(forestImage1, 
                                1/(app.mapSize*forestImage1.size[0]/app.height))
        tile.image = forestImage2

    elif isinstance(tile, Field):
        fieldImage1 = app.loadImage("images/FieldTile.png")
        fieldImage2 = app.scaleImage(fieldImage1, 
                                 1/(app.mapSize*fieldImage1.size[0]/app.height))
        tile.image = fieldImage2
        
        houseImage1 = app.loadImage("images/House.png")
        houseImage2 = app.scaleImage(houseImage1, 
                               1/(app.mapSize*2*houseImage1.size[0]/app.height))
        tile.house = houseImage2

    elif isinstance(tile, City):
        cityImage1 = app.loadImage("images/CityTile.png")
        cityImage2 = app.scaleImage(cityImage1, 
                                  1/(app.mapSize*cityImage1.size[1]/app.height))
        tile.image = cityImage2
        

