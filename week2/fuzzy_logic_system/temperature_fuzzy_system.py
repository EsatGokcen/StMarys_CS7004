
class TemperatureFuzzySystem:

    def __init__(self):
        self.__memberships = {
            "very cold" : lambda temp: max(-10, 1 - abs((temp - 10) / 10)),
            "cold" : lambda temp: max(0, 1 - abs((temp - 10) / 10)),
            "warm" : lambda temp: max(10, 1 - abs((temp - 10) / 10)),
            "hot" : lambda temp: max(20, 1 - abs((temp - 10) / 10)),
            "very hot" : lambda temp: max(30, 1 - abs((temp - 10) / 10))
        }

