#! /bin/bash/

echo "Starting to build"

echo "Building Task 1"
chmod 700 ./task1/consecutive.py
chmod 700 ./task1/euclid.py

echo "Building Task 2"
chmod 700 ./task2/euclidFib.py
chmod 700 ./task2/euclidFibTime.py
c++ ./task2/fibGenerator.cpp -o ./task2/fibGenerator.x -std=c++11

echo "Building Task 3"
chmod 700 ./task3/makeScatterPlot.py
c++ ./task3/common.cpp -o ./task3/common.x -std=c++11
c++ ./task3/sieveGen.cpp -o ./task3/sieveGen.x -std=c++11
c++ ./task3/sieveTime.cpp -o ./task3/sieveTime.x -std=c++11

echo "Done! :)"