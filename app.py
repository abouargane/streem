import streamlit as st
import pandas as pd

st.title("Calculateur de Vitesse et Distance")

# Entrée pour la vitesse de base
v_base = st.number_input("Entrez la vitesse de base (km/h)", min_value=0.0, value=100.0)
percentage = st.number_input("Entrez le pourcentage (%)", min_value=0.0, max_value=100.0, value=70.0)

# Calcul des vitesses
v_p = (percentage / 100) * v_base
v_m_min = (v_p * 1000) / 60
v_m_s = v_m_min / 60

st.write(f"Vitesse calculée : {v_p:.2f} km/h")
st.write(f"Vitesse en mètres par minute : {v_m_min:.2f}")
st.write(f"Vitesse en mètres par seconde : {v_m_s:.2f}")

# Calcul de la distance parcourue
time_min = st.number_input("Entrez le temps (minutes)", min_value=0.0, value=10.0)
distance = v_m_min * time_min
st.write(f"Distance parcourue : {distance:.2f} mètres")

# Calcul du temps nécessaire
distance_input = st.number_input("Entrez une distance (mètres) pour calculer le temps", min_value=0.0, value=2000.0)
time_required = distance_input / v_m_s if v_m_s > 0 else 0
st.write(f"Temps nécessaire : {time_required:.2f} secondes")
