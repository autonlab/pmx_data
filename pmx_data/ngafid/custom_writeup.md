# A Large-Scale Annotated Multivariate Time Series Aviation Maintenance Dataset from the NGAFID

Made available by Hong Yang and Travis Desell.

https://arxiv.org/abs/2210.07317

This data set is the largest publicly available, non-simulated, fleet-wide aircraft data set.
It contains 31,177 hours of flight data from Cessna 172 aircraft across 28,935 flights. Flight data consist of 23 sensors at 1Hz. In total, the data contain 100 million rows with a total size of 4.3 GB.

Data: https://doi.org/10.5281/zenodo.6624956 and https://www.kaggle.com/datasets/hooong/aviation-maintenance-dataset-from-the-ngafid 


Benchmarks: https://github.com/hyang0129/NGAFIDDATASET 

A repository containing helper code to automatically download and process the dataset and 2 Colab notebooks for replicating the benchmark experiments.

The above files are licensed under GNU General Public License V3.0.

## Data details

Flight dataframe is indexed by flight ID (Master Index).
The dataframe contains the following columns.
|Column | Name Description |
|:--|:--|
|volt1 | Main electrical system bus voltage (alternators and main battery)|
|volt2 | Essential bus (standby battery) bus voltage|
|amp1 | Ammeter on the main battery (+ charging, - discharging)|
|amp2 | Ammeter on the standby battery (+ charging, - discharging)|
|FQtyL | Fuel quantity left|
|FQtyR | Fuel quantity right|
|E1 FFlow | Engine fuel flow rate|
|E1 OilT | Engine oil temperature|
|E1 OilP | Engine oil pressure|
|E1 RPM | Engine rotations per minute|
|E1 CHT1 | 1st cylinder head temperature|
|E1 CHT2 | 2nd cylinder head temperature|
|E1 CHT3 | 3rd cylinder head temperature|
|E1 CHT4 | 4th cylinder head temperature|
|E1 EGT1 | 1st Exhaust gas temperature|
|E1 EGT2 | 2nd Exhaust gas temperature|
|E1 EGT3 | 3rd Exhaust gas temperature|
|E1 EGT4 | 4th Exhaust gas temperature|
|OAT | Outside air temperature|
|IAS | Indicated air speed|
|VSpd | Vertical speed|
|NormAc | Normal acceleration|
|AltMSL | Altitude miles above sea level|
|timestep | relative time of measurement |
|cluster | 1 of 36 groups of maintenance action |

The header dataframe is structured as follows.
```
<class 'pandas.core.frame.DataFrame'>
Int64Index: 28935 entries, 1 to 32820
Data columns (total 6 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   before_after           28935 non-null  object 
 1   date_diff              28935 non-null  int64  
 2   flight_length          28935 non-null  float64
 3   label                  28935 non-null  object 
 4   hierarchy              10581 non-null  object 
 5   number_flights_before  28935 non-null  int64  
dtypes: float64(1), int64(2), object(3)
memory usage: 1.5+ MB
```
|Column | Name Description |
|:--|:--|
|before_after | indicates whether flight occurs before or after associated maintenance event |
|date_diff | |
|flight_length | |
|label | |
|hierarchy | |
|number_flights_before | |

