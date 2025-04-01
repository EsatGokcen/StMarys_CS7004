import random
from typing import List, Callable, Tuple


class Particle:

    def __init__(self, bounds: List[Tuple[float, float]], objective_function: Callable[[List[float]], float]) -> None:
        self.__dimensions: int = len(bounds)
        self.__bounds: List[Tuple[float, float]] = bounds
        self.__position: List[float] = [random.uniform(lower, upper) for lower, upper in bounds]
        self.__velocity: List[float] = [0.0 for _ in range(self.__dimensions)]
        self.__objective_function = objective_function
        self.__p_best_position: List[float] = self.__position.copy()
        self.__p_best_value: float = float('inf')

    def evaluate(self) -> None:
        fitness_value = self.__objective_function(self.__position)

        if fitness_value < self.__p_best_value:
            self.__p_best_value = fitness_value
            self.__p_best_position = self.__position.copy()

    def update_velocity(self, g_best_position: List[float], w: float, c1: float, c2: float) -> None:
        for i in range(self.__dimensions):
            r1, r2 = random.random(), random.random()

            inertia_velocity = w * self.__velocity[i]
            cognitive_velocity = c1 * r1 * (self.__p_best_position[i] - self.__position[i])
            social_velocity = c2 * r2 * (g_best_position[i] - self.__position[i])

            self.__velocity[i] = inertia_velocity + cognitive_velocity + social_velocity

    def update_position(self) -> None:
        for index in range(self.__dimensions):
            self.__position[index] += self.__velocity[index]

            lower, upper = self.__bounds[index]
            if self.__position[index] < lower:
                self.__position[index] = lower
            elif self.__position[index] > upper:
                self.__position[index] = upper

    def get_position(self) -> List[float]:
        return self.__position

    def get_velocity(self) -> List[float]:
        return self.__velocity

    def get_p_best_position(self) -> List[float]:
        return self.__p_best_position

    def get_p_best_value(self) -> float:
        return self.__p_best_value
