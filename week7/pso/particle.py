"""
    def __init__(self, dimensions: int, bounds: str, position: list[float], velocity: list[float]):
        self.dimensions = dimensions
        self.bounds = bounds
        self.position = position
        self.velocity = velocity
        self.objective_function()
"""

class Particle:

    def __init__(self, objective_function, bounds_for_dimensions: list[tuple[str, int, int]] = [["x", 0, 4], ["y", 0, 4]], initial_position: list[float] = [0.0, 0.0]):
        self.dimensions = bounds_for_dimensions[0][0], bounds_for_dimensions[1][0]
        self.bounds = bounds_for_dimensions[0][1], bounds_for_dimensions[0][2], bounds_for_dimensions[1][1], bounds_for_dimensions[1][2]
        self.objective_function = objective_function
        self.position = initial_position


    def objective_function(self):
        pass
        # a callback function

    def p_best_position(self) -> list[float]:
        pass
        # particles personal best position

    def p_best_value(self) -> float:
        pass