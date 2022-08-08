# Predictive and Prognostics Maintence Data Repository 

Predictive Maintenance poses a number of challenges for machine learning. The general types of machine learning problems encountered in predictive maintenance are
1. Time to failure prediction
2. Anomaly Detection
3. Clustering
4. Fault detection and root cause analysis

This repository is to help researchers start working on predictive maintenance quickly. It provides an overview of relevant predictive maintenance data and 'quick start' scripts for researchers. We call it the Predictive and prOgnostics maiNtenance data repositorY or (PONY) for short.

| **Dataset**  | **Description**  | **Problems**  | **Location**  | **Existing Benchmark**  |
|--------------|------------------|---------------|---------------|-------------------|
| NASA Telemanom  |   | Supervised Anomaly Detection  |  https://s3-us-west-2.amazonaws.com/telemanom/data.zip | https://github.com/khundman/telemanom   |
| NASA Turbofan  | Multidimensional sensor data from simulated run to faillure experiments   | TIme to event prediction  | Not currently online, copy available from CMU team or the authors on request  |   |
| LANL Acoustic Earthquake data   | high frequency 1d timeseries with regression targets  | Time to event prediction  | www.kaggle.com/competitions/LANL-Earthquake-Prediction  |   |
| Gearbox   | Bench test gearbox with 7 induced faults to detect in 3 channel, high frequency timeseries | Fault Detection  | https://c3.ndc.nasa.gov/dashlink/resources/997/  |   |
| prediction_of_downtime_duration | Predicting downtime duration of car manufacturing assembly lines | Time to event prediction | https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory |  |

# Adding a dataset
The minimum requirments to add a dataset to this repostiory are
1. Create a directory for the data
2. Adding a row in the index table, including what type of problem the data set is used for and its relevance to predictive maintenance
3. Writing a script to download the data
4. Providing a sample script to load the data

# Additional Resources
1. https://data.phmsociety.org/

## Wishlist
It would be good to have some visual inspection data here, a graphical
data modality. I know there are people doing PMx with microscopy or
aerial inspection. Not what WE do, but it certainly falls under the PMx
bucket.
