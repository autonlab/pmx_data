# PREDICTION OF DOWNTIME DURATION OF A FACTORY IN THE FIELD OF PMx

Due to the lack of materials related to this subject, the folder contains the datasets, their description and link to the original website from which the information has been taken.


# DATASET DESCRIPTION
The dataset comes from Kesla, which is an electric car manufacturing company with several factories in use.
The aim of this project is to predict the downtime duration of various factories in order to identify the factories that are most prone to downtime.

There are 3 classes:
* 0 - low downtime (15 mins to 1 hour)
* 1 - medium downtime (1 hour to 24 hours)
* 2 - long downtime (24 hours to several days)

The data consists of 6 different csv files:
1) train_data - Has a unique event id for each observation of the downtime_duration in a particular factory_number.  Contains 876 different factories.

2) test_data - Similar to the train dataset, we are provided with an id and a factory_number, we are expected to predict the downtime_duration for each of the records.  Contains 531 different factories

3) assembly_line_info - For each of the event ids mentioned in the train_data.csv and test_data.csv files, and also some additional ids, there is a record of the assembly_line_type. There are 10 different types of assembly lines observed in the dataset. There can be multiple assembly lines in a single factory, and for the factory to be running, all the assembly lines must be functioning.

4) issue_info - For each of the event ids mentioned in the train_data.csv and test_data.csv files, and also some additional ids, there is a record of the issue_type. There are 5 different issue_type's recorded in the dataset. These are classified as an issue by an onsite engineer.

5) log_report_type_data - For each event id there is a log_report_type and a volume. Workers are allowed to report specific types of issues using a mobile application, and log_report_type is the type of the reported issue.  There are 386 different log_report_types.  volume is the volume of cars handled by the assembly line in custom company specific units.

6) car_variant_data -  For each of the event ids mentioned in the train_data.csv and test_data.csv files, and also some additional ids, there is a record of the car_variant_type that is being put together on the assembly line.  There are 53 different types of cars.

# SOURCES

The original source from which the dataset has been taken is https://github.com/aayanmaity/Predicting-the-downtime-duration-of-a-factory





