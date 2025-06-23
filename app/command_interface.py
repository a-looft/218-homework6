from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def execute(self, *args) -> str:
        pass
