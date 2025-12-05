import numpy as np
import pandas as pd

# Read FitPulse dataset
df = pd.read_csv(r"C:\Users\geeth\OneDrive\Desktop\fitpulse-anomaly-detection\original_files\fitpulse_data.csv")



# Take steps as a NumPy array
steps = np.array(df["steps"])

# Statistical operations
print("Maximum steps walked:", np.max(steps))
print("Minimum steps walked:", np.min(steps))
print("Total steps walked:", np.sum(steps))
print("Average steps per person:", np.mean(steps))

# Mathematical operations using NumPy arrays
heart_rate = np.array(df["heart_rate"])
pulse = np.array(df["pulse"])

difference = pulse - heart_rate
print("\nDifference between pulse and heart_rate (NumPy calculation):")
print(difference)
