-- Crear la tabla Usuarios
CREATE TABLE Usuarios (
    idUsuario INT IDENTITY(1, 1) PRIMARY KEY,
    nombreApellido VARCHAR(100) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE, 
    contraseña VARCHAR(100) NOT NULL,
    fechaNacimiento DATE,
    dni VARCHAR(15) NOT NULL UNIQUE,
    domicilio VARCHAR(255),
    fechaCreacion DATE NOT NULL DEFAULT GETDATE(),
    rol VARCHAR(50) NOT NULL
);