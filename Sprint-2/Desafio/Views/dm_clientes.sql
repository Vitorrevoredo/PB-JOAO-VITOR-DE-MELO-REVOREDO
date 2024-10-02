-- Dimensão clientes
CREATE VIEW dm_clientes AS
SELECT DISTINCT
	vw_fatos_locacao.idCliente,
	clientes.nomeCliente,
	clientes.cidadeCliente,
	clientes.estadoCliente,
	clientes.paisCliente
FROM vw_fatos_locacao
INNER JOIN clientes ON vw_fatos_locacao.idCliente = clientes.idCliente;