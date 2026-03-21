import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime#pour ajouter les dates
today = datetime.today().strftime("%Y-%m-%d")
if os.path.exists("habits.csv"):
    df_habits = pd.read_csv("habits.csv")
else:
    # Si le fichier n'existe pas, on crée un DataFrame vide avec les bonnes colonnes
    df_habits = pd.DataFrame(columns=["habit", "date"])
    
user = pd.read_csv("data.csv")
username = user["username"].iloc[0]

#dashboard
st.title("🚀 My Discipline Dashboard")
st.subheader(f"Welcome back {username}")
st.divider()#pour separer

#Partie habits

st.subheader("Daily Habits")
with st.expander("➕ Add a new habit"):
    new_habit = st.text_input("What is your new habit?")
    if st.button("Save Habit"):
        if new_habit != "":
            # On crée la nouvelle ligne
            new_data = pd.DataFrame({"habit": [new_habit], "date": [today]})
            # On l'ajoute au DataFrame existant
            df_habits = pd.concat([df_habits, new_data], ignore_index=True)
            # On sauvegarde
            df_habits.to_csv("habits.csv", index=False)
            st.success("Habit added!")
            st.rerun()
if "date" in df_habits.columns:
    today_habits_df = df_habits[df_habits["date"] == today]
else:
    today_habits_df = df_habits
completed = 0#
total = len(today_habits_df) #pour la longueur
# Affichage des habits avec style
if total > 0:
    for index, row in today_habits_df.iterrows():
        # AJOUT : Un petit container avec bordure pour chaque habit
        with st.container(border=True):
            if st.checkbox(f"**{row['habit']}**", key=f"habit_{index}"):
                completed += 1
else:
    st.info("No habits added for today yet.")

# 3. GESTION DES GOALS
st.divider()
st.header("Long-term Goals")

if not os.path.exists("goals.csv"):
    pd.DataFrame(columns=["goal"]).to_csv("goals.csv", index=False)

with st.container(border=True):
    new_goal = st.text_input("New Goal target:")
    if st.button("Add Goal"):
        if new_goal != "":
            df_g = pd.read_csv("goals.csv")
            # AJOUT : Utilisation de loc pour ajouter proprement
            df_g.loc[len(df_g)] = [new_goal]
            df_g.to_csv("goals.csv", index=False)
            st.rerun()

df_goals = pd.read_csv("goals.csv")
for goal in df_goals["goal"]:
    st.markdown(f"🎯 {goal}")

# 4. SCORE ET ANALYTICS
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("Consistency Score")
    if total > 0:
        score = (completed / total) * 100
    else:
        score = 0
    
    # AJOUT : Utilisation de st.metric pour un look plus "App"
    st.metric(label="Today's Progress", value=f"{int(score)}%", delta=f"{completed}/{total} tasks")
    st.progress(score / 100)

with col2:
    # 5. PARTIE MOTIVATION (Améliorée)
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
    # AJOUT : Utilisation de st.chat_message pour un style "Assistant"
    with st.chat_message("assistant"):
        st.write(random.choice(quotes))