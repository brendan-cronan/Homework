from monsters.Monster import Monster
"""Zombies attack you at a rate of 0-10 HP per turn.
Zombies are harmed by any weapon,
however, if attacked with SourStraws lose twice the number of points from an attack.
Start with between 50 and 100 HP."""
class Zombie(Monster):
    def __init__(self):
        self.health = Monster.randNum(50,100)
        self.strength = 0
        self.margin = 10
        self.name = "Zombie"

    def attack(self):
        return self.getStrength() + Monster.randNum(0,self.getMargin())

    def getHit(self,damage,weapon):
        d=damage
        if(weapon == "SourStraws"):
            d = damage * 2
        self.health -= damage
        if(self.getHealth()<=0):
            self.die()

        return self.getHealth()
