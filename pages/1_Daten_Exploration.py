import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="SocialMediaSucht", page_icon="📱",
layout="wide")
st.title("Daten Exploration")
@st.cache_data
def load_data():
 return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
df = load_data()
# Tabs
tab1, tab2, tab3 = st.tabs(["📋 Übersicht", "🔍 Datenqualität", "📊 Statistiken"])
with tab1:
    st.subheader("Dataset Übersicht")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("#### Daten-Vorschau")
        n_rows = st.slider("Anzahl Zeilen", 5, 50, 10)
        st.dataframe(df.head(n_rows), use_container_width=True)

    with col2:
        st.markdown("#### Info")
        st.write(f"**Spalten:** {len(df.columns)}")
        st.write(f'**Datentypen:**')
        st.dataframe(pd.DataFrame({
            'Typ': df.dtypes,
            'Count': df.count()
        }))

with tab2:
    st.subheader("Datenqualität")
    st.markdown("Auf dieser Seite können sie sehen wie die Qualität der Daten ist.")

    st.markdown("Fehlende Werte:")
    missing_data = df.isnull().sum()
    st.bar_chart(missing_data)
    st.write("Alle Daten sind vollständig und somit fehlen keine Werte ")

