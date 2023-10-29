-- Crear la tabla IngresosDiarios
USE Megatron;

CREATE TABLE Ventas (
    idVenta INT IDENTITY(1, 1) PRIMARY KEY,
    fecha DATE,
    productoVendido VARCHAR(255),
    precio INT,
    metodoPago VARCHAR(50),
    idEmpleado INT
);