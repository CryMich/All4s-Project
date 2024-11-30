from abc import ABC, abstractmethod

class KarmaCommand(ABC):
    def __init__(self, user):
        self.user = user

    @abstractmethod
    def execute(self):
        pass
