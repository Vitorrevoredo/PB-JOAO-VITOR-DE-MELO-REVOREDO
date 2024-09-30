-- Tabela combustivel


CREATE TABLE combustivel (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20),
    FOREING KEY (idcombustivel) REFERENCES tb_locacao(idcombustivel)
)

INSERT INTO combustivel (idcombustivel,tipoCombustivel)
SELECT DISTINCT
	idcombustivel,
	tipoCombustivel
FROM tb_locacao 