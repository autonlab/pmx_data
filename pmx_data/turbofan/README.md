# turbofan

Problem type: Time to event prediction

|  |
|  |
|  |
## Sources

Data location: https://www.kaggle.com/datasets/behrad3d/nasa-cmaps

No data citation available

No data license available.

## Additional information
The project is about turbofan engine degradation process. There is collected dataset from engine degradation simulation experiments conducted at NASA using C-MAPSS. 

We can distuinguish 4 different sets further divided into training and test subsets. Each time series from the sets is from a different engine. Each of the engines starts working in normal conditions (no fault condition noticed). 

Important note: the engines have different degrees of initial wear and manufacturing variation. There are also 3 operational settings with a substantial effect on engine performance. The data is contaminated with sensor noise. The engines operate normally in the beginning but develop a fault over some time. 

In the training set, the engines are run to failure, while in the test sets the end comes sometime before failure. The main goal is to predict RUL (Remaining Useful Life) of each engine.  The dataset includes true Remaining Useful Life (RUL) values for the test data.

Each of the columns contained in the data provides the following information (starting from the left column): 1: Engine unit number 2: Time (in cycles) 3-5: Three operational settings 6-26: Sensor readings

Data Set: FD001
Train trjectories: 100
Test trajectories: 100
Conditions: ONE (Sea Level)
Fault Modes: ONE (HPC Degradation)

Data Set: FD002
Train trjectories: 260
Test trajectories: 259
Conditions: SIX 
Fault Modes: ONE (HPC Degradation)

Data Set: FD003
Train trjectories: 100
Test trajectories: 100
Conditions: ONE (Sea Level)
Fault Modes: TWO (HPC Degradation, Fan Degradation)

Data Set: FD004
Train trjectories: 248
Test trajectories: 249
Conditions: SIX 
Fault Modes: TWO (HPC Degradation, Fan Degradation)


# SOURCES

This dataset is taken from the official NASA website but is no longer available here.
Another place where you can find this data is from kaggle website available under the following link: https://www.kaggle.com/datasets/behrad3d/nasa-cmaps

Below you can find some other useful link regarding Turbofan engine degradation dataset:

1) link for another article: https://www.sciencedirect.com/sdfe/reader/pii/S0951832018307506/pdf
2) links for GitHub codes: 
 	- https://github.com/kpeters/exploring-nasas-turbofan-dataset
	- https://github.com/jiaxiang-cheng/PyTorch-Transformer-for-RUL-Prediction
	- https://github.com/mohyunho/N-CMAPSS_DL