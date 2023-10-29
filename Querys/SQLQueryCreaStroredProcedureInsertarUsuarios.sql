-- Crear un stored procedure para insertar usuarios
CREATE PROCEDURE CrearUsuario
    @nombreApellido VARCHAR(100),
    @email VARCHAR(255),
    @contrasena VARCHAR(100),
    @fechaNacimiento DATE,
    @dni VARCHAR(15),
    @domicilio VARCHAR(255),
    @rol VARCHAR(50)
AS
BEGIN
    INSERT INTO Usuarios (nombreApellido, email, contraseña, fechaNacimiento, dni, domicilio, rol)
    VALUES (@nombreApellido, @email, @contrasena, @fechaNacimiento, @dni, @domicilio, @rol);
END;