#!/usr/bin/python                                                                                                                                                         

import sys
import matplotlib.pyplot as plt

def main():
  file_name = sys.argv[1]
  file = open(file_name, 'r')
  numbers = []
  for line in file:
    numbers.append(int(line))
  file.close()

  i = 2 # because we want an n >= 1                                                                                                                                       
  divisions = [] # to hold the number of divisions for each m, n pair                                                                                                     
  while i < len(numbers):
    m = numbers[i] # implementing it like this instead of F(k + 1), as its more readable                                                                                  
    n = numbers[i - 1]
    divisions.append(euclid(m,n))
    i += 1
  # we may want to rewrite this to calculate the gcd of several sequences of differing length                                                                             
  # or perhaps we want to put more emphasis on the number of divisions for each pair                                                                                      
  average = sum(divisions) / float(m)
  string_out = "Worst-case efficiency of Euclids Algortihm on a Fibonacci Sequence of length: " + repr(len(numbers)) + " is: " + repr(average)
  print (string_out)

  fib_numbers = numbers[2:]
  plt.scatter(fib_numbers, divisions)
  plt.xlabel("Fibonacci Numbers")
  plt.ylabel("Number of modulo divisions")
  plt.show()

# Input: integer _m, integer _n                                                                                                                                           
# Condition: _m >= _n                                                                                                                                                     
def euclid(_m,_n):
  m = _m
  n = _n

  divisions = 0
  # If the value of n, then we know that the current m                                                                                                                    
  # is the greatest common divider of both m & n                                                                                                                          
  while n != 0 :
    r = m % n
    divisions += 1
    m = n
    n = r

  return divisions # return the current m                                                                                                                                 


if __name__== "__main__":
      main()

