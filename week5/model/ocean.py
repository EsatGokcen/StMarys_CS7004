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

    def clear(self):
        """Clears the ocean by removing all agents."""
        self.__grid = [[None for _ in range(self.get_width())] for _ in range(self.get_height())]

    def get_agent(self, location: Location):
        """
        Returns the agent at location in the ocean.

        Args:
            location (Location): The location of the agent.

        Returns:
            Agent: The agent at location in the ocean.
        """
        return self.__grid[location.get_y()][location.get_x()]

    def set_agent(self, agent: Agent, location: Location):
        """
        Sets the agent at position in the ocean.

        Args:
            agent (Agent): The agent to set.
            location (Location): The location to set the agent.
        """
        self.__grid[location.get_y()][location.get_x()] = agent