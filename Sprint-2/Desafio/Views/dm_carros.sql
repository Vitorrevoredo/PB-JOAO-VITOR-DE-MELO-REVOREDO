-- Dimensao Carros
CREATE VIEW vw_dim_carro AS
SELECT 
    carros.idCarro,
    carros.kmCarro,
    carros.classiCarro,
    carros.marcaCarro,
    carros.modeloCarro,
    carros.anoCarro,
    combustivel.tipoCombustivel 
FROM carros
JOIN 
   combustivel ON carros.idcombustivel = combustivel.idcombustivel
GROUP BY carros.idCarro;
