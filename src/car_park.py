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

   @classmethod
   def from_config(cls, config_file=Path("config.json")):
      config_file = config_file if isinstance(config_file, Path) else Path(config_file)
      with config_file.open() as f:
         config = json.load(f)
      return cls(config["location"], config["capacity"], log_file=config["log_file"])

   def _log_car_activity(self, plate, action):
      current_datetime = datetime.datetime.now()
      with self.log_file.open("a") as file:
         file.write(f"{plate} {action} at {current_datetime:%Y-%m-%d %H:%M:%S}\n")

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
         self._log_car_activity(plate_number, "unlisted car exited")
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
   print("this is the CarPark class")