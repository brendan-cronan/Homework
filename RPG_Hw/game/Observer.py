from abc import ABC, abstractmethod
"""
    You gave us this one
"""
class Observer(ABC):
    @abstractmethod
    def update(self,monster):
        pass
