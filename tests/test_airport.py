import unittest
from mock import Mock
from src.airport import Airport
from src.plane import Plane

class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Mock(return_value='Plane')
        self.plane_two = Mock(return_value='Plane Two')
        self.plane_three = Mock(return_value='Plane Three')
        self.airport.land(self.plane)

    def test_land_plane_stores_plane_in_hanger(self):
        self.assertEqual(self.airport.hanger, [self.plane])

    def test_land_plane_raises_error_if_hanger_full(self):
        self.airport.land(self.plane_two)
        self.assertRaises(TypeError, self.airport.land, self.plane)

    def test_land_plane_raises_error_if_plane_grounded(self):
        self.plane.grounded = True
        self.assertRaises(TypeError, self.airport.land, self.plane)

    def test_take_off_removes_plane_from_hanger(self):
        self.airport.take_off(self.plane)
        self.assertEqual(self.airport.hanger, [])

    def test_take_off_returns_plane(self):
        self.assertEqual(self.airport.take_off(self.plane), self.plane)

    def test_take_off_raises_error_if_plane_not_grounded(self):
        self.plane_two.grounded = False
        self.assertEqual(self.airport.take_off(self.plane_two), "Cannot take off: plane not grounded")

    def test_take_off_raises_error_if_plane_not_grounded_at_that_airport(self):
        airport_2 = Airport()
        airport_2.land(self.plane_two)
        self.assertEqual(self.airport.take_off(self.plane_two), "Cannot take off: plane not grounded at this airport")

if __name__ == "__main__":
    unittest.main()
