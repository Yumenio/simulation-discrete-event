class Plane:
  def __init__(self):
    self.track = 0
    self.landing_time = 0
    self.departure_time = 0

  def __str__(self):
    return f"Plane landed on track {self.track} at {self.landing_time}, and departed at {self.departure_time}."