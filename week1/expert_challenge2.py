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

def main():
    # Example Usage:
    tech_support_system = TechSupportExpertSystem()

    # User reports an issue with slow performance
    tech_support_system.report_issue("Performance", "The device is running slow.")

    # User reports an issue with connectivity
    tech_support_system.report_issue("Connectivity", "Unable to connect to the internet.")

    # Define rules for troubleshooting
    tech_support_system.add_rule(["Performance"], "Clear temporary files and optimize settings.")
    tech_support_system.add_rule(["Connectivity"], "Check network cables and restart the router.")

    # Run troubleshooting
    print(tech_support_system.troubleshoot())

if __name__ == '__main__':
    main()