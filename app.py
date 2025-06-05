import streamlit as st
import pandas as pd
import plotly_express as px



st.header('Información estadística de carros')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Usamos un estado para controlar la visibilidad de los gráficos
if 'hist_visible' not in st.session_state:
    st.session_state.hist_visible = False

if 'scatter_visible' not in st.session_state:
    st.session_state.scatter_visible = False

# Crear botón para mostrar/ocultar histograma
hist_button = st.button('Construir/Ocultar histograma')

# Crear botón para mostrar/ocultar gráfico de dispersión
scatter_button = st.button('Construir/Ocultar gráfico de dispersión')

# Alternar visibilidad del histograma
if hist_button:
    st.session_state.hist_visible = not st.session_state.hist_visible

# Alternar visibilidad del gráfico de dispersión
if scatter_button:
    st.session_state.scatter_visible = not st.session_state.scatter_visible

# Mostrar el histograma si es visible
if st.session_state.hist_visible:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Mostrar el gráfico de dispersión si es visible
if st.session_state.scatter_visible:
    st.write('Creación de un gráfico de dispersión para odómetro y precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)