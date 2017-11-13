from game.Observer import Observer
from game.House import House
from monsters import *
from random import randint

class Neighborhood(Observer):
    def __init__(self, numHouses, debug):

        self.houses=[]
        self.monsterNum=0

        for x in range(numHouses):
            numMon=randint(0,10)

            self.monsterNum+=numMon

            house=House(numMon,x)
            house.register(self)
            self.houses.append(house)

            if(debug):#    Debug Purposes
                house.printHouse()




    def update(self,monster):
        self.monsterNum-=1
        if(self.monsterNum==0):#TODO: WIN STATE
            pass
