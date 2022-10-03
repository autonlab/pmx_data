import os
import pandas as pd
datasets = {}
for dataset in os.listdir("datasets"):
	dataset_path = os.path.join("datasets", dataset)
	dataset_name = dataset.split(".")[0]
	datasets[dataset_name] = pd.read_csv(dataset_path)

