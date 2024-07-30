import datasets
import collections
import glob
import pandas as pd
import re
from autogluon.tabular import TabularDataset, TabularPredictor        
from autogluon.tabular import TabularDataset
from autogluon.features.generators import AutoMLPipelineFeatureGenerator
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


# Define the chunk size
chunk_size = int(len(df_pandas) / 50)  # Example: Split data into 5 chunks


feature_generator = AutoMLPipelineFeatureGenerator(
    enable_datetime_features=False,
    enable_vision_features=False,    
)

label = 'label'

# Split data into chunks
chunks = [df_pandas[i:i+chunk_size] for i in range(0, len(df_pandas), chunk_size)]

# Select a chunk for training and another for testing
input1  = chunks[0]

train_data = input1.sample(int(chunk_size * 0.8), random_state=seed)
test_data  = input1.drop(train_data.index)

X_train = train_data.drop(labels=[label], axis=1)
y_train = train_data[label]

X_train_transformed = feature_generator.fit_transform(X=X_train, y=y_train)

X_test_transformed = feature_generator.transform(test_data)

