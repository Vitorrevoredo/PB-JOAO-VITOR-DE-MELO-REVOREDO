-- Forma Normal (1NF)
-- Ao analisar as estruturas das colunas da tb_locacao percebi porque todos os valores eram atômicos
-- e não havia repetição de grupos de dados ou registros com múltiplos valores em uma única coluna.
-- A tabela foi subdividida para eliminar a redundância e melhorar os relacionamentos,
--  o que levou à criação de tabelas separadas para clientes, carros, vendedores, combustíveis e locacao.

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

-- Forma Normal (2NF)
--A tabela original foi dividida em tabelas menores para garantir que cada atributo não chave dependesse 
-- inteiramente da chave primária. Por exemplo:
-- tabelas separadas para Clientes,Carros, Vendedores, locacao.
-- Cada tabela contém uma chave primária única que representa os dados de forma mais
-- organizada que permite a relação com a tabela tb_locacao.

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

  -- Forma Normal(3NF)
  -- As tabelas foram ajustadas para que cada coluna não chave dependesse apenas da chave primária, 
  -- como na criação da tabela de combustiveis,
  -- pois todas as colunas não-chave estão diretamente relacionada com sua respectiva chave primária.
 --  Por fim exclui a tb_locacao, pois a tabela estava fora dos padrões

-- Tabela combustivel


CREATE TABLE combustivel (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20),
    FOREIGN KEY (idCombustivel) REFERENCES carros(idCombustivel)
);

INSERT INTO combustivel (idCombustivel,tipoCombustivel)
SELECT DISTINCT
	idcombustivel,
	tipoCombustivel
FROM tb_locacao ;