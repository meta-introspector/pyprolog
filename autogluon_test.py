import datasets
import collections
import glob
import pandas as pd
import re
from autogluon.tabular import TabularDataset, TabularPredictor        

df_fields = pd.read_csv("report_without_numbers_sorted.csv")

fields_ds = df_fields.head(10000)['index']
fields = { x:1 for x in df_fields.head(1000)['index'].to_dict().values()}

truncated_data = []
for name in glob.glob("pyprolog-asts/*"):
    try:
        ds = datasets.load_from_disk(name)
    except FileNotFoundError as e:
        continue # not a dataset
    print(name)
    
    for x in ds:
        print (x)
        ds2 =ds[x]
        iter=ds2.iter(batch_size=1)
        for i in iter:
            for k in i:
                c = {
                    "label" : name
                } # the object to collect
                k2 = re.sub("\d+", "N", k)
                if k2 in fields :
                    v = i[k][0] # get the value
                    if isinstance(v, (str,float,int)):
                        c[k]=v
                    else:
                        print("SKIP",k,v)
                    truncated_data.append(c)

if True:                    
    df_pandas = pd.DataFrame(truncated_data)
    #df_pandas.to_csv("first_dataset.csv")
    print(df_pandas.describe())
    print(df_pandas.head())
    print("First label",first)
    predictor = TabularPredictor(
        label="label"
    ).fit(df_pandas)
    print(predictor)
