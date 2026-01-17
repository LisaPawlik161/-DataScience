import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="SocialMediaSucht", page_icon="📱",
layout="wide")
#Styling der Seite
st.markdown(
    """
    <style>
    /* Hintergrund der gesamten App */
    .stApp {
        background-color: #FFE4E6;
    }

    /* Hintergrund der Sidebar (falls vorhanden) */
    [data-testid="stSidebar"] {
        background-color: #FFD1D6;
    }

    /* Styling der Container/Boxen */
    .block-container {
        background-color: #FFE4E6;
        padding: 3rem;
        border-radius: 20px;
    }

    /* Styling für die Metriken (Zahlen-Boxen) */
    [data-testid="stMetricValue"] {
        color: #E11D48;
    }

    /* Styling für Tab-Texte */
    .stTabs [data-baseweb="tab"] {
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Visualisierungen")
@st.cache_data
def load_data():
    return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
df = load_data()

#Tabs
tab1, tab2, tab3 = st.tabs(["📊 1", "📈 2", "🔢 3"])

with tab1:
    st.subheader("Verteilungsanalyse nach Geschlecht")

    col1, col2 = st.columns([1, 3])

    with col1:
        # 1. Numerisches Feature auswählen
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        if 'Student_ID' in numeric_cols:
            numeric_cols.remove('Student_ID')

        selected_feature = st.selectbox("Feature wählen:", numeric_cols)

        # 2. Einfache Checkbox für die Aufteilung
        show_by_gender = st.checkbox("Nach Geschlecht aufteilen")

    with col2:
        # Plot erstellen
        fig, ax = plt.subplots(figsize=(10, 5))

        if show_by_gender:
            # Aufteilung nach Male / Female (oder was im Datensatz steht)
            for gender in df['Gender'].unique():
                subset = df[df['Gender'] == gender]
                ax.hist(subset[selected_feature], alpha=0.5, label=gender, bins=20)
            ax.legend(title="Geschlecht")
            ax.set_title(f'Vergleich der Geschlechter: {selected_feature}')
        else:
            # Einfaches Histogramm für alle
            ax.hist(df[selected_feature], bins=20, color='skyblue', edgecolor='black')
            ax.set_title(f'Gesamtverteilung: {selected_feature}')

        ax.set_xlabel(selected_feature)
        ax.set_ylabel('Häufigkeit (Anzahl Studenten)')

        st.pyplot(fig)


with tab2:
    st.subheader("Plattformnutzung nach Geschlecht und Schlaf")
    st.markdown("""
        Diese Grafik untersucht, ob bestimmte Plattformen (wie TikTok oder Instagram) 
        mit einer geringeren Schlafdauer korrelieren und ob es Unterschiede zwischen 
        den Geschlechtern gibt.""")

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
    st.subheader("Der Zusammenhang zwischen Schlaf und Sucht")
    st.markdown("""Einer der wichtigsten Indikatoren für Social Media Sucht ist der Schlafmangel. 
        Die rote Linie zeigt den statistischen Trend: **Weniger Schlaf führt fast immer zu einem höheren Sucht-Score.""")
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.scatter(df['Sleep_Hours_Per_Night'],
                df['Addicted_Score'],
                alpha=0.5,
                s=30)

    sns.regplot(x='Sleep_Hours_Per_Night',
                y='Addicted_Score',
                data=df,
                scatter=False,
                color='red',
                line_kws={'linewidth': 2, 'linestyle': '--'})

    plt.title('Addicted_Score vs. Sleep_Hours_Per_Night')
    plt.xlabel('Sleep_Hours_Per_Night')
    plt.ylabel('Addicted Score')
    plt.grid(True, alpha=0.3)

    st.pyplot(fig)



