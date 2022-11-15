# LI-ION BATTEY AGING --> DATASET DESCRIPTION:

The dataset originally is from NASA Ames Prognostics Center of Excellence. 
The dataset can be used in order to develop the prognostic algorithms. In particular, due to the differences in depth-of-discharge (DOD), the duration of rest periods and intrinsic variability, no two cells have the same state-of-life (SOL) at the same cycle index. The aim is to be able to manage this uncertainty, which is representative of actual usage, and make reliable predictions of Remaining Useful Life (RUL) in both the End-of-Discharge (EOD) and End-of-Life (EOL) contexts.
The Remaining Useful Life is the length of time a machine is likely to operate before it requires repair or replacement. By taking RUL into account, engineers can schedule maintenance, optimize operating efficiency, and avoid unplanned downtime. For this reason, estimating RUL is a top priority in predictive maintenance programs

In order to simulate the dynamic operation conditions in real applications, 18 650 LiCoO2 batteries were cycled under a series of random currents rather than the constant discharge currents. In the Datasets folder you can find data from 4 batteries: B0005, B0006,B0007 and B0018. These datasets have been downloaded from the GitHub repository of which the creator is VaibhavBhujade (the link to the repository is added to the Sources file which is located in the Documentation folder).
Each of the batteries were cycled under a series of random currents and each loading period lasted for 5 mins.
Charging and discharging test was performed after every 1500 periods in order to measure the battery capacity. The failure threshold for 4 of the batteries are considered as the capacities at the end of the test and the capacities are plotted against the test time (days).

For each of 4 battery datasets, the number of charge, discharge and impedance cycles is 616.
The dataset contained in the Documentation folder is already divided into the testing set and training set (each of them contains data of 4 batteries ) and Input n Capacity dataset files.


The data consist of the following structure:
- cycle --> this is the top level structure array which contains 3 types of operations: charge, discharge and impedance operations.
- type --> it provides an information about the type which can be charge, discharge or impedance
- ambient_temperature --> this is the column that gives an information about the ambient temperature (which for this data is considered to be as 24 Celsius degrees).
- time --> this is the column about the date and time of the start of the cycle (in MATLAB date vector format)
- data --> data structure which contains the measurements



Parameters for charge cycles are as follow:
- voltage
- current
- temperature
- current charge
- voltage charge
- time


Parameters for discharge cycles are as follow:
- voltage
- current
- temperature
- current load
- voltage load
- capacity
- time

Parameters for impedance cycle are as follow:
- Voltage_measured
- Current_measured
- Temperature_measured
- Current_charge
- Voltage_charge
- Time
- Capacity

For charge operation we are given with the following fields:
* Voltage_measured --> Battery terminal voltage (Volts)
* Current_measured --> Battery output current (Amps)
* Temperature_measured --> Battery temperature (degree C)
* Current_charge --> Current measured at charger (Amps)
* Voltage_charge --> Voltage measured at charger (Volts)
* Time --> Time vector for the cycle (secs)

For discharge operation we are given with the following fields:

* Voltage_measured: Battery terminal voltage (Volts)
* Current_measured: Battery output current (Amps)
* Temperature_measured: Battery temperature (degree C)
* Current_charge: Current measured at load (Amps)
* Voltage_charge: Voltage measured at load (Volts)
* Time: Time vector for the cycle (secs)
* Capacity: Battery capacity (Ahr) for discharge till 2.7V

For impedance operation we are given with the following fields:
* Sense_current: Current in sense branch (Amps)
* Battery_current: Current in battery branch (Amps)
* Current_ratio: Ratio of the above currents
* Battery_impedance: Battery impedance (Ohms) computed from raw data
* Rectified_impedance: Calibrated and smoothed battery impedance (Ohms)
* Re: Estimated electrolyte resistance (Ohms)

# SOURCES

The dataset has been downloaded from the Github Repository of which the creator is VaibhavBhujade, which is available under the following link: https://github.com/VaibhavBhujade/RUL-of-Lithium-Ion-Battery/tree/main/CSVs


Citation and References to different articles related to the subjects:

1) Y. Wu, W. Li, Y. Wang and K. Zhang, "Remaining Useful Life Prediction of Lithium-Ion Batteries Using Neural Network and Bat-Based Particle Filter," in IEEE Access, vol. 7, pp. 54843-54854, 2019, doi: 10.1109/ACCESS.2019.2913163. (https://ieeexplore.ieee.org/document/8698866)

2) A. Rastegarpanah, Y. Wang and R. Stolkin, "Predicting the Remaining Life of Lithium-ion Batteries Using a CNN-LSTM Model," 2022 8th International Conference on Mechatronics and Robotics Engineering (ICMRE), 2022, pp. 73-78, doi: 10.1109/ICMRE54455.2022.9734081. *https://ieeexplore.ieee.org/document/9734081)

3) J. Zhu, T. Tan, L. Wu and H. Yuan, "RUL Prediction of Lithium-Ion Battery Based on Improved DGWO-ELM Method in a Random Discharge Rates Environment," in IEEE Access, vol. 7, pp. 125176-125187, 2019, doi: 10.1109/ACCESS.2019.2936822. (https://ieeexplore.ieee.org/document/8809676)

4) Ji Wu, Chenbin Zhang, Zonghai Chen, An online method for lithium-ion battery remaining useful life estimation using importance sampling and neural networks, Applied Energy, Volume 173, 2016, Pages 134-140, ISSN 0306-2619, https://doi.org/10.1016/j.apenergy.2016.04.057. (https://www.sciencedirect.com/science/article/pii/S0306261916304846)

5) Y. Zhang, R. Xiong, H. He and M. G. Pecht, "Long Short-Term Memory Recurrent Neural Network for Remaining Useful Life Prediction of Lithium-Ion Batteries," in IEEE Transactions on Vehicular Technology, vol. 67, no. 7, pp. 5695-5705, July 2018, doi: 10.1109/TVT.2018.2805189.

6) Datong Liu, Jianbao Zhou, Dawei Pan, Yu Peng, Xiyuan Peng, Lithium-ion battery remaining useful life estimation with an optimized Relevance Vector Machine algorithm with incremental learning, Measurement, Volume 63, 2015, Pages 143-151, ISSN 0263-2241,
https://doi.org/10.1016/j.measurement.2014.11.031. (https://www.sciencedirect.com/science/article/pii/S0263224114005922)


Different GitHub codes links related to the Li-ion battery aging projects:
1) https://github.com/fmardero/battery_aging
2) https://github.com/JayRaval369/Li-ion-Battery-data
3) https://github.com/AmitKumarSoliyal/Lithium-ion-battery-Degradation-Analysis-using-LSTM
4) https://github.com/branden-ciranni/forecasting-battery-life
