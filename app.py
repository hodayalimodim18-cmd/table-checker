import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="בדיקת שולחן", page_icon="🍽️", layout="centered")

st.title("🍽️ בדיקת שולחן")
st.write("בחרו כיצד לחפש: לפי מספר טלפון, לפי שם, או לפי שולחן.")

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
    df['name_clean'] = df['names'].str.lower().str.strip()
    return df

df = load_data(csv_path)

# ----------------------------
# 🔹 בחירת סוג חיפוש
# ----------------------------
search_type = st.selectbox(
    "איך תרצו לחפש?",
    ["לפי טלפון", "לפי שם", "לפי שולחן"]
)

# ----------------------------
# 🔹 חיפוש לפי טלפון
# ----------------------------
if search_type == "לפי טלפון":
    phone = st.text_input("הכניסו מספר טלפון:")

    if st.button("בדיקה"):
        phone_input = phone.strip().replace("-", "").replace(" ", "")
        row = df[df['phone_clean'] == phone_input]

        if row.empty:
            st.warning("מספר הטלפון לא נמצא.")
        else:
            table_num = row.iloc[0]['table']
            st.success(f"✨ השולחן שלך הוא: **{table_num}**")

            st.info("מי יושב איתך בשולחן:")
            st.write(", ".join(df[df['table'] == table_num]['names'].tolist()))

# ----------------------------
# 🔹 חיפוש לפי שם
# ----------------------------
elif search_type == "לפי שם":
    name = st.text_input("הכניסו שם (או חלק ממנו):")

    if st.button("חיפוש"):
        name_clean = name.lower().strip()
        results = df[df['name_clean'].str.contains(name_clean)]

        if results.empty:
            st.warning("לא נמצאו אנשים עם השם הזה.")
        else:
            for _, row in results.iterrows():
                st.success(f"✨ {row['names']} — שולחן **{row['table']}**")
                
                st.info("מי יושב איתו/ה:")
                st.write(", ".join(df[df['table'] == row['table']]['names'].tolist()))

# ----------------------------
# 🔹 פילטור לפי שולחן
# ----------------------------
elif search_type == "לפי שולחן":
    tables = sorted(df['table'].unique())
    selected_table = st.selectbox("בחרו שולחן:", tables)

    st.write(f"✨ אנשים שיושבים בשולחן **{selected_table}**:")
    st.info(", ".join(df[df['table'] == selected_table]['names'].tolist()))
