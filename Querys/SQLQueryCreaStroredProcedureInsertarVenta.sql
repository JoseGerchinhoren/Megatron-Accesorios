-- Modificar el stored procedure para insertar registros en la tabla Ventas
CREATE PROCEDURE InsertarVenta
    @Fecha DATE,
    @ProductoVendido VARCHAR(255),
    @Precio INT,
    @MetodoPago VARCHAR(50),
    @IdEmpleado INT
AS
BEGIN
    INSERT INTO Ventas (fecha, productoVendido, precio, metodoPago, idEmpleado)
    VALUES (@Fecha, @ProductoVendido, @Precio, @MetodoPago, @IdEmpleado);
END;