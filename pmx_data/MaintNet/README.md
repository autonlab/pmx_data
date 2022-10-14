
# MAINTNET - DATASET DESCRIPTION:

These data contain technical language employed in maintenance logbooks. Their primary purpose is to facilitate the study of technical language. However, some aspects of these data may support classification tasks as well. The home of the data is https://people.rit.edu/fa3019/MaintNet/index.html

There are three different technical domains represented; avaiation, automotive, and facility. Each domain contains four datasets describing abbreviations, morphosyntactic information, a domain term bank, and maintenance data.

## Aviation Historical Maintenance Dataset
These data contain 4 datasets describing abbreviations, morphosyntactic information, a domain term bank, and maintenance data. The datasets are structured as follows.

*grammar*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 57 entries, 0 to 56
Data columns (total 6 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   Word                  57 non-null     object
 1   Description           57 non-null     object
 2   Compound              57 non-null     object
 3   Lemma                 57 non-null     object
 4   Stem                  57 non-null     object
 5   Part of Speech (POS)  57 non-null     object
dtypes: object(6)
memory usage: 2.8+ KB
```

*maintnet_aviation_dataset_deidentified*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6169 entries, 0 to 6168
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   IDENT    6169 non-null   int64 
 1   PROBLEM  6169 non-null   object
 2   ACTION   6169 non-null   object
dtypes: int64(1), object(2)
memory usage: 144.7+ KB
```

*aviation_abbriviation*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 65 entries, 0 to 64
Data columns (total 3 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   Abbriviation_Code     65 non-null     int64 
 1   Abbreviated           65 non-null     object
 2   Standard_Description  65 non-null     object
dtypes: int64(1), object(2)
memory usage: 1.6+ KB
```

*domain_words2_termBank*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 2 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Word     100 non-null    object
 1   Example  100 non-null    object
dtypes: object(2)
memory usage: 1.7+ KB
```

This data set is hosted at https://people.rit.edu/fa3019/MaintNet/data_aviation.html

Please aknowledge the MaintNet when using this dataset.
This is the entire dataset.

## Vehicle Historical Maintenance Dataset
These data contain 4 datasets describing abbreviations, morphosyntactic information, a domain term bank, and maintenance data. The datasets are structured as follows.

*grammar*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 57 entries, 0 to 56
Data columns (total 6 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   Word                  57 non-null     object
 1   Description           57 non-null     object
 2   Compound              57 non-null     object
 3   Lemma                 57 non-null     object
 4   Stem                  57 non-null     object
 5   Part of Speech (POS)  57 non-null     object
dtypes: object(6)
memory usage: 2.8+ KB
```

*Labeled_Car_Dataset200*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Dept        200 non-null    int64  
 1   JobDate     200 non-null    object 
 2   JobTime     200 non-null    object 
 3   jobno       200 non-null    int64  
 4   ReasonID    200 non-null    int64  
 5   Reason      200 non-null    object 
 6   Notes       200 non-null    object 
 7   Unnamed: 7  1 non-null      float64
dtypes: float64(1), int64(3), object(4)
memory usage: 12.6+ KB
```

*domain_words2_termBank*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 2 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Word     100 non-null    object
 1   Example  100 non-null    object
dtypes: object(2)
memory usage: 1.7+ KB
```

This data set is hosted at https://people.rit.edu/fa3019/technical/vehicle.html

The data are owned by Connecticut Open Data. Requesting permission for the use of the dataset for your research may be required. See the link above for more detail.

## Facility Historical Maintenance Dataset
These data contain 4 datasets describing abbreviations, morphosyntactic information, a domain term bank, and maintenance data. The datasets are structured as follows.

*facilty_grammar*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 59 entries, 0 to 58
Data columns (total 6 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   Word                  59 non-null     object
 1   Description           59 non-null     object
 2   Compound              7 non-null      object
 3   Lemma                 59 non-null     object
 4   Stem                  59 non-null     object
 5   Part of Speech (POS)  59 non-null     object
dtypes: object(6)
memory usage: 2.9+ KB
```

*facility_abbriviation*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 60 entries, 0 to 59
Data columns (total 3 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   Abbriviation_Code     60 non-null     int64 
 1   Abbreviated           60 non-null     object
 2   Standard_Description  60 non-null     object
dtypes: int64(1), object(2)
memory usage: 1.5+ KB
```

*facility_domain*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 259 entries, 0 to 258
Data columns (total 2 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Word     259 non-null    object
 1   Example  259 non-null    object
dtypes: object(2)
memory usage: 4.2+ KB
```

*Facility_Maintenance200*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 6 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   WORK_ID         200 non-null    int64 
 1   SITE_ID         200 non-null    object
 2   DATE_REQUESTED  200 non-null    object
 3   PROB_TYPE       200 non-null    object
 4   DATE_COMPLETED  200 non-null    object
 5   DESCRIPTION     200 non-null    object
dtypes: int64(1), object(5)
memory usage: 9.5+ KB
```

This data set is hosted at https://people.rit.edu/fa3019/MaintNet/data_facility.html

The data are owned by Baltimore City Maryland. Requesting permission for the use of the dataset for your research may be required. See the link above for more detail.
