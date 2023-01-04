import dask.dataframe as dd
import pandas as pd
import numpy as np

flight_data_df = dd.read_parquet('all_flights/one_parq')

flight_header_df = pd.read_csv('all_flights/flight_header.csv', index_col = 'Master Index')

flight_data_df = flight_data_df.compute()
grouped = flight_data_df.groupby('Master Index')

