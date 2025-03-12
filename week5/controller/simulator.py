import time

from week5.view.gui import Gui
from week5.model.ocean import Ocean


class Simulator:
    """Class representing a simulator."""

    def __init__(self) -> None:
        """
        Initialise the Simulator object.

        Initialises the environment, and generates the initial population of agents.
        """
        self.__ocean = Ocean()
        self.__agents = []
        self.__generate_initial_population()
        self.__is_running = False

        # TODO: Define a dictionary, agent_colours, containing colours for each agent (class name - colour string pairs)
        # TODO: Initialise a new Gui object
        # TODO: Render the Gui by invoking the appropriate method

    def __generate_initial_population(self) -> None:
        """
        Generate the initial population of agents.
        """
        # TODO: Generate the initial population
        pass

    def run(self) -> None:
        """Run the simulation."""
        self.__is_running = True

        while self.__is_running:
            self.__update()
            self.__render()
            time.sleep(1)
            if self.__gui.is_closed():
                self.__is_running = False

    def __render(self) -> None:
        """Render the current state of the simulation."""
        # TODO: Render the Gui by invoking the appropriate method

    def __update(self) -> None:
        """Update the simulation state."""
        # TODO: Invoke the act method for each agent