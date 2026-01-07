import streamlit as st
import pandas as pd
st.title("Daten Exploration")
@st.cache_data
def load_data():
 return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
df = load_data()
