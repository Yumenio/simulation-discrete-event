import math
from plane import Plane
from va import uni,exp

class Airport:
  def __init__(self, total_time = 60*24*7, landing_tracks = 5):
    self.tracks = [math.inf for i in range(landing_tracks)]
    self.tracks_history = [[] for track in self.tracks] # save tuple (landing,departure)
    self.plane_history = [] # keeping record of all planes that departed

    # waiting queue for landing
    self.queue = []

    self.current_time = 0
    self.next_arrival_time = exp(0.05) # time of the first arrival
    self.total_time = total_time

  def idle_tracks(self):
    candidates = [i for i in self.tracks if i == math.inf]
    if not candidates:
      return -1

    index = int(uni(0,len(candidates))) # randomize output if possible
    return index

  def on_arrival(self):
    new_plane = Plane()
    self.plane_history.append(new_plane)
    track = self.idle_tracks() # -1 when all tracks are occupied
    if track == -1:
      self.queue.append(new_plane)

    else:
      self.on_landing(new_plane, track)

    current_arrival_time = self.next_arrival_time # ya este arrival fue procesado y toca general el sgte
    self.next_arrival_time = current_arrival_time + exp(0.05)
    
  def on_landing(self, plane,track_id):
    plane.track = track_id
    self.tracks_history.append( self.next_arrival_time, (self.tracks[track_id]) )