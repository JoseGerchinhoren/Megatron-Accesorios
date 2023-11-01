import streamlit as st
import pyodbc
import json
from ingresaVentas import venta
from creaUsuarios import crear_usuario

# Cargar configuración desde el archivo config.json
with open("../config.json") as config_file:
    config = json.load(config_file)

# Crear una variable de sesión para almacenar el estado de inicio de sesión
logged_in = st.session_state.get("logged_in", False)
user_rol = st.session_state.get("user_rol", "")

# Función para verificar las credenciales y obtener el rol del usuario
def login(username, password):
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

        query = "SELECT rol FROM Usuarios WHERE nombreApellido = ? AND contraseña = ?"
        cursor.execute(query, (username, password))
        row = cursor.fetchone()

        if row:
            rol = row[0]
            st.session_state.logged_in = True
            st.session_state.user_rol = rol
            st.success(f"Bienvenido, {username}! Inicio de sesión exitoso!")
            # Redirigir después de iniciar sesión
            st.experimental_rerun()  # Recargar la aplicación para mostrar el contenido correcto
        else:
            st.error("Credenciales incorrectas. Inténtalo de nuevo")

        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"Error al conectar a la base de datos: {e}")

# Función para cerrar sesión
def logout():
    st.session_state.logged_in = False
    st.session_state.user_rol = ""
    st.success("Sesión cerrada exitosamente")

def main():
    st.title("Megatron Accesorios - Sistema de Gestión")

    if logged_in:
        st.sidebar.title("Menú")

        if user_rol == "admin":
            selected_option = st.sidebar.selectbox("Seleccione una opción:", ["Inicio", "Nueva Venta", "Cobros de Arreglos", "Pedidos de Fundas", "Arreglos", "Control de Ingresos", "Clientes", "Crear Usuario"])
            if selected_option == "Nueva Venta":
                venta()  # Cargar la pestaña para ingresar ventas
            if selected_option == "Crear Usuario":
                crear_usuario()  # Cargar la pestaña para crear usuarios
            
        else:
            selected_option = st.sidebar.selectbox("Seleccione una opción:", ["Inicio", "Nueva Venta", "Cobros de Arreglos", "Pedidos de Fundas", "Arreglos", "Control de Ingresos", "Clientes"])
            if selected_option == "Nueva Venta":
                venta()  # Cargar la pestaña para ingresar ventas

    else:
        st.sidebar.title("Inicio de Sesión")
        username = st.text_input("Nombre de Usuario:")
        password = st.text_input("Contraseña:", type="password")

        if st.button("Iniciar Sesión"):
            login(username, password)

    # Mostrar opción de cerrar sesión si está autenticado
    if logged_in:
        st.sidebar.button("Cerrar Sesión", on_click=logout)

if __name__ == "__main__":
    main()
