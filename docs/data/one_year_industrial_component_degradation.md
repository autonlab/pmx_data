# one year industrial component degradation

Problem type: Time to failure prediction

Note: Data is hosted on kaggle, and requires setup before downloading (see comments in get_data.sh)

|  |
|  |
|  |
## Sources

Data location: https://www.kaggle.com/datasets/inIT-OWL/one-year-industrial-component-degradation

No data citation available

No data license available.

## Additional information
# ONE YEAR INDUSTRIAL COMPONENT DEGRADATION DATASET DESCRIPTION


The dataset consist of the machine data taken from the degrading component recorded from the sensors located on the component over the period of 12 months.

In total, the dataset consist of 519 files, each of them is saved in the following format:
MM-DDTHHMMSSNUMmodeX.csv
The MM applies to a month when the data recording was taken (from 1 to 12 month, not the calendar month).
DD applies to a day of the month.
T starts the Time section, where HH(Hour) MM(minute) SS(Second) applies to the start time of a day of the recording.
NUM means the sample number.
ModeX applies to a mode (which varies from 1 to 8, depending on the mode).
Each of the files is more or less 8 seconds sample with a time resolution of 4ms which in total gives 2048 time-samples for every file.
In this dataset you are given with  different modes and different speeds values that the machine might be operated in.

The purpose of this dataset is to enable an option to analyze the component degradation process over the course of the year. Based on such analysis you would be able to check if the component has been replaced at the some point or not, you might check if the wear can be accurately predicted and also you might make a prediction of the RUL (that stand for Remaining Useful Life) in order to determinate the maintenance windows (what is the part of predictive maintenance).

# SOURCES

In this section I provide sources and references for the origin of the dataset, articles and codes found for the Industry component degradation.

The dataset comes from the kaggle website and is available for everyone under the terms which yo can open via the following link: https://creativecommons.org/licenses/by-sa/3.0/
The License belongs to CC BY-SA 3.0
References are as follow: von Birgelen, Alexander; Buratti, Davide; Mager, Jens; Niggemann, Oliver: Self-Organizing Maps for Anomaly Localization and Predictive Maintenance in Cyber-Physical Production Systems. In: 51st CIRP Conference on Manufacturing Systems (CIRP CMS 2018) CIRP-CMS, May 2018.

Below I provide the citation to the article connected with the dataset topic:
Alexander von Birgelen, Davide Buratti, Jens Mager, Oliver Niggemann, Self-Organizing Maps for Anomaly Localization and Predictive Maintenance in Cyber-Physical Production Systems, Procedia CIRP, Volume 72, 2018, Pages 480-485, ISSN 2212-8271, https://doi.org/10.1016/j.procir.2018.03.150. (https://www.sciencedirect.com/science/article/pii/S221282711830307X)

I provide also the access via the following link: https://github.com/Iuryck/Machine_Degradation to the sample GitHub code found on the internet (author: Iuryck Santos) about the "component degradation over time, analyzed with machine learning".

The notebook with a code is available also on kaggle website (link provided: https://www.kaggle.com/code/bhavdeepsingh33/one-year-industrial-component-degradation).
This Notebook has been released under the Apache 2.0 open source license (https://www.apache.org/licenses/LICENSE-2.0).
