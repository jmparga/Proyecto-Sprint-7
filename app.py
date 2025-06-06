"""This app creates a chart"""
import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('C:/Users/dammy/vehicles_env/Sprint7/vehicles_us.csv')
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creacion de un histograma para el conjunto')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width = True)
