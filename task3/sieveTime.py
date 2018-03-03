# File name: consecutive.py
# Authors: John Salman, Jack Newman

#!/usr/bin/python                                                                                                             \
                                                                                                                               
from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
import os
import math # sqrt()                                                                                                           

def main():
  n = int(sys.argv[1])
  timesFinal = []
  i = 2
  while (i <= n):
    x = 0
    timesSum = 0
    while x < 99:
      timesSum += sieve(i)
      x += 1
    timesFinal.append(timesSum / 100.0)
    i += 1

    l = 2
    numbers = []
    while (l <= n):
      numbers.append(l)
      l += 1

  plt.scatter(numbers, timesFinal)
  plt.xlabel("N")
  plt.ylabel("Time")
  plt.tight_layout()
  if(sys.argv[2] == "save"):
    imgname = os.path.splitext(sys.argv[1])[0] + ".png"
    plt.savefig(imgname)
  else:
    plt.show()


def sieve(_n):
  start = timer()
  prime = []
  primeRem = []
  i = 2
  prime.append(0)
  prime.append(0)
  while (i <= _n):
    prime.append(int(i))
    i += 1

  m = math.sqrt(_n)
  p = 2
  while (p <= int(m)):
    if (prime[p] != 0):
      j = p * p
      while j <= _n:
        prime[j] = 0
        j += p
    p += 1
  j = 0

  p = 2
  while (p <= _n):
    if (prime[p] != 0):
      primeRem.append(int(prime[p]))
      j += 1
    p += 1


  end = timer()
  return end - start


if __name__== "__main__":
      main()
