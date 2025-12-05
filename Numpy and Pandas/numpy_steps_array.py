import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\geeth\OneDrive\Desktop\fitpulse-anomaly-detection\original_files\fitpulse_data.csv")



steps = np.array(df["steps"])
print("Steps Array:")
print(steps)

heart_rate = np.array(df["heart_rate"])
print("\nHeart Rate Array:")
print(heart_rate)
