import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="SocialMediaSucht", page_icon="📱",
layout="wide")

st.title("Visualisierungen")
@st.cache_data
def load_data():
    return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
df = load_data()

#Tabs
tab1, tab2, tab3 = st.tabs(["📊 1", "📈 2", "🔢 3"])

with tab1:
    st.subheader("1")

with tab2:
    st.subheader("Welche Plattform wird am meisten genutzt?")
    fig, ax = plt.subplots(figsize=(12, 6))
    for category in df['Gender'].unique():
        subset = df[df['Gender'] == category]
        plt.scatter(subset['Most_Used_Platform'], subset['Sleep_Hours_Per_Night'], label=category, alpha=0.6)
    plt.title('Platform in Abhängigkeit des Geschlechts und der Anzahl der Schlafstunden')
    plt.xlabel('Meist genutzte Plattform')
    plt.ylabel('Schlafstunden pro Nacht')
    plt.legend()
    st.pyplot(fig)

with tab3:
    st.subheader("3")



