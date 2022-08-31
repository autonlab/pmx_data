#%%
import os
import pandas as pd
import numpy as np

#    • Channel 1 is the input side Accelerometer
#    • Channel 2 is the output side Accelerometer
#    • Channel 3 is the Tachometer Signal: 10 pulse per revolution

#%%
data_d=dict()

for file in os.listdir('data'):
    data_df = pd.read_csv(f"data/{file}",names=["input_accel","output_accel","tachometer"])
    (n,d)=data_df.shape
    data_df["time"] = np.linspace(0.0,2.0,n)

    run_number = int(file.replace("Run_","")[:-4])
    print(run_number, data_df.shape)
    data_d[run_number] = data_df.copy()
    
