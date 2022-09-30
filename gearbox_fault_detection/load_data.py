import os
import pandas as pd
import numpy as np

data_d=dict()

for file in os.listdir('datasets'):
    data_df = pd.read_csv(os.path.join("datasets", file))

    #add time column
    (n,d)=data_df.shape
    samples_per_second = 66666.67
    step = 1 / samples_per_second
    data_df["time"] = np.linspace(0.0,step*n,n)

    run_number = int(file.replace("Run_","")[:-4])
    print(run_number, data_df.shape)
    data_d[run_number] = data_df.copy()
