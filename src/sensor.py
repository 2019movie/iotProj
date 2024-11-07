from car_park import CarPark
class Sensor:
    def __init__(self, car_park, id, is_active=False):
        self.car_park = car_park

        if id is not None and isinstance(id, int):
            self.id = id
        else:
            self.id = 0

        self.is_active = is_active

    def __str__(self):
        return f"Sensor id ({str(self.id)}), status ({str(self.is_active)}); part of carpark ({str(self.car_park)})"

class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass


if __name__ == "__main__":
    car_park2 = CarPark()
    sensor1 = Sensor(car_park2, 1, True )
    print(sensor1)