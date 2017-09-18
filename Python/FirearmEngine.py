from Spaces import *






    #Player is in WORLD, in LOCATION in SURROUNDINGS in SCENE

    #A WORLD has LOCATIONS: "Inn, Dungeon, Wilderness, Forest"
    
    #A LOCATION has SURROUNDINGS: "basement, master bedroom, outside, living room"
    #A LOCATION has pathways
    #A LOCATION is in a WORLD
    
    #A SURROUNDING has description: "You are in the innkeeper's basement"
    #A SURROUNDING has scenes: exploring, fighting, searching
    #A SURROUNDING has entities: player, goblins, etc
    #A SURROUNDING has pathways to other locations
    #A SURROUNDING is in a LOCATION
    
    #A SCENE has description: "You are currently in battle"
    #A SCENE has scene specific actions: Fight, loot, attack, run away
    #A SCENE is in a LOCATION

    #AN ENTITY have stats: HP, MP, Energy
