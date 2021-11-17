from va import uni,exp,norm,vad,bern
from citizen import Citizen

def fill(lbound,rbound, prob):
  return [ (i,prob) for i in range(lbound,rbound)]

def new_born():
  age = 0
  sex = bern(0.5)
  return Citizen(age,sex)

def new_man():
  age = uni(0,100)
  sex = 1
  return Citizen(age,sex)

def new_woman():
  age = uni(0,100)
  sex = 0
  return Citizen(age,sex)

def main(W,M):
  women = [new_woman() for i in range(W)]
  men =   [new_man() for i in range(M)]

  # hardcoding the simulation functions
  die = {(1,  (0,12)): 0.25,
         (1, (12,45)): 0.15,
         (1, (45,76)): 0.35,
         (1,(76,125)): 0.65,
         (0,  (0,12)): 0.25,
         (0, (12,45)): 0.10,
         (0, (45,76)): 0.30,
         (0,(76,125)): 0.70
         }
  
  pregnant = {(0, (12,15)): 0.20,
              (0, (15,21)): 0.45,
              (0, (21,35)): 0.80,
              (0, (35,45)): 0.40,
              (0, (45,60)): 0.20,
              (0, (60,125)): 0.05,
              }

  # t = [new_born() for i in range(10000)]
  # print(sum([1 for i in t if i.sex]))

if __name__ == "__main__":
  W = 20
  M = 20
  main(20,20)