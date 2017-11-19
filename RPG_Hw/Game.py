#!/usr/bin/env python3
from game import *
from monsters import *
import sys


class Game:
    self.hood
    DEFAULT_HOUSE_NUMBER=10
    def __init__(self, numHouses=10, debug=False):
        self.hood = Neighborhood(numHouses, debug)

    def move(self,stringDir):
        direc=Game.getDir(stringDir)
        playerLoc=self.hood.getPlayer().getLocation()
        newLoc=[]
        newLoc[0]=playerLoc[0]+direc[0]
        newLoc[1]=playerLoc[1]+direc[1]
        self.hood.movePlayer(x,y)


    def getDir(stringDir):
        direc=[]
        direction=stringDir.upper()
        if(direction=="NORTH"):
            direc[0]=0
            direc[1]=-1
        if(direction=="EAST"):
            direc[0]=1
            direc[1]=0
        if(direction=="SOUTH"):
            direc[0]=0
            direc[1]=1
        if(direction=="WEST"):
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
