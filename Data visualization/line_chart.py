import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\geeth\OneDrive\Desktop\fitpulse-anomaly-detection\original_files\fitpulse_data.csv")


plt.plot(df["customer_id"], df["heart_rate"], label="Heart Rate", color="red")
plt.xlabel("Customer ID")
plt.ylabel("Heart Rate")
plt.title("Heart Rate Trend by Customer")
plt.legend()
plt.show()
