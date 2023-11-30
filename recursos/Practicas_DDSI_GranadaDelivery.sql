-- caso ejemplo de 

-- Crear la tabla Producto
CREATE TABLE Producto (
    IDProducto INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Descripcion TEXT,
    Precio DECIMAL(10, 2) NOT NULL
);

-- Crear la tabla Stock
CREATE TABLE Stock (
    IDProducto INT PRIMARY KEY,
    Cantidad INT NOT NULL,
    FOREIGN KEY (IDProducto) REFERENCES Producto(IDProducto)
);

-- Crear la tabla Pedido
CREATE TABLE Pedido (
    Cpedido INT PRIMARY KEY,
    Ccliente INT NOT NULL,
    FechaPedido DATE NOT NULL,
    FOREIGN KEY (Ccliente) REFERENCES Cliente(Ccliente)
);

-- Crear la tabla DetallePedido
CREATE TABLE DetallePedido (
    Cpedido INT,
    IDProducto INT,
    Cantidad INT NOT NULL,
    PRIMARY KEY (Cpedido, IDProducto),
    FOREIGN KEY (Cpedido) REFERENCES Pedido(Cpedido),
    FOREIGN KEY (IDProducto) RE
);
