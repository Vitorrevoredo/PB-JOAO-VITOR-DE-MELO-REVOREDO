-- tabela com informações de locação

CREATE TABLE info_Locacoes (
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


INSERT INTO info_locacoes
SELECT
	tb_locacao.idLocacao,
	clientes.idCliente,
    carros.idCarro,
    combustivel.idcombustivel,
    vendedores.idVendedor,
    tb_locacao.dataLocacao,
    tb_locacao.horaLocacao,
    tb_locacao.qtdDiaria,
    tb_locacao.vlrDiaria,
    tb_locacao.dataEntrega,
    tb_locacao.horaEntrega
 FROM tb_locacao
 JOIN clientes on tb_locacao.idCliente = clientes.idCliente
 JOIN carros ON tb_locacao.idCarro = carros.idCarro 
 JOIN combustivel ON tb_locacao.idcombustivel = combustivel.idcombustivel
 JOIN vendedores ON tb_locacao.idVendedor = vendedores.idVendedor