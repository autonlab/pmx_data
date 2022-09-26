import numpy as np
import pandas as pd
import os

def make_data_dict(path):
	data_dict = {}
	
	for name in os.listdir(path):
		name_path = os.path.join(path, name)

		dataset_name = name.split(".")[0]
		data_dict[dataset_name] = pd.DataFrame(np.load(name_path))

	return data_dict

labeled_anomalies = pd.read_csv(os.path.join("datasets", "labeled_anomalies.csv"))

train = make_data_dict(os.path.join("datasets", "train"))
test = make_data_dict(os.path.join("datasets", "test"))