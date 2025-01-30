# Challenge 2
# Create a simple rule based chatbot

class RuleEngine():

    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"] in text.lower():
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."

def main():
    engine = RuleEngine()
    engine.add_rule("hello", "Hi there!")
    engine.add_rule("goodbye", "Goodbye!")

    while True:
        user_input = input("You: ")
        response = engine.apply_rules(user_input)
        print(response)

        if user_input.lower() == "goodbye":
            break

if __name__ == '__main__':
    main()