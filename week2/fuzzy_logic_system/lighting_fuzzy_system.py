class SmartHomeLighting:

    def __init__(self):
        # Fuzzy rules
        self.rules = {
            'brighten': [('low', 'partially_occupied'), ('low', 'fully_occupied')],
            'maintain': [('medium', 'partially_occupied')],
            'dim': [('high', 'unoccupied'), ('high', 'partially_occupied')]
        }

        # Membership functions for ambient light level
        self.light_memberships = {
            'low': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'medium': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'high': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

        # Membership functions for room occupancy
        self.occupancy_memberships = {
            'unoccupied': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'partially_occupied': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'fully_occupied': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

    def __fuzzify(self, value, memberships):
        # Fuzzification: Calculate membership degrees for each linguistic term
        return {term: func(value) for term, func in memberships.items()}

    def __infer(self, fuzzified_light, fuzzified_occupancy):
        # Inference: Apply rules based on fuzzified values of light level and occupancy
        brighten_degree = max(
            min(fuzzified_light[light], fuzzified_occupancy[occupancy])
            for light, occupancy in self.rules['brighten']
        )
        maintain_degree = max(
            min(fuzzified_light[light], fuzzified_occupancy[occupancy])
            for light, occupancy in self.rules['maintain']
        )
        dim_degree = max(
            min(fuzzified_light[light], fuzzified_occupancy[occupancy])
            for light, occupancy in self.rules['dim']
        )
        return {'brighten': brighten_degree, 'maintain': maintain_degree, 'dim': dim_degree}