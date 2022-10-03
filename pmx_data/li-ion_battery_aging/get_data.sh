#!/bin/bash
mkdir datasets
cd datasets
wget https://github.com/VaibhavBhujade/RUL-of-Lithium-Ion-Battery/raw/main/CSVs/Input%20n%20Capacity.csv
wget https://github.com/VaibhavBhujade/RUL-of-Lithium-Ion-Battery/raw/main/CSVs/testing_data.csv
wget https://github.com/VaibhavBhujade/RUL-of-Lithium-Ion-Battery/raw/main/CSVs/training_data.csv
mv "Input n Capacity.csv" input_n_capacity.csv
cd ..
