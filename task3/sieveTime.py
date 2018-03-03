#!/usr/bin/python                                                                                                             \
                                                                                                                               
from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
import os
import math # sqrt()                                                                                                           

def main():
  n = int(sys.argv[1])
  timesFinal = []
  for i in range(2, _n + 1):
    x = 0
    while x < 99:
      timesSum += sieve(i)
      x += 1
    timesFinal.append(timesSum / 100.0)


  fib_numbers = numbers[2:]
  plt.scatter(fib_numbers, timesFinal)
  plt.xlabel("Fibonacci Numbers")
  plt.ylabel("Number of modulo divisions")
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
  for i in range(2, _n):
    prime[i] = i
  m = sqrt(_n)
  for p in range(2, m + 1):
    if (prime[p] != 0):
      j = p * p
      while j <= _n:
        prime[j] = 0
        j += p
  j = 0
  for p in range(2, _n + 1):
    if (prime[p] != 0):
      primeRem[j] = prime[p]
      j += 1


  end = timer()
  return end - start


if __name__== "__main__":
      main()
