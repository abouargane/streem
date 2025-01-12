import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calculateur de Vitesse et Distance", layout="centered")
st.title("Calculateur de Vitesse et Distance")

def convert_seconds_to_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours} heures, {minutes} minutes, {seconds:.2f} secondes"

st.markdown("""
    <style>
    .main {background-color: #f5f5f5;}
    .stButton button {background-color: #4CAF50; color: white;}
    .stNumberInput div {font-size: 18px;}
    .stTextInput div {font-size: 18px;}
    </style>
    """, unsafe_allow_html=True)

st.header("Vitesse maximale aérobie")
v_base = st.number_input("Entrez la vitesse de base (km/h)", min_value=0.0, value=100.0)
percentage = st.number_input("Entrez le pourcentage (%)", min_value=0.0, max_value=100.0, value=70.0)

# Calcul des vitesses
v_p = (percentage / 100) * v_base
v_m_min = (v_p * 1000) / 60
v_m_s = v_m_min / 60

st.header("Résultats des vitesses calculées")
st.write(f"Vitesse calculée : **{v_p:.2f} km/h**")
st.write(f"Vitesse en mètres par minute : **{v_m_min:.2f}**")
st.write(f"Vitesse en mètres par seconde : **{v_m_s:.2f}**")

st.header("Calcul du temps pour une distance au choix")
distance_choice = st.number_input("Entrez une distance au choix (mètres)", min_value=0.0, value=1000.0)
time_for_choice_distance = distance_choice / v_m_s if v_m_s > 0 else 0
st.write(f"Temps pour parcourir {distance_choice} mètres : **{convert_seconds_to_time(time_for_choice_distance)}**")

col1, col2 = st.columns(2)

with col1:
    st.header("Calcul de la distance parcourue")
    time_min = st.number_input("Entrez le temps (minutes)", min_value=0.0, value=10.0)
    distance = v_m_min * time_min
    st.write(f"Distance parcourue : **{distance:.2f} mètres**")

with col2:
    st.header("Calcul de temps de passege par tour")
    distance_input = st.number_input("Entrez une distance (mètres) pour calculer le temps", min_value=0.0, value=2000.0)
    time_required = distance_input / v_m_s if v_m_s > 0 else 0
    st.write(f"Temps nécessaire : **{convert_seconds_to_time(time_required)}**")
