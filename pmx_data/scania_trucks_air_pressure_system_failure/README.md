# Dataset Description

Problem type: Tabular Failure Classification

| Size (GB) | Features | Rows  | Contains missing data? | Target Column | Notes |
| --------- | -------- | ----- | ---------------------- | ------------- | ----- |
| 0.054     | 171      | 76000 | True                   | class         |       |

## Performance Benchmarks

| Benchmark | Metric  | Source  |
| --------- | ------- | ------- |
| 0.989     | ROC AUC | AutonML |

---

This data concerns the APS (Air Pressure System) for Scania Trucks. The APS system generates pressurized air which is utilized in various functions in a truck, such as braking and gear changes.

Each row represents a truck failure.  The target variable is binary.
* The positive class consists of trucks with failures of a component of the Air Pressure System.
* The negative class consists of trucks with failures not related to APS.

The data consist of a training set and a testing set.  The training set contains 60000 examples in which 59000 belong to the negative class and 1000 to the positive class.  The test set contains 16000 examples.

The exact names of the attributes have been anonymized for proprietary reasons.  There are 171 different attributes; some are single numerical
counters, while some sets of attributes that represent histograms consisting of bins with different conditions.  For example if we were measuring
the ambient temperature 'T' then the histogram could be defined with 4 bins where:

bin 1 collects values for temperature T < -20
bin 2 collects values for temperature T >= -20 and T < 0
bin 3 collects values for temperature T >= 0 and T < 20
bin 4 collects values for temperature T > 20 

Each bin would be a different attribute in the data.  Attribute names contain both an identifier and a bin ID, of the form "Identifier_Bin"


# Sources

If you use this dataset for your research please cite it with:

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

Data License: [GPL 2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

Papers that use this dataset:

@inproceedings{Selvi_2022, doi = {10.1109/icais53314.2022.9742716}, url = {https://doi.org/10.1109%2Ficais53314.2022.9742716}, year = 2022, month = {feb}, publisher = {{IEEE}}, author = {K Tamil Selvi and N Praveena and K Pratheksha and S Ragunanthan and R Thamilselvan}, title = {Air Pressure System Failure Prediction and Classification in Scania Trucks using Machine Learning}, booktitle = {2022 Second International Conference on Artificial Intelligence and Smart Energy ({ICAIS})} }

@incollection{Gondek_2016, doi = {10.1007/978-3-319-46349-0_36}, url = {https://doi.org/10.1007%2F978-3-319-46349-0_36}, year = 2016, publisher = {Springer International Publishing}, pages = {398--402}, author = {Christopher Gondek and Daniel Hafner and Oliver R. Sampson}, title = {Prediction of Failures in the Air Pressure System of Scania Trucks Using a Random Forest and Feature Engineering}, booktitle = {Lecture Notes in Computer Science} }