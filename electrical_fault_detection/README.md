

This dataset is a collection of line currents and voltages for different fault conditions.

As the electrical powers system is getting in size, then also its complexity in such sectors as generetation, transmission, distribution and load systems changes. Because of the faults that might occur, there can be detected some severe economic losses together with reduction of the reliability of the electrical system. One of the most crucial parts in the power system is the transmission line, which role is to transmit electric power from the source area to the distribution network. The faults on electrical power system transmission lines are supposed to be first detected and classified correctly and should be cleared in the least possible time.

The power system which was modeled for this simulate fault analysis consist of 4 generators. Then there is simulated the circuit under normal conditions as well as under various fault conditions. After it, the sensors values are collected and the measured Line Voltages and Line Currents at the output side of the power system is saved.

In the dataset folder we are provided with 2 datasets. The first one, called classData, contains the data which further would be used to classify the types of fault. We are given here with Inputs and outputs data. The inputs data consist of such columns with sensor recordings as: Ia,Ib,Ic (Each of these sensors present line current for the particular phase: A, B or C) and Va,Vb,Vc (Each of these sensors present line voltage for the particular phase: A, B or C The Outputs data consist of the following columns which represent part of the fault line: G, C, B, A. Fot this output data we can receive 1 if failure occurred, else 0 occurs. Example of reading this data: For the Outputs [G C B A] if we have: [0 0 0 0] - means that there is no fault [1 0 0 1] - means that there is LG (Line to Ground) fault (between phase A and Ground) [0 0 1 1] - means that there is LL (Line to Line) fault (between phases A and B) [1 0 1 1] - means that there is LLG (Line to Line to Ground) fault (between phases A, G and Ground) [0 1 1 1] - means that there is LLL (Line to Line to Line) fault (between all 3 phases) [1 1 1 1] - means that there is LLLG (Line to Line to Line to Ground) fault (3 phases symmetrical fault)

Second dataset called detect_dataset is the file that contains the data to give the possibility to detect faults in a power system. We are given here with the same inputs as in the classData which is [Ia,Ib,Ic,Va,Vb,Vc] and also we have here the outputs which gives us information about the failure occurence: the 0 value is shown when there is no fault and 1 when the fault occurred.

# SOURCES

Here you can find some useful links to original sources with the dataset and codes used for this project analysis purpose.

Originally the dataset was downloaded from the kaggle website and there is also located some codes that you may find useful while using this dataset. You can access this website under the following link: https://www.kaggle.com/datasets/esathyaprakash/electrical-fault-detection-and-classification

Another kaggle link: https://www.kaggle.com/code/elakapoor/predictive-electrical-fault-analysis/notebook

Also there is an article about the fault detection which is available here: https://www.sciencedirect.com/science/article/pii/S0263224121008824 Citation for the this article: Rahman Dashti, Mohammad Daisy, Hamid Mirshekali, Hamid Reza Shaker, and Mahmood Hosseini Aliabadi. A survey of fault prediction and location methods in electrical energy distribution networks. Measurement, 184:109947, 2021.

Here is also another interesting article which was written in order to bring awareness awareness to the developing of fault detection systems using the data collected from sensor devices/physical devices of various systems for predictive maintenance. The article is available under the following link: https://doi.org/10.1108/JQME-10-2020-0107 Citation: Divya, D., Marath, B. and Santosh Kumar, M.B. (2022), "Review of fault detection techniques for predictive maintenance", Journal of Quality in Maintenance Engineering, Vol. ahead-of-print No. ahead-of-print.
