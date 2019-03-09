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

    def test_land_plane_stores_plane_in_hanger(self):
        self.airport.land(self.plane)
        self.assertEqual(self.airport.hanger, [self.plane])

    def test_land_plane_raises_error_if_hanger_full(self):
        self.airport.land(self.plane)
        self.airport.land(self.plane_two)
        self.assertEqual(self.airport.land(self.plane_three), "Cannot land plane: hanger full")

    def test_land_plane_raises_error_if_plane_already_landed(self):
        self.airport.land(self.plane)
        self.plane.grounded = True
        self.assertEqual(self.airport.land(self.plane), "Cannot land plane: plane already landed")

    def test_take_off_removes_plane_in_array(self):
        self.airport.land(self.plane)
        self.airport.take_off(self.plane)
        self.assertEqual(self.airport.hanger, [])

    def test_take_off_raises_error_if_hanger_empty(self):
        self.assertEqual(self.airport.take_off(self.plane), "Cannot take off: hanger empty")

    def test_take_off_raises_error_if_plane_not_grounded(self):
        self.airport.land(self.plane)
        self.plane_two.grounded = False
        self.assertEqual(self.airport.take_off(self.plane_two), "Cannot take off: plane not grounded")

if __name__ == "__main__":
    unittest.main()
