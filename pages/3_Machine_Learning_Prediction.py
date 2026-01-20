import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Machine Learning_Prediction", page_icon="📱", layout="wide")

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


st.title("Machine Learning Prediction")
@st.cache_data
def load_data():
    return pd.read_csv('data/Sozial_Media_Sucht_cleaned.csv')
df = load_data()

# Tabs
tab1, tab2 = st.tabs(["🎯 Training", "🔮 Deine Vorhersage"])

#datenformat auch aus beispiel übernommen (also die Grundform und auf meins übertragen)
try:
    df = load_data()

    # nur numerischen Spalten
    feature_cols = ['Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 'Mental_Health_Score']
    target_col = 'Addicted_Score'

    if target_col not in df.columns:
        st.error(f"❌ Ziel-Variable '{target_col}' nicht gefunden!")
        st.stop()

    X = df[feature_cols]
    y = df[target_col]


    # Training
    with tab1:
        st.subheader("Modell Training & Vergleich")
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown("#### Einstellungen")
            # Modell auswählen
            model_choice = st.selectbox(
                "Algorithmus auswählen:",
                ["Linear Regression", "Decision Tree Regressor", "Random Forest Regressor"]
            )
            test_size = st.slider("Test-Set Größe (Anteil):", 0.1, 0.4, 0.2, 0.05)
            train_button = st.button("🚀 Training starten", type="primary")

#training aus den Folien
        with col2:
            if train_button:
                with st.spinner("Modell lernt..."):
                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=test_size, random_state=42
                    )

                    if model_choice == "Linear Regression":
                        model = LinearRegression()
                    elif model_choice == "Decision Tree Regressor":
                        model = DecisionTreeRegressor(max_depth=5, random_state=42)
                    else:
                        model = RandomForestRegressor(n_estimators=100, random_state=42)

                    model.fit(X_train, y_train)

                    #für die vorhersage
                    st.session_state['trained_model'] = model
                    st.session_state['model_name'] = model_choice

                    y_pred = model.predict(X_test)

                    # berechnen
                    r2 = r2_score(y_test, y_pred)
                    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

                    st.success(f"✅ {model_choice} erfolgreich trainiert!")

                    #anzeigen
                    st.markdown("#### 📊 Ergebnisse")
                    m_col1, m_col2, m_col3 = st.columns(3)
                    m_col1.metric("Accuracy (Bestwert 1.0)", f"{r2:.2f}")
                    m_col2.metric("Fehler", f"{rmse:.2f}")
                    m_col3.metric("Trainings-Daten", len(X_train))

                    # Visualisierung:
                    st.markdown("#### 🎯 Vorhersage vs. Realität")
                    fig, ax = plt.subplots(figsize=(10, 5))
                    sns.regplot(x=y_test, y=y_pred, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
                    ax.set_xlabel('Tatsächlicher Sucht-Score')
                    ax.set_ylabel('Vorhergesagter Sucht-Score')
                    ax.set_title(f'Analyse der Vorhersagegenauigkeit ({model_choice})')
                    st.pyplot(fig)

                    # Feature Importance
                    if model_choice != "Linear Regression":
                        st.markdown("#### 🔑 Wichtigste Einflussfaktoren")
                        importances = model.feature_importances_
                        importance_df = pd.DataFrame({
                            'Faktor': feature_cols,
                            'Bedeutung (in %)': importances * 100
                        })
                        # Nach wichtigkeit sortieren
                        importance_df = importance_df.sort_values(by='Bedeutung (in %)', ascending=False)
                        # anzeigen
                        st.table(importance_df.style.format({'Bedeutung (in %)': '{:.1f}%'}))

    #Tab 2
    with tab2:
        st.subheader("📱 Social Media Sucht-Check")
        st.write("Gib deine Daten ein, um eine Schätzung deines Sucht-Scores basierend auf Linearer Regression zu erhalten.")

        # Prüfen ob bereits ein Modell trainiert wurde
        if 'trained_model' not in st.session_state:
            st.warning("⚠️ Bitte trainiere zuerst ein Modell im Tab 'Training & Evaluation'!")
        else:
            st.success("Modell wurde aktiviert.")

            with st.form("user_input"):
                c1, c2 = st.columns(2)
                with c1:
                    in_age = st.number_input("Alter", 10, 100, 20)
                    in_usage = st.slider("Stunden am Handy", 0.0, 24.0, 5.0)
                with c2:
                    in_sleep = st.slider("Stunden Schlaf", 0.0, 12.0, 7.0)
                    in_mental = st.slider("Mental Health (1-10)", 1, 10, 5)

                predict_button = st.form_submit_button("🔮 Wert berechnen")

                if predict_button:
                    # Das gespeicherte Modell aus dem Session State holen
                    model = st.session_state['trained_model']

                    # Vorhersage machen
                    input_data = pd.DataFrame([[in_age, in_usage, in_sleep, in_mental]], columns=feature_cols)
                    res = model.predict(input_data)[0]
                    res = max(0, min(10, res))  # Begrenzung auf 0-10

                    st.markdown("---")
                    st.metric("Geschätzter Addicted Score", f"{res:.2f} / 10")
                    if res > 7:
                        st.error("Klassifizierung: Hohes Suchtrisiko nach Modell-Einschätzung.")
                    elif res > 4:
                        st.warning("Klassifizierung: Moderates Suchtrisiko.")
                    else:
                        st.success("Klassifizierung: Unbedenkliches Nutzungsverhalten.")
                    st.progress(res / 10)

except FileNotFoundError:
    st.error("❌ Datei `Sozial_Media_Sucht_cleaned.csv` nicht gefunden. Bitte prüfen Sie den Dateinamen im Hauptordner!")