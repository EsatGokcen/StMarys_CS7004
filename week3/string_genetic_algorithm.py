import random
import string


class StringGeneticAlgorithm:

    def __init__(self, target: str = "hello", population_size: int = 100):
        self.__target = target
        self.__population = []
        self.__population_size = population_size

    def initialise_population(self):
        for _ in range(self.__population_size):
            random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(len(self.__target)))
            self.__population.append(random_string)

    def constructor(self):
        pass