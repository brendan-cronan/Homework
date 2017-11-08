from abc import ABCMeta, abstractmethod, ABC
from random import randint

class Monster(ABC):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.health=100
        self.strength=0
        self.margin=0
        print("Parent!")

    def attack(self):
        pass

    @staticmethod
    def randNum(lowBound,upBound):
        return randint(lowBound,upBound)
