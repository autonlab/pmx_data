import os
import pandas as pd

train = pd.read_csv(os.path.join("datasets", "train.csv"))
test = pd.read_csv(os.path.join("datasets", "test.csv"))