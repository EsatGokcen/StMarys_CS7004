from typing import List
from week5.model.agent import Agent
from week5.model.environment import Environment
from week5.model.location import Location


class Ocean(Environment):
    """
    Represents an ocean environment.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initialises an Ocean object with the given width and height.

        Args:
            width (int): The width of the ocean grid.
            height (int): The height of the ocean grid.
        """
        super().__init__(width, height)
        self.__grid = [[None for _ in range(width)] for _ in range(height)]