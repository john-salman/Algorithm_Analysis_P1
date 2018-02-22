#!/usr/bin/python                                                                                                                                                         

import sys

def main():
  file = open('m_numbers.txt', 'r')
  m_numbers = []
  n_numbers = []
  for line in file:
      if line >= 3:
          m_numbers.append(int(line))
      n_numbers.append(int(line))
  for i in range(75):
    print n_numbers[i]
  file.close()

  i = 0
  divisions = []
  while i < len(m_numbers):
    m = m_numbers[i]
    i += 1

    j = 0
    n = n_numbers[j]
    while m >= n:
        divisions.append(euclid(m,n))
        j += 1
        n = n_numbers[j]
    average = sum(divisions) / float(m)
    string_out = "Average-case efficiency of Euclids Algortihm on input size: " + repr(m) + " is: " + repr(average)
    print (string_out)


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

