from sensor import ExitSensor, EntrySensor
from display import Display
class CarPark:
   def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
      self.location = "Unknown"
      if location is not None and len(location) > 0:
         self.location = location

      self.capacity = 0
      if capacity is not None and capacity > 0 and isinstance(capacity, (int,float)):
         self.capacity = capacity

      self.plates = []
      if plates is not None:
         self.plates.append(plates)

      self.sensors = []
      if sensors is not None:
         self.sensors.append(sensors)

      self.displays = []
      if displays is not None:
         self.displays.append(displays)

   def __str__(self):
      return f"Car park location ({str(self.location)}), capacity ({str(self.capacity)}). Has {str(len(self.displays))} display and {str(len(self.sensors))} sensors"

   def register(self, component):
      if not isinstance(component, (Sensor, Display)):
         raise TypeError(f"Object must be type of Sensor or Display")

      if isinstance(component, Sensor):
         self.sensors.append(component)
      elif isinstance(component, Display):
         self.displays.append(component)

   def add_car(self, number_plate):
      self.plates.append(number_plate)
      self.update_displays()

   def remove_car(self, number_plate):
      try:
         self.plates.remove(number_plate)
         self.update_displays()
      except ValueError:
         return f"{number_plate} not found in the plates list."

   def update_displays(self):
      for each_display in self.displays:
         each_display.update(f"Remaining car bays: {str(len(self.plates)-self.capacity)}")
      # Todo: new display message  "Remaining car bays:  current time:  current temperature: "

if __name__ == "__main__":
   carpark1 = CarPark("City", 100)
   print(carpark1)
   display1 = Display(carpark1, 1, "Hello World")
   print(display1)
   sensor2 = EntrySensor(carpark1, 2, True)
   print(sensor2)
   sensor3 = ExitSensor(carpark1, 3, True)
   print(sensor3)
   print(f'===end of test===')