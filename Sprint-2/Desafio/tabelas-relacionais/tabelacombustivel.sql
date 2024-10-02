-- Tabela combustivel


CREATE TABLE combustivel (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20),
    FOREIGN KEY (idCombustivel) REFERENCES info_locacoes(idCombustivel)
);

INSERT INTO combustivel (idCombustivel,tipoCombustivel)
SELECT DISTINCT
	idcombustivel,
	tipoCombustivel
FROM tb_locacao ;