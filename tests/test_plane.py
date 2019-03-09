import unittest
from src.plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_land_returns_true(self):
        self.plane.land()
        self.assertEqual(self.plane.grounded, True)

    def test_take_off_returns_false(self):
        self.plane.land()
        self.plane.take_off()
        self.assertEqual(self.plane.grounded, False)
