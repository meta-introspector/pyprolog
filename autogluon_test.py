import datasets
import collections
import glob
import pandas as pd
import re
from autogluon.tabular import TabularDataset, TabularPredictor        
MAXFILES=400000000
MAXFIELDS=200000000

df_fields = pd.read_csv("report_without_numbers_sorted.csv")
fields = { x:1 for x in df_fields.head(MAXFIELDS)['index'].to_dict().values()} 
truncated_data = []
for name in glob.glob("pyprolog-asts/*")[0:MAXFILES]:
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
            c = {
                "label" : name
            } # the object to collect
            
            for k in i:
                k2 = re.sub("\d+", "N", k)
                dskip = 0
                for skip in ("lineno","offset"):
                    if k2.endswith(skip):
                        dskip = 1
                if dskip==0:
                    if k2 in fields :
                        v = i[k][0] # get the value
                        if isinstance(v, (str,float,int)):
                            c[k2]=v # fold the fields together
            truncated_data.append(c)

if True:                    
    df_pandas = pd.DataFrame(truncated_data)
    #df_pandas.to_parquet("first_dataset.parquet")

    # try:
    #     df_pandas.to_feather("first_dataset.fth")
    # except Exception as e:
    #     print(e)
    # try:
    #     df_pandas.to_parquet("first_dataset.parquet")
    # except Exception as e:
    #     print(e)
    # try:
    #     df_pandas.to_orc("first_dataset.orc")
    # except Exception as e:
    #     print(e)
    try:
        df_pandas.to_pickle("first_dataset3.pkl")
    except Exception as e:
        print(e)
    try:
        df_pandas.to_json("first_dataset3.json")
    except Exception as e:
        print(e)
    try:
        df_pandas.to_csv("first_dataset3.csv",escapechar="\\")
    except Exception as e:
        print(e)
        
    
    print(df_pandas.describe())
    print(df_pandas.head())
    predictor = TabularPredictor(
        label="label"
    ).fit(df_pandas)
    print(predictor)
