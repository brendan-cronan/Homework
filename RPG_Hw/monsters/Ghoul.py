from monsters.Monster import Monster
"""Ghouls attack at a rate of 15-30 HP per turn. They are harmed by all weapons,
 but receive 5X the attackers attack if attacked with NerdBombs.
 Start with 40-80 HP."""
class Ghoul(Monster):

    def __init__(self):
        self.health = Monster.randNum(40,80)
        self.strength = 15
        self.margin = 15
        self.name= "Ghoul"

    def attack(self):
        return self.getStrength() + Monster.randNum(0,self.getMargin())




    def getHit(self,damage,weapon):
        d=damage
        if(weapon == "NerdBomb"):
            d=damage*5
        self.health -= damage
        if(self.getHealth()<=0):
            self.die()

        return self.getHealth()
