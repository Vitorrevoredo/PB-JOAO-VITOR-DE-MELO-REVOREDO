-- Tabela de Clientes

CREATE TABLE clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40),
    FOREIGN KEY (idCliente) REFERENCES tb_locacao(idCliente)
   );


INSERT INTO clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT
    idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM
    tb_locacao;
    
