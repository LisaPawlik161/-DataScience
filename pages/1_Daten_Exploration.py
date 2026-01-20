import streamlit as st
import pandas as pd
import plotly.express as px

#voreinstellungen
st.set_page_config(page_title="Daten_Exploration", page_icon="📱",
layout="wide")
#Styling der Seite
st.markdown(
    """
    <style>
    /* Hintergrund der gesamten App */
    .stApp {
        background-color: #FFE4E6;
    }

    /* Hintergrund der Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFD1D6;
    }

    /* Styling der Container/Boxen */
    .block-container {
        background-color: #FFE4E6;
        padding: 3rem;
        border-radius: 20px;
    }

    /* Styling für die Metriken  */
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

st.title("Daten Exploration")

#laden der datenquelle
@st.cache_data
def load_data():
 return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
df = load_data()


# Tabs
tab1, tab2, tab3 = st.tabs([" 📋 Übersicht", " 🛡️ Datenqualität", " 📓 Variablenbeschreibung"])

with tab1:

    st.markdown("#### 🔍 Daten-Vorschau")
    n_rows = st.select_slider("Anzeige-Umfang", options=[5, 10, 20, 50], value=10)
    st.dataframe(df.head(n_rows), use_container_width=True, hide_index=True)
    st.divider()

    st.markdown("#### 🧬 Struktur")
    type_counts = df.dtypes.value_counts().reset_index()
    type_counts.columns = ['Typ', 'Anzahl']
    st.bar_chart(type_counts, x='Typ', y='Anzahl', height=200)


#einblender für details
    with st.expander("Detailierte Spalten-Infos"):
        info_df = pd.DataFrame({
            'Name': df.columns,
            'Typ': df.dtypes.values
        })
        st.table(info_df)


with tab2:
    st.subheader("Analyse der Datenqualität")

    st.markdown("#### 🚫 Fehlende Werte")
    missing_data = df.isnull().sum()
    missing_data = missing_data[missing_data > 0]
    if not missing_data.empty:
        col_miss1, col_miss2 = st.columns([1, 2])
        with col_miss1:
            st.warning(f"Es fehlen insgesamt {missing_data.sum()} Werte.")
            st.write(missing_data)
        with col_miss2:
            st.bar_chart(missing_data)
    else:
        st.success("✅ Perfekt! Keine fehlenden Werte im gesamten Datensatz gefunden.")
    st.divider()


with tab3:
    st.header("Variablenbeschreibung")

    st.markdown("#### Die Sucht-Skala (Addicted Score)")
    st.write("Der Score von **0 bis 10** gibt an, wie stark die psychische Abhängigkeit ausgeprägt ist.")

    # Erstellung (Dictionary)
    risk_data = {
        "Score": ["0.0 - 3.9", "4.0 - 6.9", "7.0 - 10.0"],
        "Risiko": ["Gering", "Moderat", "Hoch"],
        "Symptome": [
            "Kontrollierte Nutzung, kaum Auswirkungen auf den Alltag.",
            "Vernachlässigung von Hobbys, unruhiger Schlaf, längere Online-Zeiten.",
            "Soziale Isolation, Entzugserscheinungen, starke Konflikte im Umfeld."
        ]
    }


    # farben für die tabelle
    def color_risk(val):
        if "Gering" in str(val): return 'background-color: #d4edda'
        if "Moderat" in str(val): return 'background-color: #fff3cd'
        if "Hoch" in str(val): return 'background-color: #f8d7da'
        return ''
    st.table(pd.DataFrame(risk_data).style.applymap(color_risk, subset=['Risiko']))


    st.markdown("#### Allgemeine Beschreibung")

    #dictionary
    full_variables = {
        "Spaltenname": [
            "Academic_Level",
            "Avg_Daily_Usage_Hours", "Most_Used_Platform", "Affects_Academic_Performance",
            "Sleep_Hours_Per_Night", "Mental_Health_Score", "Relationship_Status",
            "Conflicts_Over_Social_Media", "Addicted_Score"
        ],
        "Beschreibung": [
            "Bildungsstand (z.B. Undergraduate, Graduate, High School).",
            "Tägliche Nutzungszeit sozialer Medien in Stunden.",
            "Die Plattform, auf der die meiste Zeit verbracht wird (z.B. Instagram, TikTok).",
            "Gibt an, ob die Nutzung die schulischen/akademischen Leistungen negativ beeinflusst.",
            "Durchschnittliche Anzahl an Schlafstunden pro Nacht.",
            "Selbsteinschätzung der mentalen Gesundheit (1-10).",
            "Beziehungsstatus (Single, In Relationship, Complicated).",
            "Häufigkeit von Streitigkeiten/Konflikten wegen Social Media (0-5).",
            "Der berechnete Sucht-Score (Zielvariable für die Vorhersage)."
        ]

    }
    df_full = pd.DataFrame(full_variables)
    st.dataframe(df_full, hide_index=True, use_container_width=True)


    st.divider()


