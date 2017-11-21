from game.Observer import Observer
from game.House import House
from game.Player import Player
from monsters import *
from random import randint

"""
This class is a container for all the houses.

It listens for any decrease in the number of monsters in the Neighborhood
when it reaches 0, you win!.

this handles a lot of the player/house interactions.

can also check if a space is valid and handles directions that
directly translate to changes in array position

"""
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

    #getter
    def getPlayer(self):
        return self.player

    #checks for indices that could be out of bounds
    def isValidSpace(self,x,y):
        if(x < self.numHouse and y < self.numHouse and x >= 0 and y >= 0):
            #print("Valid")
            return True
        else:
            #print("{:d},{:d} Is out of the bounds of {:d} {:d}, {:d} {:d}".format(x,y,0,self.numHouse,0,self.numHouse))
            print("You reach the end of the Neighborhood. \nChoose a different Direction")
            return False

    """
        Handles the player/house battle interactions.
    """
    def attackHouse(self):
        #set up a lot of temp variables
        playerPos=self.player.getLocation()
        xpos=playerPos[0]
        ypos=playerPos[1]
        tmpHouse=self.houses[xpos][ypos]
        tmpHouse.printHouse()#current house

        #while they dont leave...
        winput=False
        while not winput:
            wep=input("Which weapon would you like to use?\n>> ")
            self.player.printPlayer()
            atkVal=0.0
            if wep=="" or wep == "leave":#exit the loop
                winput=True
                break
            elif wep in Player.SHORT_WEAPONS.keys():#if it is a shortened version of the weapon name
                atkval=self.player.attack(Player.SHORT_WEAPONS[wep])
                tmpHouse.atk(atkval,Player.SHORT_WEAPONS[wep])

                dmg=tmpHouse.damage()
                self.player.getHit(dmg)
                print("You took {:f} damage.\nYour new health is {:f}\n".format(dmg,self.player.getHealth()))


                suc=True
            elif wep in Player.WEAPONS:#normal weapon name
                atkval=self.player.attack(wep)
                tmpHouse.atk(100.01,wep)

                dmg=tmpHouse.damage()
                self.player.getHit(dmg)
                print("You took {:f} damage.\nYour new health is {:d}".format(dmg,self.player.getHealth()))

                suc=True
            else:#try again.
                print("Incorrect Input. Try again.")
                suc=False



    #changes the players location and adds/removes him from that house
    def movePlayer(self,x,y):
        loc=self.player.getLocation()

        self.houses[loc[0]][loc[1]].remPlayer()

        self.player.movePlayer(x,y)
        self.player.printPlayer()

        self.houses[x][y].addPlayer(self.player)
        self.houses[x][y].printHouse()



    #if total # of monsters in hood=0, you win!
    def update(self,monster):
        self.monsterNum-=1
        if(self.monsterNum==0):
            print("Congratulations! You win!")
            exit()

    #printer method
    def printHouses(self):
        for a in range(0,len(self.houses)):
            for b in range(0,len(self.houses)):
                self.houses[a][b].printHouse()
