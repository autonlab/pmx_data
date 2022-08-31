# AUTONOMOUS UNDERWATER VEHICLE FAULT DIAGNOSIS - DATASET DESCRIPTION

The dataset consists of 1225 data samples for 5 fault types (labels).
The dataset comes from the Haizhe which is a small autonomous underwater quadrotor vehicle. This machine consists of 4 brushless motors, 4 propellers, 4 electronic speed control, 1 depth sensor, 1 nine-axis inertial measurement unit and 1 microcontroller unit.

The dataset is divided into 2 folders, test data and train data. Each of these subfolders contains 5 sunfolders with .csv files corresponding to the 5 fault types:
- AddWeight that corresponds to load increase (what is a fault type)
- Normal - means the normal state
- PressureGain constant - contains data that corresponds to failure of the depth sensor
- PropellerDamage bad - that subfolder contains that that corresponds to severe damage to the propeller
- PropellerDamage slight - which corresponds to slight damage to the propeller.

Each of the fault type subfolders described above, contains state data recordings of the machine over a certain period of time. The name of fault type subfolder represents the true label of the sample.

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

The dataset can be used to validate a model-free fault diagnosis method.  The method is proposed in the paper cited below, titled "Model-free fault diagnosis for autonomous underwater vehicles using sequence convolutional neural network".

# SOURCES:

The dataset originally comes from the Mendeley Data website and is available via the following link: https://data.mendeley.com/datasets/7rp2pmr6mx/1

If you use this dataset for your research please cite it with:

~~~
% The entry below contains non-ASCII chars that could not be converted
% to a LaTeX equivalent.
@MISC{Ji2021-qt,
  title     = "Autonomous underwater vehicle fault diagnosis dataset",
  author    = "Ji, Daxiong",
  abstract  = "The dataset contains 1225 data samples for 5
               \textbackslashtextit\{fault types\} (labels). We divided the
               dataset into the training set and the test set through random
               stratified sampling. The test set accounted for $20\%$ of the
               total dataset. Our experimental subject is `Haizhe', which is a
               small quadrotor AUV developed in the laboratory. For each
               \textbackslashtextit\{fault type\}, `Haizhe' was tested several
               times. For each time, `Haizhe' ran the same program and sailed
               underwater for 10-20 seconds to ensure that
               \textbackslashtextit\{state data\} was long enough. The
               \textbackslashtextit\{state data\} recorded in each test were
               then used as a data sample, and the corresponding
               \textbackslashtextit\{fault type\} was the true label of the
               data sample. The dataset was used to validate a model-free fault
               diagnosis method proposed in our paper published in Ocean
               Engineering（Model-free fault diagnosis for autonomous underwater
               vehicles using sequence convolutional neural network, Ocean
               Engineering. 232(2021)108874.
               https://doi.org/10.1016/j.oceaneng.2021.108874）.",
  publisher = "Mendeley",
  year      =  2021
}
~~~

Citation and references to the papers that uses this data and which can be very useful for the additional sources about the data and projects performed using this dataset:
1. Ji D., Wang R., Zhai Y., Gu H. Dynamic modeling of quadrotor AUV using a novel CFD simulation. Ocean Eng. 2021;237:109651. doi: 10.1016/j.oceaneng.2021.109651.
2. Ji D., Yao X., Li S., Tang Y., Tian Y. Model-free fault diagnosis for autonomous underwater vehicles using sequence convolutional neural network. Ocean Eng. 2021;232:108874. doi: 10.1016/j.oceaneng.2021.108874.
3. Ji D, Yao X, Li S, Tang Y, Tian Y. Autonomous underwater vehicle fault diagnosis dataset. Data Brief. 2021 Oct 14;39:107477. doi: 10.1016/j.dib.2021.107477. PMID: 34712754; PMCID: PMC8529076.