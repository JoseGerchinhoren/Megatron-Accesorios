import streamlit as st
import pyodbc
import json
from ingresaVentas import venta
from creaUsuarios import crear_usuario

# Crear una variable de sesión para almacenar el nombre y apellido del usuario
user_nombre_apellido = st.session_state.get("user_nombre_apellido", "")

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

def buscar_usuarios(nombre_usuario_input):
    cursor = db.cursor()
    query = "SELECT nombreApellido FROM Usuarios WHERE nombreApellido LIKE ?"
    cursor.execute(query, f"%{nombre_usuario_input}%")
    usuarios = [usuario[0] for usuario in cursor.fetchall()]
    cursor.close()
    return usuarios

# Definir las variables para el estado de inicio de sesión
logged_in = st.session_state.get("logged_in", False)
user_rol = st.session_state.get("user_rol", "")

# Función para verificar las credenciales y obtener el rol del usuario
def login(username, password):
    try:
        conn = db
        cursor = conn.cursor()

        query = "SELECT rol FROM Usuarios WHERE nombreApellido = ? AND contraseña = ?"
        cursor.execute(query, (username, password))
        row = cursor.fetchone()

        if row:
            rol = row[0]
            st.session_state.logged_in = True
            st.session_state.user_rol = rol  # Actualizar el rol en la sesión
            st.session_state.user_nombre_apellido = username  # Almacenar el nombre y apellido en la sesión
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

        if selected_option == "Inicio":
            st.write(f"Bienvenido, {user_nombre_apellido}! - Megatron Accesorios - Sistema de Gestión")

        # Agregar una etiqueta que muestre el nombre del usuario
        st.write(f"Usuario: {user_nombre_apellido}")

    else:
        st.sidebar.title("Inicio de Sesión")

        # Inicializar un formulario para el inicio de sesión
        with st.form(key="login_form"):
            username = st.text_input("Nombre de Usuario:")
            password = st.text_input("Contraseña:", type="password")

            login_submitted = st.form_submit_button("Iniciar Sesión")

            if login_submitted and username and password:
                login(username, password)

if __name__ == "__main__":
    main()