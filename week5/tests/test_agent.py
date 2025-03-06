import unittest
from week5.model.location import Location
from week5.model.agent import Agent


class TestAgent(unittest.TestCase):
    """
    Unit tests for the Agent class.
    """

    def test_get_location(self):
        """
        Test getting location for Agent objects.
        """
        location = Location(3, 4)
        agent = Agent(location)

        self.assertEqual(agent.get_location(), location)

    def test_set_location(self):
        """
        Test setting location for Agent objects.
        """
        location = Location(3, 4)
        agent = Agent(location)

        new_location = Location(5, 6)
        agent.set_location(new_location)

        self.assertEqual(agent.get_location(), new_location)

    def test_location_attributes(self):
        """
        Test location attributes for Agent objects.
        """
        location = Location(3, 4)
        agent = Agent(location)

        self.assertEqual(agent.get_location().get_x(), 3)
        self.assertEqual(agent.get_location().get_y(), 4)

    def test_location_setters(self):
        """
        Test location setters for Agent objects.
        """
        location = Location(3, 4)
        agent = Agent(location)

        agent.get_location().set_x(5)
        agent.get_location().set_y(6)

        self.assertEqual(agent.get_location().get_x(), 5)
        self.assertEqual(agent.get_location().get_y(), 6)

if __name__ == '__main__':
    unittest.main()