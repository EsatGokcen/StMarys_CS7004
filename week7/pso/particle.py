"""
    def __init__(self, dimensions: int, bounds: str, position: list[float], velocity: list[float]):
        self.dimensions = dimensions
        self.bounds = bounds
        self.position = position
        self.velocity = velocity
        self.objective_function()
"""
import random

class Particle:

    def __init__(self, bounds: list[tuple[int, int]], objective_function, initial_position: list[float] = None):
        self.dimensions = len(bounds)
        self.bounds = bounds
        self.objective_function = objective_function
        if initial_position:
            self.position = initial_position
        else:
            self.position = [random.randint(bound[0], bound[1]) for bound in self.bounds]
        self.velocity = 0


    def objective_function(self):
        pass
        # a callback function

    def p_best_position(self) -> list[float]:
        pass
        # particles personal best position

    def p_best_value(self) -> float:
        pass