#!/bin/bash
# Given a text file file.txt, print just the 10th line of the file.

cat file.txt | while read line
do 
   echo $line
done

# Solution 1:
sed -n '10p' file.txt

# Solution 2:
awk 'FNR==10' file.txt

# Solution 3:
tail -n+10 file.txt | head -1
