# File name: euclid.py
# Authors: John Salman, Jack Newman

#!/usr/bin/python                                                                                                                                                         

import sys
import os
import matplotlib.pyplot as plt


def main():
  file_name = sys.argv[1] # our input comes in from a file provided at the command line                                                                                   
  file = open(file_name, 'r')
  numbers = [] #the array to hold all our numbers                                                                                                                         
  for line in file:
      numbers.append(int(line))
  file.close()

  i = 2 # to start at m = 3                                                                                                                                               
  divisions = [] # this list holds the number of divisions required to compute the gcd(m,n)                                                                               
  averages = [] # array to hold the average case efficiency for each value of m                                                                                           
  while i < len(numbers):
    divisionCount = 0
    m = numbers[i] # hold the m constant for each loop                                                                                                                    
    i += 1

    j = 0
    n = numbers[j] # start the n values at 1 for each value of m                                                                                                          
    while m > n: # essentially gcd(m,m)                                                                                                                                  
        divisionCount += euclid(m,n) # count the divisions for this pair                                                                                                 
        j += 1
        n = numbers[j] # increase n's value by one                                                                                                                        

    divisions.append(divisionCount)
    average = divisionCount / float(m) # following the average-case efficiency formula from the spec                                                                     
    averages.append(average) # we need to store these values for use in the scatter plot                                                                                  
    # string_out = "Average-case efficiency of Euclids Algorithm on input size: " + repr(m) + " is: " + repr(average)
    # print (string_out)


    # print(numbers)
    # print(divisions)
    # print(averages)

    # here is where we would place the matplotlib code 
  _numbers = numbers[2:]
  # print(_numbers)

  plt.scatter(_numbers, averages)
  plt.xlabel("M")
  plt.ylabel("averages")
  plt.tight_layout()
  if(sys.argv[2] == "save"):
    imgname = os.path.splitext(sys.argv[1])[0] + ".png"
    plt.savefig(imgname)
  else:
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

