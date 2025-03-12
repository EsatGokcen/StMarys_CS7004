from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import TYPE_CHECKING

from week5.controller.config import Config
from week5.model.location import Location

if TYPE_CHECKING:
    from week5.model.environment import Environment


class Gui(tk.Tk):
    """
    Graphical User Interface (GUI) for visualising the simulation environment.

    Attributes:
        __environment (Environment): The environment instance to visualise.
        __agent_colours (dict): A dictionary mapping agent classes to their corresponding colors.
        __legend_panel (tk.Frame): The legend panel displaying agent types and their counts.
        __closed (bool): Flag indicating whether the GUI window is closed.
    """

    def __init__(self, environment: Environment, agent_colours: dict):
        """
        Initialise the GUI with the given environment and agent colours.

        Args:
            environment (Environment): The environment instance to visualise.
            agent_colours (dict): A dictionary mapping agent classes to their corresponding colors.
        """
        super().__init__()
        self.__environment = environment
        self.__agent_colours = agent_colours
        self.__legend_panel = None
        self.__closed = False

        self.__init_gui()
        self.__init_info()
        self.__init_world()

    def render(self):
        """Render the current state of the environment."""
        self.update_legend()

        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        for row_index in range(self.__environment.get_height()):
            row = []
            for col_index in range(self.__environment.get_width()):
                agent = self.__environment.get_agent(Location(col_index, row_index))

                # TODO: Set the current agent colour

                # TODO: Create a new Canvas object with appropriate attributes (width, height, background colour, border width, relief set to "solid")

                # TODO: Add the cell to the grid

                # TODO: Add the cell to the row

        self.update()
        self.update_idletasks()