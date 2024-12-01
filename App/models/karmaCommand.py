from abc import ABC, abstractmethod

class KarmaCommand(ABC):
    def __init__(self, student):
        self.student = student

    @abstractmethod
    def execute(self):
        pass
