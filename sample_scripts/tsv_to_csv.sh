#!/bin/bash
wget https://hostingsite.com/url/data.zip
unzip -d datasets data.zip
rm data.zip

#change all files from tsv to csv
for FILENAME in $(ls datasets)
do
        cat datasets/$FILENAME | tr "\\t" "," > datasets/${FILENAME%%.txt}.csv
        rm datasets/$FILENAME
done

