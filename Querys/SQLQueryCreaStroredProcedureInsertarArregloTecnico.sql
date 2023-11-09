USE Megatron;
GO

CREATE PROCEDURE InsertarArregloTecnico
    @fecha DATE,
    @nombreCliente VARCHAR(250),
    @contacto VARCHAR(250),
    @modelo VARCHAR(250),
    @falla VARCHAR(250),
    @tipoDesbloqueo VARCHAR(250),
    @imagenPatron VARBINARY(MAX),
    @estado VARCHAR(250),
    @observaciones VARCHAR(250),
    @idUsuario INT
AS
BEGIN
    INSERT INTO ArreglosTecnico (
        fecha,
        nombreCliente,
        contacto,
        modelo,
        falla,
        tipoDesbloqueo,
        imagenPatron,
        estado,
        observaciones,
        idUsuario
    )
    VALUES (
        @fecha,
        @nombreCliente,
        @contacto,
        @modelo,
        @falla,
        @tipoDesbloqueo,
        @imagenPatron,
        @estado,
        @observaciones,
        @idUsuario
    );
END;
GO
