import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# Reading CSV
marks=pd.read_csv('mark-list.csv')
pd.set_option("display.max_rows", None, "display.max_columns", None)

#print(marks)

## for only English ## 

# Training
# n_estimators=100 means 100 trees
# "contamination" means % of randomness present in our dataset
# max_features means how many featues you need to include while training the isolation-forest algorithm, here 1.0 means it draw single feature from the dataset
#model=IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.2), max_features=1.0)
#model.fit(marks[['English']])

# Prediction
#marks['anomailes_scores_eng']=model.decision_function(marks[['English']])
#marks['anomaly_eng']=model.predict(marks[['English']])

# here, 1 for good data and -1 for bad data
#print(marks.head(10))
#print(marks)

### for only Maths ###

#model=IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.2), max_features=1.0)
#model.fit(marks[['Mathematics']])

# Prediction
#marks['anomailes_scores_math']=model.decision_function(marks[['Mathematics']])
#marks['anomaly_math']=model.predict(marks[['Mathematics']])

# here, 1 for good data and -1 for bad data
#print(marks)

## for both Eng and Maths ## 

model=IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.2), max_features=1.0)
model.fit(marks[['English', 'Mathematics']])

# Prediction
marks['anomailes_scores_both']=model.decision_function(marks[['English', 'Mathematics']])
marks['anomaly_for_both']=model.predict(marks[['English', 'Mathematics']])

# here, 1 for good data and -1 for bad data
print(marks)


