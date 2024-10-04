--Tabela carros 


CREATE TABLE carros (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idcombustivel INT,
    FOREIGN KEY (idCarro) REFERENCES locacao(idCarro),
    FOREIGN KEY (idcombustivel) REFERENCES combustivel(idcombustivel)
)

INSERT OR IGNORE INTO carros
SELECT DISTINCT
	locacao.idCarro,
	tb_locacao.kmCarro,
	tb_locacao.classiCarro,
	tb_locacao.marcaCarro,
	tb_locacao.modeloCarro,
	tb_locacao.anoCarro,
	tb_locacao.idcombustivel
FROM locacao
JOIN tb_locacao ON locacao.idCarro = tb_locacao.idCarro 

