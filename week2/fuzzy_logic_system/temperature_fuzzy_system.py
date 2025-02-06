import matplotlib.pyplot as plt


class TemperatureFuzzySystem:

    def __init__(self):
        self.__memberships = {
            "very cold" : lambda temp: max(0, 1 - abs((temp - 0) / 10)), #max(lower boundry, 1 - abs((temp - peak) / 10))
            "cold" : lambda temp: max(0, 1 - abs((temp - 10) / 10)),
            "warm" : lambda temp: max(0, 1 - abs((temp - 20) / 10)),
            "hot" : lambda temp: max(0, 1 - abs((temp - 30) / 10)),
            "very hot" : lambda temp: max(0, 1 - abs((temp - 40) / 10))
        }

    def plot_membership_functions(self, temp_range: tuple[int, int] = (0,50)):
        lower_bound = temp_range[0]
        upper_bound = temp_range[1]
        x = range(lower_bound, upper_bound + 1)

        very_cold_y = []
        for temp in x:
            very_cold_y.append(self.__memberships["very cold"](temp))

        # MatPlotLib Graph
        plt.plot(x, very_cold_y)
        plt.title("Membership Functions for Linguistic Terms")
        plt.xlabel("Temperature")
        plt.ylabel("Membership Degree")
        plt.legend(["Very Cold", "Cold", "Warm", "Hot", "Very Hot"])
        plt.plot(x, very_cold_y, label='Line 1')
        plt.legend()
        plt.show()