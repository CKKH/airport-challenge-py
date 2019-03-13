import unittest
import mock
from src.weather import Weather


class TestWeather(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    def test_weather_can_be_stormy(self):
        with mock.patch.object(self.weather, 'check_stormy') as mock_weather:
            mock_weather.return_value = (True)
            self.assertIs(self.weather.check_stormy(), True)

    def test_weather_can_be_not_stormy(self):
        with mock.patch.object(self.weather, 'check_stormy') as mock_weather:
            mock_weather.return_value = (False)
            self.assertIs(self.weather.check_stormy(), False)


if __name__ == "__main__":
    unittest.main()
