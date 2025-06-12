"""This app creates a chart"""
import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv')

st.title('Proyecto Sprint 7')

# checkbox

if st.checkbox("Show/Hide"):

    # display the text if the checkbox returns True value
    st.text("Showing the widget")
# radio button

status = st.radio("Select Graph: ", ('Histogram', 'Dispersion'))

# conditional statement to print
if status == 'Histogram':
    st.write('Histograma de dataset')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width = True)


else:
    st.write('Dispersión odometro VS precio')
    fig = px.scatter(car_data, x="odometer", y="price") 
    st.plotly_chart(fig, use_container_width = True)
# End-of-file (EOF)