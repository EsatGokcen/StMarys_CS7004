# Program a weather expert system that has facts as well as rules

class WeatherExpertSystem:

    def __init__(self):
        self.__facts = set()
        self.__rules = []

    def add_fact(self, fact):
        self.__facts.add(fact)

    def add_rule(self, conditions, result):
        self.__rules.append((conditions,result))

    def infer(self):
        for conditions, result in self.__rules:
            if all(condition in self.__facts for condition in conditions):
                return result
            return "Default"