#Importar librerias
import pandas as pd
import streamlit as st
import plotly_express as px

#Leer archivo csv
vehicles_df = pd.read_csv('vehicles_us.csv')


#Mostrar encabezado
st.header('Auto Sales')


# Mostrar el DataFrame en la aplicación
# Formatear los valores numéricos en el DataFrame como cadenas 
formatted_df = vehicles_df.map(lambda x: "{:.0f}".format(x) if isinstance(x, (int, float)) else x)
st.dataframe(formatted_df)


# Extraer la marca de la columna 'model' para crear la columna 'brand'
vehicles_df['brand'] = vehicles_df['model'].str.split(' ', expand=True)[0]


# Histograma de condición vs año del modelo
st.header('Histogram of Condition vs Model Year')

# Filtrar valores nulos en 'model_year' y 'condition'
vehicles_df = vehicles_df.dropna(subset=['model_year', 'condition'])

# Botón para crear histograma
hist_button = st.button('Build Histogram') # crear un botón
if hist_button:
    # Crear el histograma
    fig = px.histogram(vehicles_df, x='model_year', color='condition', barmode='overlay')
    # Mostrar el histograma
    st.plotly_chart(fig, use_container_width=True)


# Grafico de dispersión Precio vs Año y Kilometraje
st.header('Price vs Model Year/Odometer')
# Lista de opciones para el eje x
opciones_eje_x = ['odometer', 'model_year']  # Agrega las opciones que desees
# Permitir al usuario seleccionar una opción para el eje x
eje_x = st.selectbox('Select an option:', opciones_eje_x)
# Botón para crear grafico de dispersión
scatt_button = st.button('Build Scatter plot') # crear un botón
if scatt_button:
    # Crear el gráfico de dispersión con el eje x seleccionado
    fig = px.scatter(vehicles_df, x=eje_x, y="price")
    # Mostrar gráfico
    st.plotly_chart(fig)



#GRAFICO DE BARRAS
st.header('Vehicle types by manufacturer')
# Contar la cantidad de tipos de carro por marca
counts_by_brand_type = vehicles_df.groupby(['brand', 'type']).size().unstack(fill_value=0)
# Botón para crear grafico de barras
bar_button = st.button('Build Bar plot') # crear un botón
if bar_button:
    # Crear el gráfico de barras apiladas con Plotly Express
    fig = px.bar(counts_by_brand_type, barmode='stack')
    # Personalizar el diseño del gráfico
    fig.update_layout(
        xaxis={'categoryorder':'total descending'},  # Ordenar las marcas por la suma total de tipos de carro
        xaxis_tickangle=-45  # Rotar las etiquetas del eje x para mayor legibilidad
    )
    # Mostrar el gráfico
    st.plotly_chart(fig)


#HISTOGRAMA PARA COMPARAR LOS PRECIOS POR FABRICANTE
st.header('Compare price distribution by manufacturer')
st.write ('Select two options of manufacturer to compare price distribution')
# Función para crear el histograma interactivo
def plot_price_histogram(brand1, brand2):
    # Filtrar el DataFrame para incluir solo las marcas seleccionadas
    filtered_df = vehicles_df[(vehicles_df['brand'] == brand1) | (vehicles_df['brand'] == brand2)]
    # Botón para crear histograma
    histo_button = st.button('Build Histogram 2') # crear un botón
    if histo_button:
        # Crear el histograma
        fig = px.histogram(filtered_df, x='price', color='brand', 
                        histnorm='percent', nbins= 40)
        # Mostrar el histograma
        st.plotly_chart(fig)

# Lista de opciones para seleccionar la marca
brands_list = vehicles_df['brand'].unique()

# Permitir al usuario seleccionar dos marcas
brand1 = st.selectbox('Select Manufacturer 1:', brands_list)
brand2 = st.selectbox('Select Manufacturer 2:', brands_list)

# Generar el histograma interactivo
plot_price_histogram(brand1, brand2)

