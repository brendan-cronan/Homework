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
    def genWeapon(self,number):
        if(number==0):
            return "SourStraws"
        if(number==1):
            return "ChocolateBars"
        if(number==2):
            return "NerdBomb"
    def __init__(self):
        self.health = 100
        self.inventory={
        "HersheyKisses":999,
        "SourStraws":0,
        "ChocolateBars":0,
        "NerdBomb":0
        }
        for x in range(10):
            inventory[genWeapon(randInt(0,2))]+=

    def attack(self,weapon):
        if weapon in self.inventory:
            if(self.inventory[weapon] > 0):
                damage=randint(lowBound,upBound)
