#!/usr/bin/python                                                                                                                                                         

import sys
import matplotlib.pyplot as plt
import os

def main():
  file_name = sys.argv[1]
  file = open(file_name, 'r')
  time_averages = []
  for line in file:
    time_averages.append(int(line))
  file.close()

  N_numbers = []
  i = 1
  while (i < len(time_averages + 1)):
    N_numbers.append(int(i))
    i += 1


  plt.scatter(N_numbers, time_averages)
  plt.xlabel("N")
  plt.ylabel("Time")
  plt.tight_layout()
  if(sys.argv[2] == "save"):
    imgname = os.path.splitext(sys.argv[1])[0] + ".png"
    plt.savefig(imgname)
  else:
    plt.show()


if __name__== "__main__":
      main()

