import os
import pandas as pd
from sklearn.model_selection import train_test_split

data_dir = './train-valid-test_data'
if not os.path.isdir(data_dir):
   os.makedirs(data_dir)
   
data_path = './data.tsv'

dataframe = pd.read_csv(data_path, sep='\t')

train, valid_test = train_test_split(dataframe, test_size=0.2, random_state=42, shuffle=True)
valid, test = train_test_split(valid_test, test_size=0.5, random_state=42, shuffle=True)

# determine the path where to save the train and test file
train_path = data_dir + '/train.tsv'
valid_path = data_dir + '/valid.tsv'
test_path = data_dir + '/test.tsv'

# save the train and test file
# again using the '\t' separator to create tab-separated-values files
train.to_csv(train_path, sep='\t', index=False)
valid.to_csv(valid_path, sep='\t', index=False)
test.to_csv(test_path, sep='\t', index=False)


