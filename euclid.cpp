#include <iostream>
#include <iomanip>
#include <fstream>
#include <chrono>
#include <vector>
#include <cstdlib>


using namespace std;

vector<int> ReadFile (ifstream & input);
int euclid(int _m, int _n);

int main(int argc, char * argv [] ) {
  ifstream file;
  file.open("numbers.txt");
  if (file.fail())
    {
      cout << "File:  not found\n";
      exit (2);
    }
  vector<int> numbers = ReadFile(file);// store value from txt file into a vector
  file.close();

  // declaration of necessary variables
  vector <int> :: iterator i;
  i = numbers.begin();

  // variable to be used in "gcd(m,n)" format
  int m;
  int n;
  int final; // to recieve the output of the algorithm
  chrono::duration<float, milli> elapsed_time; // holds the difference of the stop and start time

  while(i < numbers.end()) {
    m = *i;
    i++;
    n = *i;
    i++;

    auto start = chrono::system_clock::now(); // get the current time, was unable to find the proper variable type, i think its time_point maybe
    final = euclid(m, n);
    auto stop = chrono::system_clock::now();
    elapsed_time = stop - start;

    cout << "It took " << elapsed_time.count() << " seconds to calculate gcd(" << m << ", " << n << ") = " << final << "." << endl;
  }

  return 0;
}

// Input: integer _m, integer _n
// Condition: _m >= _n
int euclid(int _m, int _n) {
  int m = _m;
  int n = _n;
  int r;
  // If the value of n, then we know that the current m
  // is the greatest common divider of both m & n
  while (n != 0) {
    r = m % n;
    m = n;
    n = r;
  }
  return m; // return the current m
}

// Input: should be reading from a .txt with paired integer values
vector<int> ReadFile(ifstream & input) {
  vector<int> numbers;
  int a;
  while(input >> a) {
    numbers.push_back(a);
  }
  return numbers;
}
