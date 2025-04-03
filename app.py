import streamlit as st
import joblib
import numpy as np

# Caricamento modelli
model_latlong = joblib.load("model_latlong.pkl")
model_extra = joblib.load("model_extra.pkl")

st.title("Stima del prezzo immobiliare")

opzione = st.radio("Scegli il metodo di inserimento:", ["Latitudine e Longitudine", "Età + Distanza MRT + Minimarket"])

if opzione == "Latitudine e Longitudine":
    lat = st.number_input("Latitudine", min_value=24.9, max_value=25.1, format="%.6f")
    long = st.number_input("Longitudine", min_value=121.4, max_value=121.6, format="%.6f")

    if st.button("Stima il prezzo"):
        pred = model_latlong.predict(np.array([[lat, long]]))[0]
        st.success(f"Prezzo stimato: **{pred:.2f}** NT$/ping")

else:
    age = st.slider("Età dell'immobile (anni)", 0, 50, 10)
    dist = st.number_input("Distanza dalla stazione MRT (metri)", 0.0, 10000.0, 500.0)
    stores = st.slider("Numero di minimarket nelle vicinanze", 0, 10, 2)

    if st.button("Stima il prezzo"):
        pred = model_extra.predict(np.array([[age, dist, stores]]))[0]
        st.success(f"Prezzo stimato: **{pred:.2f}** NT$/ping")