from abc import ABC, abstractmethod

class Input(ABC):
    @abstractmethod
    def get_string(self, message):
        pass