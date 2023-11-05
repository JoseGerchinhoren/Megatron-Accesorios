import streamlit as st
import pyodbc
import pandas as pd
import json
import datetime

# Cargar configuración desde el archivo config.json
with open("../config.json") as config_file:
    config = json.load(config_file)

# Conexión a la base de datos SQL Server
db = pyodbc.connect(
    driver=config["driver"],
    server=config["server"],
    database=config["database"],
    uid=config["user"],
    pwd=config["password"]
)

def visualiza_ventas():
    st.title("Visualizar Ventas")

    # Construir la consulta SQL en función de los filtros
    query = "SELECT * FROM Ventas WHERE 1 = 1"

    # Filtro de fecha
    fecha_filtro = None
    if st.sidebar.checkbox("Ventas del día"):
        fecha_filtro = (datetime.date.today(), datetime.date.today())
    elif st.sidebar.checkbox("Ventas del mes"):
        today = datetime.date.today()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=1, month=today.month + 1) - datetime.timedelta(days=1)
        fecha_filtro = (first_day_of_month, last_day_of_month)

    # Filtro de ID de Usuario
    id_usuario = st.sidebar.text_input("Filtrar por ID de Usuario", key="id_usuario")

    # Construir la consulta SQL en función de los filtros
    if fecha_filtro:
        query += f" AND fecha >= '{fecha_filtro[0]}' AND fecha <= '{fecha_filtro[1]}'"

    if id_usuario:
        query += f" AND idUsuario = '{id_usuario}'"
    
    query += " ORDER BY idVenta DESC"

    # Ejecutar la consulta y obtener los resultados en un DataFrame
    ventas_df = pd.read_sql(query, db)

    # Mostrar la tabla de ventas
    st.dataframe(ventas_df)

    # Calcular y mostrar el total de precios
    total_precios = ventas_df["precio"].sum()
    st.write(f"Total de ventas: ${total_precios:}")

def main():
    visualiza_ventas()

if __name__ == "__main__":
    main()
