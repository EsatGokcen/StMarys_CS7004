import random
import string


class StringGeneticAlgorithm:

    def __init__(self, target: str = "hello", population_size: int = 100):
        self.__target = target
        self.__population = []
        self.__population_size = population_size

    def __initialise_population(self):
        for _ in range(self.__population_size):
            random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(len(self.__target)))
            self.__population.append(random_string)
        print(self.__population)

    def __fitness(self, candidate: str):
        score = 0
        for index in range(len(self.__target)):
            if self.__target[index] == candidate[index]:
                score += 1
        return score

    def __selection(self, probabilities):
        first_parents = random.choices(self.__population, weights=probabilities, k=self.__population_size)
        second_parents = random.choices(self.__population, weights=probabilities, k=self.__population_size)
        pairs = zip(first_parents, second_parents)
        return pairs

    def run(self):
        self.__initialise_population()
        fitness_scores = dict()
        for candidate in self.__population:
            fitness_scores.update({candidate: self.__fitness(candidate)})

        probabilities = []
        for score in fitness_scores.values():
            probabilities.append(score / len(self.__target))

        self.__selection(probabilities)