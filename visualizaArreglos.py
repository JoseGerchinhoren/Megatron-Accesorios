import streamlit as st
import pyodbc
import pandas as pd
import json

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

def visualizar_arreglos():
    st.title("Visualizar Arreglos de Servicio Técnico")

    # Construir la consulta SQL para obtener los arreglos de servicio técnico
    query = "SELECT * FROM ArreglosTecnico ORDER BY idArreglo DESC"

    # Ejecutar la consulta y obtener los resultados en un DataFrame
    arreglos_df = pd.read_sql(query, db)

    # Consulta SQL para obtener la información de los usuarios
    query_usuarios = "SELECT idUsuario, nombreApellido FROM Usuarios"
    usuarios_df = pd.read_sql(query_usuarios, db)

    # Fusionar (unir) el DataFrame de arreglos con el DataFrame de usuarios
    arreglos_df = pd.merge(arreglos_df, usuarios_df, on="idUsuario", how="left")

    # Cambiar los nombres de las columnas
    arreglos_df.columns = ["ID", "Fecha", "Nombre del Cliente", "Contacto", "Modelo", "Falla", "Tipo Desbloqueo", "Imagen Patrón", "Estado", "Observaciones", "ID Usuario", "Nombre de Usuario"]

    # Cambiar el orden del DataFrame
    arreglos_df = arreglos_df[[
        "ID",
        "Fecha",
        "Nombre del Cliente",
        "Contacto",
        "Modelo",
        "Falla",
        "Tipo Desbloqueo",
        "Imagen Patrón",
        "Estado",
        "Observaciones",
        "Nombre de Usuario"
    ]]

    # Agregar un filtro por estado
    estados = arreglos_df['Estado'].unique()
    filtro_estado = st.selectbox("Filtrar por Estado:", ["Todos"] + list(estados))

    if filtro_estado != "Todos":
        arreglos_df = arreglos_df[arreglos_df['Estado'] == filtro_estado]

    # Mostrar la tabla de arreglos de servicio técnico
    st.dataframe(arreglos_df)

def main():
    visualizar_arreglos()

if __name__ == "__main__":
    main()
