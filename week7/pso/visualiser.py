import matplotlib.pyplot as plt


class Visualiser:
    def __init__(self, bounds, treasure_location):
        self.__bounds = bounds
        self.__treasure_location = treasure_location
        self.__fig, self.__ax = plt.subplots()
        self.__swarm_plot = None

    def setup(self):
        # Configure axis limits, aspect ratio, and labels
        self.__ax.set(xlim=self.__bounds[0], ylim=self.__bounds[1],
                      aspect='equal', title="Treasure Hunt - PSO Visualisation",
                      xlabel="X", ylabel="Y")
        # Plot the treasure marker
        self.__ax.plot(*self.__treasure_location, marker="*", color="gold",
                       markersize=15, label="Treasure")
        # Add a legend for the treasure marker
        self.__ax.legend()

    def update(self, particle_positions):
        # Clear the swarm plot
        if self.__swarm_plot:
            self.__swarm_plot.remove()

        # Extract x and y coordinates from particle positions and plot them
        x_positions, y_positions = zip(*particle_positions)
        self.__swarm_plot, = self.__ax.plot(x_positions, y_positions, "bo", markersize=8)

        # Pause briefly to update the plot
        plt.pause(0.5)
