from random import uniform
from math import log,sqrt

def uni(a,b):
  u = uniform(0,1)
  return (b-a)*u + a

def bern(p):
  u = uni(0,1)
  return 1 if p > u else 0

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


def vad(params):  # params is a List of tuples (value,prob)
  params.sort(key= lambda h: h[1], reverse=True)
  acc = 0
  u = uniform(0,1)
  i = 0 # indexer 
  while True:
    if acc > u:
      break # stop, and the i-th entry in param is the result
    
    # else, continue iterating
    i+=1
    acc+= params[i][1]

  return params[i][0] # return value of the i-th tuple