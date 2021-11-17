from random import uniform
from math import log

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

