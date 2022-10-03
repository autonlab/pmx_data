#!/bin/bash
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00447/data.zip
unzip -d datasets data.zip
rm data.zip
rm datasets/documentation.txt
rm datasets/description.txt

#change all files from tsv to csv
for FILENAME in $(ls datasets)
do
        cat datasets/$FILENAME | tr "\\t" "," > datasets/${FILENAME%%.txt}.csv
        rm datasets/$FILENAME
done

