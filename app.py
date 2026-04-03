import streamlit as st
import pandas as pd

st.set_page_config(page_title="ML Dashboard", layout="wide")

st.title("🚀 ML Experiment Tracker")

data = pd.read_csv("runs.csv")

col1, col2, col3 = st.columns(3)
col1.metric("Best Accuracy", data["accuracy"].max())
col2.metric("Lowest Loss", data["loss"].min())
col3.metric("Fastest Time", data["time"].min())

st.divider()

run_filter = st.selectbox("Select Run", data["run_id"])
filtered = data[data["run_id"] == run_filter]

st.subheader("🔍 Selected Run Details")
st.dataframe(filtered)

st.subheader("📊 Experiment Results")
st.dataframe(data)

st.subheader("📈 Accuracy per Run")
st.line_chart(data.set_index("run_id")["accuracy"])

best = data.loc[data["accuracy"].idxmax()]

st.subheader("🏆 Best Run Details")
st.json(best.to_dict())


