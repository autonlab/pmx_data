#!/bin/bash

mkdir datasets
cd datasets

#add or change this list of numbers to get data for different plants
#plants number 1 through 70
for PLANTNUM in 1 3
do
	mkdir $PLANTNUM
	cd $PLANTNUM
	wget -O a.csv "https://github.com/robot007/PHM15/raw/master/site${PLANTNUM}a.csv"
	wget -O b.csv "https://github.com/robot007/PHM15/raw/master/site${PLANTNUM}b.csv"
	wget -O c.csv "https://github.com/robot007/PHM15/raw/master/site${PLANTNUM}c.csv"

	#add column names to csv's, they currently only exist in the documentation
	sed -i "1s/^/Component number m,time t,S1,S2,S3,S4,R1,R2,R3,R4\n/" a.csv
	sed -i "1s/^/n,t,E1,E2\n/" b.csv
	sed -i "1s/^/t1,t2,f\n/" c.csv
	cd ..
done

cd ..
