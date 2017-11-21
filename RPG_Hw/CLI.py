#!/usr/bin/env python3
import sys
from Game import Game
class CLI:
    directions={"n":"north","s":"south","e":"east","w":"west"}
    def __init__(self,_game):
        self.game=Game()
        leave=False
        userIn=""
        while not leave:
            userIn=input(CLI.getPrompt()).lower()

            self.parseInput(userIn)

            leave= userIn == "quit"


        if(leave):
            print("Goodbye!")


    def movePlayer(self,direc):
        print("You are moving {}".format(direc))
        self.game.move(direc)


    def parseInput(self,cmd):
        if cmd in CLI.directions.keys():
            direc=CLI.directions[cmd]
            self.movePlayer(direc)
        elif cmd in CLI.directions.values():
            self.movePlayer(cmd)
        if(cmd == "quit" or cmd == "q"):
            exit()



    def getPrompt():
        return "\nList of Commands includes...\nNorth, South, East, West, (n,s,e,w), Attack(atk), Stay(empty), or Quit(q).\n\nPlease Enter Your Command Here:\n >> "


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
