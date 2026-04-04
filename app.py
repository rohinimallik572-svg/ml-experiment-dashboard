st.subheader("🤖 AI Experiment Assistant")

question = st.text_input("Ask a question about your experiment runs")

if question:
    best_acc = data.loc[data["accuracy"].idxmax()]
    fastest = data.loc[data["time"].idxmin()]
    lowest_loss = data.loc[data["loss"].idxmin()]

    response = ""

    if "best" in question.lower():
        response = f"Run {best_acc['run_id']} is the best overall because it has the highest accuracy ({best_acc['accuracy']}) and relatively low loss ({best_acc['loss']})."

    elif "fastest" in question.lower():
        response = f"Run {fastest['run_id']} is the fastest with runtime {fastest['time']}. However, its accuracy is {fastest['accuracy']}."

    elif "loss" in question.lower():
        response = f"Run {lowest_loss['run_id']} has the lowest loss ({lowest_loss['loss']}), indicating better model fit."

    elif "why" in question.lower():
        response = f"{best_acc['run_id']} performs best because it balances high accuracy ({best_acc['accuracy']}), low loss ({best_acc['loss']}), and efficient runtime ({best_acc['time']})."

    else:
        response = "Ask things like: 'Which run is best?', 'Why is a run better?', 'Which is fastest?'"

    st.success(response)
