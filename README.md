# Predictive and Prognostics Maintence Data Repository 

Predictive Maintenance poses a number of challenges for machine learning. The general types of machine learning problems encountered in predictive maintenance are
1. Time to failure prediction
2. Anomaly Detection
3. Clustering
4. Failure root cause analysis

This repository is to help researchers start working on predictive maintenance quickly. It provides an overview of relevant predictive maintenance data and 'quick start' scripts for researchers. We call it the Predictive and prOgnostics maiNtenance data repositorY or (PONY) for short.

+---------------+-------------------+---------------+--------------------------------------------------------+------------------------------------------+
| **Dataset**   | **Description**   | **Problems**  | **Location**                                           | **Repositories**                         |
+===============+===================+===============+========================================================+==========================================+
| Loghub        |                   |               |                                                        |                                          |
+---------------+-------------------+---------------+--------------------------------------------------------+------------------------------------------+
| Nasa          |                   | Supervised    | https://s3-us-west-2.amazonaws.com/telemanom/data.zip  | https://github.com/khundman/telemanom    |
| Telemanom     |                   | Anomaly       |                                                        |                                          |
|               |                   | Detection     |                                                        |                                          |
|               |                   |               |                                                        |                                          |
+---------------+-------------------+---------------+--------------------------------------------------------+------------------------------------------+
| Nasa          | Multi-dimensional | Time to event | Not currently available online.                        |                                          |
| Turbofan      | sensor data       | Prediction    | CMU team maintains a copy, also available from the     |                                          |
|               | from simulated    |               | author on request.                                     |                                          |
|               | run to failure    |               |                                                        |                                          |
|               | experiments       |               |                                                        |                                          |
+---------------+-------------------+---------------+--------------------------------------------------------+------------------------------------------+
| LANL          | high frequency    | Time to event | www.kaggle.com/competitions/LANL-Earthquake-Prediction |                                          |
| Acousitic     | 1-d timeseries    | prediction    |                                                        |                                          |
| Earthquake    | data with         |               |                                                        |                                          |
| Data          | regression        |               |                                                        |                                          |
+---------------+-------------------+---------------+--------------------------------------------------------+------------------------------------------+

# Adding a dataset
The minimum requirments to add a dataset to this repostiory are
1. Create a directory for the data
2. Adding a row in the index table, including what type of problem the data set is used for and its relevance to predicctive maintenance
3. Writing a script to download the data
4. Providing a sample script to load the data

## Wishlist
It would be good to have some visual inspection data here, a graphical
data modality. I know there are people doing PMx with microscopy or
aerial inspection. Not what WE do, but it certainly falls under the PMx
bucket.