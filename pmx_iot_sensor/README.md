# PMx IoT SENSOR - DATASET DESCRIPTION:

The data is originally available at the following link: https://bit.ly/2nwwwiE.

The database is derived from a proxy of automotive components, such as motors, rotors and heat exchangers, among others, whose failure brings the entire assembly line to a halt, which automatically generates considerable downtime and additional costs. It is therefore important to predict the failure of these and other components in order to be able to avoid such situations in the future and thus improve product quality and save energy spent on machine work. It was decided to implement predictive maintenance techniques on heat exchangers, whose function was to cool extemporaneously in extremely high-temperature synthetic fluids flowing out of the assembly line, in an effort to reduce the number of problems caused by continuous downtime due to clogged lines.
 
The database consists of 944 observations and 10 features.
The description of the features found in this dataset is as follows:
- footfall: the total number of workers in the shop floor at a particular instance of time
- tempMode: temperature mode (1-7), where one is minimum, and seven is maximum
- AQ: Air Quality sensor, with modes between 1 to 7, where modes 1-5 are acceptable levels of air quality and mode 6 -7 are considered not acceptable
- Ultrasound Sensor: used to detect high or low-frequency sounds due to leakage
- CS: Current Sensor to monitor the current flow. Its level is between 1- 7, where 1 in minimal level and 7 is maximum current flow
- VOC: (PhotoIonization Detector) sensors used for detecting low concentrations of Volatile Organic Compound to detect clogging in conduits of heat exchanger unit
- RP: outside room Pressure
- IP: Inside Pressure of machine conduits for leak detection
- Temperature: actual temperature of machinery
- Output: the target variable predicting whether the equipment is running or failed. It is a binary coded variable, where 0 depicts running, and 1 represents failure

# SOURCES RELATED TO~ THE IoT SENSORS IN THE FIELD OF PMx:

There is one interesting article in which the researchers for the experiment purposes use this dataset. The references are as follows:
Nangia, Shikhil & Makkar, Sandhya & Hassan, Rohail. (2020). IoT based Predictive Maintenance in Manufacturing Sector. SSRN Electronic Journal. 10.2139/ssrn.3563559. 

The original dataset can be found under the following link: https://github.com/shikhilnangia/iotsensor

Links to some interesting articles found on the internet about the IoT sensors in PMx:
1) https://www.techtarget.com/iotagenda/feature/IoT-based-predictive-maintenance-staves-off-machine-failures

2) https://www.itconvergence.com/blog/5-benefits-iot-based-predictive-maintenance/

3) https://www.scnsoft.com/blog/iot-predictive-maintenance-guide
