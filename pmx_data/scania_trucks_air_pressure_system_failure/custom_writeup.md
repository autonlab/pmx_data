
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

