from sensor import Sensor, ExitSensor, EntrySensor
from display import Display
from car import Car
import datetime


class CarPark:
   def __init__(self, location, capacity, sensors=None, displays=None):
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
      return f"Car park location ({str(self.location)}), capacity ({str(self.capacity)}). Has {str(len(self.displays))} display and {str(len(self.sensors))} sensors"

   def register(self, component):
      '''method allow car park to register sensors and displays'''
      if not isinstance(component, (Sensor, Display)):
         raise TypeError(f"Object must be type of Sensor or Display")

      if isinstance(component, Sensor):
         self.sensors.append(component)
      elif isinstance(component, Display):
         self.displays.append(component)

   def add_car(self, number_plate):
      '''method will call when car enters the car park. It record the plate number and update display'''
      if (not self.is_plate_in_carpark(number_plate)):
         self.plates.append(number_plate)
         current_datetime = datetime.datetime.now()
         new_car = Car(number_plate, current_datetime)
         self.cars.append(new_car)
      self.update_displays()


   def remove_car(self, plate_number):
      '''method will call when car exits the car park. It remove the plate number and update display'''
      try:
         self.plates.remove(plate_number)
         for car in self.cars:
            if car.plate_number == plate_number:
               print(f'{car} leavning carpark.')
               self.cars.remove(car)
         self.update_displays()
      except ValueError:
         return f"{number_plate} not found in the plates list."

   def is_plate_in_carpark(self, plate_number):
      '''Method to check if a car's plate number is already in the list.'''
      if plate_number in self.plates:
         return True  # Plate is already in the list
      else:
         return False  # Plate is not in the list

   @property
   def available_bays(self):
     if self.capacity >= len(self.plates):
        return (self.capacity - len(self.plates))
     else:
        return 0

   def remaining_car_bays(self):
     if self.capacity >= len(self.plates):
        return (self.capacity - len(self.plates))
     else:
        return 0

   def update_displays(self):
      for each_display in self.displays:
         each_display.update(f"Remaining car bays: {str(self.remaining_car_bays)}")
      # Todo: new display message  "Remaining car bays:  current time:  current temperature: "

if __name__ == "__main__":
   carpark1 = CarPark("City", 100)
   #print(carpark1)
   display1 = Display(carpark1, 1, "Hello World")
   #print(display1)
   sensor2 = EntrySensor(carpark1, 2, True)
   sensor3 = ExitSensor(carpark1, 3, True)
   carpark1.register(display1)
   print(carpark1)
   carpark1.register(sensor2)
   print(carpark1)
   carpark1.register(sensor3)
   print(carpark1)

   carpark1.add_car("aa1234")
   carpark1.add_car("bb333")
   print(f'remaining car bay: {carpark1.remaining_car_bays()}')
   carpark1.add_car("bb333")
   print(f'Car "bb333" in carpark: {carpark1.is_plate_in_carpark("bb333")}')

   print(f'remaining car bay: {carpark1.remaining_car_bays()}')
   print(f"aa1234 remove")
   carpark1.remove_car("aa1234")
   print(f'remaining car bay: {carpark1.remaining_car_bays()}')

   print(f'available_bays: {carpark1.available_bays}')

   print(f'===end of test===')