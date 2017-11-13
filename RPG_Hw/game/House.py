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
            self.monsters.append(self.makeMonster(randint(0,3)))

    def printHouse(self):
        print("\n\nHouse #{:d}, Number of Monsters={:d}".format(self.houseNum,self.numMonsters))
        for x in range(self.numMonsters):
            print("\t")
            self.monsters[x].printMonster()

    def update(self):
        update_observers()



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
