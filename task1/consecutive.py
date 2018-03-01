#!/usr/bin/python                                                                                                                                                         

import sys

def main():
  file_name = sys.argv[1]
  file = open(file_name, 'r')
  m_numbers = []
  n_numbers = []
  for line in file:
      if line >= 3:
          m_numbers.append(int(line))
      n_numbers.append(int(line))
  file.close()

  i = 0
  divisions = []
  while i < len(m_numbers):
    m = m_numbers[i]
    i += 1

    j = 0
    n = n_numbers[j]
    while m >= n:
        divisions.append(consecutive(m,n))
        j += 1
        n = n_numbers[j]
    average = sum(divisions) / float(m)
    string_out = "Average-case efficiency of Consecutive-Integer Algortihm on input size: " + repr(m) + " is: " + repr(average)
    print (string_out)

# Input: integer _m, integer _n                                                                                                                                           
# Condition: _m >= _n & n != 0                                                                                                                                            
def consecutive(_m,_n):
    m = _m
    n = _n
    r = _n
    divisions = 0
    while r > 1 :
            if (m % r == 0 and n % r == 0) :
              divisions += 2
              return divisions # this is the gcd                                                                                                                          
            r -= 1 # else go down by one                                                                                                                                  
    return divisions



if __name__== "__main__":
      main()

