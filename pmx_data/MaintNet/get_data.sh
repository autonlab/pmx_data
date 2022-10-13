#!/bin/bash

mkdir datasets
cd datasets

# Aircraft data
mkdir aircraft
cd aircraft
wget https://people.rit.edu/fa3019/technical/data/aviation_abbriviation.csv
wget https://people.rit.edu/fa3019/technical/data/grammar.csv
wget https://people.rit.edu/fa3019/technical/data/domain_words2_termBank.csv
wget https://people.rit.edu/fa3019/technical/data/maintnet_aviation_dataset_deidentified.csv
cd ..

# Automotive data
mkdir automotive
cd automotive
wget https://people.rit.edu/fa3019/technical/car_abbriviation.csv
wget https://people.rit.edu/fa3019/technical/data/grammar.csv
wget https://people.rit.edu/fa3019/technical/data/domain_words2_termBank.csv
wget https://people.rit.edu/fa3019/technical/data/Labeled_Car_Dataset200.csv
cd ..

# Facility data
mkdir facility
cd facility
wget https://people.rit.edu/fa3019/technical/data/facility_abbriviation.csv
wget https://people.rit.edu/fa3019/technical/data/facilty_grammar.csv
wget https://people.rit.edu/fa3019/technical/data/facility_domain.csv
wget https://people.rit.edu/fa3019/technical/data/Facility_Maintenance200.csv
cd ..

cd ..
