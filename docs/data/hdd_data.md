# hdd data

Problem type: Time to failure prediction

|  |
|  |
|  |
## Sources

Data location: https://www.backblaze.com/b2/hard-drive-test-data.html

No data citation available

No data license available.

## Additional information


The whole BackBlaze dataset is available to download from BackBlaze.com website, available under the following link: https://www.backblaze.com/b2/hard-drive-test-data.html

I will be adding systematically new datasets to the repository.

For providing the example dataset taken from the BackBlaze website, the Prediction HDD Failure folder is given with the dataset that comes from 2013 and contains the following columns:

* Date - This is the information about the date when the file was created.
* Serial Number - This is the column that provides us with the information about the manufacturer-assigned serial number of the drive.
* Model - This is the column that provides us with the information about the manufacturer-assigned model number of the drive.
* Capacity - This column is about the drive capacity given in bytes.
* Failure - That column contains the information about the possible failure of the drive. If it is "0", then it means that the drive does not have any failures, but if it contains "1", it means that it was the last day the drive was operational before failure occurred.
* Based on the year from which the dataset come from, the amount of the columns with data is as follows:
    - from 2013 to 2014 -  we are given with 80 columns of data, where we can distinguish the Raw and Normalized records are taken for 40 different SMART stats (as was reported by the given drive). Each value presents the number reported by the drive 
    - from 2015 to 2017 - we are given with 90 columns of data, where we can distinguish the Raw and Normalized records taken for 45 different SMART stats (as was reported by the given drive). Each value presents the number reported by the drive 
    - 2018 (Q1) -  we are given with 100 columns of data, where we can distinguish the Raw and Normalized records taken for 50 different SMART stats (as was reported by the given drive). Each value presents the number reported by the drive 
    - 2018 (Q2) -  we are given with 104 columns of data, where we can distinguish the Raw and Normalized records taken for 52 different SMART stats (as was reported by the given drive). Each value presents the number reported by the drive 
    - 2018 (Q4) -  we are given with 124 columns of data, where we can distinguish the Raw and Normalized records taken for 62 different SMART stats (as was reported by the given drive). Each value presents the number reported by the drive 

# Sources

In the documentation folder I provide you with the article about Proactive Prediction of Hard Disk Drive Failure given in pdf format about and also below you can find some very useful links for the HDD failures in the predictive maintenance.

Link to BackBlaze website where you can find not only benchmark datasets but also a lot of different and useful reports about the published statistics and insights based on the hard drives: https://www.backblaze.com/b2/hard-drive-test-data.html

Other link to useful articles:
1) https://www.sciencedirect.com/science/article/pii/S1877050920319700 - this is the article titled: "A disk failure prediction method based on LSTM network due to its individual specificity";
2) https://www.backblaze.com/blog/using-machine-learning-to-predict-hard-drive-failures/ - article from BackBlaze website titled: "Using Machine Learning to Predict Hard Drive Failures";
3) article from the international journal of distributed sensor networks titled: "Random-forest-based failure prediction for hard disk drives";
4) https://www.researchgate.net/publication/314682447_Hard_Drive_Failure_Prediction_using_Decision_Trees this is the article from the research gate about "Hard Drive Failure Prediction using Decision Trees";
5) article from Hindawi website titled: "Hard Disk Drive Failure Prediction for Mobile Edge Computing Based on an LSTM Recurrent Neural Network".

Links to GitHub code:
1) https://github.com/badlogicmanpreet/htm-drivefailures
2) https://github.com/ayush-agarwal-0502/Machine-Predictive-Maintainence-Anomaly-Detection/blob/main/Lab1-XGBoost-For-Timeseries%20(1).ipynb

Another sample project about Hard Drive Reliability available on the data world website under the following link: https://data.world/scuttlemonkey/hard-drive-reliability-sample
