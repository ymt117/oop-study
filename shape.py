from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def contains(self):
        pass