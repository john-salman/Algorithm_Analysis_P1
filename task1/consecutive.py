#!/usr/bin/python                                                                                                                                                         

import sys
import os
import matplotlib.pyplot as plt



def main():
  file_name = sys.argv[1]
  file = open(file_name, 'r')
  numbers = []
  for line in file:
      numbers.append(int(line))
  file.close()

  i = 2
  divisions = []
  averages = []
  while i < len(numbers):
    print(numbers[i])
    divisionCount = 0
    m = numbers[i]
    i += 1

    j = 0
    n = numbers[j]
    while m > n:
        divisionCount += consecutive(m,n)
        j += 1
        n = numbers[j]

    divisions.append(divisionCount)

    average = divisionCount / float(m)
    averages.append(average)
    # string_out = "Average-case efficiency of Consecutive-Integer Algortihm on input size: " + repr(m) + " is: " + repr(average)
    # print (string_out)

  # print(divisions)
  # print(averages)
  _numbers = numbers[2:]
  plt.scatter(_numbers, averages)
  plt.xlabel("M")
  plt.ylabel("averages")
  plt.tight_layout()
  imgname = os.path.splitext(sys.argv[1])[0] + "png"
  plt.savefig(imgname)
  # plt.show()

# Input: integer _m, integer _n                                                                                                                                           
# Condition: _m >= _n & n != 0                                                                                                                                            

# # # I HAVE PULLED THIS DIRECTLY FROM SECTION 1.1 EXACTLY.
def consecutive(_m,_n):
  divisions = 0
  t = min(_m,_n)
  while t > 0:
    if _m % t == 0 and _n % t == 0:
      return divisions + 2 # because we still did 2 last divisions and found the gcd
    t -= 1
    divisions += 2 # count both divisions seperately as indicated in the spec
  return divisions

if __name__== "__main__":
      main()

