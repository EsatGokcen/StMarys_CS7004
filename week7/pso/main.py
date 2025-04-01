from matplotlib import pyplot as plt

from swarm import Swarm
from visualiser import Visualiser

# Declare treasure location
TREASURE_LOCATION = [3.0, 3.0]


def treasure_map(position: list[float]) -> float:
    return (position[0] - TREASURE_LOCATION[0]) ** 2 + (position[1] - TREASURE_LOCATION[1]) ** 2


def run():
    # Grid bounds and treasure location
    bounds = [(0.0, 10.0), (0.0, 10.0)]

    # Number of particles and PSO parameters
    num_hunters = 4
    inertia_weight = 0.7
    cognitive_coefficient = 1.5
    social_coefficient = 1.5
    max_iterations = 100

    # Create the swarm and visualiser
    swarm = Swarm(num_hunters, bounds, treasure_map)
    visualiser = Visualiser(bounds, TREASURE_LOCATION)
    visualiser.setup()

    # PSO loop with visualisation
    for iteration in range(max_iterations):
        swarm.evaluate_particles()
        swarm.update_particles(inertia_weight, cognitive_coefficient, social_coefficient)

        # Get the current positions of all particles
        particle_positions = [particle.get_position() for particle in swarm.get_particles()]
        visualiser.update(particle_positions)

        # Check for convergence
        _, best_value = swarm.get_best_solution()
        print(f"Iteration {iteration + 1}: Best value = {best_value:.4f}")

    plt.show()


if __name__ == "__main__":
    run()
