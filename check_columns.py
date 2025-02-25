import pandas as pd

# Load CSV file
df = pd.read_csv("dataset_50_circuits.csv")

# Print all column names
print("Columns in CSV:", df.columns)
