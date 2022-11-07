
# PLANT FAULT DETECTION - DATASET DESCRIPTION:

Introduction to the dataset: PHM Data Challenge 2015: Fault detection and prognostics, a common problem in industrial plant monitoring. The final aim is the ability to detect plant faults.

The dataset is about fault detection and prognostics in industrial plant monitoring. The goal is to detect plant failure events in advance from a set of potential faults together with localizing faults in time.

The dataset for a particular plant consist of 3 data files titled: 
* Plant(Number)a --> the data in this file give the following information: time series of sensor measurements and control reference signals for each of a number of control components of the plant
* Plant(Number)b --> this file provides the information about time series data that represents additional measurements of a fixed number of plant zones over the same period of time where a zone may cover one or more plant components
* Plant(Number)c --> this file represents plant fault events, each characterized by a start time, an end time, and a failure code

Each plant is specific through its number of components and the number of zones, however each plant logs faults from the same fixed set of faults.
Faults 1 to 5 are of interest (fault with code 6 represents all other faults which are not in focus).

The frequency of measurements: ~1 sample every 15 mins.
Time series data: spans a period of ~3 to 4 years.

The task for the description above is to predict future failure events of types 1 to 5 and the time of their occurrence from the past data.

Sample description of dataset for Plant Number 1:
We are given with 3 files:
* Plant(1)a.csv --> this is the file about Plant measurements per component: The columns, starting from the left, refer to the following items:  Component number “m”, time “t”, sensors “S1”-“S4”, and control references “R1”-“R4”.
* Plant(1)b.csv --> this is the file that contains additional plant measurements per zone in the plant with the following columns: zone number “n”, time “t”, sensors “E1” and “E2”.
* Plant(1)c.csv --> this is the file that provides the Faults with the following columns: Start time “t1”, end time “t2”, and fault code “F”.

Due to the large size of the entire database, get_data.sh currently only gets data for plants 1 and 3.  The script can be easily modified to get data for additional plants, which number 1 through 70.


#SOURCES AND CITATION FOR DATASET AND ARTICLES RELEVANT TO THE SUBJECT:

The dataset comes from PHM Data Challenge (from 2015) which is a competition open to all potential conference attendees and is organized every year.
The data can be fully downloaded from the GitHub website available under the following link: https://github.com/robot007/PHM15.

The original description of competition together with provided details about data is available on phmsociety website (available here: https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2015/phm-data-challenge-3/



Citation for the articles that might be found useful:
1) Hu G, Zhou T and Liu Q (2021) Data-Driven Machine Learning for Fault Detection and Diagnosis in Nuclear Power Plants: A Review. Front. Energy Res. 9:663296. doi: 10.3389/fenrg.2021.663296

2) XIE, Cong, et al. Feature extraction and ensemble decision tree classifier in plant failure detection. In: Annual Conference of the Prognostics and health management society. 2015. (The article in PDF format is also available in the Documentation folder).
