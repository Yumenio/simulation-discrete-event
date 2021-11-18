import math
from plane import Plane
from va import uni,exp,norm

class Airport:
  def __init__(self, total_time = 60*24*7, landing_tracks = 5):
    self.tracks = [math.inf for i in range(landing_tracks)]
    self.tracks_history = [[] for track in self.tracks] # save tuple (landing,departure)
    self.plane_history = [] # keeping record of all planes processed

    # waiting queue for landing
    self.queue = []

    # dicts
    self.A = {}
    self.D = {}

    self.current_time = 0
    self.next_arrival_time = exp(0.05) # time of the first arrival
    self.total_time = total_time

  def idle_tracks(self):
    candidates = [s for s,i in enumerate(self.tracks) if i == math.inf]
    if not candidates:
      return -1

    index = int(uni(0,len(candidates))) # randomize output if possible
    return candidates[index]

  def on_arrival(self):
    new_plane = Plane()
    self.plane_history.append(new_plane)
    track = self.idle_tracks() # -1 when all tracks are occupied
    if track == -1:
      self.queue.append(new_plane)

    else:
      self.on_landing(new_plane, track)

    # generate next arrival time given that this one was processed
    current_arrival_time = self.next_arrival_time
    self.next_arrival_time = current_arrival_time + exp(0.05)
    
  def on_landing(self, plane,track_id):
    plane.track = track_id
    plane.landing_time = self.next_arrival_time

    ellapsed_time = self.handle_plane(plane, track_id) # sim all possible proccess that a plane can go through
    plane.departure_time = self.current_time + ellapsed_time
    self.tracks[track_id] = plane.departure_time
    self.tracks_history[track_id].append( ( plane.landing_time, plane.departure_time ) )

  def handle_plane(self, plane, track_id):
    acc = 0

    acc += norm(10,5) # landing
    acc += exp(1/30) # fueling
    acc += exp(1/30) if uni(0,1) > 0.5 else 0 # plane loads with a 1/2 prob
    acc += exp(1/30) if uni(0,1) > 0.5 else 0 # plane unloads with a 1/2 prob
    acc += exp(1/15) if uni(0,1) < 0.1 else 0 # plane needs repair with a 1/10 prob
    acc += norm(10,5) # depart

    return acc

  def on_depart(self):
    track_id = -1
    min = math.inf
    for i in range(len(self.tracks)):
      if min > self.tracks[i]:
        min = self.tracks[i]
        track_id = i

    self.tracks[track_id] = math.inf
    if self.queue:
      p = self.queue.pop()
      self.on_landing(p,track_id)

  def sim(self):
    while True:
      next_on_track = min(self.tracks)
      self.current_time = min(self.next_arrival_time, next_on_track)
      if self.current_time < next_on_track: # closest event is an arrival
        self.on_arrival()
      else:
        self.on_depart()  # closest event is a departure

      if self.current_time > self.total_time:
        break

    # print results
    ans = [0 for i in range(5)]
    for i in range(5):
      for record in self.tracks_history[i]:
        # print(f"Track {i}: Plane arrived at {record[0]} and departed at {record[1]}")
        ans[i] += min(record[1],self.total_time) - record[0]
      print(f"Track {i} was idle for {self.total_time - ans[i]} minutes")
