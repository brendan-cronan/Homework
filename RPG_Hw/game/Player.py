from game import *
from random import randint
class Player:


    def __init__(self):
        self.health = randint(500,700)
        self.atk=randint(15,30)
        # x , y of house
        self.loc = [0,0]



        self.inventory={
        "HersheyKisses":9999,
        "SourStraws":0,
        "ChocolateBars":0,
        "NerdBomb":0
        }
        #initialize the inventory with random items
        for x in range(10):
            wep=Player.genWeapon()
            self.inventory[wep]=self.inventory[wep] + Player.AMT_USES[wep]


    def genWeapon():
        number = randint(0,2)
        if(number==0):
            return "SourStraws"
        if(number==1):
            return "ChocolateBars"
        if(number==2):
            return "NerdBomb"


    def attack(self,weapon):
        if weapon in self.inventory:
            if(self.inventory[weapon] > 0):
                damage=self.atk * uniform( Player.BASE_MOD[weapon], Player.MARGINS[weapon] )
                self.inventory[weapon] = self.inventory[weapon] - 1
                print("You did {:f} damage".format(damage))
                return damage
            else:
                print("You are out of {}.".format(weapon))


    def getLocation(self):
        return self.loc

    def movePlayer(self,x,y):
        self.loc[0]=x
        self.loc[1]=y



    def getHit(self,damage):
        if(damage==-1):
            self.health=self.health+1
            weapon=Player.genWeapon()
            self.inventory[weapon]= self.inventory[weapon]+Player.AMT_USES[weapon]

        else:
            self.health=self.health-damage
            if(self.health <= 0):
                print("Sorry. You lose! Try again.")
                exit()

    def printPlayer(self):
        print("\nPlayer:\n\t[ Health: {:d}  /  Attack: {:d} ]\n\tInventory:"
        .format(self.health,self.atk))

        for x in self.inventory:
            print("\t-\t{}\t:\t{:d}".format(x,self.inventory[x]))


    BASE_MOD={
        "HersheyKisses":1,
        "SourStraws":1,
        "ChocolateBars":2,
        "NerdBomb":3.5
    }
    MARGINS={
        "HersheyKisses":0,
        "SourStraws":.75,
        "ChocolateBars":.4,
        "NerdBomb":1.5
    }
    AMT_USES={
        "HersheyKisses":9999,
        "SourStraws":2,
        "ChocolateBars":4,
        "NerdBomb":1
    }
    SHORT_WEAPONS={
        "hs":"HersheyKisses",
        "ss":"SourStraws",
        "cb":"ChocolateBars",
        "nb":"NerdBomb"
    }
    WEAPONS={
        "HersheyKisses",
        "SourStraws",
        "ChocolateBars",
        "NerdBomb"
    }
