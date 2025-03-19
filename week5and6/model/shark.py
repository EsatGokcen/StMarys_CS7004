from week5and6.model.agent import Agent
from week5and6.model.location import Location
from week5and6.model.ocean import Ocean


class Shark(Agent):

    def __init__(self, location: Location):
        super().__init__(location)

    def act(self, ocean: Ocean):
        # The swim method should be invoked by the act method and pass the ocean object to it.
        pass

    def __swim(self):
        # moves the shark to a free adjacent location
        pass
