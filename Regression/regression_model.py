# Regression Model - FitPulse Dataset

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load dataset (absolute path)
df = pd.read_csv(r"C:\Users\geeth\OneDrive\Desktop\fitpulse-anomaly-detection\original_files\fitpulse_data.csv")

# We will predict pulse from heart_rate (simple regression)
X = df[["heart_rate"]]
y = df["pulse"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create & train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
print("Model Coefficient:", model.coef_)
print("Model Intercept:", model.intercept_)

# Plot regression line
plt.scatter(X_test, y_test, color="blue", label="Actual Values")
plt.plot(X_test, y_pred, color="red", label="Predicted Regression Line")
plt.xlabel("Heart Rate")
plt.ylabel("Pulse")
plt.title("Regression: Predicting Pulse From Heart Rate")
plt.legend()
plt.tight_layout()
plt.show()
