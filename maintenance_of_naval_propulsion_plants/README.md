# DESCRIPTION FOR DATASET ABOUT: "CONDITION BASED MAINTENANCE OF NAVAL PROPULSION PLANTS"


The dataset consists of data records taken from a sophisticated simulator of Gas Turbines (mounted on a Frigate characterized by a Combined Diesel Electric and Gas propulsion plant).

For the purpose of this simulator, blocks have been carefully developed that together form the structure of the simulator, these blocks include the propeller, hull, gas turbine, gearbox and controller. In addition, it is also possible to take into account the situation where there is a decrease in performance over time of the components that make up the gas turbine structure (such as the turbine and the compressor).

The parameters describing the propulsion system are as follows:
- Vessel speed (linear function of lever position lp).
- Compressor degradation factor kMc.
- The degradation coefficient of the turbine kMt.
Having information about these 3 parameters, it is possible by their combination to make a description of the degradation state.

In order to discretize the compressor degradation state, the compressor degradation coefficient was studied in the [1; 0.95] domain, while the turbine degradation coefficient was studied in the [1; 0.975] domain.

The ship's speed was tested by sampling real speed from 3 knots (kt) to 27 kt with a granularity of representation equal to tree knots.

The dataset file saved in txt format consist of 18 column (16 column that contain Gas Turbine measures (features) that indirectly represents the state pf the system subject to the performance decay and 2 columns which represent the coefficient state).


The columns are as follow:
- Lever position (lp) [ ]
- Ship speed (v) [knots]
- Gas Turbine (GT) shaft torque (GTT) [kN m]
- GT rate of revolutions (GTn) [rpm]
- Gas Generator rate of revolutions (GGn) [rpm]
- Starboard Propeller Torque (Ts) [kN]
- Port Propeller Torque (Tp) [kN]
- Hight Pressure (HP) Turbine exit temperature (T48) [C]
- GT Compressor inlet air temperature (T1) [C]
- GT Compressor outlet air temperature (T2) [C]
- HP Turbine exit pressure (P48) [bar]
- GT Compressor inlet air pressure (P1) [bar]
- GT Compressor outlet air pressure (P2) [bar]
- GT exhaust gas pressure (Pexh) [bar]
- Turbine Injecton Control (TIC) [%]
- Fuel flow (mf) [kg/s]
- GT Compressor decay state coefficient
- GT Turbine decay state coefficient

# SOURCES INFORMATION FILE

The dataset has been downloaded and added to the repository from the UCI Dataset Repository website and is available under the following link: https://archive.ics.uci.edu/ml/datasets/Condition+Based+Maintenance+of+Naval+Propulsion+Plants
Citation:
A. Coraddu, L. Oneto, A. Ghio, S. Savio, D. Anguita, M. Figari, Machine Learning Approaches for Improving Condition?Based Maintenance of Naval Propulsion Plants, Journal of Engineering for the Maritime Environment, 2014, DOI: 10.1177/1475090214540874, (In Press)

Source of an origin of the dataset:
Andrea Coraddu(2), Luca Oneto(1), Alessandro Ghio(1), Stefano Savio(2), Davide Anguita(3), Massimo Figari(2) 
1 - Smartlab - Non-Linear Complex Systems Laboratory 
DITEN - UniversitÂˆÃ  degli Studi di Genova, Genoa (I-16145), Italy. 
2 - Marine Technology Research Team 
DITEN - UniversitÂˆÃ  degli Studi di Genova, Genoa (I-16145), Italy. 
3 - Smartlab - Non-Linear Complex Systems Laboratory 
DIBRIS - UniversitÂˆÃ  degli Studi di Genova, Genoa (I-16145), Italy. 
cbm '@' smartlab.ws 
www.cbm.smartlab.ws

This dataset is also available to download from the kaggle website, where in addition you may find some codes written with the use of this dataset: https://www.kaggle.com/datasets/elikplim/maintenance-of-naval-propulsion-plants-data-set




## References to different articles:


For additional source of information, you can find very useful reading the following documents (for which the citation is provided):   

* Altosole M, Benvenuto G, Figari M, Campora U. Real-time simulation of a COGAG naval ship propulsion system. Proceedings of the Institution of Mechanical Engineers, Part M: Journal of Engineering for the Maritime Environment. 2009;223(1):47-62. doi:10.1243/14750902JEME121

* (Article provided in PDF format is available in the Documentation folder): Coraddu, A., Oneto, L., Ghio, A., Savio, S., Anguita, D., & Figari, M. (2016). Machine learning approaches for improving condition-based maintenance of naval propulsion plants. Proceedings of the Institution of Mechanical Engineers, Part M: Journal of Engineering for the Maritime Environment, 230(1), 136-153.

* Mehyo, Mohamad & Özcan, Hakan & Hassan, Ahmed Hassan Ahmed. (2019). Studying the Condition Based Maintenance Dataset of Naval Propulsion Plants Using Regression ANN. 

* Francesca Cipollini, Luca Oneto, Andrea Coraddu, Alan John Murphy, Davide Anguita,
Condition-based maintenance of naval propulsion systems: Data analysis with minimal feedback,
Reliability Engineering & System Safety, Volume 177, 2018, Pages 12-23, ISSN 0951-8320, https://doi.org/10.1016/j.ress.2018.04.015.
(https://www.sciencedirect.com/science/article/pii/S0951832017309973)

* Francesca Cipollini, Luca Oneto, Andrea Coraddu, Alan John Murphy, Davide Anguita, Condition-Based Maintenance of Naval Propulsion Systems with supervised Data Analysis, Ocean Engineering, Volume 149, 2018, Pages 268-278, ISSN 0029-8018, https://doi.org/10.1016/j.oceaneng.2017.12.002.
(https://www.sciencedirect.com/science/article/pii/S0029801817307242)

* A. Coraddu, L. Oneto, A. Ghio, S. Savio, M. Figari and D. Anguita, "Machine learning for wear forecasting of naval assets for condition-based maintenance applications," 2015 International Conference on Electrical Systems for Aircraft, Railway, Ship Propulsion and Road Vehicles (ESARS), 2015, pp. 1-5, doi: 10.1109/ESARS.2015.7101499.

* Greene, William. (2006). Evaluation of non-intrusive monitoring for condition based maintenance applications on US Navy propulsion plants. 


## Links to the codes:

Below I attached also some useful links Codes:
1) Topic: Revisiting Machine Learning Datasets - Condition Based Maintenance of Naval Propulsion Plants Dataset (link: https://simonwenkel.com/2019/04/19/revisitingML-naval-propulsion.html)
2) GitHub code: the topic is Condition Based Maintenance of Naval Propulsion Plants Data Set, written by Ha Nguyen (link https://github.com/trungha-ngx/statistics-project-condition-based-maintenance)

  









