from game.Observer import Observer
from game.Observable import Observable

from monsters import *
from random import randint

class House(Observer,Observable):

    def __init__(self,numMonsters,houseNum):
        self.numMonsters=numMonsters
        self.houseNum=houseNum

        self.monsters=[]
        self.observers=[]
        for x in range(numMonsters):
            self.monsters.append(self.makeMonster(randint(0,4)))

    def printHouse(self):
        print("\nHouse #{:d}, Number of Monsters={:d}".format(self.houseNum,self.numMonsters))
        #for x in range(self.numMonsters):
        #    print("\t")
        #    self.monsters[x].printMonster()

    def update(self,monster):
        if monster in monsters:
            monsters.remove(monster)
            monsters.append(Person())
        update_observers(monster)

    def addPlayer(self, player):
        self.player=player
    def remPlayer(self):
        self.player=None

    """This takes a random number 1-4 and creates a monster based upon this."""
    def makeMonster(self,num):
        if(num==0):
            return Ghoul()
        if(num==1):
            return Vampire()
        if(num==2):
            return Werewolf()
        if(num==3):
            return Zombie()
        if(num==4):
            return Person()
