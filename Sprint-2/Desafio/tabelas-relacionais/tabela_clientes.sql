-- Tabela de Clientes

CREATE TABLE clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40),
    FOREIGN KEY (idCliente) REFERENCES locacao(idCliente)
   );


INSERT INTO clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT
    locacao.idCliente, 
    tb_locacao.nomeCliente, 
    tb_locacao.cidadeCliente, 
    tb_locacao.estadoCliente, 
    tb_locacao.paisCliente
FROM
    tb_locacao
JOIN locacao ON tb_locacao.idCliente = locacao.idCliente
    
