import datasets
import collections
import glob
import pandas as pd
import re
from autogluon.tabular import TabularDataset, TabularPredictor        
from autogluon.tabular import TabularDataset
from autogluon.features.generators import AutoMLPipelineFeatureGenerator
import sys
import logging
from text_utils import try_write
ag_logger = logging.getLogger('autogluon')
logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

seed = 43

df_pandas = pd.read_pickle("first_dataset2.pkl")
       
#predictor = TabularPredictor(
#    label="label"
# Split data into training and testing sets
#train_df, test_df = train_test_split(df_pandas, test_size=0.2, random_state=42)

# Fit the predictor
#predictor = TabularPredictor(label="label").fit(train_df)

# Evaluate the predictor
#performance = predictor.evaluate(test_df)


chunks = 10
# Define the chunk size
df_size = len(df_pandas)
chunk_size = int( df_size / chunks)+1  # Example: Split data into 5 chunks
sample_size = int(chunk_size * 0.8)+1

print(dict(sample_size=sample_size,
           df_size=df_size,
           chunks=chunks,
           chunk_size=chunk_size))
assert(sample_size>0)

feature_generator = AutoMLPipelineFeatureGenerator(
    enable_datetime_features=False,
    enable_vision_features=False,
    verbosity=3
)

label = 'label'

# Split data into chunks
chunks = [df_pandas[i:i+chunk_size] for i in range(0, len(df_pandas), chunk_size)]

# Select a chunk for training and another for testing
input1  = chunks[0]


train_data = input1.sample(sample_size, random_state=seed)
test_data  = input1.drop(train_data.index)

try_write(train_data,"train_Data")
try_write(test_data,"test_Data")

X_train = train_data.drop(labels=[label], axis=1)
try_write(X_train,"X_train")
y_train = train_data[label]
try_write(y_train.to_frame("y_train"),"y_train")


X_train_transformed = feature_generator.fit_transform(X=X_train, y=y_train)

feature_generator.save('feature_generator.pkl')

try_write(X_train_transformed,"X_train_transformed")

X_test_transformed = feature_generator.transform(test_data)
try:
    try_write(X_test_transformed.to_frame("X_test_transformed"),"X_test_transformed")
except:
    try_write(X_test_transformed,"X_test_transformed")
    

