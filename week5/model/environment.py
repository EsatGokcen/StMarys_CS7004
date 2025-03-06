from abc import ABC, abstractmethod
from week5.model.agent import Agent
from week5.model.location import Location


class Environment(ABC):
    """
    Abstract base class representing an environment.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initialises an Environment object with the given width and height.

        Args:
            width (int): The width of the environment grid.
            height (int): The height of the environment grid.
        """
        self.__width = width
        self.__height = height