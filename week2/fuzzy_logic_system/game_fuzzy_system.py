class GameFuzzySystem:

    def __init__(self):
        self.__energy = {
            "low" : [0, 30],
            "medium" : [31, 70],
            "high" : [71, 100]
        }
        self.__proximity = {
            "close" : [0, 30],
            "medium" : [31, 70],
            "far" : [71, 100]
        }
        self.__rules = {
            () : "attack",
            () : "defend",
            () : "run away"
        }

