# ROBOT EXECUTION FAILURES - DATASET DESCRIPTION:

These datasets were collected, defined and evaluated in order to improve the classification accuracy.
The dataset folder consist of force and torque measurements on a robot after failure detection.


We are given with 5 different datasets, whereas each of them defines a different learning problem.

* LP1 --> failures in approach to grasp position
* LP2 --> failures in transfer of a part
* LP3 --> position of part after a transfer failure
* LP4 --> failures in approach to ungrasp position
* LP5 --> failures in motion with part

Each of the datasets consist of different number of instances:
For LP1 this is 88
For LP2 this is 47
For LP3 this is 47
For LP4 this is 117
For LP5 this is 164

There are 90 features in each of the 5 datasets. Each of these features represents a torque or a force measured after failure detection.
Each failure is characterized by 15 force/torque samples collected at regular intervals starting immediately after the failure is detected.
Każdy z przykładów w danej bazie danych definiowany jest w następujący sposób:

Column 1 is the name of the class which is (in brackets are given percentages of instances per class in each dataset): 
- For LP1: normal(24%), collision(19%), obstruction(39%), fr_collision(18%);
- For LP2: normal(43%), back_col(15%), front_col(13%), right_col(11%), left_col(19%);
- For LP3: ok(43%), moved(32%), slightly_moved(19%), lost(6%);
- For LP4: normal(21%), collision(62%), obstruction(18%);
- For LP5: normal(27%), collision_in_tool(16%), collision_in_part(29%), bottom_obstruction(13%), bottom_collision.

Columns from 2 to 7 represents the following features:
Fx1	Fy1	Fz1	Tx1	Ty1	Tz1
Fx2	Fy2	Fz2	Tx2	Ty2	Tz2
....
Fx15	Fy15	Fz15	Tx15	Ty15	Tz15

* Fx, Fy and Fz from 1 to 15 is the evolution of force Fx Fy and Fz respectively
* Tx, Ty and Tz from 1 to 15 is the evolution of the torques Tx, Ty and Tz respectively.


 
# Different sources and links to codes and articles:

The dataset was downloaded from the kaggle website, available under the following link: https://www.kaggle.com/datasets/prashant111/robot-execution-failures

License CC0: Public Domain (link available: https://creativecommons.org/publicdomain/zero/1.0/)

The dataset is also available to download from the UCI Repository (the citation policy is as follows: Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science).

Original Owner and Donor of this dataset:
Luis Seabra Lopes and Luis M. Camarinha-Matos 
Universidade Nova de Lisboa, 
Monte da Caparica, Portugal.

The dataset files format that are available in this repository was changed but the data in the original format (.data) together with some additional files about the data, converting files to a more standard format, description is available on the UCI repository website (link to the page is located above).


Links to codes:
On the kaggle website you can find 2 sample codes, available under the following titles (and links):
1. Robot Failure EDA (https://www.kaggle.com/code/stpeteishii/robot-failure-eda)
2. Robot Execution Failures fc8f9a5c-5 (https://www.kaggle.com/code/kerneler/starter-robot-execution-failures-fc8f9a5c-5)


Link to GitHub Codes:
1) https://github.com/WWW5911/Robot-Execution-Failures
2) https://github.com/cakoch10/Analysis-of-Robot-Execution-Failures
3) https://github.com/Etavia/Robot-Failure-NN


Publication and articles relevant to this subject:
* Seabra Lopes, L. (1997) "Robot Learning at the Task Level: a Study in the Assembly Domain", Ph.D. thesis, Universidade Nova de Lisboa, Portugal.

* Seabra Lopes, L. and L.M. Camarinha-Matos (1998) Feature Transformation Strategies for a Robot Learning Problem, "Feature Extraction, Construction and Selection. A Data Mining Perspective", H. Liu and H. Motoda (edrs.), Kluwer Academic Publishers.

* Camarinha-Matos, L.M., L. Seabra Lopes, and J. Barata (1996) Integration and Learning in Supervision of Flexible Assembly Systems, "IEEE Transactions on Robotics and Automation", 12 (2), 202-219.

* B. Twala, "Robot execution failure prediction using incomplete data," 2009 IEEE International Conference on Robotics and Biomimetics (ROBIO), 2009, pp. 1518-1523, doi: 10.1109/ROBIO.2009.5420900.

* Diryag A, Mitić M, Miljković Z. Neural networks for prediction of robot failures. Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science. 2014;228(8):1444-1458. doi:10.1177/0954406213507704
  
* Rahmani, M.E., Amine, A. & Fernandes, J.E. Multi-stage Genetic Algorithm and Deep Neural Network for Robot Execution Failure Detection. Neural Process Lett 53, 4527–4547 (2021). https://doi.org/10.1007/s11063-021-10610-x

* KOOHI, Tahereh; MIRZAIE, Elham; TADAION, Ghamarnaz. Failure prediction using robot execution data. In: Proceedings of the 5th Symposium on Advances in Science and Technology. 2011. p. 1-7.



