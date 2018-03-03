#include <math.h> // sqrt                                                                                                                                                                     
#include <iostream> // cout                                                                                                                                                                   
#include <stdlib.h> // atoi                                                                                                                                                                   
#include <chrono> // for clock and duration                                                                                                                                                   

using namespace std;

void time_sieve(int prime[], int primeRem[], int _n);

int main (int argc, char* argv[]) {
  if (argv[1] == NULL) { // user failed to provide the first arguement                                                                                                                        
    cout << "Please provide an n value to calculate up to (i.e. ./a.x 32)" << endl;
    return 1;
  }

  int n = atoi(argv[1]);
  if (n < 2) {
    cout << "Providing an n value less than 2 will generate errors, exiting." << endl;
    return 1;
  }

  int prime[n];
  int primeRem[n/2]; // I wasn't sure how big to make the remainder array, so beware of garbage values at the end                                                                             

  for (int i = 2; i <= n; i++) {
    time_sieve(prime, primeRem, i);
  }

  return 0;
}

// algorithm taken from the book, section 1.1 page 7                                                                                                                                          
// Input: the initial array to hold integers 2 -> n, the second array to hold the primes, and the value of n (or length)                                                                      
// Output: the number of primes in the array                                                                                                                                                  
void time_sieve (int prime[], int primeRem[], int _n) {

  auto sieve_start = chrono::high_resolution_clock::now(); // start the clock                                                                                                                 

  int n = _n;
  for( int i = 2; i <= n; i++) {
    prime[i] = i;
  }
  int m = sqrt(n);
  int j;
  for ( int p = 2; p <= m; p++) {
    if (prime[p] != 0) {
      j = p * p;
      while ( j <= n ) {
        prime[j] = 0;
        j += p;
      }
    }
  }
  j = 0;
  for (int p = 2; p <= n; p++) {
    if ( prime[p] != 0 ){
      primeRem[j++] = prime[p];
    }
  }

  auto sieve_stop = chrono::high_resolution_clock::now(); // stop the clock                                                                                                                   
  chrono::duration<double, milli> sieve_time = sieve_stop - sieve_start;

  cout << "Elapsed time for the Sieve of Eratosthenes: " << sieve_time.count() << "s on input of size: " << n << endl;

  return;
}
