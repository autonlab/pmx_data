#!/bin/bash
#above comment specifies that this script will use bash shell interpreter

#download data zip file from the hosting site using wget
#curl 'https://www.accessdata.fda.gov/MAUDE/ftparea/device[1998-2022].zip' 
wget https://www.accessdata.fda.gov/MAUDE/ftparea/mdrfoithru2022.zip
unzip -d datasets mdrfoithru2022.zip
rm mdrfoithru2022.zip
wget https://www.accessdata.fda.gov/MAUDE/ftparea/patientthru2022.zip
unzip -d datasets patientthru2022.zip
rm patientthru2022.zip
for year in {2000..2022}; do
	wget https://www.accessdata.fda.gov/MAUDE/ftparea/device${year}.zip
	unzip -d datasets device${year}.zip
	rm device${year}.zip
	wget https://www.accessdata.fda.gov/MAUDE/ftparea/foitext${year}.zip
	unzip -d datasets foitext${year}.zip
	rm foitext${year}.zip

done

#if your data is already in a csv format that is easy to ingest, no further steps are needed.

