-- Forma Normal (1NF)
-- Ao analisar as estruturas das colunas da tb_locacao percebi porque todos os valores eram atômicos
-- e não havia repetição de grupos de dados ou registros com múltiplos valores em uma única coluna.
-- A tabela foi subdividida para eliminar a redundância e melhorar os relacionamentos,
--  o que levou à criação de tabelas separadas para clientes, carros, vendedores, e combustíveis.

CREATE TABLE locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40),
    idCarro INT,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idcombustivel INT,
    tipoCombustivel VARCHAR(20),
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INT,
    nomeVendedor VARCHAR(15),
    sexoVendedor CHAR(1),
    estadoVendedor VARCHAR(40)
);
-- Forma Normal (2NF)
--A tabela original foi dividida em tabelas menores para garantir que cada atributo não chave dependesse inteiramente da chave primária. Por exemplo:
-- tabelas separadas para Clientes,Carros, Vendedores e Combustivel.
-- Cada tabela agora contém uma chave primária única que representa os dados de forma mais organizada e sem redundância e una chave estrangeira que permite a relação
-- com a tabela tb_locacao

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
  -- As tabelas foram ajustadas para que cada coluna não chave dependesse apenas da chave primária, como na criação da tabela de combustiveis,
  -- pois todas as colunas não-chave estão diretamente relacionada com sua respectiva chave primária.
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
