import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="בדיקת שולחן", page_icon="🍽️", layout="centered")

st.title("🍽️ בדיקת שולחן")
st.write("בחרו כיצד לחפש: לפי מספר טלפון, לפי שם, או לפי שולחן.")

df = pd.read_csv("guests.csv", dtype={"phone": "string"})
df['phone'] = df['phone'].astype(str).str.zfill(10)


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
    df['phone'] = (
    df['phone']
    .astype(str)
    .str.replace(" ", "")
    .str.replace("-", "")
    .str.strip()
)

    phone_input = st.text_input("הכניסו מספר טלפון:")

    if st.button("בדיקה"):
        # phone_input = phone.strip().replace("-", "").replace(" ", "")
        row = df[df['phone'] == phone_input]

        if row.empty:
            st.warning("מספר הטלפון לא נמצא.")
        else:
            table_num = row.iloc[0]['table']
            st.success(f"✨ השולחן שלך הוא: **{table_num}**")

            # st.info("מי יושב איתך בשולחן:")
            # st.write(", ".join(df[df['table'] == table_num]['names'].tolist()))

# ----------------------------
# 🔹 חיפוש לפי שם
# ----------------------------
elif search_type == "לפי שם":
    name = st.text_input("הכניסו שם מלא:")

    if st.button("חיפוש"):
        # name_clean = name.lower().strip()
        results = df[df['name'].str.contains(name)]

        if results.empty:
            st.warning("לא נמצאו אנשים עם השם הזה.")
        # else:
        #     for _, row in results.iterrows():
        #         st.success(f"✨ {row['names']} — שולחן **{row['table']}**")
                
                # st.info("מי יושב איתו/ה:")
                # st.write(", ".join(df[df['table'] == row['table']]['names'].tolist()))

# ----------------------------
# 🔹 פילטור לפי שולחן
# ----------------------------
elif search_type == "לפי שולחן":
    tables = sorted(df['table'].unique())
    selected_table = st.selectbox("בחרו שולחן:", tables)

    st.write(f"✨ אנשים שיושבים בשולחן **{selected_table}**:")
    st.info(", ".join(df[df['table'] == selected_table]['names'].tolist()))
