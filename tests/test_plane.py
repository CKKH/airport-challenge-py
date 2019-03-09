import unittest
from src.plane import Plane

class TestPlane(unittest.TestCase):

    def test_land_returns_true(self):
        plane = Plane()
        plane.land()
        self.assertEqual(plane.grounded, True)

    def test_take_off_returns_false(self):
        plane = Plane()
        plane.land()
        plane.take_off()
        self.assertEqual(plane.grounded, False)
