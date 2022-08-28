# Predictive and Prognostics Maintence Data Repository 

Predictive Maintenance poses a number of challenges for machine learning. The general types of machine learning problems encountered in predictive maintenance are
1. Time to failure prediction
2. Anomaly detection
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
| cnc_mill_tool_wear | Time series machining data across 18 CNC milling experiments | Fault Detection | https://www.kaggle.com/datasets/shasun/tool-wear-detection-in-cnc-mill |  |
| diesel_engine_faults | Diesel engine data from failure scenarios across 4 operating states | Fault Detection | https://data.mendeley.com/datasets/k22zxz29kr/1 |  |
| autonomous_underwater_vehicle | Time series measurements from an underwater vehicle with 5 fault types | Fault Detection | https://data.mendeley.com/datasets/7rp2pmr6mx/1 |  |
| electrical_fault_detection | Line currents and voltages of electrical system with 4 fault conditions | Fault Detection and Classification | https://www.kaggle.com/datasets/esathyaprakash/electrical-fault-detection-and-classification |  |
| hdd_data | 2013 BlackBlaze hard drive failure data | Time to failure prediction | https://www.backblaze.com/b2/hard-drive-test-data.html |  |
| hydraulic_sensor_system | Time series sensor readings on a hydraulic test rig with target condition values | Fault Detection and Classification | https://archive.ics.uci.edu/ml/datasets/Condition+monitoring+of+hydraulic+systems# |  |
| li-ion_battery_aging | Data from tests on 4 Lithium-Ion batteries cycled under random currents | Time to failure prediction | https://github.com/VaibhavBhujade/RUL-of-Lithium-Ion-Battery/tree/main/CSVs |  |
| maintenance_of_naval_propulsion_plants | Synthetic gas turbine data | Time to failure prediction | https://archive.ics.uci.edu/ml/datasets/Condition+Based+Maintenance+of+Naval+Propulsion+Plants |  |
| nasa_milling_prognostic_dataset | Investigating wear on a milling machine under several runs in various operating conditions | Fault Detection | https://www.kaggle.com/datasets/vinayak123tyagi/milling-data-set-prognostic-data |  |
| one_year_industrial_component_degradation | High-frequency time series data documentating degradation of an industrial component over the course of a year | Time to failure prediction | https://www.kaggle.com/datasets/inIT-OWL/one-year-industrial-component-degradation |  |
| pmx_iot_sensor | Data on failure of heat exchagers on an assembly line | Time to failure prediction | https://github.com/shikhilnangia/iotsensor/blob/master/iot_sensor_dataset.csv |  |
| pmx_for_ga | Per-second sensor data from flights of a Cessna 172S preceeding maintenance | Time to failure prediction | https://www.kaggle.com/datasets/hooong/ngafid-mc-20210917 |  |
| plant_fault_detection | Time series measurement from 70 plants with 6 fault types | Fault detection | https://github.com/robot007/PHM15 |  |
| predictive_maintenance_fault_classification | Sensor data from a drill press under induced fault conditions | Fault detection and classification | https://github.com/nagdevAmruthnath/Predictive-Maintenance |  |
| pmx_for_aircraft_machine_and_components | telemetry time series data and maintenance records for aircraft | Time to failure prediction | https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance |  |
| pmx_from_elevator_industry | Data on elevator ball bearing wear | Time to failure prediction | https://zenodo.org/record/3653909#.YsmqoC8Rrys |  |
| production_plant_data_for_condition_monitoring | Sensor data from 8 run-to-failure experiements on a production line component | Time to failure prediction | https://www.kaggle.com/datasets/inIT-OWL/production-plant-data-for-condition-monitoring |  |
| robot_execution_failures | Sensor data from a robot after 5 different types of failures | Time to failure prediction | https://www.kaggle.com/datasets/prashant111/robot-execution-failures |  |
| scania_trucks_air_pressure_system_failure | Classifying whether truck failure is a result of its air pressure system | Fault classification | https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks |  |



# Adding a dataset
The minimum requirements to add a dataset to this repository are
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
