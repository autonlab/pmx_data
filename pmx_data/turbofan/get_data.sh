#!/bin/bash
#Requires kaggle api, see https://github.com/Kaggle/kaggle-api for installation and setup instructions
kaggle datasets download --unzip behrad3d/nasa-cmaps
mv CMaps datasets
rm datasets/readme.txt
rm "datasets/Damage Propagation Modeling.pdf"
rm datasets/x.txt

#looping through each train and test file but not RUL files
for FILENAME in $(ls datasets/t*)
do
	FILENAME_CSV=${FILENAME%%.txt}.csv

	#values are space separated rather than comma separated; change this
        cat $FILENAME | tr " " "," > $FILENAME_CSV
        rm $FILENAME

	#there are 2 spaces at the end of each line, now 2 commas, we want to remove both of them
	sed -i "s/..$//" $FILENAME_CSV

	#add column names as first line
	sed -i "1s/^/unit number,time (cycles),os1,os2,os3,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21\n/" $FILENAME_CSV
done

