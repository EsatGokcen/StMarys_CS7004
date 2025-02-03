# Program a weather expert system that has facts as well as rules

class WeatherExpertSystem:

    def __init__(self):
        self.__facts = set()
        self.__rules = []

    def add_fact(self, fact):
        self.__facts.add(fact)

    def add_rule(self, conditions, result):
        self.__rules.append((conditions,result))