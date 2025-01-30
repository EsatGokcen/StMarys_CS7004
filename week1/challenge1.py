# Rule Engine
# Challenge asks to implement a simple rule based system
# using lambda functions

class RuleEngine():

    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "Default"


def main():
    engine = RuleEngine()
    engine.add_rule(lambda x: x < 12570, "0% tax")
    engine.add_rule(lambda x: 12570 < x < 50270, "20% tax")
    engine.add_rule(lambda x: 50270 < x < 125140, "40% tax")
    engine.add_rule(lambda x: x < 125140, "45% tax")

    answer = int(input("What is your annual income? "))

    result = engine.apply_rules(answer)
    print(result)

if __name__ == '__main__':
    main()