from monsters.Monster import Monster
class Person(Monster):
    def __init__(self):
        self.health = Monster.randNum(100,200)
        self.strength = 10
        self.margin = 10
        self.name = "Person"

    def attack(self):
        return self.strength + randNum(0,self.margin)
