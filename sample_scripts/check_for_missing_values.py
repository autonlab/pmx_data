import os
import pandas as pd
#run this once you've downloaded your dataset to check if any of the csv's have missing values
#it will look through all the subfolders recursively and print a message if they have missing values in any of their files
#if there are no missing values, it will not print anything.

def make_data_dict(path):
	missingvalues = False
	data_dict = {}
	
	for name in os.listdir(path):
		name_path = os.path.join(path, name)
		
		#for each directory, make a sub-dictionary
		#for each csv, import it as a dataframe
		if os.path.isdir(name_path):
			data_dict[name] = make_data_dict(name_path)
		else:
			dataset_name = name.split(".")[0]
			data_dict[dataset_name] = pd.read_csv(name_path)
			if not missingvalues: 
				missingvalues = data_dict[dataset_name].isnull().values.any()
	if missingvalues:
		print("Null values in " + path)
	return data_dict

datasets = make_data_dict("datasets")
