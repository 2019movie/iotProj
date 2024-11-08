#from car_park import CarPark
from random import randint
import random
from abc import ABC, abstractmethod
class Sensor(ABC):
    def __init__(self, car_park, id, is_active=False):
        self.car_park = car_park

        if id is not None and isinstance(id, int):
            self.id = id
        else:
            self.id = 0

        self.is_active = is_active

    def __str__(self):
        return f"Sensor id ({str(self.id)}), status ({str(self.is_active)}); part of carpark [{str(self.car_park)}]"

    def _scan_plate(self):
        return 'FAKE-' + format(randint(0,999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

    @abstractmethod
    def update_car_park(self, plate_number):
        pass

class EntrySensor(Sensor):
    def __str__(self):
        return f"Entry Sensor: Sensor id: {self.id}"


    def update_car_park(self, plate_number):
        self.car_park.add_car(plate_number)
        print(f"Incoming vehicle detected. Plate: {plate_number}")

class ExitSensor(Sensor):
    def __str__(self):
        return f"Exit Sensor: Sensor id: {self.id}"

    def _scan_plate(self):
        try:
            return random.choice(self.car_park.plates)
        except IndexError:
            print("no more car in carpark")
    def update_car_park(self, plate_number):
        self.car_park.remove_car(plate_number)
        print(f"Outgoing vehicle detected. Plate: {plate_number}")


if __name__ == "__main__":
    print(f'This is Sensor class')
    # car_park2 = CarPark("Perth City", 122)
    # sensor1 = Sensor(car_park2, 1, True )
    # print(sensor1)
    # print(f"Test Entry sensor")
    # sensor2 = EntrySensor(car_park2, 2, True)
    # print(sensor2)
    # print(f"Test Exit sensor")
    # sensor3 = ExitSensor(car_park2, 3, True)
    # print(sensor3)
    print(f'{format(randint(0,999), "03d")}')
