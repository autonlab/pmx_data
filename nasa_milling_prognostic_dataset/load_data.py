import pandas as pd
mill = pd.read_csv("datasets/mill.csv")
mill = mill.drop("Unnamed: 0", axis=1)
