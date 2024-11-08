import unittest
from car_park import CarPark
from pathlib import Path

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.test_log_file = "test_log.txt"
    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
           self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        #self.assertRaises(ValueError, remove_car, 'test')
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("test for not sensor or display")

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street"
                              , 100
                              , log_file=self.test_log_file)
        self.assertTrue(Path(self.test_log_file).exists())



    def test_car_logged_when_entering(self):
        new_carpark = CarPark("123 Example Street"
                              , 100
                              , log_file=self.test_log_file)
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street"
                              , 100
                              , log_file = self.test_log_file)
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_write_config(self):
        new_carpark = CarPark("Mooning place"
                              , 34
                              , log_file = self.test_log_file)
        new_carpark.write_config()
        with new_carpark.config_file.open() as file:
            line = file.readlines()
        self.assertEqual('{"location": "Mooning place", "capacity": 34, "log_file": "test_log.txt"}',line[0])


    def test_tear_down(self):
        # Remove the log file after the test
        if Path(self.test_log_file).exists():
            Path(self.test_log_file).unlink()

if __name__ == "__main__":
   unittest.main()


