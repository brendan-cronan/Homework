from abc import ABCMeta, abstractmethod, ABC
from random import randint

class Monster(ABC):
    __metaclass__ = ABCMeta

    def __init__(self):
        print("Parent!")
