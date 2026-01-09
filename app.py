import streamlit as st
import pandas as pd
st.set_page_config(page_title="SocialMediaSucht", page_icon="📱",
layout="wide")
#Styling der App Startseite
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    h1 {
        color: #990057;
    }
</style>
""", unsafe_allow_html=True)

st.title("📱 Social Media Sucht der Studenten")
st.markdown(""" Diese App analysiert die Social Media Sucht der Studenten. Wir nutzen täglich mehrere Stunden Social Media. Ob es nur eine Nachricht ist, die
wir verschicken oder den Feed auf Instagram, den wir folgen.
Vielleicht nutzen wir auch ein bisschen zu viel Social-Media, vor allem in Situationen
wo es nicht passt oder wo wir mehr acht auf andere Dinge geben sollten, wie zum
Beispiel in der Universität.""")

st.markdown("""👈 **Wähle eine Seite in der Sidebar!** """)
@st.cache_data
def load_data():
 return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
df = load_data()




col1, col2, col3 = st.columns(3)
col1.metric("Datensätze", len(df))
col2.metric("Features", len(df.columns))
col3.metric("Durchschnittsalter", round(df['Age'].mean())) # z.B.
st.markdown("""Einen Überblick über die Datensätze!""")
st.dataframe(
    df.head(10),
    use_container_width=True,
    hide_index=True
)


