# Challenge 3
# Create a simple chatbot using regex
# Regex = Regular Expressions, can be used by importing re

import re

class RuleEngine():

    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if re.search(rule["condition"], text, re.IGNORECASE):
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."

def main():
    engine = RuleEngine()

    engine.add_rule(r'\bhello\b', 'Hi there!')
    engine.add_rule(r'\bthank you\b', "You are welcome")
    engine.add_rule(r'\bgoodbye\b|\bbye\b', "Goodbye!")
    engine.add_rule(r'\bmy name is (.+?)\b', r'Nice to meet you!') # , {0} - did not work...

    while True:
        user_input = input("You: ")
        response = engine.apply_rules(user_input)
        print(response)

        if user_input.lower() == "goodbye":
            break
        if user_input.lower() == "bye":
            break
        if user_input == "q":
            break

if __name__ == '__main__':
    main()
