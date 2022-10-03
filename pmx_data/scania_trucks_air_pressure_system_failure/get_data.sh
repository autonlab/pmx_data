#!/bin/bash

mkdir datasets
cd datasets

wget https://archive.ics.uci.edu/ml/machine-learning-databases/00421/aps_failure_test_set.csv
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00421/aps_failure_training_set.csv

#remove first 21 lines as they're a header that will interfere with csv being read
tail -n +21 aps_failure_test_set.csv > test.csv
tail -n +21 aps_failure_training_set.csv > train.csv

rm aps_failure_test_set.csv
rm aps_failure_training_set.csv

cd ..
