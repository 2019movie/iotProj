#from car_park import CarPark
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
        return f'Display id: {str(self.id)}, message: {str(self.message)}, power on: {str(self.is_on)}, part of {str(self.car_park)}'

    def update(self, data):
        self.is_on = True
        for key, value in data.items():
            if key == "available_bays":
                self.message = self.message + f" Available bays: {value}"
            if key == "temperature":
                self.message = self.message + f" Temperature is: {value}"


if __name__ == "__main__":
    print(f'This is display class')
    # carpark1 = CarPark("City", 100)
    # display1 = Display(carpark1, 1, "Hello World")
    # print(display1)
    # display1.update("It is a test!")
    # print(display1)
