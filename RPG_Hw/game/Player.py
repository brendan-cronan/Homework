from game import *
from random import randint
class Player:

    #inits some basic attributes of the "Player"
    def __init__(self):
        self.health = randint(400,600)#changed these around a bit so it was easier
        self.atk=randint(15,30)#changed these around a bit so it was easier
        # x , y of house
        self.loc = [0,0]



        self.inventory={#holds the number of uses * the number of candies
        "HersheyKisses":9999,
        "SourStraws":0,
        "ChocolateBars":0,
        "NerdBomb":0
        }
        #initialize the inventory with random items
        for x in range(10):
            wep=Player.genWeapon()
            self.inventory[wep]=self.inventory[wep] + Player.AMT_USES[wep]

    #gets a random weapon to add to the inventory
    def genWeapon():
        number = randint(0,2)
        if(number==0):
            return "SourStraws"
        if(number==1):
            return "ChocolateBars"
        if(number==2):
            return "NerdBomb"

    """
        This is taking the given weapon, checking if it is in the inventory,

        If the player has any of the weapon,

        then calculates the damage based on the minimum modifier and adding the
        margin of "randomness" it can have.

        then decreases the inventory by 1.

        Prints some stuff.

    """
    def attack(self,weapon):
        if weapon in self.inventory:
            if(self.inventory[weapon] > 0):
                damage=self.atk * uniform( Player.BASE_MOD[weapon], Player.MARGINS[weapon] )
                self.inventory[weapon] = self.inventory[weapon] - 1
                print("You did {:f} damage".format(damage))
                return damage
            else:
                print("You are out of {}.".format(weapon))

    #getters
    def getLocation(self):
        return self.loc
    def getHealth(self):
        return self.health

    #changes location.
    def movePlayer(self,x,y):
        self.loc[0]=x
        self.loc[1]=y


    #takes damage from monsters or adds health/candy from people
    def getHit(self,damage):
        if(damage==-5):#person
            self.health=self.health+5
            weapon=Player.genWeapon()
            self.inventory[weapon]= self.inventory[weapon]+Player.AMT_USES[weapon]

        else:#monster
            self.health=self.health-damage
            if(self.health <= 0):
                print("Sorry. You lose! Try again.")#lose state
                exit()

    #printer method
    def printPlayer(self):
        print("\nPlayer:\n\t[ Health: {:f}  /  Attack: {:d} ]\n\tInventory:"
        .format(self.health,self.atk))

        for x in self.inventory:
            print("\t-\t{}\t:\t{:d}".format(x,self.inventory[x]))


    BASE_MOD={#minimum modifier that it can provide
        "HersheyKisses":1,
        "SourStraws":1,
        "ChocolateBars":2,
        "NerdBomb":3.5
    }
    MARGINS={#margin that this modifier can increase by.
        "HersheyKisses":0,
        "SourStraws":.75,
        "ChocolateBars":.4,
        "NerdBomb":1.5
    }
    AMT_USES={#how many uses you get per new candy
        "HersheyKisses":9999,
        "SourStraws":2,
        "ChocolateBars":4,
        "NerdBomb":1
    }
    SHORT_WEAPONS={#abbreviations for the weapons
        "hs":"HersheyKisses",
        "ss":"SourStraws",
        "cb":"ChocolateBars",
        "nb":"NerdBomb"
    }
    WEAPONS={#long names for the weapons
        "HersheyKisses",
        "SourStraws",
        "ChocolateBars",
        "NerdBomb"
    }
