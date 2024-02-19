import pandas as pd
import streamlit as st
import plotly_express as px

vehicles_df = pd.read_csv('vehicles_us.csv')
st.header('Venta de Vehiculos')

# Obtener las columnas numéricas para los botones
numeric_columns = vehicles_df.select_dtypes(include=['float64', 'int64']).columns.tolist()

# Crear los botones para seleccionar la columna
selected_column = st.selectbox('Seleccionar columna', numeric_columns)

hist_button = st.button('Construir histograma') # Crear un botón

if hist_button: # Al hacer clic en el botón
    # Escribir un mensaje
    st.write(f'Creación de un histograma para la columna: {selected_column}')
            
    # Crear un histograma
    fig = px.histogram(vehicles_df, x=selected_column)
        
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)