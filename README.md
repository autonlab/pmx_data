# Predictive and Prognostics Maintence Data Repository

Predictive Maintenance poses a number of challenges for machine learning. The general types of machine learning problems encountered in predictive maintenance are:

1. Time to failure prediction
2. Anomaly detection
3. Clustering
4. Fault detection and root cause analysis

This repository is to help researchers start working on predictive maintenance quickly. It provides an overview of relevant predictive maintenance data and 'quick start' scripts for researchers. We call it the Predictive and prOgnostics maiNtenance data repositorY or (PONY) for short.

| **Dataset**                                    | **Description**                                                                                                                     | **Problems**                       |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| autonomous_underwater_vehicle                  | Time series measurements from an underwater vehicle with 5 fault types                                                              | supervised_fault_classification    |
| cnc_mill_tool_wear                             | Time series machining data across 18 CNC milling experiments                                                                        | Fault Detection                    |
| delta_robot                                    | Time series sensor data for a robot used in a production line                                                                       | Anomaly detection                  |
| diesel_engine_faults                           | Diesel engine data from failure scenarios across 4 operating states                                                                 | Fault Detection                    |
| electrical_fault_detection                     | Line currents and voltages of electrical system with 4 fault conditions                                                             | Fault Detection and Classification |
| gearbox_fault_detection                        | Bench test gearbox with 7 induced faults to detect in 3 channels, high frequency timeseries                                         | Fault Detection                    |
| gearbox_fault_diagnosis                        | Vibration measurements from healthy and faulty gearboxes with varying loads and recoring frequencies                                | Fault detection                    |
| hdd_data                                       | 2013 BlackBlaze hard drive failure data                                                                                             | Time to failure prediction         |
| hydraulic_sensor_system                        | Time series sensor readings on a hydraulic test rig with target condition values                                                    | Fault Detection and Classification |
| li-ion_battery_aging                           | Data from tests on 4 Lithium-Ion batteries cycled under random currents                                                             | Time to failure prediction         |
| machinery_faults_datasets                      | Extremely large dataset of simulated time series machinery data with 6 operating states, each of which can have several fault types | Fault classification               |
| nasa_milling_prognostic_dataset                | Investigating wear on a milling machine under several runs in various operating conditions                                          | Fault Detection                    |
| maintenance_of_naval_propulsion_plants         | Synthetic gas turbine data                                                                                                          | Time to failure prediction         |
| one_year_industrial_component_degradation      | High-frequency time series data documentating degradation of an industrial component over the course of a year                      | Time to failure prediction         |
| plant_fault_detection                          | Time series measurement from 70 plants with 6 fault types                                                                           | Fault detection                    |
| pmx_for_ga                                     | Per-second sensor data from flights of a Cessna 172S preceeding maintenance                                                         | Time to failure prediction         |
| pmx_for_aircraft_machine_and_components        | telemetry time series data and maintenance records for aircraft                                                                     | Time to failure prediction         |
| pmx_from_elevator_industry                     | Data on elevator ball bearing wear                                                                                                  | Time to failure prediction         |
| pmx_iot_sensor                                 | Data on failure of heat exchagers on an assembly line                                                                               | Time to failure prediction         |
| prediction_of_downtime_duration                | Predicting downtime duration of car manufacturing assembly lines                                                                    | Time to event prediction           |
| predictive_maintenance_fault_classification    | Sensor data from a drill press under induced fault conditions                                                                       | Fault detection and classification |
| production_plant_data_for_condition_monitoring | Sensor data from 8 run-to-failure experiements on a production line component                                                       | Time to failure prediction         |
| pump_sensor                                    | Time series sensor readings from a water pump with status                                                                           | Anomaly detection                  |
| robot_execution_failures                       | Sensor data from a robot after 5 different types of failures                                                                        | Time to failure prediction         |
| Air pressure system failures in Scania trucks. | Classifying whether truck failure is a result of its air pressure system                                                            | classification                     |
| solar_power_generation                         | Power generation and weather data for 2 solar power plants                                                                          | Fault detection                    |
| telemanom                                      | Telemetry data from 2 spacecraft with labeled anomalies in the testing set                                                          | Supervised Anomaly Detection       |
| turbofan                                       | Multidimensional sensor data from simulated run to failure experiments                                                              | Time to event prediction           |

# Adding a dataset

The minimum requirements to add a dataset to this repository are:

1. Create a directory for the data
2. Adding a row in the index table, including what type of problem the data set is used for and its relevance to predictive maintenance
3. Writing a script to download the data
4. Providing a sample script to load the data

# Additional Resources

https://data.phmsociety.org/

# Wishlist

It would be good to have some visual inspection data here, a graphical data modality. I know there are people doing PMx with microscopy or aerial inspection. Not what WE do, but it certainly falls under the PMx bucket.