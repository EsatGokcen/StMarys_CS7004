from particle import Particle


class Swarm:
    def __init__(self, num_particles: int, bounds: list[tuple[float, float]], objective_function: callable):
        self.__particles = [Particle(bounds, objective_function) for _ in range(num_particles)]
        self.__g_best_position = None
        self.__g_best_value = float('inf')

    def evaluate_particles(self):
        for particle in self.__particles:
            particle.evaluate()
            if particle.get_p_best_value() < self.__g_best_value:
                self.__g_best_value = particle.get_p_best_value()
                self.__g_best_position = particle.get_p_best_position()

    def update_particles(self, w: float, c1: float, c2: float):
        for particle in self.__particles:
            particle.update_velocity(self.__g_best_position, w, c1, c2)
            particle.update_position()

    def get_particles(self):
        return self.__particles

    def get_best_solution(self):
        return self.__g_best_position, self.__g_best_value
