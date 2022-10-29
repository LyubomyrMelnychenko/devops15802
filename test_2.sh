#!/bin/bash
counter=1
while [ $counter -le 10 ]
do
    echo $counter
    let counter=$counter+1
done
#for i in range(10);
#for i in "$@";
#do 
#    echo $i
#done