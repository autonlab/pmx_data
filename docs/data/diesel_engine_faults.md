# Diesel Engine Faults

Problem type: Diagnostics / Fault Classification

Note: data is in .mat format.

| Size (GB) |
| --------- |
| 0.0061    |

## Performance Benchmarks

| Benchmark | Metric   | Source                                                                                                                                                          | Algorithm Used                                        |
| --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 99.3      | Accuracy | [Application of Machine Learning in Diesel Engines Fault Identification](https://doi.org/10.1007/978-3-319-99268-6_6)                                           | Random Forest                                         |
| 100.0     | Accuracy | [Research on Diesel Engine Fault Diagnosis Method Based on Stacked Sparse Autoencoder and Support Vector Machine ](https://doi.org/10.3390/electronics11142249) | Stacked Sparse Autoencoder and Support Vector Machine |
## Sources

Data location: https://data.mendeley.com/datasets/k22zxz29kr/1

If you use this dataset for your research please cite it with:

- @misc{https://doi.org/10.17632/k22zxz29kr.1, doi = {10.17632/K22ZXZ29KR.1}, url = {https://data.mendeley.com/datasets/k22zxz29kr/1}, author = {Pestana, Denys}, keywords = {Artificial Intelligence, Signal Processing, Mechanics}, title = {Diesel Engine Faults Features Dataset (3500-DEFault)}, publisher = {Mendeley}, year = {2020} }

Data License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Papers that use this dataset:

- @incollection{Pestana_Viana_2018, doi = {10.1007/978-3-319-99268-6_6}, url = {https://doi.org/10.1007%2F978-3-319-99268-6_6}, year = 2018, month = {aug}, publisher = {Springer International Publishing}, pages = {74--89}, author = {Denys Pestana-Viana and Ricardo H. R. Guti{\'{e}}rrez and Amaro A. de Lima and Fabr{\'{\i}}cio L. e Silva and Luiz Vaz and Thiago de M. Prego and Ulisses A. Monteiro}, title = {Application of Machine Learning in~Diesel Engines Fault Identification}, booktitle = {Mechanisms and Machine Science} }
- @article{Bai_2022, doi = {10.3390/electronics11142249}, url = {https://doi.org/10.3390%2Felectronics11142249}, year = 2022, month = {jul}, publisher = {{MDPI} {AG}}, volume = {11}, number = {14}, pages = {2249}, author = {Huajun Bai and Xianbiao Zhan and Hao Yan and Liang Wen and Yunbin Yan and Xisheng Jia}, title = {Research on Diesel Engine Fault Diagnosis Method Based on Stacked Sparse Autoencoder and Support Vector Machine}, journal = {Electronics} }
- NIXON, Steve, et al. A machine learning approach to diesel engine health prognostics using engine controller data. In: 10th Annual Conference of the Prognostics and Health Management Society, PHM 2018. Prognostics and Health Management Society, 2018.

## Additional information
The main purpose of this dataset is for fault diagnosis of Diesel engines, through the analysis of the variation of the pressure curves inside the cylinders and the torsional vibration response of the crankshaft.

A fault simulation model based on a thermodynamic model was developed, from which certain feature vectors were selected, which were first obtained from processing signals such as pressure and temperature inside the cylinder and torsional vibration of the engine flywheel. These vectors were then used as input data for machine learning which aimed to discriminate several operating states of the machine:
- normal (without faults) --> 250 scenarios;
- lowering of intake manifold pressure --> 250 scenarios;
- compression ratio in the cylinders --> 1500 scenarios;
- Reduction of the amount of fuel injected into the cylinders --> 1500 scenarios.

In total, the entire database counts 3,500 different failure scenarios for the 4 operating states described above.  Due to the lowest common error in the estimation of average and maximum combustion cycle pressures, between the experimental and simulated data, the engine speed frequency was set to 2500 RPM for all scenarios during the validation stage of the thermodynamic and dynamic models.