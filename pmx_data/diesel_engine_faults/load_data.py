import scipy.io
import os
import pandas as pd

#I'm not sure how to extract this data in a sensible way
#finding a correspondence between the description of the dataset
#and the actual content is difficul
#I'm going to leave this for now and com back to it

datasets = {}
for dataset in os.listdir("datasets"):
	dataset_path = os.path.join("datasets", dataset)
	dataset_name = dataset.split(".")[0]
	print(dataset_name)
	mat = scipy.io.loadmat(dataset_path)
	print(mat.keys())
	print(mat['__header__'])
	print(mat['__version__'])
	print(mat['__globals__'])
	print(mat['None'])
	mdata = mat['__function_workspace__']
	print(mdata)
	datasets[dataset_name] = mdata[0]

df = pd.DataFrame.from_dict(datasets)
print(df)
