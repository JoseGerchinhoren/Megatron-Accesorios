import streamlit as st
import pyodbc
import json

# Cargar configuración desde el archivo config.json
with open("../config.json") as config_file:
    config = json.load(config_file)

# Función para insertar un pedido de funda en la base de datos
def insertar_pedido_funda(fecha, pedido, nombreCliente, contacto, estado, monto_sena, id_usuario):
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

        # Llamar a la stored procedure para insertar el pedido de funda
        cursor.execute("EXEC InsertarPedidoFunda ?, ?, ?, ?, ?, ?, ?", (fecha, pedido, nombreCliente, contacto, estado, monto_sena, id_usuario))
        conn.commit()
        conn.close()
        st.success("Pedido de funda registrado exitosamente")

    except Exception as e:
        st.error(f"Error al registrar el pedido de funda: {e}")

def ingresaPedidoFunda(id_usuario):
    st.title("Registrar Pedido de Funda")

    # Campos para ingresar los datos del pedido de funda
    fecha = st.date_input("Fecha del Pedido:")
    pedido = st.text_input("Pedido:")
    nombreCliente = st.text_input("Nombre del Cliente:")
    contacto = st.text_input("Contacto:")
    estado = st.selectbox("Estado:", ["Señado", "Pedido", "Avisado", "Entregado", "Cancelado"])

    # Campo adicional para el monto de señal si el estado es "Señado"
    monto_sena = None
    if estado == "Señado":
        monto_sena = st.text_input("Monto de seña:")
    if monto_sena:
        if monto_sena.isdigit():
            monto_sena = int(monto_sena)
        else:
            st.warning("El monto debe ser un número entero.")
            monto_sena = None
    else:
        monto_sena = None

    # Botón para registrar el pedido de funda
    if st.button("Registrar Pedido"):
        if fecha and pedido and nombreCliente and contacto and estado:
            insertar_pedido_funda(fecha, pedido, nombreCliente, contacto, estado, monto_sena, id_usuario)
        else:
            st.warning("Por favor, complete todos los campos.")

if __name__ == "__main__":
    ingresaPedidoFunda()
