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

        if(debug):
            self.player.printPlayer()

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


    def getPlayer(self):
        return self.player
    def movePlayer(self,x,y):
        loc=self.player.getLocation()

        self.houses[loc[0]][loc[1]].remPlayer()

        self.player.movePlayer(x,y)

        self.houses[x][y].addPlayer(player)




    def update(self,monster):
        self.monsterNum-=1
        if(self.monsterNum==0):#TODO: WIN STATE
            pass
