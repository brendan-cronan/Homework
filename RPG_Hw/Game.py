#!/usr/bin/env python3
from game import *
from monsters import *
import sys

"""
    The game class handles most of the Game Logic present in the, well, game

    holds the neighborhood object and instantiates most of everything.

"""
class Game:
    DEFAULT_HOUSE_NUMBER=10#constant for ease of use.
    #makes neighborhood.
    def __init__(self, numHouses=10, debug=False):
        self.hood = Neighborhood(numHouses, debug)

    #calls the lower level attack logic
    def attack(self):
        self.hood.attackHouse()

    #moves the player.
    def move(self,stringDir):
        direc=Game.getDir(stringDir)
        playerLoc=self.hood.getPlayer().getLocation()
        newLoc=[0,0]
        newLoc[0]=playerLoc[0]+direc[0]
        newLoc[1]=playerLoc[1]+direc[1]

        if(self.hood.isValidSpace(newLoc[0],newLoc[1])):
            self.hood.movePlayer(newLoc[0],newLoc[1])

    """
        This takes a string direction and turns it into a set of two instructions
        that tell the row and col to either inc/dec
    """
    def getDir(stringDir):
        direc=[0,0]
        direction=stringDir.lower()
        if(direction=="north"):
            direc[0]=0
            direc[1]=-1
        if(direction=="east"):
            direc[0]=1
            direc[1]=0
        if(direction=="south"):
            direc[0]=0
            direc[1]=1
        if(direction=="west"):
            direc[0]=-1
            direc[1]=0

        return direc




    #i got this method off of a github tutorial
    #https://gist.github.com/dideler/2395703
    #I honestly could not do it cleaner than this on my own:)
    @staticmethod
    def getOpts(argv):
        opts = {}  # Empty dictionary to store key-value pairs.
        while argv:  # While there are arguments left to parse...
            if argv[0][0] == '-':  # Found a "-name value" pair.
                opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
            argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
        return opts


#not used but didnt want to lose the code
"""
if __name__ == "__main__":

    if(len(sys.argv) >= 2):
        options = Game.getOpts(sys.argv)
        b=False
        numHouse=Game.DEFAULT_HOUSE_NUMBER
        if '-d' in options:
            b=True if options['-d'] == "true" else False
        if '-h' in options:
            numHouse=int(options['-h'])

        game=Game(numHouse,b)
    else:
        game=Game(Game.DEFAULT_HOUSE_NUMBER,False)
"""
