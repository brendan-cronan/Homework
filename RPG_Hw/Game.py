#!/usr/bin/env python3
from game import *
from monsters import *
import sys


class Game:
    DEFAULT_HOUSE_NUMBER=10
    def __init__(self, numHouses=10, debug=False):
        hood = Neighborhood(numHouses, debug)
    #i got this method off of a github tutorial
    #https://gist.github.com/dideler/2395703
    #I honestly could not do it cleaner than this on my own:)
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
        if '-d' in options:
            b=True if "true" else False
            game=Game(Game.DEFAULT_HOUSE_NUMBER,b)
        if '-h' in options:
            game=Game(int(myargs['-h']),False)
    else:
        game=Game(Game.DEFAULT_HOUSE_NUMBER,False)
