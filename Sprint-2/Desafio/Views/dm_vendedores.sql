-- Dimensão vendedores
CREATE VIEW dm_vendedores AS
SELECT DISTINCT
	vw_fatos_locacao.idVendedor,
	vendedores.nomeVendedor,
	vendedores.sexoVendedor,
	vendedores.estadoVendedor
FROM vw_fatos_locacao
INNER JOIN vendedores ON vw_fatos_locacao.idVendedor = vendedores.idVendedor;