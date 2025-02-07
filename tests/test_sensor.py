import unittest
from sensor import Sensor, ExitSensor, EntrySensor
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.sensor_exit = ExitSensor(self.car_park, 2, is_active=True)
        self.sensor_entry = EntrySensor(self.car_park, 1, is_active=True)

    def test_EntrySensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor_entry, EntrySensor)
        self.assertEqual(self.sensor_entry.id,1)
        self.assertEqual(self.sensor_entry.is_active, True)
        self.assertIsInstance(self.car_park, CarPark)

    def test_EntrySensor_detect_vehicle(self):
        self.sensor_entry.detect_vehicle()
        self.assertEqual(len(self.car_park.plates),1)
        self.assertIsInstance(self.car_park.plates[0], str)

    def test_ExitSensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor_exit, ExitSensor)
        self.assertEqual(self.sensor_exit.id,2)
        self.assertEqual(self.sensor_exit.is_active, True)
        self.assertIsInstance(self.car_park, CarPark)

    def test_ExitSensor_detect_vehicle(self):
        self.sensor_entry.detect_vehicle()
        self.sensor_entry.detect_vehicle()
        self.assertEqual(len(self.car_park.plates),2)
        self.sensor_exit.detect_vehicle()
        self.assertEqual(len(self.car_park.plates),1)


    def test_Sensor_resigster_method(self):
        self.assertIn(self.sensor_entry, self.car_park.sensors)
        self.assertIn(self.sensor_exit, self.car_park.sensors)
        self.assertEqual(len(self.car_park.sensors),2)