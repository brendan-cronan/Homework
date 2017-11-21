from monsters.Monster import Monster
"""Persons help you by giving you candy.
Each piece of candy increases your health by 1 point.
A person can give you 1 piece of candy per turn.
Persons have 100 health and are not harmed by your attacks."""
class Person(Monster):
    def __init__(self):
        self.health = 100
        self.strength = -5
        self.margin = 0
        self.observers=[]
        self.name = "Person"

    def getHit(self,damage,weapon):
        return self.getHealth()

    def attack(self):
        return self.getStrength()
