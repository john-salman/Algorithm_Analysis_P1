# project_1

John Salman
Jack Newman


/task1/ Files:

input files: consec5000.txt - Wants a file that can be created by `seq N > inputFile`
python consecutive.py <input file>
no expected output. It will create a png file containing the scatter-plot

input files: consec5000.txt - Wants a file that can be created by `seq N > inputFile`
python euclid.py <input file> <save/show>
Save option will save a png file like above, show will display the graph (must have ssh'd with "_X" option)


/task2/ Files:

input files: a file generated from fibGenerator.x
python euclidFib.py <input file> <save/show>
Worst-case efficiency of Euclids Algortihm on a Fibonacci Sequence of length: N is: average.
This program also has the same save/show option as above.

input files: a file generated from fibGenerator.x
python euclidFibTime.py <input file> <save/show>
No expected output. Save/Show option works the same as above.

input files: n/a
./fibGenerator.x N <output file>
N must be lower than about 95
No standard out output but it will create an output file that will contain the Fibonacci numbers each on their own line.


/task3/ Files:

input files: two files with numbers seperated by newlines
./common.x <list 1 file> <list 2 file>
Example Output:
Our loop ran 13 times.
1 3 4 5

input files: file with times seperated by newlines
python makeScatterPlot.py <input file> <save/show>
No expected output. Save/show option works the same as above.


/tools/ Files:

input files: n/a
bash generateC.sh <file.txt> <n>
Example Output:
file: numbers.txt created
Generating...
Done.

input files: n/a
bash generateR.sh <file.txt> <n>
Example Output:
File: numbers.txt generated
Generating random numbers...
Done