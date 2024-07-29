import datasets
import collections
import glob
import pandas as pd
import re
from autogluon.tabular import TabularDataset, TabularPredictor        


df_pandas = pd.read_pickle("first_dataset.pkl")
        
    
print(df_pandas.describe())
print(df_pandas.head())
predictor = TabularPredictor(
    label="label"
).fit(df_pandas)
print(predictor)
