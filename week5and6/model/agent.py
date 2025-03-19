from abc import ABC, abstractmethod
from week5and6.model.location import Location
from week5and6.model.ocean import Ocean


class Agent(ABC):
    def __init__(self, location: Location) -> None:
        self.__location = location

    def set_location(self, location: Location) -> None:
        self.__location = location

    def get_location(self) -> Location:
        return self.__location

    @abstractmethod
    def act(self, ocean: Ocean):
        pass