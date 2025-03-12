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