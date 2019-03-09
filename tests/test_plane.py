import unittest
from src.plane import Plane

class TestPlane(unittest.TestCase):

    def test_land_returns_grounded(self):
        plane = Plane()
        plane.land()
        self.assertEqual(plane.status, 'Grounded')
