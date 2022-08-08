#!/bin/bash
mkdir datasets
cd datasets
wget https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory/raw/main/Datasets/assembly_line_info.csv
wget https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory/raw/main/Datasets/car_variant_data.csv
wget https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory/raw/main/Datasets/issue_info.csv
wget https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory/raw/main/Datasets/log_report_type_data.csv
wget https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory/raw/main/Datasets/test_data.csv
wget https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory/raw/main/Datasets/train_data.csv
cd ..
