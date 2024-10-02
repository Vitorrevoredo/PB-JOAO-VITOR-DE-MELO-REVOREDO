-- Dimensao Vendedor
CREATE VIEW vw_dim_vendedor AS
SELECT 
	vendedores.idVendedor,
	vendedores.nomeVendedor,
	vendedores.sexoVendedor,
	vendedores.estadoVendedor
FROM 
    vendedores 
GROUP BY vendedores.idVendedor;
