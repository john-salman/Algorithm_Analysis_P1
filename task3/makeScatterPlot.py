#!/usr/bin/python                                                                                                                                                         

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




  plt.scatter(fib_numbers, divisions)
  plt.xlabel("Fibonacci Numbers")
  plt.ylabel("Number of modulo divisions")
  plt.tight_layout()
  if(sys.argv[2] == "save"):
    imgname = os.path.splitext(sys.argv[1])[0] + ".png"
    plt.savefig(imgname)
  else:
    plt.show()


if __name__== "__main__":
      main()

