import pandas as pd

# Load the dataset
data = pd.read_csv("data/app_usage.csv")

# Show first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Basic information about data
print("\nDataset information:")
print(data.info())

# Basic statistics
print("\nStatistical summary:")
print(data.describe())
