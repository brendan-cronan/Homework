from abc import ABCMeta, abstractmethod, ABC
from random import randint
from game.Observable import Observable
class Monster(ABC,Observable):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.health = 100
        self.strength = 0
        self.margin = 0
        self.name = "MONSTER"
    @abstractmethod
    def attack(self):
        pass

    def getHealth(self):
        return self.health


    @staticmethod
    def randNum(lowBound,upBound):
        return randint(lowBound,upBound)

    def printMonster(self):
        print('Name: {},\t Health: {:d}, Strength: {:d}, Atk Margin: {:d}'.format(self.name,self.health,self.strength,self.margin))
