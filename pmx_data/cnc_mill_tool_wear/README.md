# Dataset Description

Problem type: Time Series Fault Detection

| Size (GB) | Features | Rows | Contains missing data? | Are all time series the same length? | Avg. time series length |
| --------- | -------- | ---- | ---------------------- | ------------------------------------ | ----------------------- |
| 0.011     | 47       | 18   | False                  | False                                | 1500                    |
# Sources

Data location: https://www.kaggle.com/datasets/shasun/tool-wear-detection-in-cnc-mill

No data citation available

Data License: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

Papers that use this dataset:

@article{Ghosh_2007, doi = {10.1016/j.ymssp.2005.10.010}, url = {https://doi.org/10.1016%2Fj.ymssp.2005.10.010}, year = 2007, month = {jan}, publisher = {Elsevier {BV}}, volume = {21}, number = {1}, pages = {466--479}, author = {N. Ghosh and Y.B. Ravi and A. Patra and S. Mukhopadhyay and S. Paul and A.R. Mohanty and A.B. Chattopadhyay}, title = {Estimation of tool wear during {CNC} milling using neural network-based sensor fusion}, journal = {Mechanical Systems and Signal Processing} }

@article{Jaen_Cuellar_2021, doi = {10.3390/s21248431}, url = {https://doi.org/10.3390%2Fs21248431}, year = 2021, month = {dec}, publisher = {{MDPI} {AG}}, volume = {21}, number = {24}, pages = {8431}, author = {Arturo Yosimar Jaen-Cuellar and Roque Alfredo Osornio-R{\'{\i}}os and Miguel Trejo-Hern{\'{a}}ndez and Israel Zamudio-Ram{\'{\i}}rez and Geovanni D{\'{\i}}az-Salda{\~{n}}a and Jos{\'{e}} Pablo Pacheco-Guerrero and Jose Alfonso Antonino-Daviu}, title = {System for Tool-Wear Condition Monitoring in {CNC} Machines under Variations of Cutting Parameter Based on Fusion Stray Flux-Current Processing}, journal = {Sensors} }

---
The database consists of a series of files, wherein, each of these files contains sensor data taken in the course of conducting a single experiment.
A series of these machining experiments were conducted using wax blocks(2" x 2" x 1.5") with a CNC milling machine located in the System-level Manufacturing and Automation Research Testbed (SMART) at the University of Michigan.
Data from the machine was collected taking into account the changes taking place regarding tool condition, feed speed and clamping pressure.
Each experiment ended with the creation of a finished wax part, the top surface of which had the letter "S" engraved on it.

You can use this dataset for the experiment in the fields such as:
- Tool wear detection: you can use here supervised binary classification in order to perform the identification process of worn and unworn cutting tools.  Out of 18 experiments, 8 were conducted with an unworn tool, whereas 10 were run with a worn tool.
- Detection of inadequate clamping: in this case, the data would be used in order to detect the condition when a workpiece is not being held in the vise with sufficient pressure to pass visual inspection. The experiments were run with the pressures values of 2.5, 3 and 4 bar. Moreover this data could also be used for a detection of the conditions at which a critical point occurs which further prevents the machining operation from completing.


In the dataset we can distinguish 18 files with the experiments data recordings and one train file where you can find a general data from each of the 1 different experiments. A sampling rate of the collected data was 100ms.
In this train file there are 7 different columns:

The inputs (features):
* No - experiment number 
* material - the material on which the experiment has been conducted - in this case this is wax.
* feed rate - the relative velocity of the cutting tool along the workpiece (mm/s)
* clamp_pressure - the pressure used to hold the workpiece in the vise (bars)
Each of the measurements from the experiments (files experiment_1 to experiment_18) were taken from 4 motors in the CNC (X, Y, Z axes and spindle). 
These measurements might be used in 2 ways:
1) as if every CNC measurement is an independent observation where the operation being performed is given in the column titled the Machining_Process. Active machining operations are labeled as "Layer 1 Up", "Layer 1 Down", "Layer 2 Up", "Layer 2 Down", "Layer 3 Up", and "Layer 3 Down". 
2) as if each of the 1 experiments is taken as an observation for time series classification.

The outputs (predictions):
* tool_condition - provides an information about label for unworn and worn tools.
* machining_finalized - that column informs whether the machining was completed without the workpiece moving out of the pneumatic vise or not.
* passed_visual_inspection - this column indicates if the workpiece passed visual inspection. This is only available when the machining process in the experiment was completed.


Features available in the machining datasets are as follow:

For X axis:
* X1_ActualPosition: actual x position of part (mm)
* X1_ActualVelocity: actual x velocity of part (mm/s)
* X1_ActualAcceleration: actual x acceleration of part (mm/s/s)
* X1_CommandPosition: reference x position of part (mm)
* X1_CommandVelocity: reference x velocity of part (mm/s)
* X1_CommandAcceleration: reference x acceleration of part (mm/s/s)
* X1_CurrentFeedback: current (A)
* X1_DCBusVoltage: voltage (V)
* X1_OutputCurrent: current (A)
* X1_OutputVoltage: voltage (V)
* X1_OutputPower: power (kW)

For Y axis:
* Y1_ActualPosition: actual y position of part (mm)
* Y1_ActualVelocity: actual y velocity of part (mm/s)
* Y1_ActualAcceleration: actual y acceleration of part (mm/s/s)
* Y1_CommandPosition: reference y position of part (mm)
* Y1_CommandVelocity: reference y velocity of part (mm/s)
* Y1_CommandAcceleration: reference y acceleration of part (mm/s/s)
* Y1_CurrentFeedback: current (A)
* Y1_DCBusVoltage: voltage (V)
* Y1_OutputCurrent: current (A)
* Y1_OutputVoltage: voltage (V)
* Y1_OutputPower: power (kW)

For Z axis:
* Z1_ActualPosition: actual z position of part (mm)
* Z1_ActualVelocity: actual z velocity of part (mm/s)
* Z1_ActualAcceleration: actual z acceleration of part (mm/s/s)
* Z1_CommandPosition: reference z position of part (mm)
* Z1_CommandVelocity: reference z velocity of part (mm/s)
* Z1_CommandAcceleration: reference z acceleration of part (mm/s/s)
* Z1_CurrentFeedback: current (A)
* Z1_DCBusVoltage: voltage (V)
* Z1_OutputCurrent: current (A)
* Z1_OutputVoltage: voltage (V)

For Spindle:
* S1_ActualPosition: actual position of spindle (mm)
* S1_ActualVelocity: actual velocity of spindle (mm/s)
* S1_ActualAcceleration: actual acceleration of spindle (mm/s/s)
* S1_CommandPosition: reference position of spindle (mm)
* S1_CommandVelocity: reference velocity of spindle (mm/s)
* S1_CommandAcceleration: reference acceleration of spindle (mm/s/s)
* S1_CurrentFeedback: current (A)
* S1_DCBusVoltage: voltage (V)
* S1_OutputCurrent: current (A)
* S1_OutputVoltage: voltage (V)
* S1_OutputPower: current (A)
* S1_SystemInertia: torque inertia (kg*m^2)

For the Machine:
* M1_CURRENT_PROGRAM_NUMBER: number the program is listed under on the CNC
* M1_sequence_number: line of G-code being executed
* M1_CURRENT_FEEDRATE: instantaneous feed rate of spindle

The last column in the experiment files is titles as Machining_Process - this column provides an information about the current machining stage being performed. There is included the information about the preparation, tracing up and down the Spindle (S) curve and involves different lanes and also repositions  of the spindle as it moves through the air to a certain starting point.

Additional resources:
"https://www.kaggle.com/code/koheimuramatsu/cnc-milling-machine-tool-wear-detection/notebook"
"https://github.com/SaeedShurrab/Tool-Wear-Detection-in-CNC-Milling-Operartions"
"https://github.com/flyinginte/toolwear_cncmilling"