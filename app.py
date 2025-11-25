import streamlit as st
import pandas as pd

st.set_page_config(page_title="בדיקת שולחן", page_icon="🍽️", layout="centered")

# טוענים את הטבלה
@st.cache_data
def load_data():
    return pd.read_csv("guests.csv")

df = load_data()

st.title("🍽️ בדיקת שולחן לפי מספר טלפון")
st.write("הכניסו את מספר הטלפון כפי שנרשם במערכת (ללא רווחים).")

phone = st.text_input("מספר טלפון:")

if st.button("בדיקה"):
    if phone.strip() == "":
        st.error("נא להכניס מספר טלפון.")
    else:
        result = df[df["phone"] == phone]
        if result.empty:
            st.warning("מספר הטלפון לא נמצא במערכת.")
        else:
            table_num = int(result.iloc[0]["table"])
            st.success(f"✨ השולחן שלך הוא: **{table_num}**")
