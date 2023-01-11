# pmx for aircraft machine and components

Problem type: Time to failure prediction

Note: Data is hosted on kaggle, and requires setup before downloading (see comments in get_data.sh)

|  |
|  |
|  |
## Sources

Data location: https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance

No data citation available

No data license available.

## Additional information
# PREDICTIVE MAINTENANCE FOR AIRCRAFT MACHINE AND COMPONENTS - DATASET DESCRIPTION:

The aim of this project is to predict failures due to some certain components of a machine in a period of time of 24 hours.
In the dataset we can distinguish 5 files with data and each of them present some other information.

PdM_telemetry – this is Telemetry Time Series Data. It consists of 6 columns – each of them present different values.
1 – this is the datetime when the measurement of sensors recordings.
2 – gives machine ID number.
The rest of the columns is from the hourly averaged sensors recordings 
3 – gives us the values from voltage sensor.
4 – presents values from rotation sensors.
5 – stands for the pressure sensor recordings.
6 – contains values from vibration sensor.
The values were collected from 100 machines for the year 2015.


PdM_maint – this is the dataset from the maintenance. This means that if a component of a machine is replaced, the record of such event is taken and recorded in this dataset.
There are 2 situations in which the components can be replaced:
1.	During the regular scheduled visit, when the technician simply replaces it (what is called the Proactive Maintenance). From this data we have 2014 records.
2.	In the situation when the component breaks down what means that the technician has a responsibility to perform an unscheduled maintenance in order to replace the broken component (what is called the Reactive Maintenance). Such situation is considered to be a failure and data recorded during such event is captured under the Failures dataset. This data gives 2015 records.
The data is rounded to the closest hour due to the telemetry data which was collected at an hourly rate.

PdM_machines – this dataset consist of 3 columns and  simply gives us the information about machine ID, model type and age of the machines.

PDM_failures – this is the dataset that gives us the information about the failures that occurred during the operation of the machines. Each of the records represents the replacement of a component due to a failure. This is the subset of the Maintenance data as this data consist of records from planned and unplanned (when the failure occurred) maintenances.
The data from this dataset is also rounded to the closest hour.


PDM_error – this dataset consists of the records taken when the error occurred while the machine was in operating conditions. Due to the fact that these errors do not shut down the machines, these are not considered to be the failures. 
This dataset also has datetime rounded to the closest hour.

# USEFUL SOURCES RELATED TO THE SUBJECT:

Here is given the original repository from which the dataset was taken and also some very useful links I found on the internet to different codes written for the purpose of performing the predictive maintenance analysis:


The original repository can be found under the following link:
https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance


Below are given very useful links for the additional resources:

1) https://github.com/jegun19/predictive_maintenance/blob/main/train_forecasting.ipynb

2) https://github.com/medinikb/Predictive-Maintenance-using-ML/tree/8c0283de34c38d2065264ede70446997b25d14ba

3) https://medium.com/@Medini_2020/predictive-maintenance-using-machine-learning-3d8b62d5df8e

4) https://github.com/ashishpatel26/Predictive_Maintenance_using_Machine-Learning_Microsoft_Casestudy#readme

5) https://github.com/HarshGupta-DS/Predictive-Maintainence-using-Data-Analysis-and-Time-Series-Forecasting

6) https://medium.com/@Medini_2020/predictive-maintenance-using-machine-learning-3d8b62d5df8e - this is the case study written by Medini Kumar Bora
