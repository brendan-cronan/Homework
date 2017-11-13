from monsters.Monster import Monster
class Ghoul(Monster):

    def __init__(self):
        self.health = Monster.randNum(100,200)
        self.strength = 10
        self.margin = 10
        self.name= "Ghoul"
    def attack(self):
        return self.strength + Monster.randNum(0,self.margin)
