import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime
today = datetime.today().strftime("%Y-%m-%d")
if os.path.exists("habits.csv"):
    df_habits = pd.read_csv("habits.csv")
else:
    
    df_habits = pd.DataFrame(columns=["habit", "date"])
try: 
    user = pd.read_csv("data.csv")
    username = user["username"].iloc[0]
except:
    username="User"

#dashboard
st.title("🚀 My Discipline Dashboard")
st.subheader(f"Welcome back {username}")
st.divider()

#Partie habits

st.subheader("Daily Habits")
with st.expander("➕ Add a new habit"):
    new_habit = st.text_input("What is your new habit?")
    if st.button("Save Habit"):
        if new_habit != "":
            new_data = pd.DataFrame({"habit": [new_habit], "date": [today]})
            df_habits = pd.concat([df_habits, new_data], ignore_index=True)
            df_habits.to_csv("habits.csv", index=False)
            st.success("Habit added!")
            st.rerun()
if "date" in df_habits.columns:
    today_habits_df = df_habits[df_habits["date"] == today]
else:
    today_habits_df = df_habits
completed = 0#
total = len(today_habits_df)
if total > 0:
    for index, row in today_habits_df.iterrows():
        with st.container(border=True):
            if st.checkbox(f"**{row['habit']}**", key=f"habit_{index}"):
                completed += 1
else:
    st.info("No habits added for today yet.")

# partie GOALS
st.divider()
st.header("Long-term Goals")

if not os.path.exists("goals.csv"):
    pd.DataFrame(columns=["goal"]).to_csv("goals.csv", index=False)

with st.container(border=True):
    new_goal = st.text_input("New Goal target:")
    if st.button("Add Goal"):
        if new_goal != "":
            df_g = pd.read_csv("goals.csv")
            df_g.loc[len(df_g)] = [new_goal]
            df_g.to_csv("goals.csv", index=False)
            st.rerun()

df_goals = pd.read_csv("goals.csv")
for goal in df_goals["goal"]:
    st.markdown(f"🎯 {goal}")

# partie score 
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("Consistency Score")
    if total > 0:
        score = (completed / total) * 100
    else:
        score = 0
    st.metric(label="Today's Progress", value=f"{int(score)}%", delta=f"{completed}/{total} tasks")
    st.progress(score / 100)
# partie motivation
with col2:
    st.subheader("Daily Motivation")
    quotes = [
        "Show up for yourself everyday.",
        "Do it for your future self.",
        "Upgrade your life in silence.",
        "Out of suffering have emerged the strongest souls.",
        "It’s the quality of one’s conviction that determines success.",
        "It's on you to get to where you want to be.",
        "Dream big, work hard, stay focused.",
        "Your future is created by what you do today, not tomorrow."
    ]
    with st.chat_message("assistant"):
        st.write(random.choice(quotes))