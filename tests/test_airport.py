import unittest
from mock import Mock
from src.airport import Airport

class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Mock(return_value='Plane')

    def test_land_plane_stores_plane_in_array(self):
        self.airport.land(self.plane)
        self.assertEqual(self.airport.hanger, [self.plane])

    def test_take_off_stores_plane_in_array(self):
        self.airport.land(self.plane)
        self.airport.take_off(self.plane)
        self.assertEqual(self.airport.hanger, [])

if __name__ == "__main__":
    unittest.main()
