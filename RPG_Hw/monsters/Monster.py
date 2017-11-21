from abc import ABCMeta, abstractmethod, ABC
from random import randint
from game.Observable import Observable
"""
    This is the abstract class for the monsters and has all of the methods that
    are not specific to these monsters.

    Implements the Observable behavior for them as well.

"""
class Monster(ABC,Observable):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.health = 100
        self.strength = 0
        self.observers=[]
        self.margin = 0
        self.name = "MONSTER"
    @abstractmethod
    def attack(self):#pass on these two since they are specific
        pass
    @abstractmethod
    def getHit(self,damage,weapon):
        pass

    #getters
    def getHealth(self):
        return self.health
    def getStrength(self):
        return self.strength
    def getMargin(self):
        return self.margin
    def getName(self):
        return self.name

    #stupid function i didnt use
    @staticmethod
    def randNum(lowBound,upBound):
        return randint(lowBound,upBound)
    #upon death, update observers
    def die(self):
        self.update_observers(self)
    #basic info to display to user.
    def __str__(self):
        return "{}, ".format(self.name)
    #prints extended info.
    def printMonster(self):
        print('Name: {},\t Health: {:d}, Strength: {:d}, Atk Margin: {:d}'.format(self.name,self.health,self.strength,self.margin))
