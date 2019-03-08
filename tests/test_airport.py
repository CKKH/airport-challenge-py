import unittest
from src.airport import Airport

class TestAirport(unittest.TestCase):
    def test_dummy_test(self):
        """ Dummy test to ensure unittest functioning """

        airport = Airport()
        result = airport.hello_world()
        self.assertEqual(result, 'hello, world')

if __name__ == "__main__":
    unittest.main()
