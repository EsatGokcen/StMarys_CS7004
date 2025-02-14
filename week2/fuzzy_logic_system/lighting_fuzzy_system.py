class SmartHomeLighting:

    def __init__(self):
        # Fuzzy rules
        self.rules = {
            'brighten': [('low', 'partially_occupied'), ('low', 'fully_occupied')],
            'maintain': [('medium', 'partially_occupied')],
            'dim': [('high', 'unoccupied'), ('high', 'partially_occupied')]
        }