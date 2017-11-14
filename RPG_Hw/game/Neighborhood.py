from game.Observer import Observer
from game.House import House
from game.Player import Player
from monsters import *
from random import randint

class Neighborhood(Observer):
    def __init__(self, numHouses, debug):

        self.houses=[]
        row = []
        self.monsterNum=0

        self.player=Player()


        for x in range(numHouses):
            row=[]

            for y in range(numHouses):
                numMon=randint(0,10)

                self.monsterNum+=numMon

                house=House(numMon,y)
                house.register(self)
                row.append(house)

                if(debug):#    Debug Purposes
                    print ("\n\n{:d}, {:d}".format(x,y))
                    house.printHouse()

        self.houses.append(row)




    def update(self,monster):
        self.monsterNum-=1
        if(self.monsterNum==0):#TODO: WIN STATE
            pass
