#!/bin/bash
#some datasets I found download as csv's with no column names
#this is a sample script to add a line at the top of each csv containing a header with the column names
#replace "colname1,coname2,colname3,colname4" with a string containing your dataset's column names, in order, separated by commas

wget https://hostingsite.com/url/data.zip
unzip -d datasets data.zip
rm data.zip

#add column names to each csv
cd datasets

for FILE in $(find . -name '*.csv')
do
	mv $FILE ${FILE}.tmp
	echo "colname1,coname2,colname3,colname4" | cat - ${FILE}.tmp > $FILE
	rm ${FILE}.tmp
done

cd ..
