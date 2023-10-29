import streamlit as st
import pyodbc
import json

# Crear una variable de sesión para almacenar el estado de inicio de sesión
logged_in = st.session_state.get("logged_in", False)

# Función para verificar las credenciales y obtener el rol del usuario
def login(username, password):
    try:
        # Cargar configuración desde el archivo config.json
        with open("../config.json") as config_file:
            config = json.load(config_file)

        # Conexión a la base de datos SQL Server
        conn = pyodbc.connect(
            driver=config["driver"],
            server=config["server"],
            database=config["database"],
            uid=config["user"],
            pwd=config["password"]
        )

        cursor = conn.cursor()

        query = "SELECT rol FROM Usuarios WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        row = cursor.fetchone()

        if row:
            rol = row[0]
            st.session_state.logged_in = True
            st.success(f"Bienvenido, {username}! Inicio de sesión exitoso!")
        else:
            st.error("Credenciales incorrectas. Inténtalo de nuevo")

        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"Error al conectar a la base de datos: {e}")

# Función para cerrar sesión
def logout():
    st.session_state.logged_in = False
    st.success("Sesión cerrada exitosamente")

def main():
    st.title("Megatron Accesorios - Sistema de Gestión")

    if logged_in:
        st.sidebar.title("Menú")

        selected_option = st.sidebar.selectbox("Seleccione una opción:", ["Inicio", "Ingresos Diarios", "Cobros de Arreglos", "Pedidos de Fundas", "Arreglos", "Control de Ingresos", "Clientes"])

        # Agregar lógica para cargar las pestañas correspondientes

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
