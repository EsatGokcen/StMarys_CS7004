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

def main():
    expert_system = WeatherExpertSystem()
    expert_system.add_fact("high_temperature")  # Example: High temperature
    expert_system.add_fact("low_humidity")  # Example: Low humidity
    expert_system.add_rule(["high_temperature", "low_humidity"], "Comfortable")

    result = expert_system.infer()
    print(result)

if __name__ == '__main__':
    main()