import unittest
from src.plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()
        self.plane.land()

    def test_land_returns_true(self):
        self.assertEqual(self.plane.grounded, True)

    def test_take_off_returns_false(self):
        self.plane.take_off()
        self.assertEqual(self.plane.grounded, False)
