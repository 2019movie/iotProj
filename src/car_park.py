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

if __name__ == "__main__":
   carpark = CarPark("City", 100)
   print(carpark)