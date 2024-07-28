import datasets
import collections
import glob
import pandas as pd
import re
from autogluon.tabular import TabularDataset, TabularPredictor        

for name in glob.glob("pyprolog-asts/*"):
    try:
        ds = datasets.load_from_disk(name)
    except FileNotFoundError as e:
        continue # not a dataset
    print(name)
    for x in ds:
        df_pandas = pd.DataFrame(ds[x])
        print(df_pandas.head())
        #print(df_pandas.describe())
        #print(df_pandas[0].describe())
        predictor = TabularPredictor(
            label='_type'
        ).fit(df_pandas)
        print(predictor.head())
