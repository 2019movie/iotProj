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

        self.register()


    def __str__(self):
        return f'Display id: {str(self.id)}, message: {str(self.message)}, power on: {str(self.is_on)}, part of {str(self.car_park)}'

    def update(self, data):
        self.is_on = True
        self.message = ""
        for key, value in data.items():
            if key == "message":
                self.message = self.message + value
            if key == "available_bays":
                self.message = self.message + f" Available bays: {value}"
            if key == "temperature":
                self.message = self.message + f" Temperature is: {value}"

    def get_message_on_display(self):
        return self.message

    def register(self):
        # register the display to car_park display list
        if self.car_park:
            self.car_park.displays.append(self)

if __name__ == "__main__":
    print(f'This is display class')
