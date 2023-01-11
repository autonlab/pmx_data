# production plant data for condition monitoring

Problem type: Time to failure prediction

Note: Data is hosted on kaggle, and requires setup before downloading (see comments in get_data.sh)

|  |
|  |
|  |
## Sources

Data location: https://www.kaggle.com/datasets/inIT-OWL/production-plant-data-for-condition-monitoring

No data citation available

No data license available.

## Additional information
# Production Plant Data for Condition Monitoring - DATASET DESCRIPTION

The dataset has been created in order to give the possibility to predict the condition of an important component within the production lines. This condition is essential for the function of the plant and the resulting product quality.

The dataset consist of 8 run-to-failure experiments (we can distinguish files: C8, C9, C7, C16, C15, C13, C14 and C11, whereas C7 and C13 are divided into 2 parts. The results in each of the files listed relate to a different experiment that consists of a running until failure process for the particular studied machine). In this data we are given previously properly selected features that are related to the component. The machine studied in all of the experiments is the same but not all the experiments have recorded the same signals.
Each of the files is divided into 2 types of the columns: the first one is the timestamp and the second is the sensor part. The second part consist of 25 signals (each file gives the signals records for a different component)

For the purpose of the conducted experiment, the following steps were taken with the data obtained:
* By using the leave-one-out method of selections (this method is a special case of cross-validation where the number of folds equals the number of instances in the data set), the training and prediction data were selected.
* Ultimately, it was decided to select data from the component under test for prediction.
* The training data for the "new" condition was created by selecting and combining a certain amount of data from all other components.
* Self-Organizing Map was trained on the learning data to present the "new" condition.
* Visualization and calculation of the degradation of the component under test was performed. 
* The same procedure was carried out for all experiments, in order to obtain degradation predictions for all tested components.

# SOURCES

The dataset has been dowloaded from the kaggle website and is available under the following link: 
https://www.kaggle.com/datasets/inIT-OWL/production-plant-data-for-condition-monitoring

Below you are also provided with the proper License and copyrights:

LICENSE: von Birgelen, Alexander; Buratti, Davide; Mager, Jens; Niggemann, Oliver: Self-Organizing Maps for Anomaly Localization and Predictive Maintenance in Cyber-Physical Production Systems. In: 51st CIRP Conference on Manufacturing Systems (CIRP CMS 2018) CIRP-CMS, May 2018.
CC BY-SA 3.0: https://creativecommons.org/licenses/by-sa/3.0/


On the same website you can also find some useful codes written for this dataset purposes:

https://www.kaggle.com/code/nabiwishes/unsupervised-learning-pattern-finding
https://www.kaggle.com/code/kerneler/starter-production-plant-data-for-a10cff31-e



Citation for the article contained in the Documentation folder in PDF format:
A. von Birgelen, D. Buratti, J. Mager, and O. Niggemann, “Self-organizing maps for anomaly localization and predictive maintenance in cyber-physical production systems,” Procedia CIRP, vol. 72, pp. 480–485, 2018, 51st CIRP Conference on Manufacturing Systems. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S221282711830307X


There is also an interesting article about the Condition Monitoring which can be found under the following link: https://ieeexplore.ieee.org/document/9609512
Citation for this article is also provided there: P. Samant, M. Bhushan, A. Kumar, R. Arya, S. Tiwari and S. Bansal, "Condition Monitoring of Machinery: A Case Study," 2021 6th International Conference on Signal Processing, Computing and Control (ISPCC), 2021, pp. 501-505, doi: 10.1109/ISPCC53510.2021.9609512.


Another citation for the article connected with the dataset subject: 
Alexander von Birgelen, Davide Buratti, Jens Mager, Oliver Niggemann, Self-Organizing Maps for Anomaly Localization and Predictive Maintenance in Cyber-Physical Production Systems, Procedia CIRP, Volume 72, 2018, Pages 480-485, ISSN 2212-8271, https://doi.org/10.1016/j.procir.2018.03.150.
(https://www.sciencedirect.com/science/article/pii/S221282711830307X)
