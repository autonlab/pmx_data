The delta robot is a part of a smart factory and performs pick and place of barrels and springs in a customized pen production line.
Parameters contained in the dataset are obtained from the feed forward controller and are movement dependent.
The dataset can be used to detect anomalies in the system.
The dataset folder consist of 2 subfolders which contain files saved in .csv format.

The file titled BarrelMovement contains parameter readings from the barrel pick and place movement.
The second subfolder that contains files titled SpringMovement_Converged and SpringMovement_withTransientData. These files contain parameter readings for spring pick and place movement; the second file (TransientData) also includes data points which have not converged to the final steady state values (the parameters are still being updated given the calculated error in the control loop), whereas the Converged file is similar to BarrelMovement and as the name implies, this file contains the converged parameter values for a specific movement.

The datasets contain the following parameter sensor readings, received from a delta robot:
p0 : Motor inertia \
p1 : Gravity \
p2 : Mass \
p3 : Spring offset \
p4 : Coulomb friction 0 \
p5 : Coulomb friction 1 \
p6 : Coulomb friction 2 \
p7 : Spring constant \
p8 : Viscose friction 0 \
p9 : Viscose friction 1 \
p10 : Viscose friction 2 \

Below is the learning rate for all of the parameters:
lambda0 = 0.0005 \
lambda1 = 0.08 \
lambda2 = 0.09 \
lambda3 = 0.07 \
lambda4 = 0.1 \
lambda5 = 0.1 \
lambda6 = 0.1 \
lambda7 = 0.2 \
lambda8 = 0.01 \
lambda9 = 0.01 \
lambda10 = 0.01 \


Hint added by the authors:
It is best to normalize the data so that the patterns in the parameter readings can be acquired for different models. The authors have used scikit learn library for pre-processing the data.