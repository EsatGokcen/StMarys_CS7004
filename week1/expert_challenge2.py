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
