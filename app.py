# ===============================
# App de análisis de vehículos
# ===============================

import streamlit as st
import pandas as pd
import plotly.express as px

# dataset
df = pd.read_csv("vehicles_us.csv")

# Título
st.header("🚗 Análisis de vehículos en venta 🚗")

# Mostrar una vista previa de los datos
st.write("Vista previa de los datos:")
st.dataframe(df.head())

st.subheader("Selecciona qué gráficos mostrar:")

show_hist = st.checkbox("Histograma de odómetro")
show_scatter = st.checkbox("Dispersión precio vs odómetro")

if show_hist:
    fig = px.histogram(df, x="odometer", nbins=40,
                       title="Distribución del odómetro")
    st.plotly_chart(fig)

if show_scatter:
    fig = px.scatter(df, x="odometer", y="price",
                     title="Relación entre precio y odómetro")
    st.plotly_chart(fig)
