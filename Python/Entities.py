from Grammar import *

class Entity():
    def __init__(self):

        self.scene = None
        
        self.name = None
        self.type = "Default Entity"
        self.description = None
        self.actions = {}
        
        self.hp = 10
        self.mp = 10
    
        self.inventory = []
    
    def fullName(self):
        return "%s the %s" % (self.name, self.type)
        
    def describeSelf(self):
        if self.description == None:
            print("This is %s"
                %(self.fullName()))
        else:
            print(self.description)
        
    def die(self):
        print("%s has died" % self.name)
        self.surrounding.entities.remove(self)
        
    def damage(self, other, damage):
        other.hp -= damage;
        print("%s hit %s for %d damage!"
            % (self.fullName(), other.name, damage))
        
        if other.hp <= 0:
            other.die()
            print("[debug] Nice.")
        else:
            print("%s has %d health remaining"
                %(other.name, other.hp))
    def addAction(self, actionName, actionMethod):
        self.actions[actionName] = actionMethod
        
    def goToSurrounding(self, newSurrounding):
        self.surrounding = newSurrounding;
        newSurrounding.player = self
        
    def isUsable():
        return (
                self.name != None
            and self.type != None
            and self.description != None
            and self.surrounding != None
        )
    
class Player(Entity):
    def __init__(self, name="player"):

        super().__init__()

        self.scene = None
        
        self.name = name
        self.type = "human"
        self.description = "This is you, you look like you."
        
        self.hp = 100
        self.mp = 100

        self.energy = 100
        self.bullets = 15

        self.inventory = []

    def addItem(self, item):
        self.addToInventory(item)
    def addToInventory(self, item):
        self.inventory.append(item)

    def printStats(self):
        print("--------------------------")
        print("%s : %d HP | %d MP | %d Energy | %d Bullets"
              % (self.name, self.hp, self.mp, self.energy, self.bullets))
        print("--------------------------")

    def printInventory(self):
        print("--- Inventory ---")
        for item in self.inventory:
            print(item)
        print("-----------------")
    def shoot(self, other, damage = 10):
        if self.bullets < 0:
            print("You have no bullets left!")
        else:
            self.damage(other, damage)
            self.bullets -= 1;
            print("You shoot %s for %d damage! (%d HP Left) %d bullets remaining"
                  %(other.name, damage, other.hp, self.bullets))

class Spider(Entity):
    def __init__(self, name ="Frank"):

        super().__init__()

        self.scene = None

        self.name = name
        self.type = "Spider"
        self.hp = 10
        self.mp = 0

        self.addAction(self.name, lambda: self.describeSelf())
        self.addAction("kick %s" % self.name, lambda : self.surrounding.player.damage(self, 6))
        self.addAction("shoot %s" % self.name, lambda: self.surrounding.player.shoot(self))
            
    def bite(self, other):
        self.damage(other, 1);
