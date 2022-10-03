wget https://c3.ndc.nasa.gov/dashlink/static/media/dataset/PHM09_competition_1.zip
unzip PHM09_competition_1.zip -d datasets
rm PHM09_competition_1.zip

#add column names to each csv
cd datasets
for FILE in $(ls)
do
	mv $FILE ${FILE}.tmp
	echo "input_accel,output_accel,tachometer" | cat - ${FILE}.tmp > $FILE
	rm ${FILE}.tmp
done
cd ..