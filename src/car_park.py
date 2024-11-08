from sensor import Sensor, ExitSensor, EntrySensor
from display import Display
from car import Car
import datetime
from pathlib import Path
import json


class CarPark:
   def __init__(self, location, capacity
                , log_file=Path("log.txt")
                , sensors=None, displays=None):
      self.config_file = Path("config.json")
      self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
      self.log_file.touch(exist_ok=True)
      self.location = "Unknown"

      if location is not None and len(location) > 0:
         self.location = location

      self.capacity = 0
      if capacity is not None and capacity > 0 and isinstance(capacity, (int,float)):
         self.capacity = capacity

      self.plates = []
      self.cars = []

      self.sensors = []
      if sensors is not None:
         self.register(sensors)

      self.displays = []
      if displays is not None:
         self.register(displays)

   def __str__(self):
      return (f"Car park location ({str(self.location)})"
              f", capacity ({str(self.capacity)})"
              f". Has {str(len(self.displays))} display and"
              f" {str(len(self.sensors))} sensors")

   def write_config(self):
      with open(self.config_file, "w") as file:
         json.dump({"location": self.location,
                    "capacity": self.capacity,
                    "log_file": str(self.log_file)}, file)
   def add_log(self, message=""):
      if len(message) > 0:
         with self.log_file.open('a') as file:
            file.write(f"{message}")
      else:
         with self.log_file.open('a') as file:
            file.write(f"")

   def _log_car_activity(self, plate, action):
      current_datetime = datetime.datetime.now()
      with self.log_file.open("a") as file:
         file.write(f"{plate} {action} at {current_datetime:%Y-%m-%d %H:%M:%S}\n")

   def register(self, component):
      #method allow car park to register sensors and displays
      if not isinstance(component, (Sensor, Display)):
         raise TypeError(f"Object must be type of Sensor or Display")

      if isinstance(component, Sensor):
         self.sensors.append(component)
      elif isinstance(component, Display):
         self.displays.append(component)

   def add_car(self, number_plate):
      #method will call when car enters the car park. It records the plate number and update display
      if not self.is_plate_in_carpark(number_plate):
         self.plates.append(number_plate)
         current_datetime = datetime.datetime.now()
         new_car = Car(number_plate, current_datetime)
         self.cars.append(new_car)
         #self.add_log(f"{number_plate} entered carpark at {current_datetime.strftime('%A, %B %d, %Y at %I:%M %p')}\n")
         self._log_car_activity(number_plate, "entered")
      self.update_displays()


   def remove_car(self, plate_number):
      #method will call when car exits the car park. It remove the plate number and update display
      try:
         self.plates.remove(plate_number)
         for car in self.cars:
            if car.plate_number == plate_number:
               current_datetime = datetime.datetime.now()
               self.cars.remove(car)
               self._log_car_activity(plate_number, "exited")
               #self.add_log(f"{plate_number} exited carpark at {current_datetime.strftime('%A, %B %d, %Y at %I:%M %p')}\n")

         self.update_displays()
      except ValueError:
         raise ValueError(f"{plate_number} not found in the plates list.")


   def is_plate_in_carpark(self, plate_number):
      #Method to check if a car's plate number is already in the list.
      if plate_number in self.plates:
         return True  # Plate is already in the list
      else:
         return False  # Plate is not in the list

   @property
   def available_bays(self):
     if self.capacity >= len(self.plates):
        return self.capacity - len(self.plates)
     else:
        return 0

   def remaining_car_bays(self):
     if self.capacity >= len(self.plates):
        return self.capacity - len(self.plates)
     else:
        return 0

   def update_displays(self):
       current_datetime = datetime.datetime.now()

       data = {
           "available_bays": self.available_bays,
           "temperature": 25,
          "time": current_datetime
       }

       for each_display in self.displays:
           each_display.update(data)



if __name__ == "__main__":
   carpark2 = CarPark("City", 100,
                      log_file ="log_3.txt")
   carpark1 = CarPark("City", 100)
   #print(carpark1)
   display1 = Display(carpark1, 1, "Hello World")
   #print(display1)
   sensor_in = EntrySensor(carpark1, 2, True)
   sensor_out = ExitSensor(carpark1, 3, True)
   carpark1.register(display1)
   print(carpark1)
   carpark1.register(sensor_in)
   print(carpark1)
   carpark1.register(sensor_out)
   print(carpark1)

   #carpark1.add_car("aa1234")
   carpark1.add_car("cc6778")
   carpark1.add_car("bb333")
   # sensor_in.detect_vehicle()
   # sensor_in.detect_vehicle()
   # sensor_in.detect_vehicle()
   # sensor_in.detect_vehicle()
   # print(f'remaining car bay: {carpark1.remaining_car_bays()}')
   carpark1.add_car("bb333")
   carpark1.remove_car("bb333")
   # sensor_in.detect_vehicle()
   # print(f'Car "bb333" in carpark: {carpark1.is_plate_in_carpark("bb333")}')
   # sensor_out.detect_vehicle()
   # print(f'remaining car bay: {carpark1.remaining_car_bays()}')
   # sensor_out.detect_vehicle()
   # sensor_out.detect_vehicle()
   # sensor_out.detect_vehicle()
   # print(f'remaining car bay: {carpark1.remaining_car_bays()}')
   # sensor_out.detect_vehicle()
   #
   # print(f'available_bays: {carpark1.available_bays}')
   #
   # print(f'random pick: {random.choice(carpark1.plates)}')
   pathtest = Path("new_log.txt")
   print(f"new log file exists> {pathtest.exists()}")
   pathtest = Path("log3.txt")
   print(f"log3.txt file exists> {pathtest.exists()}")
   pathtest = Path("log_3.txt")
   print(f"log_3.txt file exists> {pathtest.exists()}")
   carpark1.add_log()

   carpark1.write_config()
   carpark2.write_config()

   print(f'===end of test===')