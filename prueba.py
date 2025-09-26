import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Simulamos datos
np.random.seed(42)
df = pd.DataFrame({
    "mes": pd.date_range("2023-01-01", periods=24, freq="M"),
    "region": np.random.choice(["Lima", "Cusco", "Arequipa"], size=24),
    "producto": np.random.choice(["A", "B", "C"], size=24),
    "ventas": np.random.randint(50, 200, size=24)
})

st.title("Dashboard de Ventas Interactivo")

# Widget: selección de región
region_sel = st.selectbox("Selecciona región:", sorted(df["region"].unique()))

# Widget: selección de producto
producto_sel = st.selectbox("Selecciona producto:", sorted(df["producto"].unique()))

# Filtrar datos
df_filtrado = df[(df["region"] == region_sel) & (df["producto"] == producto_sel)]

st.write("Datos filtrados:", df_filtrado)

# Mostrar gráfico de tendencia
chart = alt.Chart(df_filtrado).mark_line(point=True).encode(
    x="mes:T",
    y="ventas:Q"
)
st.altair_chart(chart, use_container_width=True)

pip install streamlit pandas altair
streamlit run app.py

