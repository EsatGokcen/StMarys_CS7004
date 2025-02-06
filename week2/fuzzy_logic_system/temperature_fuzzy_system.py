import matplotlib.pyplot
import matplotlib.pyplot as plt


class TemperatureFuzzySystem:

    def __init__(self):
        self.__memberships = {
            "very cold" : lambda temp: max(-10, 1 - abs((temp - 0) / 10)), #max(lower boundry, 1 - abs((temp - peak) / 10))
            "cold" : lambda temp: max(0, 1 - abs((temp - 10) / 10)),
            "warm" : lambda temp: max(10, 1 - abs((temp - 20) / 10)),
            "hot" : lambda temp: max(20, 1 - abs((temp - 30) / 10)),
            "very hot" : lambda temp: max(30, 1 - abs((temp - 40) / 10))
        }

    def plot_membership_functions(self, temp_range: tuple[int, int] = (0,50)):
        x = temp_range[0]
        y = temp_range[1]

        plt.plot(x, y)
        plt.title("Membership Functions for Linguistic Terms")
        plt.xlabel("Temperature")
        plt.ylabel("Membership Degree")
        plt.legend("Legend")