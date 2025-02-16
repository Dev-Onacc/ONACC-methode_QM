import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Fonction de correction par Quantile Mapping
def quantile_mapping(simulated, observed):
    quantiles = stats.rankdata(simulated) / (len(simulated) + 1)
    sorted_obs = np.sort(observed)
    corrected_values = np.interp(quantiles, np.linspace(0, 1, len(sorted_obs)), sorted_obs)
    return corrected_values

# Fonction pour calculer les métriques de performance
def calculate_performance_metrics(observed, simulated, corrected):
    rmse_sim = np.sqrt(mean_squared_error(observed, simulated))
    rmse_corr = np.sqrt(mean_squared_error(observed, corrected))
    bias_sim = np.mean(simulated - observed)
    bias_corr = np.mean(corrected - observed)
    return rmse_sim, rmse_corr, bias_sim, bias_corr

# Interface Streamlit
st.image("logo.png", width=80) 
st.title("Correction des Biais Climatiques par Quantile Mapping")

# Téléversement des fichiers
st.sidebar.header("Téléversement des données")
uploaded_sim = st.sidebar.file_uploader("Importer les données simulées (.xlsx)", type="xlsx")
uploaded_obs = st.sidebar.file_uploader("Importer les données observées (.xlsx)", type="xlsx")

if uploaded_sim and uploaded_obs:
    # Chargement des fichiers
    df_sim = pd.read_excel(uploaded_sim)
    df_obs = pd.read_excel(uploaded_obs)

    # Vérification des colonnes nécessaires
    required_columns = ["date", "temperature_min", "temperature_max", "precipitation"]
    if not all(col in df_sim.columns for col in required_columns) or not all(col in df_obs.columns for col in required_columns):
        st.error(f"Les fichiers doivent contenir les colonnes suivantes : {required_columns}")
    else:
        # Convertir la colonne 'date' au format datetime
        df_sim["date"] = pd.to_datetime(df_sim["date"])
        df_obs["date"] = pd.to_datetime(df_obs["date"])

        # Sélection de l'intervalle de dates
        min_date = df_sim["date"].min()
        max_date = df_sim["date"].max()
        selected_dates = st.sidebar.date_input("Sélectionner la période", [min_date, max_date], min_value=min_date, max_value=max_date)

        # Convertir les dates sélectionnées en datetime64[ns]
        selected_dates = [pd.to_datetime(date) for date in selected_dates]

        # Filtrer les données en fonction de la période sélectionnée
        filtered_sim = df_sim[(df_sim["date"] >= selected_dates[0]) & (df_sim["date"] <= selected_dates[1])]
        filtered_obs = df_obs[(df_obs["date"] >= selected_dates[0]) & (df_obs["date"] <= selected_dates[1])]

        # Correction des biais pour chaque variable
        corrected_data = filtered_sim.copy()
        for variable in ["temperature_min", "temperature_max", "precipitation"]:
            simulated = filtered_sim[variable].values
            observed = filtered_obs[variable].values
            corrected_values = quantile_mapping(simulated, observed)
            corrected_data[f"{variable}_corrige"] = corrected_values  

        # Affichage des statistiques
        st.write("### Statistiques avant et après correction")
        stats_data = {
            "Variable": ["Température Min", "Température Max", "Précipitation"],
            "Moyenne Observée": [np.mean(filtered_obs["temperature_min"]), np.mean(filtered_obs["temperature_max"]), np.mean(filtered_obs["precipitation"])],
            "Moyenne Simulée": [np.mean(filtered_sim["temperature_min"]), np.mean(filtered_sim["temperature_max"]), np.mean(filtered_sim["precipitation"])],
            "Moyenne Corrigée": [np.mean(corrected_data["temperature_min_corrige"]), np.mean(corrected_data["temperature_max_corrige"]), np.mean(corrected_data["precipitation_corrige"])]
        }
        st.dataframe(pd.DataFrame(stats_data))

        # Calcul des métriques de performance
        rmse_sim, rmse_corr, bias_sim, bias_corr = calculate_performance_metrics(filtered_obs["temperature_min"], filtered_sim["temperature_min"], corrected_data["temperature_min_corrige"])
        st.write(f"### Performances des corrections de biais")
        st.write(f"RMSE - Température Min (Simulée): {rmse_sim:.2f}")
        st.write(f"RMSE - Température Min (Corrigée): {rmse_corr:.2f}")
        st.write(f"Biais - Température Min (Simulée): {bias_sim:.2f}")
        st.write(f"Biais - Température Min (Corrigée): {bias_corr:.2f}")

        # Graphique Température Minimale
        st.write("### Température Minimale")
        fig_temp_min = go.Figure()
        fig_temp_min.add_trace(go.Scatter(x=filtered_sim["date"], y=filtered_obs["temperature_min"], mode='lines', name="Observée", line=dict(color='#2FB0FE')))
        fig_temp_min.add_trace(go.Scatter(x=filtered_sim["date"], y=filtered_sim["temperature_min"], mode='lines', name="Simulée", line=dict(color='#FEB56A')))
        fig_temp_min.add_trace(go.Scatter(x=filtered_sim["date"], y=corrected_data["temperature_min_corrige"], mode='lines', name="Corrigée", line=dict(color='#8DE285')))
        fig_temp_min.update_layout(title="Évolution de la Température Minimale", xaxis_title="Date", yaxis_title="Température (°C)")
        st.plotly_chart(fig_temp_min, use_container_width=True)

        # Graphique Température Maximale
        st.write("### Température Maximale")
        fig_temp_max = go.Figure()
        fig_temp_max.add_trace(go.Scatter(x=filtered_sim["date"], y=filtered_obs["temperature_max"], mode='lines', name="Observée", line=dict(color='#2FB0FE')))
        fig_temp_max.add_trace(go.Scatter(x=filtered_sim["date"], y=filtered_sim["temperature_max"], mode='lines', name="Simulée", line=dict(color='#FEB56A')))
        fig_temp_max.add_trace(go.Scatter(x=filtered_sim["date"], y=corrected_data["temperature_max_corrige"], mode='lines', name="Corrigée", line=dict(color='#8DE285')))
        fig_temp_max.update_layout(title="Évolution de la Température Maximale", xaxis_title="Date", yaxis_title="Température (°C)")
        st.plotly_chart(fig_temp_max, use_container_width=True)

        # Graphique Précipitations
        st.write("### Précipitations")
        fig_prec = go.Figure()
        fig_prec.add_trace(go.Scatter(x=filtered_sim["date"], y=filtered_obs["precipitation"], mode='lines', name="Observée", line=dict(color='#2FB0FE')))
        fig_prec.add_trace(go.Scatter(x=filtered_sim["date"], y=filtered_sim["precipitation"], mode='lines', name="Simulée", line=dict(color='#FEB56A')))
        fig_prec.add_trace(go.Scatter(x=filtered_sim["date"], y=corrected_data["precipitation_corrige"], mode='lines', name="Corrigée", line=dict(color='#8DE285')))
        fig_prec.update_layout(title="Évolution des Précipitations", xaxis_title="Date", yaxis_title="Précipitation (mm)")
        st.plotly_chart(fig_prec, use_container_width=True)

        # Carte de chaleur des écarts pour la température minimale
        st.write("### Carte de Chaleur des Écarts de Température Minimale")
        diff_temp_min = corrected_data["temperature_min_corrige"] - filtered_obs["temperature_min"]
        fig_heatmap_min = plt.figure(figsize=(8, 6))
        sns.heatmap(diff_temp_min.values.reshape(-1, 1), cmap="coolwarm", cbar_kws={'label': 'Écart Température Min (°C)'})
        st.pyplot(fig_heatmap_min)

        # Bouton de téléchargement
        st.write("### Télécharger les données corrigées")
        corrected_file = corrected_data.to_excel("donnees_corrigees.xlsx", index=False, engine='openpyxl')
        with open("donnees_corrigees.xlsx", "rb") as f:
            st.download_button(
                label="Télécharger le fichier corrigé",
                data=f,
                file_name="donnees_corrigees.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
