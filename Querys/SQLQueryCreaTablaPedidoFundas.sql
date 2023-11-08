USE Megatron;
CREATE TABLE pedidosFundas (
    idPedidoFunda INTEGER PRIMARY KEY IDENTITY(1, 1),
    fecha DATE,
	pedido VARCHAR(500),
    nombreCliente TEXT,
    contacto VARCHAR(250),
    estado TEXT,
    idUsuario INTEGER,
);