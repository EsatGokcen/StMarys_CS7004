from week5.model.location import Location


class Agent:
    def __init__(self, location: Location) -> None:
        """
        Constructor for the Agent class.

        Parameters:
        - location: A Location object representing the agent's initial location.
        """
        self.__location = location