import unittest
from mock import Mock
import mock
from src.airport import Airport
from src.plane import Plane


class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Mock(return_value='Plane')
        self.plane_two = Mock(return_value='Plane Two')

    def test_land_plane_stores_plane_in_hanger(self):
        with mock.patch.object(self.airport, 'forecast') as mock_forecast:
            mock_forecast.return_value = (False)
            self.airport.land(self.plane)
            self.assertEqual(self.airport.hanger, [self.plane])

    def test_land_plane_raises_error_if_weather_stormy(self):
        with mock.patch.object(self.airport, 'forecast') as mock_forecast:
            mock_forecast.return_value = (True)
            self.assertRaises(TypeError, self.airport.land, self.plane_two)

    def test_land_plane_raises_error_if_hanger_full(self):
        with mock.patch.object(self.airport, 'forecast') as mock_forecast:
            mock_forecast.return_value = (False)
            self.airport.land(self.plane)
            self.airport.land(self.plane_two)
            plane_three = Mock(return_value='Plane Three')
            self.assertRaises(TypeError, self.airport.land, plane_three)

    def test_take_off_removes_plane_from_hanger(self):
        with mock.patch.object(self.airport, 'forecast') as mock_forecast:
            mock_forecast.return_value = (False)
            self.airport.land(self.plane)
            self.airport.take_off(self.plane)
            self.assertEqual(self.airport.hanger, [])

    def test_take_off_plane_raises_error_if_weather_stormy(self):
        with mock.patch.object(self.airport, 'forecast') as mock_forecast:
            mock_forecast.return_value = (False)
            self.airport.land(self.plane)
            mock_forecast.return_value = (True)
            self.assertRaises(TypeError, self.airport.take_off, self.plane)

    def test_take_off_raises_error_if_plane_not_grounded_at_that_airport(self):
        with mock.patch.object(self.airport, 'forecast') as mock_forecast:
            mock_forecast.return_value = (False)
            self.airport.land(self.plane)
            airport_two = Airport()
            self.assertRaises(TypeError, airport_two.take_off, self.plane)


if __name__ == "__main__":
    unittest.main()
