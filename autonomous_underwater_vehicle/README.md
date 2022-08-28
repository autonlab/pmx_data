# AUTONOMOUS UNDERWATER VEHICLE FAULT DIAGNOSIS - DATASET DESCRIPTION

The dataset related to the subject consists of 1225 data samples for 5 fault types (labels).
The dataset comes from the Haizhe which is a small autonomous underwater quadrotor vehicle. This machine consists of 4 brushless motors, 4 propellers, 4 electronic speed control, 1 depth sensor, 1 nine-axis inertial measurement unit and 1 microcontroller unit.
The dataset taken is further divided into 2 subfolders" test data and train data. Each of these subfolders contains 5 "fault type" subfolders with .csv files:
- AddWeight - corresponds to load increase
- Normal - corresponds to normal state
- PressureGain constant - corresponds to failure of the depth sensor
- PropellerDamage bad - corresponds to severe damage to the propeller
- PropellerDamage slight - corresponds to slight damage to the propeller.
Each of the fault type subfolders described above, contains state data recordings of the machine over a certain period of time. The name of fault type subfolder represents the true label of the sample.
We can distinguish 17 different columns:
1. time: The absolute time for ‘Haizhe’ to record data.
2. pwm1: Duration (in microseconds) of high level in 100 Hz PWM wave. It is the control signal used to control the Motor 1.
3. pwm2: Duration (in microseconds) of high level in 100 Hz PWM wave. It is the control signal used to control the Motor 2.
4. pwm3: Duration (in microseconds) of high level in 100 Hz PWM wave. It is the control signal used to control the Motor 3.
5. pwm4: Duration (in microseconds) of high level in 100Hz PWM wave. It is the control signal used to control the Motor 4.
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

Dataset can be used to validate a model-free fault diagnosis method (the method is proposed in the paper titled Model-free fault diagnosis for autonomous underwater vehicles using sequence convolutional neural network. The citation is contained in the sources file in Documentation folder).

# Sources for the given dataset:

The dataset originally comes from the Mendeley Data website and is available via the following link: https://data.mendeley.com/datasets/7rp2pmr6mx/1

Citation and references to the papers that uses this data and which can be very useful for the additional sources about the data and projects performed using this dataset:
1. Ji D., Wang R., Zhai Y., Gu H. Dynamic modeling of quadrotor AUV using a novel CFD simulation. Ocean Eng. 2021;237:109651. doi: 10.1016/j.oceaneng.2021.109651.
2. Ji D., Yao X., Li S., Tang Y., Tian Y. Model-free fault diagnosis for autonomous underwater vehicles using sequence convolutional neural network. Ocean Eng. 2021;232:108874. doi: 10.1016/j.oceaneng.2021.108874.
3. Ji D, Yao X, Li S, Tang Y, Tian Y. Autonomous underwater vehicle fault diagnosis dataset. Data Brief. 2021 Oct 14;39:107477. doi: 10.1016/j.dib.2021.107477. PMID: 34712754; PMCID: PMC8529076.

