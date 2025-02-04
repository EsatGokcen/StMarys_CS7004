# Backward Chaining
# Implement an expert system with backward chaining for a loan eligibility expert system.
# The goal is to be eligible for a loan (e.g., mortgage or personal loan).
# Eligibility is based on income thresholds and credit rating.

class LoanEligibilitySystem:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, fact_type, value):
        self.facts[fact_type] = value

    def add_rule(self, goal, conditions):
        self.rules.append({"goal": goal, "conditions": conditions})

    def check_loan_eligibility(self, goal):
        if not all(self.facts.values()):
            return "Incomplete financial information for evaluation."

        for rule in self.rules:
            if rule["goal"] == goal:
                conditions_met = all(self.facts[condition] >= threshold for condition, threshold in rule["conditions"].items())

                if conditions_met:
                    return f"The individual is eligible for a {goal} loan."

        return f"The individual is not eligible for a {goal} loan based on their financial situation."