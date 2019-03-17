#!/bin/bash

#Write a bash script to calculate the frequency of each word in a text file
cat file.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1}'