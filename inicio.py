import streamlit as st
import pyodbc
import json
from ingresaVentas import venta
from creaUsuarios import crear_usuario
from visualizaVentas import visualiza_ventas
from ingresaPedidoFunda import ingresaPedidoFunda

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

        query = "SELECT rol, idUsuario FROM Usuarios WHERE nombreApellido = ? AND contraseña = ?"
        cursor.execute(query, (username, password))
        row = cursor.fetchone()

        if row:
            rol, id_usuario = row
            st.session_state.logged_in = True
            st.session_state.user_rol = rol
            st.session_state.user_nombre_apellido = username
            st.session_state.id_usuario = id_usuario  # Inicializa el id_usuario en la sesión
            st.experimental_rerun()
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
    st.session_state.user_nombre_apellido = ""  # Limpiar el nombre y apellido al cerrar sesión
    st.success("Sesión cerrada exitosamente")

def main():
    st.title("Megatron Accesorios - Sistema de Gestión")

    if logged_in:
        st.sidebar.title("Menú")

        if user_rol == "admin":
            selected_option = st.sidebar.selectbox("Seleccione una opción:", ["Inicio", "Nueva Venta", "Visualizar Ventas", "Nuevo Pedido de Funda", "Arreglos", "Control de Ingresos", "Clientes", "Crear Usuario"])  # Agrega "Visualizar Ventas" al menú
            if selected_option == "Nueva Venta":
                venta(st.session_state.id_usuario)
            if selected_option == "Crear Usuario":
                crear_usuario()
            if selected_option == "Visualizar Ventas":  # Agrega una condición para mostrar visualizaVentas
                visualiza_ventas()
            if selected_option == "Nuevo Pedido de Funda":
                ingresaPedidoFunda(st.session_state.id_usuario)

        else:
            selected_option = st.sidebar.selectbox("Seleccione una opción:", ["Inicio", "Nueva Venta", "Visualizar Ventas", "Nuevo Pedido de Funda", "Arreglos", "Control de Ingresos", "Clientes"])
            if selected_option == "Nueva Venta":
                venta(st.session_state.id_usuario)
            if selected_option == "Crear Usuario":
                crear_usuario()
            if selected_option == "Visualizar Ventas":
                visualiza_ventas()
            if selected_option == "Nuevo Pedido de Funda":
                ingresaPedidoFunda(st.session_state.id_usuario)

        if selected_option == "Inicio":
            st.write(f"Bienvenido, {user_nombre_apellido}! - Megatron Accesorios - Sistema de Gestión")

        st.write(f"Usuario: {user_nombre_apellido}")

    else:
        st.sidebar.title("Inicio de Sesión")

        with st.form(key="login_form"):
            username = st.text_input("Nombre de Usuario:")
            password = st.text_input("Contraseña:", type="password")

            login_submitted = st.form_submit_button("Iniciar Sesión")

            if login_submitted and username and password:
                login(username, password)

    if logged_in:
        st.sidebar.button("Cerrar Sesión", on_click=logout)

if __name__ == "__main__":
    main()