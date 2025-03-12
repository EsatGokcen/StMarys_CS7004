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

    def __init_gui(self):
        """Initialise GUI settings."""
        self.title(Config.simulation_name)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def __init_info(self):
        """Initialise the legend panel."""
        self.legend_panel = tk.Frame(self)
        self.legend_panel.grid(row=0, column=0)

    def __init_world(self):
        """Initialise the world grid."""
        self.grid_frame = tk.Frame(self)
        self.grid_frame.grid(row=1, column=0)

        # TODO: Redraw the grid

    def update_legend(self):
        """Update the legend panel with agent counts."""
        agent_counts = {}

        # Iterate over all cells in the environment grid
        for row_index in range(self.__environment.get_height()):
            for col_index in range(self.__environment.get_width()):
                agent = self.__environment.get_agent(Location(col_index, row_index))

                # Count the occurrences of each type of agent
                if agent:
                    agent_class = agent.__class__
                    agent_counts[agent_class] = agent_counts.get(agent_class, 0) + 1

        # Clear the legend panel
        for widget in self.legend_panel.winfo_children():
            widget.destroy()

        # Update the legend panel with agent counts
        sorted_counts = sorted(agent_counts.items(), key=lambda x: x[0].__name__)

        for agent_class, count in sorted_counts:
            color_label = tk.Label(self.legend_panel, bg=self.__agent_colours[agent_class], width=2, height=1)
            color_label.pack(side=tk.LEFT)

            label_text = agent_class.__name__ + " (" + str(count) + ")"
            label = tk.Label(self.legend_panel, text=label_text)
            label.pack(side=tk.LEFT)

    def on_closing(self):
        """Handle closing of the GUI window."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.__closed = True
            self.destroy()

    def is_closed(self) -> bool:
        """Check if the GUI window is closed."""
        return self.__closed