import scipy.io
import os
import pandas as pd

datasets = {}
for dataset in os.listdir("datasets"):
	dataset_path = os.path.join("datasets", dataset)
	dataset_name = dataset.split(".")[0]
	print(dataset_name)
	mat = scipy.io.loadmat(dataset_path)
	mdata = mat['__function_workspace__']
	datasets[dataset_name] = mdata[0]

df = pd.DataFrame.from_dict(datasets)
print(df)
