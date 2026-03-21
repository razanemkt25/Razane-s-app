import streamlit as st
import pandas as pd
st.set_page_config(page_title="Self Discipline & Consistency Assistant App")
st.title(" Your journey starts here !")
st.image ("motive.png")
name=st.text_input("Enter your name")
username=st.text_input("Enter your username")
if st.button("Click here"):
    df=pd.DataFrame([[name,username]],columns=["name","username"])
    df.to_csv("data.csv",index=False)
    st.success(f"Welcome {name}!")
    st.switch_page("pages/dashboard.py")
else:
        st.error("Please fill in both fields")

