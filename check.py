import pandas as pd



# Load the dataset
df = pd.read_csv("dataset_50_circuits.csv")

# Check data types
print(df.dtypes)

# Print a few rows to inspect
print(df.head())


