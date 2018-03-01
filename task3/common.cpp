/*
Usage: ./script.x <list file 1> <list file 2> <return file list OPTIONAL>
*/




/*

** MUST ** be used on sorted data sets

Current iteration will accept numbers on their own lines.

*/


#include <stdlib.h>
#include <iostream>
#include <fstream>

int main(int argc, char const *argv[]) {

	std::ifstream file1;
	std::ifstream file2;

	//Error Checking

	if(argc <= 1) {
		std::cout << "Please provide two files. List one and List two.\n";
		return 1; // Program does not have enough inline args.
	}

	// Open files associated with list 1 and list 2.
	file1.open(argv[1]);
	file2.open(argv[2]);

	// Assure the files exist.
	if(!file1.good() || !file2.good()) {
		return 1; // The files do not exist.
	}

	// Create queue to house the data sets.

	// Assure the data sets are sorted, if not: sort.

	// Commonalities function call

	// Cout commonalities function return if no output file
	// is given otherwise:

	// print commonalities array to output file

	return 0;
}


/* Commonalities function skeleton   (queue n, queue m)

	Create new array to house commonalities which
	at most can be of size(n + m).

	iterate through both queues popping the lesser value.
	and adding equal values to the commonalities array.


*/

