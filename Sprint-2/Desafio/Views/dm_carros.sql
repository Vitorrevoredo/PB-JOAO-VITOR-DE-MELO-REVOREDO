-- Dimensão veiculos
CREATE VIEW dm_carros AS
SELECT DISTINCT
	vw_fatos_locacao.idCarro,
	carros.kmCarro,
	carros.classiCarro,
	carros.marcaCarro,
	carros.modeloCarro,
	carros.anoCarro,
	combustivel.idcombustivel,
	combustivel.tipoCombustivel
FROM vw_fatos_locacao
INNER JOIN carros ON vw_fatos_locacao.idCarro = carros.idCarro 
INNER JOIN combustivel ON vw_fatos_locacao.idcombustivel = combustivel.idcombustivel