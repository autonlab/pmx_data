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