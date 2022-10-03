import os
import pandas as pd

#this dataset contains several categorical features that can take multiple values for a single observation
#we will combine it into one dataframe by changing each multi-value categorical feature into
#a set of binary features indicating the prescence or abscence of a possible value that feature could take

train_data = pd.read_csv(os.path.join('datasets', 'train_data.csv'))
test_data = pd.read_csv(os.path.join('datasets', 'test_data.csv'))

all_ids = set(list(train_data['id']) + list(test_data['id']))

for (filename, feature) in (('assembly_line_info', 'assembly_line_type'), 
							('car_variant_data', 'car_variant'),
							('issue_info', 'issue_type')):
	df = pd.read_csv(os.path.join('datasets', filename + '.csv'))

	#each dataframe contains a lot of ids that arent present in the test or train data; remove these
	df = df.loc[df['id'].apply(lambda x: x in all_ids)]

	#use pivot_table to add a col for each possible value of the feature in question
	#with a 1 to indicate that value is present and a 0 to indicate it isn't
	df['present'] = pd.Series(1, df.index)
	df = pd.pivot_table(df, index='id', columns=feature, values='present', fill_value=0)

	train_data = pd.merge(train_data, df, on='id', how='left')
	test_data = pd.merge(test_data, df, on='id', how='left')

#we need to treat log_report_type a little differently than the other features
#each log_report_type for each id is associated with an integer (>=1) volume value
#since this is never zero, we can set it to zero in our pivot table to indicate that that
#log_report_type is not present for that observation
df = pd.read_csv(os.path.join('datasets', 'log_report_type_data.csv'))
df = df.loc[df['id'].apply(lambda x: x in all_ids)]
df = pd.pivot_table(df, index='id', columns='log_report_type', values='volume', fill_value=0)

train_data = pd.merge(train_data, df, on='id', how='left')
test_data = pd.merge(test_data, df, on='id', how='left')
