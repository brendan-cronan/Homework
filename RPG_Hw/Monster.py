from abc import ABC, abstractmethod
from random import randint
class Monster(ABC):
    def __init__(health, strength):
        self.health=health
        self.strength=strength

    def randNum(lowVal,highVal):
        return randInt(lowVal,highVal)
    
