from Entities import *

class Surrounding():
    def __init__(self):
        self.name = None
        self.description = None
        self.entities = []
        self.actions = {}
        self.location = None

    def describeSelf(self):    
        if self.description != None:
            print(self.description)
            self.describeEntities();
        else:
            if self.name[0] in "aeiou":
                word = "an"
            else:
                word = "a"
            print("You look at your surroundings. It's " + Grammar.a(word))
        
    def addEntity(self, entity):
        self.entities.append(entity)
        entity.surrounding = self
        for action in entity.actions:
            self.addAction(action, entity.actions[action])

    def describeEntities(self):
        print("There " + Grammar.are(len(self.entities), "thing") + " in this room")
        for entity in self.entities:
            entity.describeSelf();
    
    def addPlayer(self, player):
        player.goToSurrounding(self)
        
    
    def addAction(self, actionName, actionMethod):
        self.actions[actionName] = actionMethod

    def describeActions(self):
        print("Possible Actions include:")
        result = ""
        for action in self.actions:
            result += action
            result += "|"
        result = result[:-1]
        print(result)
        
    def runCommand(self, command):
        if command in self.actions:
            self.actions[command]()
        else:
            print("That is not a valid command")

class Barn(Surrounding):
    def __init__(self):

        super().__init__()

        self.name = "Barn"
        self.description = "You're standing in a barn. Not much to see here except <frank> the spider"

        frank = Spider("Frank")
        barry = Spider("Barry")
        clyde = Spider("Clyde")

        self.addEntity(frank)
        self.addEntity(barry)
        self.addEntity(clyde)
        
        self.addAction("look", self.describeSelf)

        
class Shack(Surrounding):
    def __init__(self):
        super().__init__();

        self.name = "Metal Shack"
        self.description = """You are standing in the rusted husk
            of a small structure, an exit to the [east] which
            resembles an age-worn <metal door>. There is a <case>
            here.
            """
