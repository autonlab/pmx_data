#!/bin/bash
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00316/UCI%20CBM%20Dataset.zip
unzip "UCI CBM Dataset.zip"
rm "UCI CBM Dataset.zip"
rm -rf __MACOSX
mv "UCI CBM Dataset" datasets
cd datasets

#values are separated by 3 spaces; replace this with a comma
sed -i 's/   /,/g' data.txt
#remove commas at the start of each line
sed -i 's/^.//' data.txt

#replace newlines in Features.txt with commas, rename to Features.csv
cat Features.txt | tr "\n" "," > Features.csv

#make csv by concatenating Features.txt and data.txt, adding a newline in between
cat Features.csv <(echo) data.txt > data.csv

rm data.txt  Features.csv  Features.txt  README.txt
cd ..
