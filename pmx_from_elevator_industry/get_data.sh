#!/bin/bash

wget https://zenodo.org/record/3653909/files/omlstreaming/grc-datasets-pred-maintenance-v1.0.0.zip?download=1
unzip grc-datasets-pred-maintenance-v1.0.0.zip?download=1
rm grc-datasets-pred-maintenance-v1.0.0.zip?download=1
mv omlstreaming-grc-datasets-pred-maintenance-892dd65 datasets
rm datasets/README.md

#the dataset is semicolon rather than comma separated; change to csv
sed -i "s/;/,/g" datasets/predictive-maintenance-dataset.csv
