# Air pressure system failures in Scania trucks.

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

# SOURCES

License link: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html

These datasets have been downloaded from the UCI ML Repository. You can access online this data via the link below:
https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks

Citation: Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.


The data can also be downloaded from the kaggle website available under the following link:
https://www.kaggle.com/datasets/uciml/aps-failure-at-scania-trucks-data-set


Citation for this UCI dataset Policy is as follows:
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

Below you are provided with different link to the articles found so far regarding the dataset topic:

1) Sharath Solomon (2021) "Scania Trucks Air Pressure System Failure Prediction": 
https://medium.com/analytics-vidhya/scania-trucks-air-pressure-system-failure-prediction-ad6c43539d38

2) Rithwik Shetty (2021). Predicting a Failure in Scania’s Air Pressure System.
https://towardsdatascience.com/predicting-a-failure-in-scanias-air-pressure-system-aps-c260bcc4d038

3) K. T. Selvi, N. Praveena, K. Pratheksha, S. Ragunanthan and R. Thamilselvan, "Air Pressure System Failure Prediction and Classification in Scania Trucks using Machine Learning," 2022 Second International Conference on Artificial Intelligence and Smart Energy (ICAIS), 2022, pp. 220-227, doi: 10.1109/ICAIS53314.2022.9742716.
Also another link for this article: https://ieeexplore.ieee.org/document/9742716

4) Ashish Dutt (2020). Predicting the misclassification cost incurred in air pressure system failure in heavy vehicles
https://duttashi.github.io/blog/air-pressure-heavy-vehicle/

5) Citation to the PDF article attached to the Documentation folder in this dataset:
Gondek, Christopher & Hafner, Daniel & Sampson, Oliver. (2016). Prediction of Failures in the Air Pressure System of Scania Trucks Using a Random Forest and Feature Engineering. 10.1007/978-3-319-46349-0_36. 
Link to the article website: https://www.researchgate.net/publication/309195602_Prediction_of_Failures_in_the_Air_Pressure_System_of_Scania_Trucks_Using_a_Random_Forest_and_Feature_Engineering


Link to the GitHub code: https://github.com/sharathsolomon/scaniaAPSstudy

Link to the project titled: "Air Pressure Failure of Scania Trucks":
https://notebooks.githubusercontent.com/view/ipynb?browser=chrome&color_mode=auto&commit=535639c3ea968b89b95eef35483137121eda3375&device=unknown&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f5063323330312f5363616e69612d547275636b732d4150532d4661696c7572652d50726564696374696f6e2f353335363339633365613936386238396239356565663335343833313337313231656461333337352f4150532532305363616e6961253230547275636b732e6970796e62&logged_in=false&nwo=Pc2301%2FScania-Trucks-APS-Failure-Prediction&path=APS+Scania+Trucks.ipynb&platform=android&repository_id=190972147&repository_type=Repository&version=99
