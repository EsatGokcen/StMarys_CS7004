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

    # Add travel-related rules with different regex commands
    engine.add_rule(r"\bhello\b",
                         "Hi there! What type of places do you like travelling to?")
    engine.add_rule(r"\b(bye|goodbye)\b",
                         "Goodbye! Feel free to return for more travel suggestions.")
    engine.add_rule(r"\bhow are you\b",
                         "I'm just a travel bot, but I'm here to help you plan your next adventure!")
    engine.add_rule(r"\b(?:what|which)\s+places?\s+(should|can)\s+I\s+visit\b",
                         "I can suggest some amazing destinations for you!")
    engine.add_rule(r"\b(?:recommend|suggest)\s+a\s+destination\b",
                         "Sure! What type of travel experience are you looking for?")
    engine.add_rule(r"\b(?:thank you|thanks)\b",
                         "You're welcome! Enjoy your travels.")
    engine.add_rule(r"\b(?:beach|mountain|city|countryside)\b",
                         "Excellent! Let me tailor my recommendations to your preferred travel style.")
    engine.add_rule(r"\b(?:hotel|flight|activity)\s+recommendation\b",
                         "I enjoy discussing travel accommodations and activities!")

    while True:
        user_input = input("You: ")
        response = engine.apply_rules(user_input)
        print(response)

        if "goodbye" in user_input.lower():
            break
        if "bye" in user_input.lower():
            break
        if "q" in user_input.lower():
            break

if __name__ == '__main__':
    main()
