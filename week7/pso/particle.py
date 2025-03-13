import random
import copy

class Particle:

    def __init__(self, bounds: list[tuple[int, int]], objective_function, initial_position: list[float] = None):
        self.__dimensions = len(bounds)
        self.__bounds = bounds
        self.__objective_function = objective_function
        if initial_position:
            self.__position = initial_position
        else:
            self.__position = [random.randint(bound[0], bound[1]) for bound in self.__bounds]
        self.__velocity = 0
        self.__p_best_position = copy.deepcopy(self.__position)

    def objective_function(self):
        pass
        # a callback function

    def p_best_position(self) -> list[float]:
        pass
        # particles personal best position

    def p_best_value(self) -> float:
        pass