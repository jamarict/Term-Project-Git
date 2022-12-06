################################################################################
# Units are movable warriors that the player controls.

# Stats obtained from:
# https://polytopia.fandom.com/wiki/List_of_Units
################################################################################
# Generic Warrior with basic stats. All players start with one
class Unit(object):
    def __init__(self, x, y):
        # Position stored as (x,y) coordinate
        self.x = x
        self.y = y
        
        # Represents how the unit can act: Black = Can't Act or Move, 
        # Gray = Can Act but Can't Move, # White = Can Act and Move
        self.outline = "black" 
        
        # Actions include attacking and capturing cities. After acting you can't
        # move
        self.canAct = False 
        
        # Moving is traversing the board. A unit is able to act after they move
        self.canMove = False 
        
        # Cost: How many stars a player needs to create this unit
        self.cost = 3
        
        # Movement: How many tiles the unit can move from their starting
        # position.
        self.movement = 1
        
        # Range: The range of attack for the unit from their current position
        self.range = 1
        
        # Attack: Stat that determines damage dealt in combat
        self.attack = 2
        
        # Defense: Stat the determines damage retaliation and reducing damage
        self.defense = 2
        
        # Health: Damage a unit can take before they are defeated in battle
        self.health = 10
        self.maxHealth = 10
        
        # From 
        # https://emojidb.org/sword-emojis
        self.name = "⚔️"
        self.title = "Warrior"

    def __repr__(self):
        return self.name
    
    # units redraw themselves based on getCellBounds outputs
    def redraw (self, app, canvas, x0, y0, x1, y1):
        r = 3
        canvas.create_oval(x0+r, y0+r, x1-r, y1-r, fill = self.color, width = 3,
                                                         outline = self.outline)
        canvas.create_text((x0+x1)/2, (y0+y1)/2, text = self.name, font = "30")

################################################################################
#Special Units have higher cost and different stats from the basic units

# Archers have increased range and lower defense. They can attack from a
# distance and not risk retaliation damage
class Archer(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cost = 4
        
        # Range 2 allows the Archer to attack with 2 "radius" or diagonal
        # squares from its original position
        self.range = 2
        
        self.defense = 1
        # From
        # https://emojipedia.org/bow-and-arrow/
        self.name = "🏹"
        self.title = "Archer"

# Riders have increased movement and lower defense. They traverse the map with
# great pace
class Rider(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cost = 4
        
        # Movement 2 allows the Rider to move with 2 "radius" or diagonal
        # squares from its original position
        self.movement = 2
        
        self.defense = 1
        
        # From
        # https://emojipedia.org/horse/
        self.name = "🐎"
        self.title = "Rider"

# Defenders have increased defense with lower attack. They are great for soaking
# up damage but are not meant to directly attack others. They also have higher
# health
class Defender(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cost = 4
        
        self.attack = 1
        self.defense = 3
        
        self.health = 15
        self.maxHealth = 15
        
        # From 
        # https://emojings.com/shield/#:~:text=What%20does%20the%20%F0%9F%9B%A1%20%EF%B8%8F%20Shield%20emoji%20mean,shape%20with%20simple%20pattern%20and%20a%20metal%20border.
        self.name = "🛡"
        self.title = "Defender"



