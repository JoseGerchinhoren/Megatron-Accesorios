# Megatron Accesorios - Aplicación de Gestión Interna

¡Bienvenido al repositorio de Megatron Accesorios! Aquí encontrarás el código fuente y la información necesaria para implementar la aplicación de gestión interna desarrollada para Megatron Accesorios.

## Descripción del Proyecto

Este proyecto tiene como objetivo optimizar la gestión interna y mejorar la experiencia del cliente en el local de accesorios de celulares "Megatron Accesorios". La aplicación, desarrollada con Streamlit, ofrece características clave que incluyen un inicio de sesión seguro, menú dinámico adaptado a roles de usuario, gestión de ventas, pedidos de fundas, servicio técnico, gestión de usuarios, configuración personalizada y un dashboard interactivo de Power BI.

## Características Principales

- **Inicio de Sesión Seguro:**
  - Validación de credenciales para garantizar un acceso seguro.
  - Sesiones personalizadas para cada usuario.

- **Menú Dinámico:**
  - Menú interactivo adaptado al rol del usuario.
  - Opciones específicas para administradores y usuarios estándar.

- **Gestión de Ventas:**
  - Registro y seguimiento de nuevas ventas.
  - Visualización detallada de historial de ventas.

- **Pedidos de Fundas:**
  - Creación y seguimiento de pedidos de fundas personalizadas.

- **Servicio Técnico:**
  - Registro de solicitudes de servicio técnico.
  - Visualización de servicios técnicos realizados.

- **Usuarios:**
  - Creación y gestión de cuentas de usuario.
  - Búsqueda de usuarios por nombre.

- **Configuración Personalizada:**
  - Conexión a una base de datos SQL Server.
  - Carga de configuración desde un archivo config.json.

- **Experiencia del Usuario:**
  - Interfaz amigable y fácil de usar.
  - Acceso rápido a las funciones principales.

- **Dashboard de Power BI:**
  - Integración de un dashboard interactivo para análisis profundo.
  - Visualización en tiempo real de datos clave.

## Instrucciones de Instalación

Sigue estos pasos para instalar y configurar la aplicación en tu entorno local.

### Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Python 3.x
- Pip (administrador de paquetes de Python)
- SQL Server (puedes utilizar SQL Server Express)

### Configuración de la Base de Datos

Ejecuta las queries ubicadas en la carpeta `Querys` para crear la base de datos y las tablas necesarias.

### Instalación de Dependencias

1. Abre una terminal y navega hasta la raíz del proyecto.

2. Instala las dependencias utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

### Ejecución de la Aplicación

1. Ejecuta la aplicación utilizando el siguiente comando:

```bash
streamlit run app.py
```

La aplicación estará disponible en tu navegador en `http://localhost:8501`.

¡Listo! Ahora puedes explorar y utilizar la aplicación de Megatron Accesorios en tu entorno local.

---

**Nota:** Este proyecto está en desarrollo activo, y se aprecia cualquier contribución o comentario para mejorarlo. ¡Gracias por tu interés!

---

# Megatron Accessories - Internal Management Application

Welcome to the Megatron Accessories repository! Here you will find the source code and necessary information to implement the internal management application developed for Megatron Accessories.

## Project Description

This project aims to optimize internal management and enhance the customer experience at the "Megatron Accessories" cellphone accessories store. The application, developed with Streamlit, offers key features including secure login, a dynamic menu tailored to user roles, sales management, custom case orders, technical service tracking, user management, custom configuration, and an interactive Power BI dashboard.

## Key Features

- **Secure Login:**
  - Credential validation for secure access.
  - Custom sessions for each user.

- **Dynamic Menu:**
  - Interactive menu adapted to the user's role.
  - Specific options for administrators and standard users.

- **Sales Management:**
  - Registration and tracking of new sales.
  - Detailed visualization of sales history.

- **Custom Case Orders:**
  - Creation and tracking of custom case orders.

- **Technical Service:**
  - Registration of technical service requests.
  - Visualization of completed technical services.

- **Users:**
  - Creation and management of user accounts.
  - User search by name.

- **Custom Configuration:**
  - Connection to an SQL Server database.
  - Loading configuration from a config.json file.

- **User Experience:**
  - User-friendly and easy-to-use interface.
  - Quick access to key functions.

- **Power BI Dashboard:**
  - Integration of an interactive dashboard for in-depth analysis.
  - Real-time visualization of key data.

## Installation Instructions

Follow these steps to install and configure the application on your local environment.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package manager)
- SQL Server (you can use SQL Server Express)

### Database Setup

1. Run the queries located in the `Querys` folder to create the necessary database and tables.

```bash
cd Querys
sqlcmd -S <server_name> -d <database_name> -U <username> -P <password> -i create_database.sql
```

### Install Dependencies

1. Open a terminal and navigate to the project's root.

2. Install dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Run the Application

1. Run the application using the following command:

```bash
streamlit run app.py
```

The application will be available in your browser at `http://localhost:8501`.

That's it! You can now explore and use the Megatron Accessories application in your local environment.

---

**Note:** This project is actively under development, and any contributions or feedback to improve it are appreciated. Thank you for your interest!