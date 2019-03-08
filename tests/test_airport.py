import unittest
from mock import Mock
from src.airport import Airport

class TestAirport(unittest.TestCase):

    def test_land_plane_stores_plane_in_array(self):
        airport = Airport()
        plane = Mock(return_value='Plane')
        airport.land(plane)
        result = airport.hanger
        self.assertEqual(result, [plane])

    def test_take_off_stores_plane_in_array(self):
        airport = Airport()
        plane = Mock(return_value='Plane')
        airport.land(plane)
        airport.take_off(plane)
        result = airport.hanger
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
