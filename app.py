import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="בדיקת שולחן", page_icon="🍽️", layout="centered")

st.title("🍽️ בדיקת שולחן לפי מספר טלפון")
st.write("הכניסו את מספר הטלפון כפי שנרשם במערכת (ללא רווחים).")

# קובץ CSV יחסית למיקום של app.py
BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "guests.csv"

# בדיקה אם הקובץ קיים
if not csv_path.exists():
    st.error(f"קובץ guests.csv לא נמצא בנתיב: {csv_path}")
    st.stop()

# טעינת הנתונים
@st.cache_data
def load_data(path):
    # חובה לקרוא את עמודת הטלפון כמחרוזת כדי לא לאבד את האפס המוביל
    df = pd.read_csv(path, dtype={"phone": str})
    df['phone_clean'] = df['phone'].str.replace("-", "").str.replace(" ", "")
    return df

df = load_data(csv_path)

# קלט מהמשתמש
phone = st.text_input("מספר טלפון:")

if st.button("בדיקה"):
    if phone.strip() == "":
        st.error("נא להכניס מספר טלפון.")
    else:
        phone_input = phone.strip().replace("-", "").replace(" ", "")
        result = df[df['phone_clean'] == phone_input]

        if result.empty:
            st.warning("מספר הטלפון לא נמצא במערכת.")
        else:
            table_num = int(result.iloc[0]["table"])
            st.success(f"✨ השולחן שלך הוא: **{table_num}**")
