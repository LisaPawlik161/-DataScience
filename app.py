import streamlit as st
import pandas as pd
st.set_page_config(page_title="SocialMediaSucht", page_icon="📱",
layout="wide")
st.title("📱 Social Media Sucht der Studenten")
st.markdown(""" Diese App analysiert die Social Media Sucht der Studenten.""")

st.markdown("""👈 **Wähle eine Seite im Sidebar!** """)
@st.cache_data
def load_data():
 return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
df = load_data()



st.markdown("""Alle wichtigen Infos auf einem Blick""")

col1, col2, col3 = st.columns(3)
col1.metric("Datensätze", len(df))
col2.metric("Features", len(df.columns))
col3.metric("Durchschnittsalter", round(df['Age'].mean())) # z.B.
st.dataframe(df.head())


