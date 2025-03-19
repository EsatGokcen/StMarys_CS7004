import unittest
from week5and6.model.location import Location

class TestLocation(unittest.TestCase):
    """
    Unit tests for the Location class.
    """

    def test_init(self):
        """
        Test the initialisation of Location objects.
        """
        loc = Location(3, 4)
        self.assertEqual(loc.get_x(), 3)
        self.assertEqual(loc.get_y(), 4)

    def test_setters(self):
        """
        Test the setters of Location objects.
        """
        loc = Location(3, 4)
        loc.set_x(5)
        loc.set_y(6)
        self.assertEqual(loc.get_x(), 5)
        self.assertEqual(loc.get_y(), 6)

    def test_equals(self):
        """
        Test the equals method of Location objects.
        """
        loc1 = Location(3, 4)
        loc2 = Location(3, 4)
        loc3 = Location(5, 6)