from datasets import load_dataset
import os

for root, dirs, files in os.walk("pyprolog-asts"):
    for file in files:
        if file.endswith(".parquet"):
            path = os.path.join(root, file)
            print (f"path {path}")
            data_files={
                #'train': 'train.parquet',
                #'test': 'test.parquet'
            }
            name = path.replace(".","_").replace("/","_").replace("-","_")
            data_files[name]=path
            dataset = load_dataset("parquet",data_files=data_files)
            dataset.save_to_disk(name)
