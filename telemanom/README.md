# Data Description

The telemanom dataset is a labeled time series anomaly detection dataset provided by NASA, with expert-labeled telemetry anomaly data from the Soil Moisture Active Passive (SMAP) satellite and the Mars Science Laboratory (MSL) rover, Curiosity.

All data has been anonymized with regard to time and all telemetry values are pre-scaled between (-1,1) according to the min/max in the test set. Channel IDs are also anonymized, but the first letter indicates the type of channel (P = power, R = radiation, etc.). Model input data also includes one-hot encoded information about commands that were sent or received by specific spacecraft modules in a given time window. No identifying information related to the timing or nature of commands is included in the data.

The anomaly labels and metadata are available in labeled_anomalies.csv, which includes:

* channel id: anonymized channel id - first letter represents nature of channel (P = power, R = radiation, etc.)
* spacecraft: spacecraft that generated telemetry stream (SMAP or MSL)
* anomaly_sequences: start and end indices of true anomalies in stream
* class: the class of anomaly (see below)
* num values: number of telemetry values in each stream (number of rows)

The anomalies are only labeled for the test data.

There are two anomaly classes in labeled_anomalies.csv: point anomalies and contextual anomalies.  Point anomalies are single values that fall within low-density regions of values, and contextual anomalies are single values that do not fall within low-density regions yet are anomalous with regard to local values.   Point anomalies would likely be identified by properly-set alarms or distance-based methods that ignore temporal information, while contextual anomalies require more complex methodologies such as LSTMs or Hierarchical Temporal Memory (HTM) approaches to detect.  See the paper linked below for more information.

# SOURCES
The primary source of information on this dataset is: https://github.com/khundman/telemanom

A paper that uses this data:
@article{https://doi.org/10.48550/arxiv.1802.04431,
  doi = {10.48550/ARXIV.1802.04431},
  url = {https://arxiv.org/abs/1802.04431},
  author = {Hundman,  Kyle and Constantinou,  Valentino and Laporte,  Christopher and Colwell,  Ian and Soderstrom,  Tom},
  keywords = {Machine Learning (cs.LG),  Machine Learning (stat.ML),  FOS: Computer and information sciences,  FOS: Computer and information sciences},
  title = {Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding},
  publisher = {arXiv},
  year = {2018},
  copyright = {arXiv.org perpetual,  non-exclusive license}
}