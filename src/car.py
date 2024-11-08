class Car:
   def __init__(self, plate_number, entry_time):
      self.plate_number = plate_number
      self.entrytime = entry_time

   def __str__(self):
      return f'car: {self.plate_number} Entry time: {self.entrytime.strftime("%Y-%m-%d %H:%M:%S")}'

   def plate_number(self):
      return self.plate_number

   def entry_time(self):
      return self.entrytime




