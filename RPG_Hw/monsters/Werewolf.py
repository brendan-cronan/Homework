#from  Monster import Monster

class Werewolf():
    def __init__(self):
        self.health = Monster.randNum(100,200)
        self.strength = 10
        self.margin = 10

    def attack(self):
        return self.strength + Monster.randNum(0,self.margin)
