import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
st.title("Visualisierungen")
@st.cache_data
def load_data():
    return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
    df = load_data()