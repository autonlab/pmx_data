
# DIESEL ENGINE FAULTS - DATASET DESCRIPTION:

The main purpose for this dataset is the fault diagnosis in Diesel engines in order to assist the predictive maintenance, through the analysis of the variation of the pressure curves inside the cylinders and the torsional vibration response of the crankshaft.

A fault simulation model based on a thermodynamic model was developed, from which certain feature vectors were selected, which were first obtained from processing signals such as pressure and temperature inside the cylinder and torsional vibration of the engine flywheel. These vectors were then used as a form of input data for machine learning which aimed to discriminate several operating states of the machine:
- normal (without faults) --> 250 scenarios;
- lowering of intake manifold pressure --> 250 scenarios;
- compression ratio in the cylinders --> 1500 scenarios;
- Reduction of the amount of fuel injected into the cylinders --> 1500 scenarios.

In total, the entire database counts 3,500 different failure scenarios for the 4 operating states described above.
Due to the lowest common error in the estimation of average and maximum combustion cycle pressures, between the experimental and simulated data, the engine speed frequency was set to 2500 RPM for all scenarios during the validation stage of the thermodynamic and dynamic models.


# SOURCES 

Citation to the original source of the dataset:
Pestana, Denys (2020), “Diesel Engine Faults Features Dataset (3500-DEFault)”, Mendeley Data, V1, doi: 10.17632/k22zxz29kr.1
It is also available to download from the following link: https://data.mendeley.com/datasets/k22zxz29kr/1

Below you may find some links, citations and references to different articles related to the dataset subject:

1) Pestana-Viana, D. et al. (2019). Application of Machine Learning in Diesel Engines Fault Identification. In: Cavalca, K., Weber, H. (eds) Proceedings of the 10th International Conference on Rotor Dynamics – IFToMM . IFToMM 2018. Mechanisms and Machine Science, vol 61. Springer, Cham. https://doi.org/10.1007/978-3-319-99268-6_6

2) Citation to the article provided in a documentation folder: Bai, Huajun, Xianbiao Zhan, Hao Yan, Liang Wen, Yunbin Yan, and Xisheng Jia. 2022. "Research on Diesel Engine Fault Diagnosis Method Based on Stacked Sparse Autoencoder and Support Vector Machine" Electronics 11, no. 14: 2249. https://doi.org/10.3390/electronics11142249

3) Citation provided to the Interesting article (added to the Documentation folder) about Diesel Engine Health Prognostic that might also be helpful for this dataset analysis purposes: NIXON, Steve, et al. A machine learning approach to diesel engine health prognostics using engine controller data. In: 10th Annual Conference of the Prognostics and Health Management Society, PHM 2018. Prognostics and Health Management Society, 2018.