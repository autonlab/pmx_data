# nasa milling prognostic dataset

Problem type: Fault Detection

Note: Data is hosted on kaggle, and requires setup before downloading (see comments in get_data.sh)

|  |
|  |
|  |
## Sources

Data location: https://www.kaggle.com/datasets/vinayak123tyagi/milling-data-set-prognostic-data

No data citation available

No data license available.

## Additional information
# NASA MILLING PROGNOSTIC DATASET FOR PMx - DATASET DESCRIPTION

The data contained in the dataset subfolder is originally owned by NASA in .mat format. But in this repository the dataset has been downloaded from kaggle website (link in the SOURCE file) in .csv format (converted from .mat).
The tool wear was investigated in a regular cut, entry cut and exit cut.

The mill.csv data file represents experiments from runs on a milling machine under some different operating conditions.
The dataset consists of 3 different types of sensors (all of them acquired at several positions):
- acoustic emission sensor
- vibration sensor
- current sensor

The dataset contains 14 different columns, that represents the following fields:
1. row number
2. case - gives case number from 1 to 16
3. run - counter for experimental runs in each case. The number of runs was dependent on the degree of flank wear, measured between runs at irregular intervals up to a wear limit (sometimes also beyond).
4. VB - flank wear, measured after runs. Flank wear was not always measured and at times when no measurements were taken, no entry was made.
5. time - duration of experiment (restarts for each case)
6. DOC - this abbreviation stands for depth of cut (does not vary for each case)
7. feed - feed (does not vary for each case)
8. material - material (also does not vary for each case)
9. smcAC - AC spindle motor current
10. smcDC - DC spindle motor current
11. vib_table - table vibration
12. vib_spindle - spindle vibration
13. AE_table - acoustic emission at table
14. AE_spindle - acoustic emission at spindle

For detailed description, in the Documentation subfolder is available to download the README file in pdf format written by Kai Goebel (NASA Ames) & Alice Agogino (UC Berkeley) [citation provided in the SOURCES file).

# Links, citation, references to different sources related to the subject which might be very useful while using this dataset.

The dataset has originally been downloaded from the kaggle website available under the following link: https://www.kaggle.com/datasets/vinayak123tyagi/milling-data-set-prognostic-data

License:
https://www.usa.gov/government-works/

References: A. Agogino and K. Goebel (2007). BEST lab, UC Berkeley. "Milling Data Set ", NASA Ames Prognostics Data Repository (http://ti.arc.nasa.gov/project/prognostic-data-repository), NASA Ames Research Center, Moffett Field, CA


The link to the GitHub code created by Rajat Rai for prediction of the remaining useful life: https://github.com/rajatrai16921/Remaining-User-Life-Prediction-Using-NASA-Milling-Dataset

The references to the article related to the subject: Y. Zhou and W. Sun, "Tool Wear Condition Monitoring in Milling Process Based on Current Sensors," in IEEE Access, vol. 8, pp. 95491-95502, 2020, doi: 10.1109/ACCESS.2020.2995586.

The README file in pdf format contains in the documentation subfolder has been also downloaded from the kaggle website and is available under the following link in the data explorer: https://www.kaggle.com/datasets/vinayak123tyagi/milling-data-set-prognostic-data
