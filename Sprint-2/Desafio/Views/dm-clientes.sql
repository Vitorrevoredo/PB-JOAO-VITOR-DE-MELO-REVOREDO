-- Dimensão clientes
CREATE VIEW vw_dim_cliente AS
SELECT 
    clientes.idCliente,
    clientes.nomeCliente,
    clientes.cidadeCliente,
    clientes.estadoCliente,
    clientes.paisCliente
FROM 
    clientes
GROUP BY clientes.idCliente;
