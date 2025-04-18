class FuzzyGame:

    def __init__(self):
        # Fuzzy rules
        self.rules = {
            'attack': [('high', 'close'), ('high', 'medium')],
            'defend': [('medium', 'close'), ('low', 'medium')],
            'run_away': [('low', 'close'), ('medium', 'far')]
        }

        # Membership functions for energy (Low, Medium, High)
        self.energy_memberships = {
            'low': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'medium': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'high': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

        # Membership functions for proximity (Close, Medium, Far)
        self.proximity_memberships = {
            'close': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'medium': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'far': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

    def __fuzzify(self, value, memberships):
        # Fuzzification: Calculate membership degrees for each linguistic term
        return {term: func(value) for term, func in memberships.items()}

    def __infer(self, fuzzified_energy, fuzzified_proximity):
        # Inference: Apply rules based on fuzzified values of energy and proximity
        attack_degree = max(
            min(fuzzified_energy[energy], fuzzified_proximity[proximity])
            for energy, proximity in self.rules['attack']
        )
        defend_degree = max(
            min(fuzzified_energy[energy], fuzzified_proximity[proximity])
            for energy, proximity in self.rules['defend']
        )
        run_away_degree = max(
            min(fuzzified_energy[energy], fuzzified_proximity[proximity])
            for energy, proximity in self.rules['run_away']
        )
        return {'attack': attack_degree, 'defend': defend_degree, 'run_away': run_away_degree}

    def __defuzzify(self, inferred_actions):
        # Defuzzification: Choose the action with the highest membership degree
        return max(inferred_actions, key=inferred_actions.get)

    def decide_action(self, energy, proximity):
        # Fuzzification for energy and proximity
        fuzzified_energy = self.__fuzzify(energy, self.energy_memberships)
        fuzzified_proximity = self.__fuzzify(proximity, self.proximity_memberships)

        # Inference: Apply rules to determine the action
        inferred_actions = self.__infer(fuzzified_energy, fuzzified_proximity)

        # Defuzzification: Choose the final action
        return self.__defuzzify(inferred_actions)


if __name__ == "__main__":
    game = FuzzyGame()

    # Test with different combinations of energy and proximity
    test_cases = [
        (10, 20),  # Low energy, Close proximity
        (40, 50),  # Medium energy, Medium proximity
        (80, 30),  # High energy, Close proximity
        (25, 80),  # Low energy, Far proximity
        (70, 90),  # Medium energy, Far proximity
        (90, 20)  # High energy, Close proximity
    ]

    for energy, proximity in test_cases:
        action = game.decide_action(energy, proximity)
        print(f"Energy: {energy}, Proximity: {proximity} -> Action: {action}")
