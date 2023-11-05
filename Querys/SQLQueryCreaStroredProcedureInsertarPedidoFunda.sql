-- Crear la stored procedure para insertar un pedido de funda
CREATE PROCEDURE InsertarPedidoFunda
    @fecha DATE,
    @pedido VARCHAR(500),
    @nombreCliente TEXT,
    @Contacto VARCHAR(250),
    @estado TEXT,
    @idUsuario INTEGER
AS
BEGIN
    INSERT INTO pedidosFundas (fecha, pedido, nombreCliente, Contacto, estado, idUsuario)
    VALUES (@fecha, @pedido, @nombreCliente, @Contacto, @estado, @idUsuario);
END;
