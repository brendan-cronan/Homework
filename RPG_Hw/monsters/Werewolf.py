from monsters.Monster import Monster
"""Werewolves attack at a rate of 0-40 HP per turn.
They are not harmed by ChocolateBars or SourStraws. Start with 200 HP."""
class Werewolf(Monster):
    def __init__(self):
        self.health = 200
        self.strength = 0
        self.margin = 40
        self.name = "Werewolf"

    def attack(self):
        return self.strength + Monster.randNum(0,self.margin)
    def getHit(self,damage,weapon):
        d = damage
        if(weapon == "ChocolateBars" or weapon == "SourStraws"):
            d = 0
        self.health -= damage
        if(self.health<=0):
            self.die()

        return self.health
