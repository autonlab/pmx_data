import os
import pandas as pd

print("Creating summary csv for train and test sets of time series")

data = {}

for setname in ['train', 'test']:

	data[setname] =  pd.DataFrame({
		'filename': [],
		'class': []
	})

	setpath = os.path.join("datasets", setname)
	assert(os.path.isdir(setpath))

	for classname in os.listdir(setpath):

		classpath = os.path.join(setpath, classname)
		assert(os.path.isdir(classpath))

		#for each time series file, add row to the dataframe containing 
		#      the filename for the time series and its class
		for filename in os.listdir(classpath):
			data[setname].loc[len(data[setname].index)] = [filename, classname]

data['train'].to_csv("datasets/train.csv", index=False)
data['test'].to_csv("datasets/test.csv", index=False)