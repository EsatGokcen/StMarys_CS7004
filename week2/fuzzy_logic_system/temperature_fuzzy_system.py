import matplotlib.pyplot as plt


class TemperatureFuzzySystem:

    def __init__(self):
        self.__memberships = {
            "very cold" : lambda temp: max(0, 1 - abs((temp - 0) / 10)), #max(0, 1 - abs((temp - peak) / 10))
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
        cold_y = []
        warm_y = []
        hot_y = []
        very_hot_y = []

        for temp in x:
            very_cold_y.append(self.__memberships["very cold"](temp))
            cold_y.append(self.__memberships["cold"](temp))
            warm_y.append(self.__memberships["warm"](temp))
            hot_y.append(self.__memberships["hot"](temp))
            very_hot_y.append(self.__memberships["very hot"](temp))

        # MatPlotLib Graph
        plt.plot(x, very_cold_y, very_cold_ylabel="Very Cold", color='b')
        plt.plot(x, cold_y, label="Cold", color='g')
        plt.plot(x, warm_y, label="Warm", color='o')
        plt.plot(x, hot_y, label="Hot", color='r')
        plt.plot(x, very_hot_y, label="Very Hot", color='p')
        plt.title("Membership Functions for Linguistic Terms")
        plt.xlabel("Temperature")
        plt.ylabel("Membership Degree")
        plt.legend(["Very Cold", "Cold", "Warm", "Hot", "Very Hot"])
        plt.legend()
        plt.show()