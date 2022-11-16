The main purpose of this dataset is for fault diagnosis of Diesel engines, through the analysis of the variation of the pressure curves inside the cylinders and the torsional vibration response of the crankshaft.

A fault simulation model based on a thermodynamic model was developed, from which certain feature vectors were selected, which were first obtained from processing signals such as pressure and temperature inside the cylinder and torsional vibration of the engine flywheel. These vectors were then used as input data for machine learning which aimed to discriminate several operating states of the machine:
- normal (without faults) --> 250 scenarios;
- lowering of intake manifold pressure --> 250 scenarios;
- compression ratio in the cylinders --> 1500 scenarios;
- Reduction of the amount of fuel injected into the cylinders --> 1500 scenarios.

In total, the entire database counts 3,500 different failure scenarios for the 4 operating states described above.  Due to the lowest common error in the estimation of average and maximum combustion cycle pressures, between the experimental and simulated data, the engine speed frequency was set to 2500 RPM for all scenarios during the validation stage of the thermodynamic and dynamic models.