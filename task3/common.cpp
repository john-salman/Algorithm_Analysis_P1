/*
Usage: ./script.x <list file 1> <list file 2> <return file list OPTIONAL>

** MUST ** be used on sorted data sets

Current iteration will accept numbers on their own lines.

*/


#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <list>
#include <string>

std::list<int> printList(std::list<int> _list) {
	for (std::list<int>::iterator it=_list.begin(); it != _list.end(); ++it) {
		std::cout << *it << " " << std::endl;
	}
}

std::list<int> findCommonNums(std::list<int> _list1, std::list<int> _list2) {
	std::cout << "For input size N = " << (_list1.size() + _list2.size());
	int loopCounter = 0;

	// Create list for nums
	std::list<int> commonNums;

	// Create iterator itr1 and itr2 for list1 and list2 respectively.
	std::list<int>::iterator itr1 = _list1.begin(), itr2 = _list2.begin();

	while(!_list1.empty() && !_list2.empty()) {
		loopCounter++;
		if(*itr1 < *itr2) { //case in which a is less than b; pop A
			++itr1;
			_list1.pop_front();
		}
		else if(*itr2 < *itr1) { //case in which b is less than a; pop b
			++itr2;
			_list2.pop_front();
		}
		else {
			commonNums.push_back(*itr1);
			++itr1;
			++itr2;
			_list1.pop_front();
			_list2.pop_front();
		}
	}
	std::cout << " our loop ran " << loopCounter << " times." << std::endl;
	return commonNums;
}



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

	// Create list to house the data sets.
	// Decided to go with list because you can push/pop from both front and back
	// as well as being able to sort with a list function; Sorted input is required
	// for our algorithm.
	std::list<int> list1, list2;
	std::string numIn;

	// Insert Data from file into respective list
	while(getline(file1, numIn)) {
		list1.push_back(stoi(numIn));
	}
	file1.close();
	while(getline(file2, numIn)) {
		list2.push_back(stoi(numIn));
	}
	file2.close();

	// Assure the data sets are sorted.
	list1.sort();
	list2.sort();

	// Copy lists as commonalities function will destroy the lists TODO: decide if this is needed? We may not need the lists after function call
	std::list<int> list1_c = list1, list2_c = list2;

	// Commonalities function call
	std::list<int> commonNums = findCommonNums(list1_c, list2_c);

	//Print the common numbers
	printList(commonNums);

	return 0;
}