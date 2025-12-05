import pandas as pd
import numpy as np

# Read FitPulse dataset
df = pd.read_csv(r"C:\Users\geeth\OneDrive\Desktop\fitpulse-anomaly-detection\original_files\fitpulse_data.csv")



print("Original Dataset:")
print(df.head())

# Explicitly add null values (for learning)
df.loc[0, "steps"] = np.nan
df.loc[2, "blood_points"] = np.nan

print("\nDataset After Inserting np.nan:")
print(df.head())

# Take steps as a NumPy array
steps_array = df["steps"].values

print("\nChecking nulls in steps:")
print(np.isnan(steps_array))

# Drop rows with any null values
df_rows_dropped = df.dropna()
print("\nAfter Dropping Rows with Null Values:")
print(df_rows_dropped.head())

# Drop columns with any null values
df_columns_dropped = df.dropna(axis=1)
print("\nAfter Dropping Columns with Null Values:")
print(df_columns_dropped.head())

# Replacing null values with mean
df["steps"] = df["steps"].fillna(df["steps"].mean())
df["blood_points"] = df["blood_points"].fillna(df["blood_points"].mean())

print("\nAfter Filling Null Values with Mean:")
print(df.head())
