from typing import List
from week5and6.model.agent import Agent
from week5and6.model.environment import Environment
from week5and6.model.location import Location


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

    def find_free_locations(self, location: Location) -> List[Location]:
        x = location.get_x()
        y = location.get_y()

        free_locations = []

        for offset_y in range(-1, 2):
            for offset_x in range(-1, 2):
                loc_x = x + offset_x
                loc_y = y + offset_y

                if loc_x < 0:
                    loc_x = self.get_width() - 1

                if loc_y < 0:
                    loc_y = self.get_height() - 1

                if loc_x >= self.get_width():
                    loc_x = 0

                if loc_y >= self.get_height():
                    loc_y = 0

                if self.__grid[loc_y][loc_x] is None:
                    free_locations.append(Location(loc_x, loc_y))

        return free_locations