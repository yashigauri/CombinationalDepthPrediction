import pandas as pd

# Load and print first few rows of your CSV
df = pd.read_csv("dataset_50_circuits.csv")  # Make sure the file is in your project folder
print(df.head())  # Check if data is properly loaded