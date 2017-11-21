#!/usr/bin/env python3
import sys
from Game import Game
"""
    This class is primarily responsible for the command line interface operations.

    Takes care of most of the imputs and prompts for the user.

    fairly self explanatory.

"""
class CLI:
    directions={"n":"north","s":"south","e":"east","w":"west"}#abbreviations
    def __init__(self,_game):
        self.game=Game()
        leave=False
        userIn=""
        while not leave:
            userIn=input(CLI.getPrompt()).lower()

            #method to parse user input into meaningful commands
            self.parseInput(userIn)

            leave = (userIn == "quit")


        if(leave):
            print("Goodbye!")

    #call the game attack method
    def attackCmd(self):
        print("You Attack the House.")
        self.game.attack()

    #move in the specified direction
    def movePlayer(self,direc):
        print("You are moving {}".format(direc))
        self.game.move(direc)

    #turns user input into something meaningful
    def parseInput(self,cmd):
        #Movement options
        if cmd in CLI.directions.keys():
            direc=CLI.directions[cmd]
            self.movePlayer(direc)
        elif cmd in CLI.directions.values():
            self.movePlayer(cmd)
        elif cmd == "stay" or "":
            pass
        elif cmd == "quit" or cmd == "q":
            quit()
        elif cmd == "attack" or "atk":
            self.attackCmd()
        else:
            pass


    #prompt the user for instruction and list possible commands
    def getPrompt():
        return "\nList of Commands includes...\nNorth, South, East, West, (n,s,e,w), Attack(atk), Stay(empty), or Quit(q).\n\nPlease Enter Your Command Here:\n >> "


#main method and parse cmd line args.
#also calls the Game() constructor
if __name__ == "__main__":
    if(len(sys.argv) >= 2):
        options = Game.getOpts(sys.argv)
        b=False
        numHouse=Game.DEFAULT_HOUSE_NUMBER
        if '-d' in options:
            b=True if options['-d'] == "true" else False
        if '-h' in options:
            numHouse=int(options['-h'])

        command=CLI(Game(numHouse,b))
    else:
        command=CLI(Game(Game.DEFAULT_HOUSE_NUMBER,False))
