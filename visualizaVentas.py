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

    # Consulta SQL para obtener la información de los usuarios
    query_usuarios = "SELECT idUsuario, nombreApellido FROM Usuarios"
    usuarios_df = pd.read_sql(query_usuarios, db)

    # Fusionar (unir) el DataFrame de ventas con el DataFrame de usuarios
    ventas_df = pd.merge(ventas_df, usuarios_df, on="idUsuario", how="left")

    # Mostrar la tabla de ventas con la nueva columna de nombre de usuario
    st.dataframe(ventas_df)

    # Calcular y mostrar el total de precios
    total_precios = ventas_df["precio"].sum()
    st.title(f"Total de ventas: ${total_precios:}")

    # Calcular y mostrar el total por método de pago
    total_efectivo = ventas_df[ventas_df["metodoPago"] == "Efectivo"]["precio"].sum()
    total_transferencia = ventas_df[ventas_df["metodoPago"] == "Transferencia"]["precio"].sum()
    total_credito = ventas_df[ventas_df["metodoPago"] == "Tarjeta de Crédito"]["precio"].sum()
    total_debito = ventas_df[ventas_df["metodoPago"] == "Tarjeta de Débito"]["precio"].sum()

    st.write(f"Total en Efectivo: ${total_efectivo:}")
    st.write(f"Total en Transferencia: ${total_transferencia:}")
    st.write(f"Total en Tarjeta de Crédito: ${total_credito:}")
    st.write(f"Total en Tarjeta de Débito: ${total_debito:}")

def main():
    visualiza_ventas()

if __name__ == "__main__":
    main()
