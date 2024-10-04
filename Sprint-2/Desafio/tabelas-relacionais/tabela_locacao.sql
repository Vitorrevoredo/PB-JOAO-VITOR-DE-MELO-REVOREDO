-- tabela com informações de locação

CREATE TABLE locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idcombustivel INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idcombustivel) REFERENCES Combustivel(idcombustivel),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);


INSERT INTO locacao
SELECT
	tb_locacao.idLocacao,
	tb_locacao.idCliente,
    tb_locacao.idCarro,
    tb_locacao.idcombustivel,
    tb_locacao.idVendedor,
    tb_locacao.dataLocacao,
    tb_locacao.horaLocacao,
    tb_locacao.qtdDiaria,
    tb_locacao.vlrDiaria,
    tb_locacao.dataEntrega,
    tb_locacao.horaEntrega
 FROM tb_locacao
