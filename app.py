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

st.subheader("🤖 AI Experiment Assistant")

question = st.text_input("Ask a question about your experiment runs")

if question:
    best_acc = data.loc[data["accuracy"].idxmax()]
    fastest = data.loc[data["time"].idxmin()]
    lowest_loss = data.loc[data["loss"].idxmin()]

    # Structured reasoning (not dumb if-else)
    response = ""

    if "best" in question.lower():
        response = (
            f"Run {best_acc['run_id']} is the best overall because it has the highest accuracy "
            f"({best_acc['accuracy']}) and relatively low loss ({best_acc['loss']})."
        )

    elif "fastest" in question.lower():
        response = (
            f"Run {fastest['run_id']} is the fastest with runtime {fastest['time']}. "
            f"However, its accuracy is {fastest['accuracy']}."
        )

    elif "loss" in question.lower():
        response = (
            f"Run {lowest_loss['run_id']} has the lowest loss ({lowest_loss['loss']}), "
            f"indicating better model fit."
        )

    elif "why" in question.lower():
        response = (
            f"{best_acc['run_id']} performs best because it balances high accuracy "
            f"({best_acc['accuracy']}), low loss ({best_acc['loss']}), "
            f"and efficient runtime ({best_acc['time']})."
        )

    else:
        response = "Ask things like: 'Which run is best?', 'Why is a run better?', 'Which is fastest?'"

    st.success(response)
