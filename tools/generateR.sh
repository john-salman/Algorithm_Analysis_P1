# File name: consecutive.py
# Authors: John Salman, Jack Newman

#This program will generate n random numbers between x and y in file file.txt
# usage: bash generateR.sh <file.txt> <n> <x> <y>

touch $1
echo "file: $1 generated"

MODOP=$(($4-$3+1))
RANDOM=$$
echo "Generating random numbers..."
for i in $(seq $2)
do
	N=$(($(($RANDOM%$MODOP))+$3))
	echo $N >> $1
done
echo "Done"