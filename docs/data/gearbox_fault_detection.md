# gearbox fault detection

Problem type: Fault Detection

|  |
|  |
|  |
## Sources

Data location: https://c3.ndc.nasa.gov/dashlink/resources/997/

No data citation available

No data license available.

## Additional information
# DATASET DESCRIPTION

This PHM Data Challenge is focused on fault detection and magnitude estimation for a generic gearbox using accelerometer data and information about bearing geometry.  Data were sampled synchronously from accelerometers mounted on both the input and output shaft retaining plates. An attached tachometer generates 10 pulses per revolution providing very accurate zero crossing information.  Data were collected at 30, 35, 40, 45 and 50 Hz shaft speed, under high and low loading. Additionally, different repeated runs are included in the data, although the run time and load were not sufficient to induce significant fault progression. There are a total of 560 samples to be classified.  Data are provided in .csv files, with three columns - the first column is input voltage, second is output voltage, and the third is tachometer.

Sample Rate: 66,666.67 Samples per Second (200 KHz/3).
Most runs have around 133328 samples.

The dataset is large - 1.9G when unzipped.

Suggested result format is viewable here:
https://phmsociety.org/data-analysis-competition/result-format/
Essentially, this is treated as a multilabel time series classification problem, with 45 possible fault classes.

# SOURCES

You can find more information at https://c3.ndc.nasa.gov/dashlink/resources/997/, as well as on the competition blog, http://phm09challenge.blogspot.com.

When using the data in publications, please reference the following (note the creative commons license): 
(cc) PHM Society, Gearbox fault detection data set, 2010