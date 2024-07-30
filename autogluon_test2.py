import datasets
import collections
import glob
import pandas as pd
import re
from autogluon.tabular import TabularDataset, TabularPredictor        

df_pandas = pd.read_pickle("first_dataset2.pkl")
       
#print(df_pandas.describe())
#print(df_pandas.head())


#predictor = TabularPredictor(
#    label="label"
# Split data into training and testing sets
#train_df, test_df = train_test_split(df_pandas, test_size=0.2, random_state=42)

# Fit the predictor
#predictor = TabularPredictor(label="label").fit(train_df)

# Evaluate the predictor
#performance = predictor.evaluate(test_df)


#).fit(df_pandas)
#print(predictor)


# Define the chunk size
chunk_size = int(len(df_pandas) / 50)  # Example: Split data into 5 chunks

# Split data into chunks
chunks = [df_pandas[i:i+chunk_size] for i in range(0, len(df_pandas), chunk_size)]

# Select a chunk for training and another for testing
train_chunk = chunks[0]
test_chunk = chunks[1]

# Alternatively, you could use train_test_split on the selected chunk for a more random split within that chunk
# train_df, test_df = train_test_split(chunks[0], test_size=0.2, random_state=42)

# Fit the predictor on the selected training chunk
predictor = TabularPredictor(label="label",
                             ).fit(
                                 ag_args_fit={'num_gpus': 1},
                                 train_data=train_chunk,
                                 time_limit=100,
                                 presets='interpretable')
# Valid presets: ['best_quality', 'high_quality', 'good_quality', 'medium_quality', 'optimize_for_deployment', 'ignore_text', 'ignore_text_ngrams', 'interpretable', 'best_quality_v082', 'high_quality_v082', 'good_quality_v082'

# Evaluate the predictor on the selected testing chunk
performance = predictor.evaluate(test_chunk)

print("Model Performance:", performance)
