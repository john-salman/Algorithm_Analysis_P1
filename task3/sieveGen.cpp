#include <math.h> // sqrt                                                                                                                                                                     
#include <iostream> // cout                                                                                                                                                                   
#include <fstream> // file manipulation                                                                                                                                                       
#include <stdlib.h> // atoi                                                                                                                                                                   


using namespace std;

int generate_sieve(int prime[], int primeRem[], int _n);

int main (int argc, char* argv[]) {
  if (argv[1] == NULL) { // user failed to provide the first arguement                                                                                                                        
    cout << "Please provide an n value to calculate up to (i.e. ./a.x 32 example.txt)" << endl;
    return 1;
  }
  else if (argv[2] == NULL) { // user failed to provide the second arguement                                                                                                                  
    cout << "Please provide a file to write to (i.e. ./a.x 32 example.txt)" << endl;
    return 1;
  }

  int n = atoi(argv[1]);
  if (n < 1) {
    cout << "Providing an n value less than 1 will generate errors, exiting." << endl;
    return 1;
  }

  int prime[n];
  int primeRem[n/2]; // I wasn't sure how big to make the remainder array, so beware of garbage values at the end                                                                             

  int j = generate_sieve(prime, primeRem, n); // j is equal to the number of primes +1                                                                                                        

  ofstream file;
  file.open (argv[2]); // create and open the file provided in the command line, will overwrite old files                                                                                     
  for (int i = 0; i <= j; i++) {
    file << primeRem[i] << "\n"; // push in the sequence line by line                                                                                                                         
  }
  file.close();
  return 0;
}



// algorithm taken from the book, section 1.1 page 7                                                                                                                                          
// Input: the initial array to hold integers 2 -> n, the second array to hold the primes, and the value of n (or length)                                                                      
// Output: the number of primes in the array                                                                                                                                                  
int generate_sieve (int prime[], int primeRem[], int _n) {
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
      primeRem[j] = prime[p];
      j++; // because in the final comparison we still increment, this number will be off by one                                                                                              
    }
  }
  return j - 1; // to counter the extra increment                                                                                                                                             
}
