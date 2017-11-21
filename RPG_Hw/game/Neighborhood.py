from game.Observer import Observer
from game.House import House
from game.Player import Player
from monsters import *
from random import randint

class Neighborhood(Observer):
    def __init__(self, numHouses, debug):
        self.numHouse=numHouses
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

                house=House(numMon,x*numHouses+y)
                house.add_observer(self)
                row.append(house)

                if(debug):#    Debug Purposes
                    print ("\n\n{:d}, {:d}".format(x,y))
                    house.printHouse()

            self.houses.append(row)
        self.houses[0][0].addPlayer(self.player)
        #self.printHouses()

    def getPlayer(self):
        return self.player

    def isValidSpace(self,x,y):
        if(x < self.numHouse and y < self.numHouse and x >= 0 and y >= 0):
            #print("Valid")
            return True
        else:
            #print("{:d},{:d} Is out of the bounds of {:d} {:d}, {:d} {:d}".format(x,y,0,self.numHouse,0,self.numHouse))
            print("You reach the end of the Neighborhood. \nChoose a different Direction")
            return False

    def attackHouse(self):
        playerPos=self.player.getLocation()
        xpos=playerPos[0]
        ypos=playerPos[1]
        tmpHouse=self.houses[xpos][ypos]
        tmpHouse.printHouse()
        winput=False
        while not winput:
            wep=input("Which weapon would you like to use?\n>> ")
            self.player.printPlayer()
            atkVal=0.0
            if wep=="" or wep == "leave":
                winput=True
                break
            elif wep in Player.SHORT_WEAPONS.keys():
                atkval=self.player.attack(Player.SHORT_WEAPONS[wep])
                tmpHouse.atk(atkVal,wep)
                suc=True
            elif wep in Player.WEAPONS:
                atkval=self.player.attack(wep)
                tmpHouse.atk(atkVal,wep)
                suc=True
            else:
                print("Incorrect Input. Try again.")
                suc=False




    def movePlayer(self,x,y):
        loc=self.player.getLocation()

        self.houses[loc[0]][loc[1]].remPlayer()

        self.player.movePlayer(x,y)
        self.player.printPlayer()

        self.houses[x][y].addPlayer(self.player)
        self.houses[x][y].printHouse()




    def update(self,monster):
        self.monsterNum-=1
        if(self.monsterNum==0):
            print("Congratulations! You win!")
            exit()


    def printHouses(self):
        for a in range(0,len(self.houses)):
            for b in range(0,len(self.houses)):
                self.houses[a][b].printHouse()
