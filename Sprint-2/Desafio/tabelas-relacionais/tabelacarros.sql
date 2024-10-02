--Tabela carros 


CREATE TABLE carros (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idcombustivel INT,
    FOREIGN KEY (idCarro) REFERENCES info_Locacoes(idCarro),
    FOREIGN KEY (idcombustivel) REFERENCES combustivel(idcombustivel),
    FOREIGN KEY (idCarro) REFERENCES tb_locacao(idCarro)
)

INSERT OR IGNORE INTO carros
SELECT DISTINCT
	tb_locacao.idCarro,
	tb_locacao.kmCarro,
	tb_locacao.classiCarro,
	tb_locacao.marcaCarro,
	tb_locacao.modeloCarro,
	tb_locacao.anoCarro,
	tb_locacao.idcombustivel
FROM tb_locacao

