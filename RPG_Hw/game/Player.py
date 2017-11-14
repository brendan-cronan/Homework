from game import *
from random import randint
class Player:
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
    def genWeapon():
        number = randint(0,2)
        if(number==0):
            return "SourStraws"
        if(number==1):
            return "ChocolateBars"
        if(number==2):
            return "NerdBomb"
    def __init__(self):
        self.health = randint(100,125)
        self.atk=randint(10,20)
        # x , y
        self.loc = [0,0]



        self.inventory={
        "HersheyKisses":999,
        "SourStraws":0,
        "ChocolateBars":0,
        "NerdBomb":9
        }
        #initialize the inventory with random items
        for x in range(10):
            self.inventory["NerdBomb"]=8#+=Player.AMT_USES

    def attack(self,weapon):
        if weapon in self.inventory:
            if(self.inventory[weapon] > 0):
                damage=self.atk * randint( Player.BASE_MOD[weapon], Player.MARGINS[weapon] )

    def getHit(self,damage):
        if(damage==-1):
            self.health+=1
            weapon=Player.genWeapon()
            self.inventory[weapon]+=Player.AMT_USES[weapon]

        else:
            self.health-=damage
            if(self.health <= 0):
                pass
                #TODO: LOSE STATE
