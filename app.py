{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2b95844-cd7c-4261-a389-7e1d364db3e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "st.set_page_config(page_title=\"בדיקת שולחן\", page_icon=\"🍽️\", layout=\"centered\")\n",
    "\n",
    "# טוענים את הטבלה\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    return pd.read_csv(\"guests.csv\")\n",
    "\n",
    "df = load_data()\n",
    "\n",
    "st.title(\"🍽️ בדיקת שולחן לפי מספר טלפון\")\n",
    "st.write(\"הכניסו את מספר הטלפון כפי שנרשם במערכת (ללא רווחים).\")\n",
    "\n",
    "phone = st.text_input(\"מספר טלפון:\")\n",
    "\n",
    "if st.button(\"בדיקה\"):\n",
    "    if phone.strip() == \"\":\n",
    "        st.error(\"נא להכניס מספר טלפון.\")\n",
    "    else:\n",
    "        result = df[df[\"phone\"] == phone.strip()]\n",
    "        if result.empty:\n",
    "            st.warning(\"מספר הטלפון לא נמצא במערכת.\")\n",
    "        else:\n",
    "            table_num = int(result.iloc[0][\"table\"])\n",
    "            st.success(f\"✨ השולחן שלך הוא: **{table_num}**\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.11",
   "language": "python",
   "name": "py311"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
