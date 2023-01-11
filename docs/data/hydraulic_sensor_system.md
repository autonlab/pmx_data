# hydraulic sensor system

Problem type: Fault Detection and Classification

|  |
|  |
|  |
## Sources

Data location: https://archive.ics.uci.edu/ml/datasets/Condition+monitoring+of+hydraulic+systems#

No data citation available

No data license available.

## Additional information
Hydraulic System Sensor Dataset Description:

The data set used for the purpose of the project has been successfully downloaded from UCI website
and is available under the following link: https://archive.ics.uci.edu/ml/datasets/Condition+monitoring+of+hydraulic+systems.
This Database refers to the data taken from the sensors of the hydraulic test equipment to evaluate its technical condition.
Four types of faults have been superimposed together with different degrees of severity.
In total, the database has 43680 attributes.
The whole data set was created as an experiment performed by using hydraulic test rig, which
consist of a primary working and a secondary cooling-filtration circuit that are connected via the oil
tank. The constant load cycles are repeated by the system in a duration of 60 seconds. During this time
are measured values such as: pressures, volume flows and temperatures, whereas the condition of four
hydraulic components (which are cooler, valve, pump and accumulator) is quantitatively diversified.
We can distinguish there the attributes which are the numeric and continuous data sensors from the
measurements taken at the same point in time, respectively, of a hydraulic test rig’s working cycle. The
sensors were read at different sampling rates, leading to a different number of attributes per sensor,
even though they were all subjected to the same working cycle. These attributes are as follows:
1. Pressure sensors (PS1-6): 100 Hz, 6000 attributes per sensor (6 sensors)
2. Motor power sensor (EPS1): 100 Hz, 6000 attributes per sensor (1 sensor)
3. Volume flow sensors (FS1/2): 10 Hz, 600 attributes per sensor (2 sensors)
4. Temperature sensors (TS1-4): 1 Hz, 60 attributes per sensor (4 sensors)
5. Vibration sensor (VS1): 1 Hz, 60 attributes per sensor (1 sensor)
6. Efficiency factor (SE): 1 Hz, 60 attributes per sensor (1 sensor)
7. Virtual cooling efficiency sensor (CE): 1 Hz, 60 attributes per sensor (1 sensor)
8. Virtual cooling power sensor (CP): 1 Hz, 60 attributes per sensor (1 sensor)
There is no missing attributes values

In addition, the database comes with a file called profile.txt, where you can find 5 different vectors of class values.
Not counting vector 5 (named stable flag) all the others describe degradation processes over time.

The columns contained in this file are as follows:
1: cooling status / %:
	3: close to total failure
	20: reduced efficiency
	100: full efficiency

2: valve state / %:
	100: optimal switching behavior
	90: low delay
	80: long delay
	73: close to complete failure

3: Internal pump leakage:
	0: no leakage
	1: weak leakage
	2: severe leakage

4: Hydraulic accumulator / bar:
	130: optimum pressure
	115: slightly reduced pressure
	100: severely reduced pressure
	90: close to total failure

5: stable flag:
	0: conditions were stable
	1: static conditions may not yet have been reached

# Sources

Below I've included links to articles and github that can serve as quite a resource when doing research on this database yourself:

Article: L. P. Silvestrin, M. Hoogendoorn and G. Koole, "A Comparative Study of State-of-the-Art Machine Learning Algorithms for Predictive Maintenance," 2019 IEEE Symposium Series on Computational Intelligence (SSCI), 2019, pp. 760-767, doi: 10.1109/SSCI44817.2019.9003044. 
The article can be found at the following link: https://www.researchgate.net/profile/Ger-Koole-2/publication/339404826_A_Comparative_Study_of_State-of-the-Art_Machine_Learning_Algorithms_for_Predictive_Maintenance/links/5ef1bbf6a6fdcc73be96d7ba/A-Comparative-Study-of-State-of-the-Art-Machine-Learning-Algorithms-for-Predictive-Maintenance.pdf


Links to Kaggle with the materials on PM in the hydraulic systems:
1) https://www.kaggle.com/code/pulkitvyasdev/predictive-maintenance-of-hydraulic-system
2) https://www.kaggle.com/datasets/mayank1897/condition-monitoring-of-hydraulic-systems

UCI repository link, where the database is located: https://archive.ics.uci.edu/ml/datasets/Condition+monitoring+of+hydraulic+systems 
Citation: Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.


Link to github with the project: https://github.com/mjain72/Condition-monitoring-of-hydraulic-systems-using-xgboost-modeling/blob/master/HydraulicCondition.ipynb - this link is also provided with the following LICENSE: 

MIT License

Copyright (c) 2018 Mohit Jain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
