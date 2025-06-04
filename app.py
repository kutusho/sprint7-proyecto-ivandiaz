import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Información estadística de carros')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Usamos un estado para controlar la visibilidad del histograma
if 'hist_visible' not in st.session_state:
    st.session_state.hist_visible = False

# Crear un botón que alterna el estado del histograma
hist_button = st.button('Construir/Ocultar histograma')

if hist_button:  # al hacer clic en el botón
    st.session_state.hist_visible = not st.session_state.hist_visible  # Alternar la visibilidad

if st.session_state.hist_visible:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
