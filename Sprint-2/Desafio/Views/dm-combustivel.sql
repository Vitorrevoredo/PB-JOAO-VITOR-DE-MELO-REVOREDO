-- Dimensao Combustivel
CREATE VIEW vw_dim_combustivel AS
SELECT 
  combustivel.idcombustivel,
  combustivel.tipoCombustivel
FROM 
    combustivel
GROUP BY combustivel.idcombustivel ;
