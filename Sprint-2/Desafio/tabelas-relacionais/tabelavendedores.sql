-- Tabela dos vendedores

CREATE TABLE vendedores (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40),
    FOREIGN KEY (idVendedor) REFERENCES info_Locacoes(idVendedor)
);


INSERT INTO vendedores (idVendedor,nomeVendedor,sexoVendedor,estadoVendedor)
SELECT DISTINCT
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM tb_locacao;