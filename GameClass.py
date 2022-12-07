from BoardAlgorithm import *
from UnitClass import *
################################################################################
# Game Objects that handles certain game functions

class GameObject(object):
    def __init__(self, app):
        # Initialize players in the game
        self.playerList = [Player(i) for i in range(app.playerNum)]
        
        # Set current player
        self.currentPlayerNum = 0
        self.currentPlayer = self.playerList[self.currentPlayerNum]
        
        # Create map informaiton
        self.map, capitals = makeBoard(app)
        self.unitsOnBoard = dict()
        
        # Assign each player a capital and give them a unit
        for i in range(len(self.playerList)):
            player = self.playerList[i]
            capital = capitals[i]
            player.addCity(app, self, capital)
            unit = Unit(capital.x, capital.y)
            changeUnit(player, self, capital, unit)

        removeResources(self.map)

        # Change units status and player status
        switchUnitsOn(self.currentPlayer)
        
    def __repr__(self):
        return f"{type(self)}"
    
    def changeTurn(self, app): # Changes player turns
        app.targetTile = None
        switchUnitsOff(self.currentPlayer)
        self.currentPlayerNum = (self.currentPlayerNum+1) % len(self.playerList)
        self.currentPlayer = self.playerList[self.currentPlayerNum]
        switchUnitsOn(self.currentPlayer)
        

    def getTile(self, x, y): # Gets tile at associated x,y coordinates
        if (x, y) not in self.map:
            return None
        else:
            return self.map[(x, y)]
    
    def getUnit(self, x, y): # Gets unit from  dictionary, using x,y coordinates
        if (x, y) not in self.unitsOnBoard:
            return None
        else:
            return self.unitsOnBoard[(x,y)]

################################################################################

class vsCPU(GameObject): # for single player game
    def __init__(self, app):
        app.playerNum += 1
        super().__init__(app)

class multiplayer(GameObject): # For local multiplayer game
    def __init__(self, app):
        super().__init__(app)

################################################################################

class Player(object): # Player objects that represent those playing
    playerColors = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange" ]
    def __init__(self, name):
        self.name = f"Player {name}"
        self.color = self.playerColors[name]
        # Cities and units are kept track of
        self.currentCities = []
        self.currentUnits = []
        self.currency = 5
        self.firstTurn = True

    # Adds city to map and player's cities
    def addCity(self, app, game, city): 
        # Change ownership if players captures an enemy city
        if isinstance(city, City):
            city.color = self.color
            for player in game.playerList:
                    if city in player.currentCities:
                        player.currentCities.remove(city)
            self.currentCities.append(city)
        # Create base city and add it to the map
        else:
            newCity = City(city.x, city.y)
            newCity.color = self.color
            newCity.name = newCity.name + f" {len(self.currentCities) + 1}"
            createImage(app, newCity)
            self.currentCities.append(newCity)
            game.map[(city.x, city.y)] = newCity
            
    def __repr__(self):
        return f'Player {self.color}'


# Puts unit onto the board and adds to player collection
def changeUnit(player, game, city, unit):
    unit.color = city.color
    player.currentUnits.append(unit)
    game.unitsOnBoard[(city.x, city.y)] = unit

# Changes states for player's units and cities to signify their turn.
# Also acquire stars at the start of their turn
def switchUnitsOn(player):
    units = player.currentUnits
    for unit in units:
        unit.canAct = True
        unit.outline = "white"
        unit.canMove = True
    cities = player.currentCities
    for city in cities:
        city.canMakeUnits = True
        if player.firstTurn == False:
                player.currency += city.starsPerTurn
    player.firstTurn = False

# Changes stats for player's units and cities to signify the end of their turn.
def switchUnitsOff(player):
    units = player.currentUnits
    for unit in units:
        unit.canAct = False
        unit.outline = "black"
        unit.canMove = False
    cities = player.currentCities
    for city in cities:
        city.canMakeUnits = False

################################################################################

# Displays tip based on input text
def showTip(app, text):
    app.tip = text
    app.displayTip = True

################################################################################

# Removes resources that are not around any nearby cities
def removeResources(gameMap):
    for item in gameMap:
        tile = gameMap[item]
        if tile.resource == None:
            continue
        if modifiedCityCheck(gameMap, tile):
            pass
        else:
            tile.resource = None

# Check to see if there is a nearby city
def modifiedCityCheck(gameMap, tile):
    x = tile.x
    y = tile.y
    size = len(gameMap)**0.5
    for dx in range(-1, 2):
        for dy in range(-1,2):
            newX = x +dx
            newY = y + dy
            if newX < 0 or newX >= size or newY < 0 or newY >= size:
                continue
            targetTile = gameMap[(newX, newY)]
            if isinstance(targetTile, City) or isinstance(targetTile, Village):
                return True
    return False

################################################################################

#Checks combat conditions and adjusts app screens
def runCombat(app, player, enemy):
    # Check enemy exists and is on board
    if enemy != None and enemy not in app.game.currentPlayer.currentUnits:
        dx = abs(player.x - enemy.x)
        dy = abs(player.y - enemy.y)
        if (dx <= player.range and dy <= player.range):
            calculateDamage(app, player, enemy, dx, dy)
            app.mode = "inPlayScreenMode"
        else:
            showTip(app, "Not in Range")
            app.mode = "inPlayScreenMode"
    else:
        showTip(app, "Invalid Attack")        
        app.mode = "inPlayScreenMode"


# Makes calculations to determine player damage and incoming retaliation damage
# Equations From:
# https://polytopia.fandom.com/wiki/Combat
def calculateDamage(app, attacker, defender, dx, dy):
    rangeDiff = dx + dy
    attackForce = attacker.attack * (attacker.health/attacker.maxHealth)
    defenseForce = defender.defense * (defender.health/defender.maxHealth)
    totalDamage = attackForce + defenseForce
    attackResult = roundHalfUp((attackForce/totalDamage)*attacker.attack*4.5)
    defenseResult = roundHalfUp((defenseForce/totalDamage)*defender.defense*4.5)
    defender.health -= attackResult
    attacker.canAct = False
    attacker.canMove = False
    attacker.outline = "black"
    if defender.health <= 0: # Get rid of dead enemy
        del app.game.unitsOnBoard[(defender.x, defender.y)]
        for player in app.game.playerList:
            if defender in player.currentUnits:
                player.currentUnits.remove(defender)
    else:
        if attacker.range <= defender.range: # Calculate retaliation damage
            attacker.health -= defenseResult
        else:
             # Archers take extra damage for attacking at close range
            if rangeDiff <= 1 or dx == dy:
                attacker.health -= roundHalfUp(defenseResult * 1.5)
        if attacker.health <= 0: #get rid of dead friendly unit
            app.game.currentPlayer.currentUnits.remove(attacker)
            del app.game.unitsOnBoard[(attacker.x, attacker.y)]

# From
# https://www.cs.cmu.edu/~112/notes/notes-variables-and-functions.html#RecommendedFunctions
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    # You do not need to understand how this function works.
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

################################################################################

# Checks movement conditions and initiates unit movement
def moveUnit(app, player, row, col):
    dx = abs(player.x - row)
    dy = abs(player.y - col)
    if row == player.x and col == player.y: # Can't move to same tile
        app.mode = "inPlayScreenMode"
        showTip(app, "Invalid Move") 
    elif (row,col) in app.game.unitsOnBoard: # Can't move to occupied space
        app.mode = "inPlayScreenMode"
        showTip(app, "Space Occupied")
    elif row == -1 or col == -1: # Can't move off screen
        app.mode = "inPlayScreenMode"
        showTip(app, "Invalid Move")
    # Move must be in unit's range
    elif dx <= player.movement and dy <= player.movement: 
        del app.game.unitsOnBoard[(player.x, player.y)]
        player.x = row
        player.y = col
        app.game.unitsOnBoard[(row, col)] = player
        player.canMove = False
        player.outline = "gray"
        app.mode = "inPlayScreenMode"
    else:
        app.mode = "inPlayScreenMode"
        showTip(app, "Invalid Move")
    
################################################################################
# Timer Fired Functions to check player and game status

def checkPlayers(app): # Check and Remove players with no more cities 
    for player in app.game.playerList:
        if player.currentCities == []:
            app.game.playerList.remove(player)

def checkGameOver(app): # End Game when there's only 1 player left with cities
    if len(app.game.playerList) == 1:
        app.mode = "GameOverMode"

################################################################################
# Mouse Pressed Functions for button and updating game metrics

def checkButtons(app, event): #Checks if buttons is pressed or not
    for button in app.buttonHub:
        if button.buttonPressed(app, event):
            return True
    return False

def showCity(app): # Sets targetTile so cities can be displayed for players
    if isinstance(app.tile, City):
        if app.tile in app.game.currentPlayer.currentCities:
            app.targetTile = app.tile
