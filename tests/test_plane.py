import unittest
from src.plane import Plane


class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()
        self.plane.land()

    def test_land_sets_grounded_status_to_true(self):
        self.assertEqual(self.plane.grounded, True)

    def test_land_raises_error_if_plane_grounded(self):
        self.assertRaises(TypeError, self.plane.land)

    def test_take_off_sets_grounded_status_to_false(self):
        self.plane.take_off()
        self.assertEqual(self.plane.grounded, False)

    def test_take_off_raises_error_if_plane_not_grounded(self):
        self.plane.take_off()
        self.assertRaises(TypeError, self.plane.take_off)


if __name__ == "__main__":
    unittest.main()
