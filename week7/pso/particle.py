class Particle:

    def __init__(self, dimensions: int, bounds: str, position: list[float], velocity: list[float]):
        self.dimensions = dimensions
        self.bounds = bounds
        self.position = position
        self.velocity = velocity
        self.objective_function()

    def objective_function(self):
        pass
        # a callback function

    def p_best_position(self) -> list[float]:
        pass
        # particles personal best position

    def p_best_value(self) -> float:
        pass