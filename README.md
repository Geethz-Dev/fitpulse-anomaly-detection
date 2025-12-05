# FitPulse – Health Metrics Analysis & Dashboard

FitPulse is a data analytics project that focuses on understanding user activity and biometric patterns using a structured health dataset. The project covers data preprocessing, exploratory analysis, anomaly identification, and the creation of an interactive Streamlit dashboard for visual reporting.

🔍 Project Overview
The goal of FitPulse is to analyze daily activity and health indicators such as steps, heart rate, pulse, age, and gender. The project includes:

- Cleaning and preparing the dataset  
- Generating insights using NumPy, Pandas, and visualization libraries  
- Building a regression model to study relationships between variables  
- Detecting anomalies using predefined labels  
- Presenting the results through a simple and interactive dashboard

📊 Streamlit Dashboard Features
The dashboard provides the following visual insights:

1. **Bar Chart – Average Heart Rate by Age Group**  
2. **Line Chart – Average Steps by Age**  
3. **Scatter Plot – Heart Rate vs Pulse**  
4. **Table – High-Risk / Anomaly Users**

These visualizations help in identifying health trends and potential risk users.

📂 Dataset Description
The dataset includes the following attributes:

- `customer_id`  
- `age`  
- `gender`  
- `steps`  
- `heart_rate`  
- `pulse`  
- `blood_points`  
- `anomaly_label` (0 = normal, 1 = anomaly)

▶️ Running the Streamlit Dashboard
Install dependencies:

```bash
pip install -r Streamlit/requirements.txt
