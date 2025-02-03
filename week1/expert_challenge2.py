# Program a technical troubleshooting system
# The system should store common issues that have a category and description
# The system should respond with a solution depending on category and description

class TechSupportExpertSystem:

    def __init__(self):
        self.user_reports = {}
        self.rules = []

    def report_issue(self, category, description):
        self.user_reports[category] = description

    def add_rule(self, conditions, solution):
        self.rules.append({"conditions": conditions, "solution": solution})

    def troubleshoot(self):
        for rule in self.rules:
            conditions_met = all(self.user_reports[condition] for condition in rule["conditions"])

            if conditions_met:
                return f"Suggested solution: {rule['solution']}"

        return "No specific solution found for the reported issue."