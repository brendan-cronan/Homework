from game.Observer import Observer
from game.Observable import Observable

from monsters import *
from random import uniform,randint

"""
The House Object is primarily responsible for holding both monsters,
and the player when they arrive.

This class also Takes care of applying and retrieving damage from all of the
monsters inside.

This class listens for monster deaths and then adds a person in their place.

"""
class House(Observer,Observable):

    """
        this initializes everything given a random number of monsters to create
        and also adds the house as a listener to the monsters
    """
    def __init__(self,numMonsters,houseNum):
        self.numMonsters=numMonsters
        self.houseNum=houseNum

        self.monsters=[]
        self.observers=[]
        for x in range(numMonsters):
            self.monsters.append(self.makeMonster(randint(0,4)))
            self.monsters[x].add_observer(self)

    #printer method
    def printHouse(self):
        print("\nHouse #{:d}, Number of Monsters={:d}".format(self.houseNum,self.numMonsters))
        out="[ "
        for x in range(self.numMonsters):
            out="{}{}".format(out,str(self.monsters[x]))
        out="{}{}".format(out," ]")
        print(out)


    #listens for death... replaces with person and updates neighborhood
    def update(self,monster):
        if monster in self.monsters:
            self.monsters.remove(monster)
            self.monsters.append(Person())
            self.update_observers(monster)

    #
    def atk(self,dmgVal,weapon):
        for monster in self.monsters:
            monster.getHit(dmgVal,weapon)

        self.printHouse()

    def damage(self):
        total=0.01
        for monster in self.monsters:
            total = total + monster.attack()
        return total


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
