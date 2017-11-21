from game.Observer import Observer
from game.Observable import Observable

from monsters import *
from random import uniform,randint

class House(Observer,Observable):

    def __init__(self,numMonsters,houseNum):
        self.numMonsters=numMonsters
        self.houseNum=houseNum

        self.monsters=[]
        self.observers=[]
        for x in range(numMonsters):
            self.monsters.append(self.makeMonster(randint(0,4)))
            self.monsters[x].add_observer(self)

    def printHouse(self):
        print("\nHouse #{:d}, Number of Monsters={:d}".format(self.houseNum,self.numMonsters))
        out="[ "
        for x in range(self.numMonsters):
            out="{}{}".format(out,str(self.monsters[x]))
        out="{}{}".format(out," ]")
        print(out)

    def update(self,monster):
        print("update House")
        if monster in self.monsters:
            self.monsters.remove(monster)
            self.monsters.append(Person())
            self.update_observers(monster)

    def atk(self,dmgVal,weapon):
        print("Attack House")
        for monster in self.monsters:
            print(monster)
            monster.getHit(dmgVal,weapon)

        self.printHouse()



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
