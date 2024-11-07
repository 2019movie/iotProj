from car_park import CarPark
class Display:
    def __init__(self, car_park, id, message=None, is_on=False):
        self.car_park = car_park

        if id is not None and isinstance(id, int):
            self.id = id
        else:
            self.id = 0

        self.message = ""
        if message is not None and len(message) > 0:
            self.message = message

        self.is_on = is_on


    def __str__(self):
        return f'Display id: {str(self.id)}, message: {str(self.message)}, it is currently on: {str(self.is_on)}, part of {str(self.car_park)}'

if __name__ == "__main__":
    carpark1 = CarPark("City", 100)
    display1 = Display(carpark1, 1, "Hello World")
    print(display1)
