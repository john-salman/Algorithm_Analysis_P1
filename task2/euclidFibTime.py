#!/usr/bin/python                                                                                                                                                        \
                                                                                                                                                                          
from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
import os

def main():
  file_name = sys.argv[1]
  file = open(file_name, 'r')
  numbers = []
  for line in file:
    numbers.append(int(line))
  file.close()

  i = 2 # because we want an n >= 1                                                                                                                                      \
                                                                                                                                                                                                                                                                              
  timesFinal = []
  while i < len(numbers):
    m = numbers[i] # implementing it like this instead of F(k + 1), as its more readable                                                                                 \
                                                                                                                                                                          
    n = numbers[i - 1]
    
    x = 0
    timesSum = 0     
    while x < 100
      timesSum += euclid(m,n)
      x += 1
    timesFinal.append( timesSum / 100.0)
    i += 1
  # we may want to rewrite this to calculate the gcd of several sequences of differing length                                                                            \                                                                                                                                                                        
  # or perhaps we want to put more emphasis on the number of divisions for each pair                                                                                     \
                                                                                                                                                                          
  string_out = "Worst-case efficiency of Euclids Algortihm on a Fibonacci Sequence of length: " + repr(len(numbers)) + " is: " + repr(average)
  print (string_out)


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

# Input: integer _m, integer _n                                                                                                                                    \
                                                                                                                                                                    
# Condition: _m >= _n                                                                                                                                              \
                                                                                                                                                                    
def euclid(_m,_n):
  start = timer()

  m = _m
  n = _n

  # If the value of n, then we know that the current m                                                                                                             \
  # is the greatest common divider of both m & n                                                                                                                                                                                                                                                                                       
  while n != 0 :
    r = m % n
    m = n
    n = r

  end = timer()
  return end - start # return the time it took to compute                                                                                                                        \
                                                                                                                                                                    


if __name__== "__main__":
      main()
