from abc import ABC, abstractmethod

class Output(ABC):
    @abstractmethod
    def display(self, message):
        pass