#!/bin/bash
#this dataset is EXTREMELY large - 13gb total while compressed.  
#I only tested this script downloading parts of it, but it can be modified to download the whole thing.

mkdir datasets
cd datasets

#SUBSETS_TO_DOWNLOAD="normal horizontal-misalignment vertical-misalignment imbalance underhang overhang"
SUBSETS_TO_DOWNLOAD="normal"
for SUBSET in $(echo $SUBSETS_TO_DOWNLOAD)
do
	wget http://www02.smt.ufrj.br/~offshore/mfs/database/mafaulda/${SUBSET}.tgz
	tar -xzvf ${SUBSET}.tgz
	rm ${SUBSET}.tgz
done

#add column names to each csv
for FILE in $(find . -name '*.csv')
do
	mv $FILE ${FILE}.tmp
	echo "tachometer,axial underhang,radial underhang,tangential underhang,axial overhang,radial overhang,tangential overhang,microhpone" | cat - ${FILE}.tmp > $FILE
	rm ${FILE}.tmp
done

cd ..
