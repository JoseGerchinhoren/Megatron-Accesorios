USE Megatron;

CREATE TABLE ArreglosTecnico (
            idArreglo INT PRIMARY KEY IDENTITY(1,1),
            fecha date,
            nombreCliente varchar(250),
            contacto varchar(250),
            modelo varchar(250),
            falla varchar(250),
            tipoDesbloqueo varchar(250),
            imagenPatron VARBINARY(MAX),
            estado varchar(250),
            observaciones varchar(250),
			idUsuario INT
        )