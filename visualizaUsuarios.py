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

def visualizar_usuarios():
    st.title("Visualizar Usuarios")

    # Consulta SQL para obtener la información de los usuarios
    query_usuarios = "SELECT * FROM Usuarios"
    usuarios_df = pd.read_sql(query_usuarios, db)

    # Cambiar los nombres de las columnas según tus necesidades
    usuarios_df.columns = ["ID", "Nombre y Apellido", "Correo Electrónico", "Contraseña", "Fecha de Nacimiento", "DNI", "Domicilio",  "Fecha Creacion", "Rol"]

    # Quita columna Contraseña
    usuarios_df = usuarios_df[[
        "ID", "Nombre y Apellido", "Correo Electrónico", "Fecha de Nacimiento", "DNI", "Domicilio",  "Fecha Creacion", "Rol"
    ]]

    # Mostrar la tabla de usuarios
    st.dataframe(usuarios_df)

def main():
    visualizar_usuarios()  # Mostrar sección de visualización de usuarios

if __name__ == "__main__":
    main()
