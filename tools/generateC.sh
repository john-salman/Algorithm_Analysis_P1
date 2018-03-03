# File name: consecutive.py
# Authors: John Salman, Jack Newman

# This program will generate numbers consecutively from 1 to n in file file.txt

# Usage: bash generateC.sh <file.txt> <n>


touch $1
echo "file: $1 created"

echo "Generating..."
for i in $(seq $2)
do
	echo $i >> $1
done

echo "Done."
