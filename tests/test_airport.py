import unittest
from mock import Mock
from src.airport import Airport

class TestAirport(unittest.TestCase):
    def test_dummy_test(self):
        """ Dummy test to ensure unittest functioning """

        airport = Airport()
        plane = Mock(return_value='Plane')
        result = airport.land(plane)
        self.assertEqual(result, plane)

if __name__ == "__main__":
    unittest.main()
