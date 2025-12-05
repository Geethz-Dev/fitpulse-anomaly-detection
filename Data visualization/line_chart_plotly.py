# 1) Data
import pandas as pd, numpy as np
np.random.seed(42)
days = pd.date_range("2025-11-01", periods=12)
valsA = np.cumsum(np.random.randn(12)*2 + 5)
valsB = np.cumsum(np.random.randn(12)*1.5 + 4)
df = pd.DataFrame({"date": days, "Model_A": valsA.round(2), "Model_B": valsB.round(2)})
print(df)

# 2) Matplotlib (static)
import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
plt.plot(df['date'], df['Model_A'], marker='o', label='Model_A')
plt.plot(df['date'], df['Model_B'], marker='o', label='Model_B')
plt.title("Matplotlib — Static Line Plot")
plt.xlabel("Date"); plt.ylabel("Value"); plt.legend(); plt.tight_layout()
plt.show()

# 3) Plotly (interactive)
import plotly.express as px
fig = px.line(df, x='date', y=['Model_A','Model_B'], title="Plotly — Interactive Line Plot")
fig.update_traces(mode="lines+markers")
fig.show()
