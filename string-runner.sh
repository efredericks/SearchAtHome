#!/bin/bash

# string-runner.sh
# Erik Fredericks, 2020
# Modify the redirect based on the experiment being run

for i in {1..25}; do
  echo "Executing seed $i"
  { time /usr/bin/python3 string-search.py $i ; } 2> time-string-ga-$i.txt
done
