import astor
from ast2json import ast2json
import json
import pprint
import pandas as pd
import datasets
import flatten_json
from datasets import Dataset, DatasetDict

def normalize():        
    #raw_data = [x for x in collect_project_files()]
    data = astor.code_to_ast.find_py_files("./")
    
    for x in data:
        raw_data =[]

        fname = "/".join(x)
        print(fname)
        if "#" in fname: # ignore temp files with #
            continue
        flattened = flatten_json.flatten(ast2json(astor.code_to_ast.parse_file(fname)))
        raw_data.append(flattened)
        df = pd.json_normalize(raw_data)
        #df.to_csv(fname +".csv")
        df.to_pickle(fname +".pkl")
        try:
            df.to_feather(fname +".fth")
        except Exception as e:
            print("fth" + str(e))
        try:
            df.to_parquet(fname +".prq")
        except Exception as e:
            print("prq" + str(e))

normalize()
