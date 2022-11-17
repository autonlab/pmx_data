import os
import pandas as pd
import sys
#run this once you've downloaded your dataset to check if any of the csv's have missing values
#it will look through all the subfolders recursively 
#and will print "True" if any csv has missing data and "False" otherwise
#to run: python check_for_missing_values.py /path/to/dataset

def has_missing_data(path):
	for name in os.listdir(path):
		name_path = os.path.join(path, name)
		
		if os.path.isdir(name_path):
			if has_missing_data(name_path):
				return True

		elif name.split(".")[1] == "csv":
			dataframe = pd.read_csv(name_path)
			if dataframe.isnull().values.any():
				return True

		else:
			#ignore non-csv files
			pass

	return False

try:
	path = sys.argv[1]
except:
	#if run with no arguments, assume it's being run in the data folder
	path = "datasets"

print(has_missing_data(path))
