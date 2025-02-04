# Backward Chaneling
# Implement an expert system with backward chaining for a loan eligibility expert system.
# The goal is to be eligible for a loan (e.g., mortgage or personal loan).
# Eligibility is based on income thresholds and credit rating.

class LoanEligibilitySystem:
    def __init__(self):
        self.facts = {}
        self.rules = []