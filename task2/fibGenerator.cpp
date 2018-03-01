// File name: fibGenerator.cpp
// Authors: John Salman, Jack Newman
// Description: This program will generate a fibonacci sequence of length n, and write that to a file.
// To run: ./a.x n output_file  for any integer n. Output will be limited to a value of
// long long[ (2^63) - 1 ]

#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

void fibonacci(long long fib[], int n);

int main(int argc, char* argv[]) {
  if (argv[1] == NULL) { // user failed to provide the first arguement
    cout << "Please provide an n value to calculate up to (i.e. ./a.x 32 example.txt)" << endl;
    return 1;
  }
  else if (argv[2] == NULL) { // user failed to provide the second arguement
    cout << "Please provide a file to write to (i.e. ./a.x 32 example.txt)" << endl;
    return 1;
  }

  int n = atoi(argv[1]);

  long long fib[n]; // our array to contain the fibonacci sequence
  fibonacci(fib, n); // pass the array and an n value to act as the length

  ofstream file;
  file.open (argv[2]); // create and open the file provided in the command line, will overwrite old files
  for (int i = 0; i < n; i++) {
    file << fib[i] << "\n"; // push in the sequence line by line
  }
  file.close();

  return 0;
}


// Computes the fibonacci sequence up to n - 1 (or generating a sequence of n length)
// Input: an integer array of size n
// Output: modifies the values of the array by reference
// This function was derived from the algorithm on page 82 (section 2.5)
void fibonacci(long long fib[], int n) {
  fib[0] = 0;
  fib[1] = 1;
  for (int i = 2; i < n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }
  return;
}
