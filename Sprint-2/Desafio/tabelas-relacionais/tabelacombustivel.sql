-- Tabela combustivel


CREATE TABLE combustivel (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20),
    FOREIGN KEY (idCombustivel) REFERENCES tb_locacao(idCombustivel)
)

INSERT INTO combustivel (idCombustivel,tipoCombustivel)
SELECT DISTINCT
	idcombustivel,
	tipoCombustivel
FROM tb_locacao 