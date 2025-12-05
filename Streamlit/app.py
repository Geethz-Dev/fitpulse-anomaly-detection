import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------------
# Page Configuration
# ------------------------------------------------------
st.set_page_config(
    page_title="FitPulse Dashboard",
    layout="wide"
)

st.title("FitPulse Health Metrics Dashboard")
st.write("This dashboard provides key insights from the FitPulse dataset using bar, line and scatter charts.")

# ------------------------------------------------------
# Load Dataset
# ------------------------------------------------------
file_path = r"C:\Users\geeth\OneDrive\Desktop\fitpulse-anomaly-detection\original_files\fitpulse_data.csv"
df = pd.read_csv(file_path)

# Ensure correct types
df["gender"] = df["gender"].astype(str)

# ------------------------------------------------------
# Chart 1: Average Heart Rate by Age Group (Bar Chart)
# ------------------------------------------------------
st.subheader("Average Heart Rate by Age Group")

age_bins = [0, 20, 30, 40, 50, 60, 100]
age_labels = ["<20", "20–29", "30–39", "40–49", "50–59", "60+"]

df["age_group"] = pd.cut(df["age"], bins=age_bins, labels=age_labels, right=False)

hr_by_age_group = (
    df.groupby("age_group")["heart_rate"]
    .mean()
    .reset_index()
    .dropna()
)

fig_bar = px.bar(
    hr_by_age_group,
    x="age_group",
    y="heart_rate",
    title="Average Heart Rate by Age Group",
    labels={"age_group": "Age Group", "heart_rate": "Average Heart Rate"}
)

fig_bar.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Average Heart Rate",
    bargap=0.4,      # slightly wider gap -> visually thinner bars
    height=400
)

st.plotly_chart(fig_bar, use_container_width=True)

# ------------------------------------------------------
# Chart 2: Average Steps by Age (Line Chart)
# ------------------------------------------------------
st.subheader("Average Steps by Age")

steps_by_age = (
    df.groupby("age")["steps"]
    .mean()
    .reset_index()
    .sort_values("age")
)

fig_line = px.line(
    steps_by_age,
    x="age",
    y="steps",
    markers=True,
    title="Average Steps Across Age",
    labels={"age": "Age", "steps": "Average Steps"}
)

fig_line.update_layout(
    xaxis_title="Age",
    yaxis_title="Average Steps",
    height=400
)

st.plotly_chart(fig_line, use_container_width=True)

# ------------------------------------------------------
# Chart 3: Heart Rate vs Pulse (Scatter Plot)
# ------------------------------------------------------
st.subheader("Heart Rate vs Pulse")

fig_scatter = px.scatter(
    df,
    x="heart_rate",
    y="pulse",
    color="gender",
    size="blood_points",
    hover_data=["customer_id", "steps", "age"],
    title="Heart Rate vs Pulse",
    labels={"heart_rate": "Heart Rate", "pulse": "Pulse"}
)

fig_scatter.update_layout(
    xaxis_title="Heart Rate",
    yaxis_title="Pulse",
    height=400
)

st.plotly_chart(fig_scatter, use_container_width=True)

# ------------------------------------------------------
# Section 4: High-Risk / Anomaly Users Table
# ------------------------------------------------------
st.subheader("Detected Anomaly Records")

if "anomaly_label" in df.columns:
    anomalies = df[df["anomaly_label"] == 1]

    st.write(f"Total anomalies detected: {len(anomalies)}")

    if not anomalies.empty:
        st.dataframe(
            anomalies[
                [
                    "customer_id",
                    "heart_rate",
                    "pulse",
                    "steps",
                    "gender",
                    "age",
                    "blood_points",
                    "anomaly_label"
                ]
            ].reset_index(drop=True)
        )
    else:
        st.write("No anomaly records detected.")
else:
    st.write("The dataset does not contain an 'anomaly_label' column.")
