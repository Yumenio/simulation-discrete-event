from va import uni,exp,norm,vad,bern
from airport import Airport


def fill(lbound,rbound, prob):
  return [ (i,prob) for i in range(lbound,rbound)]

def main():
  airp = Airport()
  airp.sim()


if __name__ == "__main__":
  main()