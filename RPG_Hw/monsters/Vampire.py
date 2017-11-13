from monsters.Monster import Monster
"""Vampires attack at a rate of 10-20 HP per turn.
They are not harmed by ChocolateBars.
Start with 100-200 HP."""
class Vampire(Monster):

    def __init__(self):
        self.health = Monster.randNum(100,200)
        self.strength = 10
        self.margin = 10
        self.name = "Vampire"

    def attack(self):
        return self.getStrength() + Monster.randNum(0,self.getMargin())

    def getHit(self,damage,weapon):
        d = damage
        if(weapon == "ChocolateBars"):
            d = 0
        self.health -= damage
        if(self.getHealth()<=0):
            self.die()

        return self.getHealth()
