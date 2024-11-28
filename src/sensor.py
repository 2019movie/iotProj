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

        self.register()

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

    def register(self):
        # register the sensor to car_park sensors list
        if self.car_park:
            self.car_park.sensors.append(self)

class EntrySensor(Sensor):
    def __str__(self):
        return f"Entry Sensor: Sensor id: {self.id}"


    def update_car_park(self, plate_number):
        self.car_park.add_car(plate_number)
        return f"Incoming vehicle detected. Plate: {plate_number}"

class ExitSensor(Sensor):
    def __str__(self):
        return f"Exit Sensor: Sensor id: {self.id}"

    def detect_vehicle(self):
        if len(self.car_park.plates)>0:
            plate = self._scan_plate()
            self.update_car_park(plate)
    def _scan_plate(self):
        try:
            return random.choice(self.car_park.plates)
        except IndexError:
            return "no more car in carpark"
    def update_car_park(self, plate_number):
        self.car_park.remove_car(plate_number)
        return f"Outgoing vehicle detected. Plate: {plate_number}"


if __name__ == "__main__":
    print(f'This is Sensor class')
