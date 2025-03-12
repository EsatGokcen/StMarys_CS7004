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