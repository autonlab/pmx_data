# PREDICTION OF DOWNTIME DURATION OF A FACTORY IN THE FIELD OF PMx

Due to the lack of a materials related to this subject, the folder contains the datasets, their description and link to the original website from which the information has been taken.


## DATASET DESCRIPTION:
The dataset comes from Kesla that is an electric car manufacturing company with several factories in use.
The aim of this project is to predict the downtime duration of various factories in order to identify the factories that are most prone to downtime.

There are given 6 datasets for the purpose of this experiment.
The data scientists create a target where we are given with several variables that may impact the downtime duration of the factories.
We can distinguish 3 classes here:
* 0 - which means low downtime (15 mins to 1 hour);
* 1 - informs that downtime lasts anywhere between 1 hour and 24 hours;
* 2 - provides information for long downtimes that can last from 24 hours to even several days.

The task based on that data is to create a machine learning model that will be able to predict the downtime duration in order to enable the company better handling downtimes and to increase operational efficiency to better handle demand.


We are given with the following 6 different datasets in csv files:
1) train_data - which has a unique event id for each observation of the downtime_duration in a particular factory_number;
2) test_data - Similar to the train dataset, we are provided with an id and a factory_number, we are expected to predict the outage_duration for each of the records;
3) assembly_line_info - For each of the event ids mentioned in the train_data.csv and test_data.csv files and also some additional ids there is a record of the assembly_line_type that is stored in the dataset. There are 10 different types of assembly lines that are observed in the dataset. There can be multiple assembly lines in a single factory, for the factory to be running all the assembly lines must be functioning;
4) issue_info - For each of the event ids mentioned in the train_data.csv and test_data.csv files and also some additional ids there is a record of the issue_type that is stored in the dataset. There are 5 different issue_type's recorded in the dataset. These are classified as an issue by an onsite engineer;

5) log_report_type_data -  For each event id there are log_report_type and volume columns are recorded. log_report_type is a type of the recorded report as reported by a technical team member who is working on the assembly line. Workers are allowed to report specific types of issues using a mobile application. volume is the volume of cars handled by the assembly line in custom company specific units;

6) car_variant_data -  For each of the event ids mentioned in the train_data.csv and test_data.csv files and also some additional ids there is a record of the car_variant_type that is being put together on the assembly line.




The original source from which the dataset has been taken is available under the following link: https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory



The MIT License:


Copyright (c) 2021 Ayan Maity 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




