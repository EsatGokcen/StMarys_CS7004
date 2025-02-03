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
        for rule in self.__rules:
            for conditions, result in rule:
                if all(condition in self.__facts for condition in conditions):
                    return result
                return "Default"

def main():
    expert_system = WeatherExpertSystem()

    n_facts = int(input("How many facts would you like to enter?: "))

    for count in range(n_facts):
        user_fact = input("Enter fact: ")
        expert_system.add_fact(user_fact)

    expert_system.add_rule(["high_temperature", "low_humidity"], "Comfortable")
    expert_system.add_rule(["low_temperature", "high_humidity"], "Uncomfortable")
    expert_system.add_rule(["high_temperature", "high_wind"], "Comfortable")
    expert_system.add_rule(["low_temperature", "high_wind"], "Uncomfortable")

    result = expert_system.infer()
    print(result)

if __name__ == '__main__':
    main()