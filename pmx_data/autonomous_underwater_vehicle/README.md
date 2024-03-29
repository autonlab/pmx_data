# Autonomous Underwater Vehicle

Problem type: Time Series Diagnostics / Fault Classification

Note: rar data compression - requires additional setup to download (see comments in get_data.sh)

| Size (GB) | Features | Rows | Contains missing data? | Number of classes | Are all time series the same length? | Avg. time series length |
| --------- | -------- | ---- | ---------------------- | ----------------- | ------------------------------------ | ----------------------- |
| 0.025     | 17       | 1225 | False                  | 5                 | False                                | 200                     |

## Performance Benchmarks

| Benchmark | Metric   | Source                                                                                                                                                        | Algorithm Used                                 |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| 97.96     | Accuracy | [Model-free fault diagnosis for autonomous underwater vehicles using sequence Convolutional Neural Network](https://doi.org/10.1016%2Fj.oceaneng.2021.108874) | Sequence Convolutional Neural Network (SeqCNN) |
## Sources

Data location: https://data.mendeley.com/datasets/7rp2pmr6mx/1

If you use this dataset for your research please cite it with:

- @misc{https://doi.org/10.17632/7rp2pmr6mx.1, doi = {10.17632/7RP2PMR6MX.1}, url = {https://data.mendeley.com/datasets/7rp2pmr6mx/1}, author = {Ji, Daxiong}, keywords = {System Fault Diagnosis, AUV Control}, title = {Autonomous Underwater Vehicle Fault Diagnosis Dataset}, publisher = {Mendeley}, year = {2021} }

Data License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Papers that use this dataset:

- @article{Ji_2021, doi = {10.1016/j.oceaneng.2021.109651}, url = {https://doi.org/10.1016%2Fj.oceaneng.2021.109651}, year = 2021, month = {oct}, publisher = {Elsevier {BV}}, volume = {237}, pages = {109651}, author = {Daxiong Ji and Rui Wang and Yangyang Zhai and Haitao Gu}, title = {Dynamic modeling of quadrotor {AUV} using a novel {CFD} simulation}, journal = {Ocean Engineering} }
- @article{Ji_2021, doi = {10.1016/j.oceaneng.2021.108874}, url = {https://doi.org/10.1016%2Fj.oceaneng.2021.108874}, year = 2021, month = {jul}, publisher = {Elsevier {BV}}, volume = {232}, pages = {108874}, author = {Daxiong Ji and Xin Yao and Shuo Li and Yuangui Tang and Yu Tian}, title = {Model-free fault diagnosis for autonomous underwater vehicles using sequence Convolutional Neural Network}, journal = {Ocean Engineering} }
- @article{Ji_2021, doi = {10.1016/j.dib.2021.107477}, url = {https://doi.org/10.1016%2Fj.dib.2021.107477}, year = 2021, month = {dec}, publisher = {Elsevier {BV}}, volume = {39}, pages = {107477}, author = {Daxiong Ji and Xin Yao and Shuo Li and Yuangui Tang and Yu Tian}, title = {Autonomous underwater vehicle fault diagnosis dataset}, journal = {Data in Brief} }

## Additional information
The dataset comes from the Haizhe which is a small autonomous underwater quadrotor vehicle. This machine consists of 4 brushless motors, 4 propellers, 4 electronic speed control, 1 depth sensor, 1 nine-axis inertial measurement unit and 1 microcontroller unit.

The dataset is divided into 2 folders, test and train. Each of these folders contains 5 subfolders corresponding to the 5 fault types:
- Normal - no fault
- AddWeight - load increase
- PressureGain constant - failure of the depth sensor
- PropellerDamage slight - slight damage to the propeller
- PropellerDamage bad - severe damage to the propeller

Each of the fault type subfolders described above contains state data recordings of the machine over a certain period of time. The name of the subfolder represents the true label of the sample.

There are also summary csv's, called test.csv and train.csv, that map each time series csv file to a target label.

Each csv has 17 different columns:
1. time: The absolute time for ‘Haizhe’ to record data.
2. pwm1: Duration (in microseconds) of high level in 100 Hz PWM wave. It is the signal used to control Motor 1.
3. pwm2: Duration (in microseconds) of high level in 100 Hz PWM wave. It is the signal used to control Motor 2.
4. pwm3: Duration (in microseconds) of high level in 100 Hz PWM wave. It is the signal used to control Motor 3.
5. pwm4: Duration (in microseconds) of high level in 100Hz PWM wave. It is the signal used to control Motor 4.
6. depth: The depth value (in meters) measured by depth sensor.
7. press: The pressure value (in Pa) measured by depth sensor.
8. voltage: The voltage value (in V) of battery.
9. roll: The roll angles (in degrees) measured by nine-axis IMU.
10. pitch: The pitch angles (in degrees) measured by nine-axis IMU.
11. yaw: The yaw angles (in degrees) measured by nine-axis IMU.
12. a_x: The acceleration (in m/s2) along the x-axis in the body coordinate frame, measured by nine-axis IMU.
13. a_y: The acceleration (in m/s2) along the y-axis in the body coordinate frame, measured by nine-axis IMU.
14. a_z: The acceleration (in m/s2) along the z-axis in the body coordinate frame, measured by nine-axis IMU.
15. w_row: The angular velocity (in degrees/s) of rotation around the x-axis in the body coordinate frame, measured by nine-axis IMU.
16. w_pitch: The angular velocity (in degrees/s) of rotation around the y-axis in the body coordinate frame, measured by nine-axis IMU.
17. w_yaw: The angular velocity (in degrees/s) of rotation around the z-axis in the body coordinate frame, measured by nine-axis IMU.