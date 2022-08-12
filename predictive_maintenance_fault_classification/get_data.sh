#!/bin/bash
mkdir datasets
cd datasets
wget https://github.com/nagdevAmruthnath/Predictive-Maintenance/raw/master/base.csv
wget -O dry_run.csv https://github.com/nagdevAmruthnath/Predictive-Maintenance/raw/master/dry%20run.csv
wget -O imbalance1.csv https://github.com/nagdevAmruthnath/Predictive-Maintenance/raw/master/imbalance%201.csv
wget -O imbalance2.csv https://github.com/nagdevAmruthnath/Predictive-Maintenance/raw/master/imbalance%202.csv
cd ..
