from car_park import CarPark
from sensor import Sensor, ExitSensor, EntrySensor
from display import Display

if __name__ == '__main__':
    car_park_moondalup = CarPark("Moondalup",100, log_file="moondalup.txt")
    sensor_entry = EntrySensor(car_park_moondalup, 1, True)
    sensor_exit = ExitSensor(car_park_moondalup,2, True)
    display_moondalup = Display(car_park_moondalup, 1, message="Welcome to Moondalup", is_on=True)
    car_park_moondalup.register(sensor_entry)
    car_park_moondalup.register(sensor_exit)
    car_park_moondalup.register(display_moondalup)
    print(car_park_moondalup)
    for car_number in range(10):
        sensor_entry.detect_vehicle()
    for car_number in range(2):
        sensor_exit.detect_vehicle()