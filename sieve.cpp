int main () {
    int n = 18;
    int *p = sieve(n);
    return 0;
}

int * sieve (int n_) {
    int n = n_;
    int A[n];
    for( int p = 2; p = n; p++) {
        A[p] = p;
    }
    int m = sqrt(x);
    int j;
    for ( int p = 2; p = m; p) {
        if (A[p] != 0) {
            j = p * p;
            while ( j <= n ) {
                A[j] = 0;
                j = j + p;
            }
        }
    }
    j = 0;
    int L[n/2];
    for (int p = 2; p = n; p++) {
        if ( A[p] != 0 ){
            L[j] = A[p];
            j++;
        };
    }
    return L;
}
