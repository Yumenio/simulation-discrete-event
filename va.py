from random import uniform
from math import log,sqrt

def uni(a,b):
  u = uniform(0,1)
  return (b-a)*u + a

def exp(l):
  assert l != 0
  u = uniform(0,1)
  
  try:
    return (-1/l)*log(u)
  except: # in case log(u) goes wrong
    return exp(l)

def norm(mu=0,sigma=1):
  u = uniform(0,1)
  y1 = 1
  y2 = 0
  while y2 - ( ( (y1-1)**2 ) /2 ) <= 0:
    y1 = exp(1)
    y2 = exp(1)

  u = uniform(0,1)
  ans = y1 if u > 0.5 else -y1

  return ans*sqrt(sigma) + mu