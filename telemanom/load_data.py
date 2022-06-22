import pandas as pd
import numpy as pd
import os

# General parameters

def load_directory(directory):
    for file in os.listdir(directory):
        print(file)

train_df = load_directory('data/train')