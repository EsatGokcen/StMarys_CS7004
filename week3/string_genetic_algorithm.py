import random
import string


class StringGeneticAlgorithm:

    def __init__(self, target: str = "hello", population_size: int = 10, mutation_probability: int = 0.5):
        self.__target = target
        self.__population = []
        self.__population_size = population_size
        self.__mutation_probability = mutation_probability

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

    def __cross_over(self, pairs):
        offsprings = []
        for pair in pairs:
            cross_over_point = len(self.__target) // 2
            offspring = pair[0][:cross_over_point] + pair[1][cross_over_point:]
            offsprings.append(offspring)
        return offsprings

    def __mutation(self, offsprings):
        mutated_offsprings = []
        for offspring in offsprings:
            probability = random.random()
            if probability < self.__mutation_probability:
                random_letter = random.choice(string.ascii_lowercase)
                random_index = random.randint(0, len(offspring)-1)
                mutated_offspring = offspring[:random_index] + random_letter + offspring[random_index+1:]
                mutated_offsprings.append(mutated_offspring)
            else:
                mutated_offsprings.append(offspring)
        return mutated_offsprings

    def run(self):
        self.__initialise_population()
        fitness_scores = dict()
        for candidate in self.__population:
            fitness_scores.update({candidate: self.__fitness(candidate)})

        probabilities = []
        total_score = sum(fitness_scores.values())
        for score in fitness_scores.values():
            probabilities.append(score / total_score)

        pairs = self.__selection(probabilities)
        offsprings = self.__cross_over(pairs)
        print(offsprings)
        mutated_offsprings = self.__mutation(offsprings)
        print(mutated_offsprings)