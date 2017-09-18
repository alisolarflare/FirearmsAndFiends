from FirearmEngine import *
import traceback



print("Hello world!")
print("What is your name?");

player = Player()
player.name = input()

print("Hello " + player.name);
player.printStats()

barn = Barn()

player.goToSurrounding(barn)





try:
    command = input()
    while(command != "quit"):

        player.surrounding.runCommand(command)
        print("---");
        
        command = input()
        

    print("Thanks for playing Firearms and Fiends!")
except Exception as ex:
    print("An Error occoured!")
    traceback.print_exc()
    print("Press any key to shut down...")
    input()
    quit()
