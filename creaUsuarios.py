import streamlit as st
import pyodbc
import json

# Cargar configuración desde el archivo config.json
with open("config.json") as config_file:
    config = json.load(config_file)

# Función para insertar un nuevo usuario en la base de datos
def crear_usuario(nombreApellido, email, contrasena, fechaNacimiento, dni, domicilio, rol):
    try:
        # Conexión a la base de datos SQL Server
        conn_str = (
            f"DRIVER={{{config['driver']}}};"
            f"SERVER={config['server']};"
            f"DATABASE={config['database']};"
            f"UID={config['user']};"
            f"PWD={config['password']};"
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Insertar el nuevo usuario en la base de datos
        query = "EXEC CrearUsuario ?, ?, ?, ?, ?, ?, ?"
        cursor.execute(query, (nombreApellido, email, contrasena, fechaNacimiento, dni, domicilio, rol))
        conn.commit()
        conn.close()
        st.success("Usuario creado exitosamente")

    except Exception as e:
        st.error(f"Error al crear el usuario: {e}")

def crear_usuario_tab():
    st.title("Crear Usuario")

    # Campos para ingresar los datos del nuevo usuario
    nombreApellido = st.text_input("Nombre y Apellido")
    email = st.text_input("Correo Electrónico")
    contrasena = st.text_input("Contraseña", type="password")
    fechaNacimiento = st.date_input("Fecha de Nacimiento")
    dni = st.text_input("DNI")
    domicilio = st.text_input("Domicilio")
    rol = st.text_input("Rol")

    # Botón para crear el nuevo usuario
    if st.button("Crear Usuario"):
        if nombreApellido and email and contrasena and fechaNacimiento and dni and rol:
            crear_usuario(nombreApellido, email, contrasena, fechaNacimiento, dni, domicilio, rol)
        else:
            st.warning("Por favor, complete todos los campos.")

if __name__ == "__main__":
    crear_usuario_tab()
