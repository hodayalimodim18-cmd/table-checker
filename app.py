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
    df = pd.read_csv(path, dtype={"phone": str})
    df['phone_clean'] = df['phone'].str.replace("-", "").str.replace(" ", "")
    return df

df = load_data(csv_path)

# יצירת מילון מהיר לחיפוש
phone_to_data = df.set_index('phone_clean')[['table', 'names']].to_dict('index')

# קלט מהמשתמש
phone = st.text_input("מספר טלפון:")

if st.button("בדיקה"):
    phone_input = phone.strip().replace("-", "").replace(" ", "")
    data = phone_to_data.get(phone_input)
    
    if data:
        table_num = data['table']
        names = data['names']
        st.success(f"✨ השולחן שלך הוא: **{table_num}**")
        st.info(f"אנשים שיושבים איתך באותו שולחן: {names}")
    else:
        st.warning("מספר הטלפון לא נמצא במערכת.")
