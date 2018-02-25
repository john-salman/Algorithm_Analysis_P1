#!/usr/bin/python                                                                                                                                                         

import sys

def main():
  file_name = sys.argv[1]
  file = open(file_name, 'r')
  m_numbers = []
  n_numbers = []
  for line in file:
      if line >= 3: # the first insightful value for m
          m_numbers.append(int(line)) # loading the first list with our values for m
      n_numbers.append(int(line)) # loading the second with our n values
  file.close()

  i = 0
  divisions = [] # this list holds the number of divisions required to compute the gcd(m,n)
  while i < len(m_numbers):
    m = m_numbers[i] # we will hold m constant for each iteration
    i += 1

    j = 0
    n = n_numbers[j] # start n at 1
    while m >= n:
        divisions.append(euclid(m,n)) # count the divisions for this pair
        j += 1 # increase n's value by one
        n = n_numbers[j]
    average = sum(divisions) / float(m) # following the average-case efficiency formula from the spec
    string_out = "Average-case efficiency of Euclids Algortihm on input size: " + repr(m) + " is: " + repr(average)
    print (string_out)

    # here is where we would place the lines from matplotlib

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

  return divisions # return the number of divisions to reach the solution                                                                                                                                 

if __name__== "__main__":
      main()

